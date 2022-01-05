%{  
  #include <iostream>
  #include <string>
  #include <cstring>
  #include <set>

  #include "table.hpp"
  #include "tac.hpp"
  #include "types.hpp"
  #include "memory.hpp"
  #include "errors.hpp"

  #define YY_BUF_SIZE 32768

  using namespace std;

  extern int yylineno;
  extern int yycolumn;
  extern char *filename;
  // open file to extract the tokens
  extern FILE *yyin;
  extern queue<string> errors;

  // AST and TAC 
  TAC *tac = new TAC;
  NodeS *ast;

  // Predefined Types 
  extern map<string, Type*> predefinedTypes;
  extern map<string, int> primitiveWidths;

  // Crea las funciones y variables del scope0.
  void scope0(void);
  
  // Indica si nos encontramos en la ejecucion principal.
  bool __main__ = true;
  NodeExec *exec_node = NULL;
  set<string> executed;

  // Leblanc-Cook's Symbols Table
  SymbolsTable *table = new SymbolsTable;

  // Flex definitions
  typedef struct yy_buffer_state *YY_BUFFER_STATE;
  YY_BUFFER_STATE yy_create_buffer ( FILE *file, int size  );
  void yy_switch_to_buffer ( YY_BUFFER_STATE new_buffer  );
  void yy_flush_buffer ( YY_BUFFER_STATE b  );
  void yy_delete_buffer ( YY_BUFFER_STATE b  );
  YY_BUFFER_STATE current_buffer(void);
%}

%define parse.lac full

%union 
{  
  int                                   integer;
  float                                 flot;
  bool                                  boolean;
  uint64_t                              uint64;
  string                                *str;
  Node                                  *ast;
  NodeS                                 *nS;
  Type                                  *t;
  ExpressionNode                        *expr;
  NodeRoutArgDef                        *routArgsDef;
  NodeRoutArgs                          *routArgs;
  NodeRoutDecArgDef                     *routDecArgsDef;
  NodeRoutDecArgs                       *routDecArgs;
  NodeArrayElems                        *arrayElems;
  NodeForSign                           *forSign;
  NodeFunctionCallArgs                  *fcArgs;
  NodeFunctionCallPositionalArgs        *fcpArgs;
  NodeFunctionCallNamedArgs             *fcnArgs;
  vector<pair<string, ExpressionNode*>> *varList;
  pair<string, FunctionEntry*>          *funcEntry;
}

%locations
%start S

%nonassoc   <str> NEW
%right      <str> ASSIGNMENT
%left       <str> OR AND 
%left       <str> EQUIV NOT_EQUIV
%nonassoc   <str> LESS_THAN LESS_EQUAL_THAN GREATER_THAN GREATER_EQUAL_THAN
%right      <str> NOT
%left       <str> PLUS MINUS
%left       <str> ASTERISK DIV MODULE
%right      <str> POWER
%left       <str> OPEN_BRACKET CLOSE_BRACKET
%left       <str> DOT
%right      <str> POINTER
%nonassoc   <str> ID
%left       <str> OPEN_PAR

%token SEMICOLON
%token CLOSE_PAR
%token OPEN_C_BRACE 
%token CLOSE_C_BRACE
%token COMMA
%token REGISTER 
%token UNION
%token STRUCTURE
%token FORGET 
%token BREAK
%token CONTINUE
%token EXIT
%token IF 
%token THEN 
%token ELSIF
%token ELSE 
%token WHILE
%token DO 
%token DONE 
%token FOR
%token LET
%token DEF
%token DEC
%token OPT
%token AT 
%token RIGHT_ARROW
%token RETURN
%token EXEC
%token EXECONCE

%token <integer>  INT
%token <flot>     FLOAT 
%token <integer>  CHAR
%token <str>      STRING 
%token <boolean>  TRUE 
%token <boolean>  FALSE
%token <str>      T_UNIT
%token <str>      T_BOOL
%token <str>      T_CHAR 
%token <str>      T_INT 
%token <str>      T_FLOAT
%token <str>      T_STRING 

%type <ast>            I Inst Action VarInst VarDef UnionDef UnionBody StructDec
%type <ast>            RegBody Conditional OptElsif Elsifs OptElse Def RegDef
%type <ast>            LoopWhile LoopFor RoutDef Actions RoutSign RoutDec N 
%type <expr>           Exp FuncCall Array
%type <expr>           OptAssign Cond OptStep
%type <arrayElems>     ArrExp ArrElems
%type <forSign>        ForSign
%type <routArgs>       RoutArgs
%type <routArgsDef>    OptArgs MandArgs
%type <routDecArgs>    DecArgs
%type <routDecArgsDef> OptDecArgs MandDecArgs
%type <fcArgs>         ArgsExp
%type <fcpArgs>        PositionalArgs
%type <fcnArgs>        NamedArgs
%type <t>              Type OptReturn
%type <boolean>        OptRef Exec
%type <str>            IdDef UnionId RegId DecId W CondAssign
%type <nS>             S
%type <varList>        VarDefList
%type <funcEntry>      RoutId
%type <uint64>         M

%%
/* ======================= GLOBAL RULES ============================== */
  S       : I 
            { 
              if ($1 != NULL) {
                tac->backpatch($1->nextlist, tac->instructions.size());
              }

              if (__main__) {
                $$ = new NodeS($1); 
                ast = $$; 

                // Verificamos que no quedaron llamadas a funciones de solo declaraciones.
                for (pair<string, vector<pair<unsigned long long, vector<int>>>> f : tac->functionlist) {
                  addError("Function '\033[1;3m" + f.first + "\033[0m' declared but not defined.");
                }
              }
              else {
                exec_node = new NodeExec(filename, $1);
                $$ = NULL;
              }
            }
          ;
  M       : /* lambda */        { $$ = tac->instructions.size(); }
  I       : /* lambda */        { $$ = NULL; }
          | I M Inst 
            { 
              // Una instruccion puede ser NULL porque dio error o porque no tiene una
              // representacion en el arbol abtracto, como las declaraciones de variables.

              if ($1 == NULL && $3 == NULL) {
                // Si ambas instrucciones hijas son NULL, esta instruccion es NULL.
                $$ = NULL;
              } 
              else if ($3 == NULL) {
                // Si la segunda instruccion es NULL, la instruccion padre sera igual 
                // a la hija.
                $$ = $1;
              } 
              else {
                $$ = new NodeI($1, $3); 
                if ($1 != NULL) {
                  // Nos aseguramos que la primera instruccion salte a la segunda.
                  tac->backpatch($1->nextlist, $2);
                }
                $$->nextlist = $3->nextlist;
              }
            }
          ;
  Inst    : Action              { $$ = $1; }
          | Def                 { $$ = $1; }
          ;
  Action  : 
          Exp SEMICOLON 
            { 
              // Las acciones son aquellas que ejecutan un calculo y no son puramente
              // definiciones,
              $$ = $1;
              if ($1->type->toString() == "Bool") {
                // Si la expresion es booleana, nos aseguramos que salte a la siguiente
                // instruccion.
                tac->backpatch($1->truelist, tac->instructions.size());
                tac->backpatch($1->falselist, tac->instructions.size());
              } 
            }
          | BREAK SEMICOLON
            {
              if (tac->breaklist.size() == 0) {
                addError("Break instruction must be use in loops.");
              }
              else {
                tac->breaklist.top().push_back(tac->instructions.size());
                tac->gen("goto _");
              }
              $$ = NULL;
            }
          | CONTINUE SEMICOLON
            {
              if (tac->continuelist.size() == 0) {
                addError("Continue instruction must be use in loops.");
              }
              else {
                tac->continuelist.top().push_back(tac->instructions.size());
                tac->gen("goto _");
              }
              $$ = NULL;
            }
          | EXIT Exp SEMICOLON 
            {
              if ($2->type->toString() != "Int") {
                // El codigo de salida debe ser entero.
                addError(
                  "Exit code must be \033[1;3mInt\033[0m but \033[1;3m" + 
                  $2->type->toString() + "\033[0m found."
                );
              } 
              else {
                string raddr;
                if ($2->addr.back() == ']') {
                  raddr = tac->newTemp();
                  tac->gen("assignw " + raddr + " " + $2->addr);
                }
                else {
                  raddr = $2->addr;
                }

                tac->gen("exit " + $2->addr);
              }
              $$ = $2;
            }
          | RETURN Exp SEMICOLON 
            {
              string type = $2->type->toString();

              if (type == "$Error") {
                $$ = new NodeError();
              }
              else if (table->ret_type != "" && ! typecmp(table->ret_type, type)) {
                addError(
                  "Expected return type '\033[1;3m" + 
                  table->ret_type + "\033[0m' but " +
                  "'\033[1;3m" + type + "\033[0m' found."
                );
                $$ = new NodeError();
              } 

              else {
                string addr;
                if (type == "Bool") {
                  // En caso contrario hay que usar backpatching para realizar una
                  // asignacion del booleano.
                  addr = tac->newTemp();

                  // Aplicamos backpatching sobre la truelist para realizar la 
                  // asignacion de True, y luego saltamos la asignaicon de False.
                  tac->backpatch($2->truelist, tac->instructions.size());
                  tac->gen("assignb " + addr + " True");
                  string label = "Bool" + to_string(tac->instructions.size() + 2);
                  tac->gen("goto " + label);

                  // Aplicamos backpatching sobre la falselist para realizar la 
                  // asignacion de False, y luego creamos la etiqueta de salto de la
                  // asignacion a True.
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assignb " + addr + " False");
                  tac->gen("@label " + label);
                }
                else if ($2->addr.back() == ']') {
                  string assign_type = $2->type->width == 1 ? "assignb" : "assignw";
                  addr = type == "Float" ? tac->newFloat() : tac->newTemp();
                  tac->gen(assign_type + " " + addr + " " + $2->addr);
                }
                else {
                  addr = $2->addr;
                }

                $$ = new NodeReturn($2);
                tac->gen("assignw lastbase BASE");
                tac->gen("return " + addr);
              }
            }

          | RETURN SEMICOLON  
            {
              if (table->ret_type != "" && "Unit" != table->ret_type) {
                addError(
                  "Expected return type '\033[1;3m" + 
                  table->ret_type + "\033[0m' but " +
                  "'\033[1;3mUnit\033[0m' found ."
                );
                $$ = new NodeError();
              } 

              else {
                $$ = new NodeReturn();
                tac->gen("assignw lastbase BASE");
                tac->gen("return 0");
              }
            }
          | Exec STRING SEMICOLON
            {
              $2->erase(0, 1);
              $2->erase($2->size() - 1);

              if ($1 || executed.count(*$2) == 0) {
                // Creamos los auxiliares correspondientes.
                char* filename_aux = filename;
                FILE* yyin_aux = yyin;
                NodeExec *exec_node_aux = exec_node;
                int yylineno_aux = yylineno, yycolumn_aux = yycolumn;
                bool __main_aux__ = __main__;
                YY_BUFFER_STATE temp = current_buffer();

                filename = (char*) malloc($2->size() * sizeof(char));
                strcpy(filename, $2->c_str());
                yylineno = 1; 
                yycolumn = 1;
                __main__ = false;

                // check if file was succesfully opened.
                if ((yyin = fopen(filename, "r")) == 0) {
                  addError(
                    "There was an error executing \033[1;3m" + (string) filename +
                    "\033[0m."
                  );
                }
                else {
                  yy_switch_to_buffer(yy_create_buffer(yyin, YY_BUF_SIZE));
                  yyparse();
                  yy_flush_buffer(current_buffer());
                  yy_delete_buffer(current_buffer());
                }

                strcpy(filename, filename_aux);
                yyin = yyin_aux;
                yylineno = yylineno_aux;
                yycolumn = yycolumn_aux;
                __main__ = __main_aux__;

                $$ = exec_node;
                exec_node = exec_node_aux;

                yy_switch_to_buffer(temp);

                if (! errors.empty()) {
                  return 1;
                }

                if (executed.count(*$2) == 0) {
                  executed.insert(*$2);
                }
              } 
              else {
                $$ = NULL;
              }
            }
          | VarInst SEMICOLON   { $$ = $1; }
          | Conditional         { $$ = $1; }
          | LoopWhile           { $$ = $1; }
          | LoopFor             { $$ = $1; }
          ;
  Exec    : EXEC                { $$ = true; }
          | EXECONCE            { $$ = false; }
  Def     : UnionDef            { $$ = $1; }
          | RegDef              { $$ = $1; }
          | StructDec SEMICOLON { $$ = $1; }
          | RoutDef             { $$ = $1; }
          | RoutDec SEMICOLON   { $$ = $1; }
          ;


/* ======================= VARIABLES DEFINITION ====================== */
  VarInst     : VarDef              { $$ = $1; }

              | FORGET Exp 
                { 
                  if ($2->type->toString() == "$Error") {
                    $$ = NULL;
                  } 

                  else if ($2->type->category != "Pointer") {
                    string t = $2->type->toString();
                    addError("Expected a pointer but '\033[1;3m" + t + "\033[0m' found.");
                    $$ = NULL;
                  }

                  else {
                    $$ = new NodeForget($2);
                    Type *t = ((PointerType*) ($2->type))->type;
                    string type = t->toString();
                    string raddr;

                    if ($2->addr.back() == ']') {
                      raddr = type == "Float" ? tac->newFloat(): tac->newTemp();
                      tac->gen("assignw " + raddr + " " + $2->addr);
                    }
                    else {
                      raddr = $2->addr;
                    }
                    
                    // Si el tipo es un arreglo o estructura, llamamos a la funcion
                    // para liberar memoria correspondiente
                    if (type.back() == ']') {
                      freeArray(t, raddr);
                    }
                    else if (! predefinedTypes.count(type) && type[0] != '^') {
                      freeStruct(t, raddr);
                    }
                    else {
                      tac->gen("free " + raddr);
                    }
                  }
                }

              | Exp M ASSIGNMENT Exp 
                { 
                  string ltype = $1->type->toString();
                  string rtype = $4->type->toString();

                  if (ltype == "$Error" || rtype == "$Error") {
                    $$ = NULL;
                  } 

                  else if (! $1->is_lvalue) {
                    addError("Can't assign to a R-Value.");
                    $$ = NULL;
                  }

                  else if (! typecmp(ltype, rtype)) {
                    addError(
                      "Can't assign a '\033[1;3m" + rtype +
                      "\033[0m' to a '\033[1;3m" + ltype + "\033[0m'."
                    );
                    $$ = NULL;
                  } 

                  else {
                    $$ = new NodeAssign($1, $4);

                    string raddr;
                    string assign_type = ltype == "Bool" || ltype == "Char" ? "assignb" : "assignw";
                    if ($4->addr.back() == ']' && $1->addr.back() == ']') {
                      raddr = ltype == "Float" ? tac->newFloat() : tac->newTemp();
                      tac->gen(assign_type + " " + raddr + " " + $4->addr);
                    }
                    else {
                      raddr = $4->addr;
                    }


                    if (rtype != "Bool") {
                      // Si el rtype no es booleano, se hace la asignacion comun.
                      tac->gen(assign_type + " " + $1->addr + " " + raddr);
                    }
                    else {
                      // Eliminamos las dos instrucciones que debieron haber surgido por 
                      // tener un lvalue booleano.
                      tac->instructions[$2 - 2] = "";
                      tac->instructions[$2 - 1] = "";

                      // En caso contrario hay que usar backpatching para realizar una
                      // asignacion del booleano.

                      // Aplicamos backpatching sobre la truelist para realizar la 
                      // asignacion de True, y luego saltamos la asignaicon de False.
                      tac->backpatch($4->truelist, tac->instructions.size());
                      tac->gen("assignb " + $1->addr + " True");
                      string label = "Bool" + to_string(tac->instructions.size() + 2);
                      tac->gen("goto " + label);

                      // Aplicamos backpatching sobre la falselist para realizar la 
                      // asignacion de False, y luego creamos la etiqueta de salto de la
                      // asignacion a True.
                      tac->backpatch($4->falselist, tac->instructions.size());
                      tac->gen("assignb " + $1->addr + " False");
                      tac->gen("@label " + label);
                    }
                  }
                }
              ;
  VarDef      : LET Type VarDefList
                { 
                  string type = $2->toString();
                  $$ = NULL;

                  if ($2->incomplete != "") {
                    addError("Can't define instances of incomplete structures.");
                  }

                  else if (type != "$Error") {
                    string assign_type = type == "Bool" || type == "Char" ? "assignb" : "assignw";
                    // Por cada variable en la lista de definicion.
                    for (pair<string, ExpressionNode*> vardef : *$3) {
                      ExpressionNode* exp = vardef.second;
                      string rtype = exp == NULL ? "" : exp->type->toString();

                      // Verificamos que el tipo de la definicion y el tipo de la 
                      // expresion (en caso de haberla) son iguales.
                      if (exp != NULL && ! typecmp(type, rtype)) {
                        addError(
                          "Can't assign a '\033[1;3m" + rtype +
                          "\033[0m' to a '\033[1;3m" + type + "\033[0m'."
                        );
                      } 

                      else {
                        int s = table->currentScope(), offset = table->newOffset($2);
                        string addr;

                        // Verificamos si nos encontramos dentro de una funcion.
                        if (table->ret_type != "") {
                          addr = "BASE[" + to_string(offset) + "]";
                        } 
                        else if (type == "Float") {
                          addr = tac->newFloat();
                        }
                        else {
                          addr = tac->newTemp();
                        }

                        // En caso de que el tipo sea un arreglo o estructura (registro
                        // o union) reservamos la memoria necesaria.

                        // Si es un arreglo.
                        if (type.back() == ']') {
                          allocArray($2, addr);
                        }
                        // En cambio si es una estructura excepto un puntero.
                        else if (! predefinedTypes.count(type) && type[0] != '^') {
                          allocStruct($2, addr);
                        }

                        // Almacenamos la entrada.
                        Entry *e;
                        if(type.back() != ']') {
                          e = new VarEntry(vardef.first, s, "Var", $2, offset, addr);
                        }
                        else {
                          ArrayType *current = (ArrayType*) (exp == NULL ? $2 : exp->type);
                          e = new VarArrayEntry(vardef.first, s, "Var", current, offset, addr);
                        }
                        table->insert(e);

                        // En caso de haber una expresion, se realiza la asignacion.
                        if (exp != NULL) {
                          $$ = new NodeAssignList(
                            $$, 
                            new NodeAssign(new NodeID(vardef.first, $2), exp)
                          );

                          if (rtype != "Bool") {
                            string raddr;
                            if (addr.back() == ']' && exp->addr.back() == ']') {
                              raddr = rtype == "Float" ? tac->newFloat() : tac->newTemp();
                              tac->gen(assign_type + " " + raddr + " " + exp->addr);
                            }
                            else {
                              raddr = exp->addr;
                            }

                            // Si la expresion no es booleana, se realiza una asignacion 
                            // comun.
                            tac->gen(assign_type + " " + addr + " " + raddr);
                          }
                          else {
                            // En caso contrario se utiliza backpatching para realizar
                            // la asignacion correcta segun los distintos saltos.
                            
                            // Backpatching sobre la truelist.
                            tac->backpatch(exp->truelist, tac->instructions.size());
                            tac->gen("assignb " + addr + " True");
                            string label = "Bool" + to_string(tac->instructions.size() + 2);
                            // Salto para evitar la asignacion de False.
                            tac->gen("goto " + label);
                            // Backpatching sobre la falselist.
                            tac->backpatch(exp->falselist, tac->instructions.size());
                            tac->gen("assignb " + addr + " False");
                            // Label de la asignacion de True.
                            tac->gen("@label " + label);
                          }
                        }
                      }
                    }
                  }
                } 
              ;
  
  VarDefList  : IdDef OptAssign 
                {
                  $$ = new vector<pair<string, ExpressionNode*>>;
                  if (*$1 != "" && ($2 == NULL || $2->type->toString() != "$Error")) {
                    $$->push_back({*$1, $2});
                  }
                }  

              | VarDefList COMMA IdDef OptAssign  
                {
                  $$ = $1;
                  if (*$3 != "" && ($4 == NULL || $4->type->toString() != "$Error")) {
                    $$->push_back({*$3, $4});
                  } 
                }
              ;   
  
  IdDef       : ID 
                {
                  // Verificamos que no hay otro identificador igual en este scope.
                  if (! table->verifyInsert(*$1)) {
                    addError("Redefinition of '\033[1;3m" + *$1 + "\033[0m'.");
                    $$ = new string("");
                  } 
                  else {
                    $$ = $1; 
                  }
                }
  
  OptAssign   : /* lambda */                { $$ = NULL; }
              | ASSIGNMENT Exp              { $$ = $2; }
              ;


/* ======================= TYPES ===================================== */
  Type  : 
        Type OPEN_BRACKET Exp CLOSE_BRACKET 
          { 
            // Verificamos que la expresion interna sea un entero.
            if ($3->type->toString() != "Int") {
              addError(
                "Expected \033[1;3mInt\033[0m but \033[1;3m" + $1->toString() +
                "\033[0m found."
              );
              $$ = predefinedTypes["$Error"];
            }
            else if ($1->toString() == "$Error") {
              $$ = predefinedTypes["$Error"];
            } 
            else {
              $$ = new ArrayType($1, $3);
              $$->danger = $1->danger;
              $$->incomplete = $1->incomplete;
            }
          }

        | Type OPEN_BRACKET CLOSE_BRACKET 
          { 
            if ($1->toString() == "$Error") {
              $$ = predefinedTypes["$Error"];
            } 
            else {
              NodeINT *size = new NodeINT(0);
              size->addr = tac->newTemp();
              $$ = new ArrayType($1, size);
              $$->danger = $1->danger;
              $$->incomplete = $1->incomplete;
            }
          }

        | POINTER Type 
          { 
            if ($2->toString() != "$Error") {
              $$ = new PointerType($2); 
              $$->danger = false;
              $$->incomplete = $2->incomplete;
            } 
            else {
              $$ = predefinedTypes["$Error"];
            }
          }

        | ID 
          {
            Entry *e;
            // Verificamos que el identificador existe y corresponde a una estructura.
            if ((e = table->lookup(*$1)) == NULL) {
              addError("'\033[1;3m" + *$1 + "\033[0m' wasn't declared.");
              $$ = predefinedTypes["$Error"];
            } 
            else if (
              e->category != "Type" &&
              e->category != "Structure" && 
              e->category != "Incomplete Structure"
              ) {
              addError("'\033[1;3m" + *$1 + "\033[0m' isn't a type.");
              $$ = predefinedTypes["$Error"];
            } 
            else {
              $$ = new PrimitiveType(*$1);
              $$->width = ((StructureEntry*) e)->width;
              // Verificamos si estamos usando un tipo estructura dentro de la definicion
              // de la estructura.
              if ($$->width == -1) {
                $$->danger = true;
              }
              if (((StructureEntry*) e)->incomplete) {
                $$->incomplete = e->id;
                $$->danger = true;
              }
            }
          }

        | OPEN_PAR Type CLOSE_PAR             { $$ = $2; }
        | T_BOOL                              { $$ = predefinedTypes["Bool"]; }
        | T_CHAR                              { $$ = predefinedTypes["Char"]; }
        | T_INT                               { $$ = predefinedTypes["Int"]; }
        | T_FLOAT                             { $$ = predefinedTypes["Float"]; }
        | T_STRING                            
          { 
            ExpressionNode *size = new NodeINT(0);
            size->addr = tac->newTemp();
            $$ = new ArrayType(predefinedTypes["Char"], size, true); 
          }
        ;


/* ======================= EXPRESSIONS =============================== */
  W     : /* lambda */        
          { 
            $$ = new string(tac->newLabel()); 
            tac->gen("@label " + *$$);
          }

  Exp   : 
        Exp EQUIV W Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type, *t2 = $4->type, *type;

            if (t1->toString()[0] == '^' && t2->toString()[0] == '^') {
              type = predefinedTypes["Bool"];
            }
            else {
              type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            }

            $$ = new NodeBinaryOperator($1, *$2, $4, type); 

            if (t1->toString() == "Bool" && t2->toString() == "Bool") {
              // Si las expressiones son booleanas, entonces primero tenemos que usar
              // backpatching para asignar los correspondientes valores y luego 
              // compararlos.
              string label;

              // Usamos backpatching sobre la truelist de la primera expresion para 
              // realizar un salto a la asignacion de True y luego saltar sobre la
              // asignacion de False.
              $1->addr = tac->newTemp();
              tac->backpatch($1->truelist, tac->instructions.size());
              tac->gen("assignb " + $1->addr + " True");
              label = "Equiv" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);
              
              // Usamos backpatching sobre la falselist de la primera expresion para 
              // realizar un salto a la asignacion de False y luego crear la etiqueta
              // de salto de la asignacion del True.
              tac->backpatch($1->falselist, tac->instructions.size());
              tac->gen("assignb " + $1->addr + " False");
              tac->gen("@label " + label);

              // Saltamos a la segunda expresion
              tac->gen("goto " + *$3);

              // Repetimos el mismo proceso de la primera expresion.
              $4->addr = tac->newTemp();
              tac->backpatch($4->truelist, tac->instructions.size());
              tac->gen("assignb " + $4->addr + " True");
              label = "Equiv" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);
              tac->backpatch($4->falselist, tac->instructions.size());
              tac->gen("assignb " + $4->addr + " False");
              tac->gen("@label " + label);

            }

            string assign = $1->type->width == 1 ? "assignb" : "assignw";
            tac->genTACinstr(assign, "eq", "test", $1->addr, $4->addr, false, false);

            // Como el resultado es booleano, creamos la truelist y falselist 
            // correspondiente.
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif _ test");
            tac->gen("goto _");
          }

        | Exp NOT_EQUIV W Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $4->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $4, type); 

            if (t1->toString() == "Bool" && t2->toString() == "Bool") {
              // Si las expressiones son booleanas, entonces primero tenemos que usar
              // backpatching para asignar los correspondientes valores y luego 
              // compararlos.
              string label;

              // Usamos backpatching sobre la truelist de la primera expresion para 
              // realizar un salto a la asignacion de True y luego saltar sobre la
              // asignacion de False.
              $1->addr = tac->newTemp();
              tac->backpatch($1->truelist, tac->instructions.size());
              tac->gen("assignb " + $1->addr + " True");
              label = "Nequiv" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);

              // Usamos backpatching sobre la falselist de la primera expresion para 
              // realizar un salto a la asignacion de False y luego crear la etiqueta
              // de salto de la asignacion del True.
              tac->backpatch($1->falselist, tac->instructions.size());
              tac->gen("assignb " + $1->addr + " False");
              tac->gen("@label " + label);

              // Saltamos a la segunda expresion
              tac->gen("goto " + *$3);

              // Repetimos el mismo proceso de la primera expresion.
              $4->addr = tac->newTemp();
              tac->backpatch($4->truelist, tac->instructions.size());
              tac->gen("assignb " + $4->addr + " True");
              label = "Nequiv" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);
              tac->backpatch($4->falselist, tac->instructions.size());
              tac->gen("assignb " + $4->addr + " False");
              tac->gen("@label " + label);
            }

            string assign = $1->type->width == 1 ? "assignb" : "assignw";
            tac->genTACinstr(assign, "neq", "test", $1->addr, $4->addr, false, false);

            // Como el resultado es booleano, creamos la truelist y falselist 
            // correspondiente.
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif _ test");
            tac->gen("goto _");
          }

        | Exp OR M Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $4->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $4, type); 

            // Aplicamos backpatching.
            tac->backpatch($1->falselist, $3);
            $$->truelist = merge<unsigned long long>($1->truelist, $4->truelist);
            $$->falselist = $4->falselist;
          }

        | Exp AND M Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $4->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $4, type); 

            // Aplicamos backpatching.
            tac->backpatch($1->truelist, $3);
            $$->falselist = merge<unsigned long long>($1->falselist, $4->falselist);
            $$->truelist = $4->truelist;
          }

        | NOT Exp 
          { 
            // Verificamos que el tipo coincide con la operacion.
            Type *type = verifyUnaryOpType(*$1, $2->type->toString());
            $$ = new NodeUnaryOperator(*$1, $2, type); 

            // Aplicamos backpatching.
            $$->truelist = $2->falselist;
            $$->falselist = $2->truelist;
          }

        | Exp LESS_THAN Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type);  

            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "lt", "test", $1->addr, $3->addr, f1, f2);

            // Aplicamos backpatching.
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif _ test");
            tac->gen("goto _");
          }

        | Exp LESS_EQUAL_THAN Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "leq", "test", $1->addr, $3->addr, f1, f2);

            // Aplicamos backpatching.
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif _ test");
            tac->gen("goto _");
          }

        | Exp GREATER_THAN Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "gt", "test", $1->addr, $3->addr, f1, f2);

            // Aplicamos backpatching.
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif _ test");
            tac->gen("goto _"); 
          }

        | Exp GREATER_EQUAL_THAN Exp  
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "geq", "test", $1->addr, $3->addr, f1, f2);

            // Aplicamos backpatching.
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif _ test");
            tac->gen("goto _");
          }

        | Exp PLUS Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = type->toString() == "Float" ? tac->newFloat(): tac->newTemp();
            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "add", $$->addr, $1->addr, $3->addr, f1, f2);
          }

        | Exp MINUS Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = type->toString() == "Float" ? tac->newFloat(): tac->newTemp();
            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "sub", $$->addr, $1->addr, $3->addr, f1, f2);
          }

        | Exp ASTERISK Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = type->toString() == "Float" ? tac->newFloat(): tac->newTemp();
            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "mult", $$->addr, $1->addr, $3->addr, f1, f2);
          }

        | Exp DIV Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = type->toString() == "Float" ? tac->newFloat(): tac->newTemp();
            bool f1 = t1->toString() == "Float", f2 = t2->toString() == "Float";
            tac->genTACinstr("assignw", "div", $$->addr, $1->addr, $3->addr, f1, f2);
          }

        | Exp MODULE Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->genTACinstr("assignw", "mod", $$->addr, $1->addr, $3->addr, false, false);
          }

        | MINUS Exp  
          { 
            // Verificamos que el tipo coincide con la operacion
            Type *type = verifyUnaryOpType(*$1, $2->type->toString());
            $$ = new NodeUnaryOperator(*$1, $2, type); 

            // Agregamos las instrucciones del TAC.
            bool f = type->toString() == "Float";
            $$->addr = f ? tac->newFloat() : tac->newTemp();

            string raddr;
            if ($2->addr.back() == ']') {
              raddr = f ? tac->newFloat() : tac->newTemp();
              tac->gen("assignw " + raddr + " " + $2->addr);
            }
            else {
              raddr = $2->addr;
            }

            tac->gen("minus " + $$->addr + " " + raddr);
          }

        | PLUS Exp
          { 
            // Verificamos que el tipo coincide con la operacion.
            verifyUnaryOpType(*$1, $2->type->toString());
            $$ = $2; 
          }

        | Exp POWER Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType(*$2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, *$2, $3, type); 

            // Generamos el codigo TAC para la exponencial.
            string addr1, addr2;
            if (type->toString() == "Float") {
              $$->addr = tac->newFloat();
              addr1 = tac->newFloat(); 
            }
            else {
              $$->addr = tac->newTemp();
              addr1 = tac->newTemp(); 
            }
            addr2 = tac->newTemp();
  
            tac->gen("assignw " + addr1 + " " + $1->addr);
            tac->gen("assignw " + addr2 + " " + $3->addr);

            // Inicializamos el resultado en 1
            tac->gen("assignw " + $$->addr + " 1");

            // Creamos una etiqueta para el loop
            string loop_name = tac->newLabel();

            // Verificamos si el exponente es negativo o positivo y realizamos el salto
            // correspondiente
            tac->gen("lt test " + addr2 + " 0");
            // Si es negativo, saltamos a la version negativa del exponente.
            tac->gen("goif " + loop_name + "_neg test");
            
            // Version positiva del exponente
            tac->gen("@label " + loop_name + "_pos");
            // Verificamos si el exponente es igual a 0, en ese caso salimos del bucle
            tac->gen("eq test " + addr2 + " 0");
            tac->gen("goif " + loop_name + "_end test");
            // Siguiente iteracion
            tac->gen("mult " + $$->addr + " " + $$->addr + " " + addr1);
            tac->gen("sub " + addr2 + " " + addr2 + " 1");
            tac->gen("goto " + loop_name + "_pos");

            // Version negativa del exponente
            tac->gen("@label " + loop_name + "_neg");
            // Siguiente iteracion
            tac->gen("div " + $$->addr + " " + $$->addr + " " + addr1);
            tac->gen("add " + addr2 + " " + addr2 + " 1");
            // Verificamos si el exponente es igual a 0, en ese caso salimos del bucle
            tac->gen("neq test " + addr2 + " 0");
            tac->gen("goif " + loop_name + "_neg test");

            // Final del ciclo
            tac->gen("@label " + loop_name + "_end");
          }

        | Exp OPEN_BRACKET Exp CLOSE_BRACKET 
          { 
            string ltype = $1->type->toString();
            string itype = $3->type->toString();

            // Verificamos que el arreglo no sea un expresion erronea,
            if (ltype == "$Error") {
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]);
            }
            // O que no sea un arreglo.
            else if ($1->type->category != "Array") {
              addError("'\033[1;3m" + ltype + "\033[0m' type can't be indexed.");
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]); 
            } 
            // O que la expresion de acceso no sea entera.
            else if (itype != "$Error" && itype != "Int") {
              addError(
                "Expected a '\033[1;3mInt\033[0m' but '\033[1;3m" +
                itype + "\033[0m' found."
              );
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]); 
            }
            // O sea erronea.
            else if (itype == "$Error") {
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]);
            }
            
            else {
              Type *type = ((ArrayType*) $1->type)->type;
              $$ = new NodeArrayAccess($1, $3, type);

              string arraddr, raddr;
              if ($1->addr.back() == ']') {
                arraddr = tac->newTemp();
                tac->gen("assignw " + arraddr + " " + $1->addr);
              }
              else {
                arraddr = $1->addr;
              }
              if ($3->addr.back() == ']') {
                raddr = tac->newTemp();
                tac->gen("assignw " + raddr + " " + $3->addr);
              }
              else {
                raddr = $3->addr;
              }

              $$->addr = tac->newTemp();
              tac->gen("mult " + $$->addr + " " + to_string(type->width) + " " + raddr);
              tac->gen("add " + $$->addr + " " + $$->addr + " 4");
              $$->addr = arraddr + "[" + $$->addr + "]";

              // Si el tipo base es booleano, aplicamos el backpatching correspondiente.
              if (type->toString() == "Bool") {
                string raddr = tac->newTemp();
                tac->gen("assignb " + raddr + " " + $$->addr);

                $$->truelist = {tac->instructions.size()};
                tac->gen("goif _ " + raddr);
                $$->falselist = {tac->instructions.size()};
                tac->gen("goto _");
              }
            }
          }
        | POINTER Exp  
          { 
            // Verificamos que el tipo base no sea erroneo.
            string type = $2->type->toString();
            if (type == "$Error") {
              $$ = new NodePointer($2, predefinedTypes["$Error"]);
            } 
            // O no sea un puntero.
            else if ($2->type->category != "Pointer") {
              addError("'\033[1;3m" + type + "\033[0m' type can't be desreferenced.");
              $$ = new NodePointer($2, predefinedTypes["$Error"]); 
            } 
            // O no sea ^Unit
            else if (type == "^(Unit)") {
              addError("\033[1;3mNULL\033[0m can't be desreferenced.");
              $$ = new NodePointer($2, predefinedTypes["$Error"]); 
            }
            else {
              Type *type = ((PointerType*) $2->type)->type;
              $$ = new NodePointer($2, type); 

              string raddr;
              if ($2->addr.back() == ']') {
                raddr = tac->newTemp();
                tac->gen("assignw " + raddr + " " + $2->addr);
              }
              else {
                raddr = $2->addr;
              }

              // La desreferenciacion es equivalente al acceso de memoria sin 
              // desplazamiento
              $$->addr = raddr + "[0]";

              // Si el tipo base es booleano, aplicamos el backpatching correspondiente.
                if (type->toString() == "Bool") {
                  string raddr = tac->newTemp();
                  tac->gen("assignb " + raddr + " " + $$->addr);

                  $$->truelist = {tac->instructions.size()};
                  tac->gen("goif _ " + raddr);
                  $$->falselist = {tac->instructions.size()};
                  tac->gen("goto _");
                }
            }
          }

        | Exp DOT ID 
          { 
            // Verificamos que el tipo base no es erronea.
            if ($1->type->toString() == "$Error") {
              $$ = new NodeDot($1, *$3, predefinedTypes["$Error"]);
            } 
            // O no sea un tipo "primitivo" (extendiendo a las estructuras).
            else if ($1->type->category != "Primitive") {
              addError(
                "'\033[1;3m" + $1->type->toString() + 
                "\033[0m' type can't be accessed."
              );
              $$ = new NodeDot($1, *$3, predefinedTypes["$Error"]);
            } 
            else {
              Entry *e = table->lookup($1->type->toString()); 
              // O no sea una estructura.
              if (e->category != "Structure") {
                addError(
                  "'\033[1;3m" + $1->type->toString() + 
                  "\033[0m' type can't be accessed."
                );
                $$ = new NodeDot($1, *$3, predefinedTypes["$Error"]);
              } 
              
              else {
                StructureEntry *se = (StructureEntry*) e;
                VarEntry *field = (VarEntry*) table->lookup(*$3, se->def_scope);

                // O no tenga el campo indicado.
                if (field == NULL) {
                  addError(
                    "'\033[1;3m" + $1->type->toString() + 
                    "\033[0m' has no member '\033[1;3m" + 
                    *$3 + "\033[0m'."
                  );
                  $$ = new NodeDot($1, *$3, predefinedTypes["$Error"]);
                } 

                else {
                  $$ = new NodeDot($1, *$3, field->type);

                  string raddr;
                  if ($1->addr.back() == ']') {
                    raddr = tac->newTemp();
                    tac->gen("assignw " + raddr + " " + $1->addr);
                  }
                  else {
                    raddr = $1->addr;
                  }

                  // El acceso a campo es equivalente al acceso a memoria desplazado
                  // por el offset del campo.
                  $$->addr = raddr + "[" + to_string(field->offset) + "]";

                  // Si el campo es booleano agregamos el backpatching correspondiente.
                  if (field->type->toString() == "Bool") {
                    string raddr = tac->newTemp();
                    tac->gen("assignb " + raddr + " " + $$->addr);

                    $$->truelist = {tac->instructions.size()};
                    tac->gen("goif _ " + raddr);
                    $$->falselist = {tac->instructions.size()};
                    tac->gen("goto _");
                  }
                }
              }
            } 
          }

        | ID 
          { 
            Entry *e;

            // Verificamos que el ID este declarado.
            if ((e = table->lookup(*$1)) == NULL) {
              addError("'\033[1;3m" + *$1 + "\033[0m' wasn't declared.");
              $$ = new NodeID(*$1, predefinedTypes["$Error"]);
            } 
            // Y sea una variable.
            else if (e->category != "Var") {
              addError("'\033[1;3m" + *$1 + "\033[0m' isn't a variable.");
              $$ = new NodeID(*$1, predefinedTypes["$Error"]);
            } 
            else {
              VarEntry *ve = (VarEntry*) e;
              $$ = new NodeID(*$1, ve->type); 

              // Si nos encontramos fuera de una funcion, usamos la etiqueta de la 
              // variable.
              if (table->ret_type == "") {
                $$->addr = ve->addr;
              }
              // Si no, usamos desplazamiento en memoria.
              else {
                $$->addr = "BASE[" + to_string(ve->offset) + "]";
              }

              // Si la variable es booleana agregamos el backpatching correspondiente.
              if (ve->type->toString() == "Bool") {
                string raddr;

                if ($$->addr.back() == ']') {
                  raddr = tac->newTemp();
                  tac->gen("assignb " + raddr + " " + $$->addr);
                }
                else {
                  raddr = $$->addr;
                }

                $$->truelist = {tac->instructions.size()};
                tac->gen("goif _ " + raddr);
                $$->falselist = {tac->instructions.size()};
                tac->gen("goto _");
              }
            }
          }

        | NEW Type  
          { 
            if ($2->toString() != "$Error") {
              $$ = new NodeNew($2); 
              $$->addr = tac->newTemp();
              string type = $2->toString();

              // En caso de que el tipo sea un arreglo o estructura (registro o union) 
              // reservamos la memoria necesaria. 
              if (type.back() == ']') {
                allocArray($2, $$->addr);
              }
              else if (! predefinedTypes.count(type) && type[0] != '^') {
                allocStruct($2, $$->addr);
              }
              else {
                tac->gen("malloc " + $$->addr + " " + to_string($2->width));
              }
            }

            else {
              $$ = new ExpressionNode();
              $$->type = predefinedTypes["$Error"];
            }
          }

        | OPEN_PAR Exp M ASSIGNMENT Exp CLOSE_PAR         
            { 
              string ltype = $2->type->toString();
              string rtype = $5->type->toString();

              // Verificamos que alguna de las expresiones no sea erronea.
              if (ltype == "$Error" || rtype == "$Error") {
                $$ = new ExpressionNode();
                $$->type = predefinedTypes["$Error"];
              } 
              // O que la primera expresion no sea un L-Value.
              else if (! $2->is_lvalue) {
                addError(
                  "Can't assign to a R-Value."
                );
                $$ = new ExpressionNode();
                $$->type = predefinedTypes["$Error"];
              }
              // O que los tipos de ambas expresiones no coincidan
              else if (! typecmp(ltype, rtype)) {
                addError(
                  "Can't assign a '\033[1;3m" + rtype +
                  "\033[0m' to a '\033[1;3m" + ltype + "\033[0m'."
                );
                $$ = new ExpressionNode();
                $$->type = predefinedTypes["$Error"];
              } 
              
              else {
                $$ = new NodeAssign($2, $5); 
                $$->type = $5->type;

                if (rtype != "Bool") {
                  string raddr;
                  string assign_type = ltype == "Char" ? "assignb" : "assignw";

                  if ($2->addr.back() == ']' && $5->addr.back() == ']') {
                    raddr = rtype == "Float" ? tac->newFloat() : tac->newTemp();
                    tac->gen(assign_type + " " + raddr + " " + $5->addr);
                  }
                  else {
                    raddr = $5->addr;
                  }

                  // Si la expresion no es booleana, se realiza la asignacion al L-Value
                  // y a la expresion que retorna la asignacion.
                  $$->addr = rtype == "Float" ? tac->newFloat() : tac->newTemp();
                  tac->gen(assign_type + " " + $2->addr + " " + raddr);
                  tac->gen(assign_type + " " + $$->addr + " " + raddr);
                }
                else {
                  // Eliminamos las dos instrucciones que debieron haber surgido por 
                  // tener un lvalue booleano.
                  tac->instructions[$3 - 2] = "";
                  tac->instructions[$3 - 1] = "";

                  // En caso contrario tenemos que usar backpatching para hacer la 
                  // asignacion correspondiente.
                  tac->backpatch($5->truelist, tac->instructions.size());
                  tac->gen("assignb " + $2->addr + " True");
                  $$->truelist = {tac->instructions.size()};
                  tac->gen("goto _");

                  tac->backpatch($5->falselist, tac->instructions.size());
                  tac->gen("assignb " + $2->addr + " False");
                  $$->falselist = {tac->instructions.size()};
                  tac->gen("goto _");
                }

              }
            }

        | OPEN_PAR Exp CLOSE_PAR      { $$ = $2; }

        | FuncCall                    { $$ = $1; }

        | Array                       { $$ = $1; }

        | TRUE 
          { 
            $$ = new NodeBOOL(true); 
            $$->truelist = {tac->instructions.size()};
            tac->gen("goto _");
          }

        | FALSE
          { 
            $$ = new NodeBOOL(false);
            $$->falselist = {tac->instructions.size()};
            tac->gen("goto _");
          }

        | CHAR
          { 
            $$ = new NodeCHAR($1);
            $$->addr = tac->newTemp();
            int c = $1;
            tac->gen("assignb " + $$->addr + " " + to_string(c)); 
          }

        | INT
          { 
            $$ = new NodeINT($1); 
            $$->addr = tac->newTemp();
            tac->gen("assignw " + $$->addr + " " + to_string($1));
          }

        | FLOAT 
          { 
            $$ = new NodeFLOAT($1); 
            $$->addr = tac->newFloat();
            tac->gen("assignw " + $$->addr + " " + to_string($1));
          }

        | STRING 
          { 
            $$ = new NodeSTRING(*$1); 
            $$->addr = tac->newStr(*$1);
            ArrayType *t = (ArrayType*) $$->type;
            t->size->addr = tac->newTemp();
            tac->gen("assignw " + $$->addr + "[0] " + to_string($1->size()-2));
          }
        ;


/* ======================= ARRAYS ==================================== */
  Array     : OPEN_BRACKET ArrExp CLOSE_BRACKET   
              { 
                // Verificamos que no hubo errores en las expresiones que conforman el
                // arreglo.
                string type = $2->type->toString();
                if (type == "^(Unit)") {
                  addError("All elements of the array cannot be \033[1;3mNULL\033[0m.");
                  $$ = new NodeArray($2, predefinedTypes["$Error"]); 
                }
                else if (type == "$Error") {
                  $$ = new NodeArray($2, predefinedTypes["$Error"]); 
                }
                else {
                  int size = ((NodeArrayElems*) $2)->current_size;

                  // Longitud del arreglo.
                  ExpressionNode *nsize = new NodeINT(size);
                  nsize->addr = tac->newTemp();
                  tac->gen("assignw " + nsize->addr + " " + to_string(size));

                  // Tipo "Arreglo"
                  Type *t = new ArrayType($2->type, nsize);

                  // Expresion del tipo Arreglo
                  $$ = new NodeArray($2, t);

                  int offset = table->newOffset(t);

                  // Si no estamos en una funcion
                  if (table->ret_type == "") {
                    // Creamos una nueva etiqueta para reservar memoria.
                    $$->addr = tac->newTemp();
                  }
                  else {
                    // Si nos encontramos dentro de una funcion, el arreglo sera
                    // almacenado dinamicamente a pesar de ser constante.
                    $$->addr = "BASE[" + to_string(offset) + "]";
                  }

                  allocArray($$->type, $$->addr);

                  // Realizamos la asignacion de cada expresion del arreglo.
                  NodeArrayElems *exp = $2;
                  string raddr, laddr;
                  string assign_type = type == "Bool" || type == "Char" ? "assignb" : "assignw";

                  if ($$->addr.back() == ']') {
                    laddr = tac->newTemp();
                    tac->gen("assignw " + laddr + " " + $$->addr);
                  }
                  else {
                    laddr = $$->addr;
                  }

                  while (--size >= 0) {
                    if (exp->rvalue->addr.back() == ']') {
                      raddr = type == "Float" ? tac->newFloat() : tac->newTemp();
                      tac->gen(assign_type + " " + raddr + " " + exp->rvalue->addr);
                    }
                    else {
                      raddr = exp->rvalue->addr;
                    }
                    
                    tac->gen(
                      assign_type + " " + laddr + "[" + 
                      to_string(size * $2->type->width + 4) + "] " + raddr
                    );
                    exp = exp->head;
                  }

                } 
              }
            ;

  ArrExp    : ArrElems Exp  
              { 
                Type *type;
                int size;
                string type1 = $1 == NULL ? "" : $1->type->toString();
                string type2 = $2->type->toString();

                if ($1 == NULL) {
                  type = $2->type;
                  size = 1;
                } 
                
                else if (type1 == "$Error" || type2 == "$Error") {
                  type = predefinedTypes["$Error"];
                  size = 0;
                } 
                
                else if (! typecmp(type1, type2) && ! typecmp(type2, type1)) {
                  addError(
                    "All elements of an array must have the same type"
                    ", but found '\033[1;3m" + type1 + "\033[0m' and "
                    "'\033[1;3m" + type2 + "\033[0m'."
                  );
                  type = predefinedTypes["$Error"];
                  size = 0;
                } 

                else {
                  if (type1 != "" && type2 == "^(Unit)") {
                    type = $1->type;
                  } 
                  else {
                    type = $2->type;
                  }
                  size = $1->current_size + 1;
                }

                if (type->toString() != "$Error" && $2->type->toString() == "Bool") {
                  string label;
                  $2->addr = tac->newTemp();

                  tac->backpatch($2->truelist, tac->instructions.size());
                  tac->gen("assignb " + $2->addr + " True");

                  label = "Bool" + to_string(tac->instructions.size() + 2);
                  tac->gen("goto " + label);
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assignb " + $2->addr + " False");
                  tac->gen("@label " + label);
                }

                $$ = new NodeArrayElems($1, type, $2, size);
              }
            ;

  ArrElems  : /* lambda */                        { $$ = NULL; }
            | ArrElems Exp COMMA                  
              { 
                Type *type;
                string type1 = $1 == NULL ? "" : $1->type->toString();
                string type2 = $2->type->toString();
                int size;

                if ($1 == NULL) {
                  type = $2->type;
                  size = 1;
                } 

                else if (type1 == "$Error" || type2 == "$Error") {
                  type = predefinedTypes["$Error"];
                  size = 0;
                } 

                else if (type1 != type2) {
                  addError(
                    "All elements of an array must have the same type"
                    ", but found '\033[1;3m" + type1 + "\033[0m' and "
                    "'\033[1;3m" + type2 + "\033[0m'."
                  );
                  type = predefinedTypes["$Error"];
                  size = 0;
                } 

                else {
                  type = $2->type;
                  size = $1->current_size + 1;
                }

                if (type->toString() != "$Error" && $2->type->toString() == "Bool") {
                  string label;
                  $2->addr = tac->newTemp();

                  tac->backpatch($2->truelist, tac->instructions.size());
                  tac->gen("assignb " + $2->addr + " True");

                  label = "Bool" + to_string(tac->instructions.size() + 2);
                  tac->gen("goto " + label);
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assignb " + $2->addr + " False");
                  tac->gen("@label " + label);
                }

                $$ = new NodeArrayElems($1, type, $2, size);
              }
            ;


/* ======================= FUNCTION CALLS ============================ */
  FuncCall        : ID OPEN_PAR ArgsExp CLOSE_PAR   
                    { 
                      if ($3 == NULL) {
                        $$ = new ExpressionNode();
                        $$->type = predefinedTypes["$Error"];
                      } 
                      
                      else {
                        Type *type = NULL;
                        Entry *e;
                        vector<tuple<string, string, string, bool>> refs;

                        if ((e = table->lookup(*$1)) == NULL) {
                          addError("'\033[1;3m" + *$1 + "\033[0m' wasn't declared.");
                          type = predefinedTypes["$Error"];
                        } 
                        
                        else if (e->category!="Function" && e->category!="Declaration") {
                          addError("'\033[1;3m" + *$1 + "\033[0m' isn't a function.");
                          type = predefinedTypes["$Error"];
                        } 

                        else if (
                          e->category == "Function" && 
                          ((FunctionEntry*) e)->optargs_addr == ""
                        ) {
                          addError(
                            "An optional parameter cannot have a default value "
                            "that depends on the function being defined."
                          );
                          type = predefinedTypes["$Error"];
                        }
                        
                        else {
                          FunctionEntry *fe = (FunctionEntry*) e;
                          bool correctTypes = true, assigned;
                          string type_str, addr, paddr, raddr;

                          int numPositional = $3->positionalArgs.size(), i = 0;
                          int c_offset = 0, opts = 0;

                          for (tuple<string, string, bool, bool> arg : fe->args) {
                            string assign_type = get<1>(arg) == "Bool" || get<1>(arg) == "Char" ? 
                              "assignb" : "assignw";
                            assigned = false;
                            
                            if (assign_type.back() == 'w' && c_offset % 4 != 0) {
                              int diff = 4 - c_offset % 4;
                              c_offset += diff;
                            }

                            if (i < numPositional) {
                              type_str = $3->positionalArgs[i]->type->toString();
                              addr = $3->positionalArgs[i]->addr;

                              if (get<1>(arg) != type_str) {
                                addError(
                                  "Argument '\033[1;3m" + get<0>(arg) + 
                                  "\033[0m' " + "must be '\033[1;3m" + get<1>(arg) + 
                                  "\033[0m' but '\033[1;3m" + type_str + 
                                  "\033[0m' found."
                                );
                                correctTypes = false;
                              }

                              if ($3->keywords.count(get<0>(arg))) {
                                addError(
                                  "Got multiple values of '\033[1;3m" + 
                                  get<0>(arg) + "\033[0m'."
                                );
                                correctTypes = false;
                              }

                              if (! $3->positionalArgs[i]->is_lvalue && get<2>(arg)) {
                                addError(
                                  "Argument '\033[1;3m" + get<0>(arg) + 
                                  "\033[0m' " + "is passed by reference, but a L-Value "
                                  "was not passed."
                                );
                                correctTypes = false;
                              }
                              // Si el pase es por referencia y es un tipo basico
                              else if (
                                get<2>(arg) && type_str.back() != ']' && 
                                (predefinedTypes.count(type_str) || type_str[0] == '^')
                              ) {
                                refs.push_back({
                                  assign_type,
                                  $3->positionalArgs[i]->addr,
                                  "lastbase[" + to_string(c_offset) + "]",
                                  type_str == "Float"
                                });
                              }
                              // Si el pase no es por referencia, es un tipo arreglo y no
                              // es un string literal
                              else if (! get<2>(arg) && type_str.back() == ']') {
                                if (! $3->positionalArgs[i]->is_lit) {
                                  // Creamos una copia del arreglo
                                  addr = tac->newTemp();
                                  copyArray(
                                    $3->positionalArgs[i]->type, 
                                    addr, 
                                    $3->positionalArgs[i]->addr
                                  );
                                }
                                else {
                                  addr = $3->positionalArgs[i]->addr;
                                }
                              }
                              // Si el pase no es por referencia y es una estructura
                              else if (! get<2>(arg) && ! predefinedTypes.count(type_str) && type_str[0] != '^') {
                                // Creamos una copia de la estructura
                                addr = tac->newTemp();
                                copyStruct(
                                  $3->positionalArgs[i]->type, 
                                  addr, 
                                  $3->positionalArgs[i]->addr
                                );
                              }
                              else {
                                addr = $3->positionalArgs[i]->addr;
                              }

                              // Por ultimo, verificamos si la direccion es un acceso a
                              // memoria
                              if (addr.back() == ']') {
                                addr = type_str == "Float" ? tac->newFloat() : tac->newTemp();
                                tac->gen(assign_type + " " + addr + " " + $3->positionalArgs[i]->addr);
                              }

                              paddr = tac->newTemp();
                              tac->gen("param " + paddr + " " + to_string(c_offset));
                              tac->gen(assign_type + " " + paddr + "[0] " + addr);
                              assigned = true;
                            } 
                            
                            else if ($3->keywords.count(get<0>(arg))) {
                              type_str = $3->namedArgs[get<0>(arg)]->type->toString();
                              addr = $3->namedArgs[get<0>(arg)]->addr;

                              if (get<1>(arg) != type_str) {
                                addError(
                                  "Argument '\033[1;3m" + get<0>(arg) + 
                                  "\033[0m' " + "must be '\033[1;3m" + get<1>(arg) + 
                                  "\033[0m' but '\033[1;3m" + type_str + 
                                  "\033[0m' found."
                                );

                                correctTypes = false;
                              }

                              if (! $3->namedArgs[get<0>(arg)]->is_lvalue && get<2>(arg)) {
                                addError(
                                  "Argument '\033[1;3m" + get<0>(arg) + 
                                  "\033[0m' " + "is passed by reference, but a L-Value "
                                  "was not passed."
                                );
                                correctTypes = false;
                              }
                              // Si el pase es por referencia y es un tipo basico
                              else if (
                                get<2>(arg) && type_str.back() != ']' && 
                                (predefinedTypes.count(type_str) || type_str[0] == '^')
                              ) {
                                refs.push_back({
                                  assign_type,
                                  addr, 
                                  "lastbase[" + to_string(c_offset) + "]",
                                  type_str == "Float"
                                });
                              }
                              // Si el pase no es por referencia y es un tipo arreglo
                              else if (! get<2>(arg) && type_str.back() == ']') {
                                if (! $3->namedArgs[get<0>(arg)]->is_lit) {
                                  // Creamos una copia del arreglo
                                  addr = tac->newTemp();
                                  copyArray(
                                    $3->namedArgs[get<0>(arg)]->type, 
                                    addr, 
                                    $3->namedArgs[get<0>(arg)]->addr
                                  );
                                }
                                else {
                                  addr = $3->namedArgs[get<0>(arg)]->addr;
                                }
                              }
                              // Si el pase no es por referencia y es una estructura
                              else if (! get<2>(arg) && ! predefinedTypes.count(type_str) && type_str[0] != '^') {
                                // Creamos una copia de la estructura
                                addr = tac->newTemp();
                                copyStruct(
                                  $3->namedArgs[get<0>(arg)]->type, 
                                  addr, 
                                  $3->namedArgs[get<0>(arg)]->addr
                                );
                              }
                              else {
                                addr = $3->namedArgs[get<0>(arg)]->addr;
                              }

                              // Por ultimo, verificamos si la direccion es un acceso a
                              // memoria
                              if (addr.back() == ']') {
                                addr = type_str == "Float" ? tac->newFloat() : tac->newTemp();
                                tac->gen(assign_type + " " + addr + " " + $3->namedArgs[get<0>(arg)]->addr);
                              }
                              
                              $3->keywords.erase(get<0>(arg));

                              paddr = tac->newTemp();
                              tac->gen("param " + paddr + " " + to_string(c_offset));
                              tac->gen(assign_type + " " + paddr + "[0] " + addr);
                              assigned = true;
                            } 
                            
                            else if (! get<3>(arg)) {
                              addError(
                                "Missing required positional arguments."
                              );
                              correctTypes = false;
                            }

                            if (get<3>(arg)) {
                              if (e->category == "Declaration") {
                                // Almacenamos el scope y el numero de la instruccion donde
                                // se usa el arreglo de variables
                                if (tac->calllist.count(fe->id)) {
                                  tac->calllist[fe->id].push_back({
                                    tac->instructions.size(),
                                    table->scopeStack
                                  });
                                }
                                else {
                                  tac->calllist[fe->id] = {{
                                    tac->instructions.size(),
                                    table->scopeStack
                                  }};
                                }
                                tac->gen(
                                  "assignb _[" + to_string(opts) + "] " 
                                  + (assigned ? "1" : "0")
                                );
                              }
                              else {
                                tac->gen(
                                  "assignb " + fe->optargs_addr + 
                                  "[" + to_string(opts) + "] " + (assigned ? "1" : "0")
                                );
                              }

                              opts++;
                            }

                            c_offset += assign_type.back() == 'w' ? 4 : 1;
                            i++;
                          }

                          if ($3->keywords.size()) {
                            string err = "Got unexpected keywords: ";
                            for (string k : $3->keywords) {
                              err += "'\033[1;3m" + k + "\033[0m', ";
                            }
                            addError(err);
                            correctTypes = false;
                          }

                          if (! correctTypes) {
                            type = predefinedTypes["$Error"];
                          }
                        }


                        if (type == NULL) {
                          FunctionEntry *fe = (FunctionEntry*) e;
                          type = fe->return_type;
                          $$ = new NodeFunctionCall(*$1, $3, false, type); 
                          $$->addr = type->toString() == "Float" ? tac->newFloat() : tac->newTemp();
                          string n_args = to_string(fe->args.size());

                          if (e->category == "Declaration") {
                            // Almacenamos el scope y el numero de la instruccion donde
                            // se llamo a la funcion 
                            if (tac->functionlist.count(fe->id)) {
                              tac->functionlist[fe->id].push_back({
                                tac->instructions.size(),
                                table->scopeStack
                              });
                            }
                            else {
                              tac->functionlist[fe->id] = {{
                                tac->instructions.size(),
                                table->scopeStack
                              }};
                            }

                            tac->gen("call " + $$->addr + " _  " + n_args);
                          }

                          else {
                            tac->gen("call " + $$->addr + " " + fe->addr + " " + n_args);
                          }

                          // Realizamos las asignaciones por referencia correspondientes.
                          string raddr;
                          for (tuple<string, string, string, bool> assign : refs) {
                            raddr = get<3>(assign) ? tac->newFloat() : tac->newTemp();
                            tac->gen(get<0>(assign) + " " + raddr + " " + get<2>(assign));
                            tac->gen(get<0>(assign) + " " + get<1>(assign) + " " + raddr);
                          }

                          if (type->toString() == "Bool") {
                            $$->truelist = {tac->instructions.size()};
                            tac->gen("goif _ " + $$->addr);
                            $$->falselist = {tac->instructions.size()};
                            tac->gen("goto _");
                          }
                        } 
                        else {
                          $$ = new NodeFunctionCall(*$1, $3, false, type); 
                        }

                      }
                    }
                  ;

  ArgsExp         : /* lambda */         { $$ = new NodeFunctionCallArgs(NULL, NULL); }
                  | PositionalArgs                              
                    { 
                      if ($1 == NULL) {
                        $$ = NULL;
                      } 

                      else {
                        $$ = new NodeFunctionCallArgs($1, NULL);
                        $$->positionalArgs = $1->currentArgs;
                        $1->currentArgs.clear();
                      }
                    }

                  | NamedArgs                                   
                    { 
                      if ($1 == NULL) {
                        $$ = NULL;
                      } 

                      else {
                        $$ = new NodeFunctionCallArgs(NULL, $1);
                        $$->namedArgs = $1->currentArgs;
                        $$->keywords = $1->keywords;

                        $1->currentArgs.clear();
                        $1->keywords.clear();
                      }
                    }

                  | PositionalArgs COMMA NamedArgs              
                    { 
                      if ($1 == NULL || $3 == NULL) {
                        $$ = NULL;
                      } 

                      else {
                        $$ = new NodeFunctionCallArgs($1, $3);
                        
                        $$->positionalArgs = $1->currentArgs;
                        $$->namedArgs = $3->currentArgs;
                        $$->keywords = $3->keywords;

                        $1->currentArgs.clear();
                        $3->currentArgs.clear();
                        $3->keywords.clear();
                      }
                    }
                  ;

  PositionalArgs  : Exp 
                    { 
                      if ($1->type->toString() == "$Error") {
                        $$ = NULL;
                      } 

                      else {
                        $$ = new NodeFunctionCallPositionalArgs(NULL, $1);

                        if ($1->type->toString() == "Bool" && $1->addr == "") {
                          string label;

                          $1->addr = tac->newTemp();

                          tac->backpatch($1->truelist, tac->instructions.size());
                          tac->gen("assignb " + $1->addr + " True");

                          label = "B" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($1->falselist, tac->instructions.size());
                          tac->gen("assignb " + $1->addr + " False");
                          tac->gen("@label " + label);
                        }
                        else if ($1->type->toString() == "Bool") {
                          tac->instructions[tac->instructions.size() - 2] = "";
                          tac->instructions[tac->instructions.size() - 1] = "";
                        }

                        $$->currentArgs.push_back($1);  
                      }
                    }

                  | PositionalArgs COMMA Exp 
                    { 
                      if ($3->type->toString() == "$Error" || $1 == NULL) {
                        $$ = NULL;
                      } 

                      else {
                        $$ = new NodeFunctionCallPositionalArgs($1, $3);

                        $$->currentArgs = $1->currentArgs;
                        $1->currentArgs.clear();

                        if ($3->type->toString() == "Bool" && $3->addr == "") {
                          string label;

                          $3->addr = tac->newTemp();

                          tac->backpatch($3->truelist, tac->instructions.size());
                          tac->gen("assignb " + $3->addr + " True");

                          label = "B" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($3->falselist, tac->instructions.size());
                          tac->gen("assignb " + $3->addr + " False");
                          tac->gen("@label " + label); 
                        }
                        else if ($3->type->toString() == "Bool") {
                          tac->instructions[tac->instructions.size() - 2] = "";
                          tac->instructions[tac->instructions.size() - 1] = "";
                        }

                        $$->currentArgs.push_back($3);
                      }
                    }
                  ;

  NamedArgs       : ID ASSIGNMENT Exp                           
                    { 
                      if ($3->type->toString() == "$Error") {
                        $$ = NULL;
                      } 

                      else {
                        $$ = new NodeFunctionCallNamedArgs(NULL, *$1, $3);

                        if ($3->type->toString() == "Bool" && $3->addr == "") {
                          string label;

                          $3->addr = tac->newTemp();

                          tac->backpatch($3->truelist, tac->instructions.size());
                          tac->gen("assignb " + $3->addr + " True");

                          label = "B" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($3->falselist, tac->instructions.size());
                          tac->gen("assignb " + $3->addr + " False");
                          tac->gen("@label " + label);
                        }
                        else if ($3->type->toString() == "Bool") {
                          tac->instructions[tac->instructions.size() - 2] = "";
                          tac->instructions[tac->instructions.size() - 1] = "";
                        }

                        $$->currentArgs[*$1] = $3; 
                        $$->keywords.insert(*$1);
                      }
                    }

                  | NamedArgs COMMA ID ASSIGNMENT Exp           
                    { 
                      $$ = new NodeFunctionCallNamedArgs($1, *$3, $5); 
                      if ($1 != NULL && $1->currentArgs.count(*$3)) {
                        addError("Got multiple values of '\033[1;3m" + *$3 + "\033[0m'.");
                        $$ = NULL;
                      } 
                      
                      else if ($1 == NULL || $5->type->toString() == "$Error") {
                        $$ = NULL;
                      } 
                      
                      else {
                        $$->currentArgs = $1->currentArgs;

                        if ($5->type->toString() == "Bool" && $5->addr == "") {
                          string label;

                          $5->addr = tac->newTemp();

                          tac->backpatch($5->truelist, tac->instructions.size());
                          tac->gen("assignb " + $5->addr + " True");

                          label = "B" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($5->falselist, tac->instructions.size());
                          tac->gen("assignb " + $5->addr + " False");
                          tac->gen("@label " + label);
                        }
                        else if ($5->type->toString() == "Bool") {
                          tac->instructions[tac->instructions.size() - 2] = "";
                          tac->instructions[tac->instructions.size() - 1] = "";
                        }

                        $$->currentArgs[*$3] = $5;
                        $1->currentArgs.clear();

                        $$->keywords = $1->keywords;
                        $$->keywords.insert(*$3);
                        $1->keywords.clear();
                      }
                    }
                  ;


/* ======================= UNION DEFINITION ========================== */
  UnionDef  : UnionId OPEN_C_BRACE UnionBody CLOSE_C_BRACE  
              { 
                int def_s = table->currentScope();
                table->exitScope(); 
                int s = table->currentScope();

                if (*$1 != "") {
                  StructureEntry *e = (StructureEntry*) table->lookup(*$1, s);
                  e->def_scope = def_s;

                  if ($3 != NULL) {
                    e->width = ((NodeUnionFields*) $3)->max_width;
                    e->incomplete = ((NodeUnionFields*) $3)->incompletes.size();

                    for (string type : ((NodeUnionFields*) $3)->incompletes) {
                      table->incompleteTypesList[type].push_back({e, table->scopeStack});
                    }
                  } 
                  else {
                    e->width = 0;
                  }
                }

                $$ = NULL;
                table->offsets.pop_back();
              }
            ;

  UnionId   : UNION ID   
              { 
                Entry *e = table->lookup(*$2);
                int s = table->currentScope();

                if (e != NULL && e->scope == s && e->category != "Incomplete Structure") {
                  addError("Redefinition of '\033[1;3m" + *$2 + "\033[0m'.");
                  $$ = new string("");
                } 

                else if (e != NULL && e->scope == s) {
                  e->category = "Structure";
                }

                else {
                  Entry *e = new StructureEntry(*$2, s, "Structure");
                  table->insert(e);
                }

                // Verificamos si hay que completar algunas llamadas a esta funcion 
                // antes de que se definiera.
                if (table->incompleteTypesList.count(*$2)) {
                  int n = table->incompleteTypesList[*$2].size();

                  for (int j = 0; j < n; j++) {
                    // Verificamos si el scope de definicion esta en la pila de scopes 
                    // de la llamada.
                    for (int s : table->incompleteTypesList[*$2][j].second) {
                      if (s == e->scope) {
                        table->incompleteTypesList[*$2][j].first->incomplete--;
                        table->incompleteTypesList[*$2].erase(
                          table->incompleteTypesList[*$2].begin() + (j--)
                        );
                        break;
                      }
                    }
                  }

                  // Verificamos si la lista de esta estructura esta vacia
                  if (table->incompleteTypesList[*$2].size() == 0) {
                    table->incompleteTypesList.erase(*$2);
                  }
                }

                table->newScope(); 
                $$ = $2; 
                table->offsets.push_back(0);
              }
            ;  

  UnionBody  : Type IdDef SEMICOLON                          
              { 
                if (*$2 == "" || $1->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($1->danger && $1->incomplete == "") {
                  addError("A Union cannot contain itself.");
                  $$ = NULL;
                }

                else if ($1->danger) {
                  addError(
                    "A Union only can contain incomplete structures wrapers"
                    " with a pointer."
                  );
                  $$ = NULL;
                }

                else {
                  $$ = new NodeUnionFields(NULL, $1, *$2, $1->width); 
                  int s = table->currentScope();
                  Entry *e = new VarEntry(*$2, s, "Field", $1, table->offsets.back(), "", table);

                  if ($1->incomplete != "") {
                    ((NodeUnionFields*) $$)->incompletes.push_back($1->incomplete);
                  }

                  table->insert(e);
                }
              }

            | UnionBody Type IdDef SEMICOLON 
              { 
                if ($1 == NULL || *$3 == "" || $2->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($2->danger && $2->incomplete == "") {
                  addError("A Union cannot contain itself.");
                  $$ = NULL;
                }

                else if ($2->danger) {
                  addError(
                    "A Union only can contain incomplete structures wrapers"
                    " with a pointer."
                  );
                  $$ = NULL;
                }

                else {
                  int max_width = ((NodeUnionFields*) $1)->max_width;
                  max_width = max_width > $2->width ? max_width : $2->width;
                  $$ = new NodeUnionFields($1, $2, *$3, max_width); 
                  int s = table->currentScope();
                  Entry *e = new VarEntry(*$3, s, "Field", $2, table->offsets.back(), "", table);

                  ((NodeUnionFields*) $$)->incompletes = ((NodeUnionFields*) $1)->incompletes;
                  if ($2->incomplete != "") {
                    ((NodeUnionFields*) $$)->incompletes.push_back($2->incomplete);
                  }

                  table->insert(e);
                }
              }
            ;


/* ======================= REGISTER DEFINITION ======================= */
  RegDef    : RegId OPEN_C_BRACE RegBody CLOSE_C_BRACE  
              { 
                int def_s = table->currentScope();
                table->exitScope();
                int s = table->currentScope();

                if (*$1 != "") {
                  StructureEntry *e = (StructureEntry*) table->lookup(*$1, s);
                  e->def_scope = def_s;
                  if ($3 != NULL) {
                    e->width = table->offsets.back();

                    e->incomplete = ((NodeUnionFields*) $3)->incompletes.size();

                    for (string type : ((NodeUnionFields*) $3)->incompletes) {
                      table->incompleteTypesList[type].push_back({e, table->scopeStack});
                    }
                  }
                  else {
                    e->width = 0;
                  }

                  // Verificamos si hay que completar algunas llamadas a esta funcion 
                  // antes de que se definiera.
                  if (table->incompleteTypesList.count(*$1)) {
                    int n = table->incompleteTypesList[*$1].size();

                    for (int j = 0; j < n; j++) {
                      // Verificamos si el scope de definicion esta en la pila de scopes 
                      // de la llamada.
                      for (int s : table->incompleteTypesList[*$1][j].second) {
                        if (s == e->scope) {
                          table->incompleteTypesList[*$1][j].first->incomplete--;
                          table->incompleteTypesList[*$1].erase(
                            table->incompleteTypesList[*$1].begin() + (j--)
                          );
                          break;
                        }
                      }
                    }

                    // Verificamos si la lista de esta estructura esta vacia
                    if (table->incompleteTypesList[*$1].size() == 0) {
                      table->incompleteTypesList.erase(*$1);
                    }
                  }
                }

                $$ = NULL;
                table->offsets.pop_back();
              }
            ;   

  RegId     : REGISTER ID 
              { 
                Entry *e = table->lookup(*$2);
                int s = table->currentScope();

                if (e != NULL && e->scope == s && e->category != "Incomplete Structure") {
                  addError("Redefinition of '\033[1;3m" + *$2 + "\033[0m'.");
                  $$ = new string("");
                } 

                else if (e != NULL && e->scope == s) {
                  e->category = "Structure";
                }

                else {
                  Entry *e = new StructureEntry(*$2, s, "Structure");
                  table->insert(e);
                }

                // Verificamos si hay que completar algunas llamadas a esta funcion 
                // antes de que se definiera.
                if (table->incompleteTypesList.count(*$2)) {
                  int n = table->incompleteTypesList[*$2].size();

                  for (int j = 0; j < n; j++) {
                    // Verificamos si el scope de definicion esta en la pila de scopes 
                    // de la llamada.
                    for (int s : table->incompleteTypesList[*$2][j].second) {
                      if (s == e->scope) {
                        table->incompleteTypesList[*$2][j].first->incomplete--;
                        table->incompleteTypesList[*$2].erase(
                          table->incompleteTypesList[*$2].begin() + (j--)
                        );
                        break;
                      }
                    }
                  }

                  // Verificamos si la lista de esta estructura esta vacia
                  if (table->incompleteTypesList[*$2].size() == 0) {
                    table->incompleteTypesList.erase(*$2);
                  }
                }

                table->newScope(); 
                $$ = $2; 
                table->offsets.push_back(0);
              }
            ; 

  RegBody   : Type IdDef OptAssign SEMICOLON  
              { 
                bool cond = *$2 == "" || $1->toString() == "$Error" ||
                  ($3 != NULL && $3->type->toString() == "$Error");

                if (cond) {
                  $$ = NULL;
                } 

                else if ($1->danger && $1->incomplete == "") {
                  addError("A Register cannot contain itself.");
                  $$ = NULL;
                }

                else if ($1->danger) {
                  addError(
                    "A Register only can contain incomplete structures wrapers"
                    " with a pointer."
                  );
                  $$ = NULL;
                }

                else if ($3 != NULL && $1->toString() != $3->type->toString()) {
                  addError(
                    "Can't assign a '\033[1;3m" + $3->type->toString() +
                    "\033[0m' to a '\033[1;3m" + $1->toString() + "\033[0m'."
                  );
                  $$ = NULL;
                }
                
                else {
                  $$ = new NodeRegFields(NULL, $1, *$2, $3);
                  int s = table->currentScope(), offset = table->newOffset($1);

                  Entry *e = new VarEntry(*$2, s, "Field", $1, offset, "", table);
                  table->insert(e);

                  if ($1->incomplete != "") {
                    ((NodeUnionFields*) $$)->incompletes.push_back($1->incomplete);
                  }
                }
              }

            |  RegBody Type IdDef OptAssign SEMICOLON    
              { 
                if (*$3 == "" || $2->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($4 != NULL && $2->toString() != $4->type->toString()) {
                  addError(
                    "Can't assign a '\033[1;3m" + $4->type->toString() +
                    "\033[0m' to a '\033[1;3m" + $2->toString() + "\033[0m'."
                  );
                  $$ = NULL;
                }

                else if ($1 == NULL) {
                  $$ = NULL;
                }

                else if ($2->danger && $2->incomplete == "") {
                  addError("A Register cannot contain itself.");
                  $$ = NULL;
                }

                else if ($2->danger) {
                  addError(
                    "A Register only can contain incomplete structures wrapers"
                    " with a pointer."
                  );
                  $$ = NULL;
                }

                else {
                  $$ = new NodeRegFields($1, $2, *$3, $4);
                  int s = table->currentScope(), offset = table->newOffset($2);

                  Entry *e = new VarEntry(*$3, s, "Field", $2, offset, "", table);
                  table->insert(e);

                  ((NodeUnionFields*) $$)->incompletes = ((NodeUnionFields*) $1)->incompletes;
                  if ($2->incomplete != "") {
                    ((NodeUnionFields*) $$)->incompletes.push_back($2->incomplete);
                  }
                }
              }
            ;


/* ======================= STRUCTURE DECLARATION ===================== */
  StructDec : STRUCTURE IdDef 
              {
                if (*$2 != "") {
                  int s = table->currentScope();
                  StructureEntry *e = new StructureEntry(*$2, s, "Incomplete Structure");
                  e->incomplete = true;
                  table->insert(e);
                }
                $$ = NULL;
              }


/* ======================= CONDITIONALS ============================== */
  Conditional : If Cond THEN M I N M OptElsif M OptElse DONE  
                { 
                  $$ = new NodeConditional($2, $5, $8, $10);

                  tac->backpatch($2->truelist, $4);

                  vector<unsigned long long> t;
                  if ($5 != NULL) {
                    t = merge<unsigned long long>($5->nextlist, $6->nextlist);
                  }
                  else {
                    t = $6->nextlist;
                  }

                  if ($8 != NULL && $10 != NULL) {
                    tac->backpatch($2->falselist, $7);
                    t = merge<unsigned long long>(t, $8->truelist);
                    tac->backpatch($8->falselist, $9);
                    t = merge<unsigned long long>(t, $10->nextlist);
                  }
                  
                  else if ($8 != NULL) {
                    tac->backpatch($2->falselist, $7);
                    t = merge<unsigned long long>(t, $8->truelist);
                    t = merge<unsigned long long>(t, $8->falselist);
                  }

                  else if ($10 != NULL) {
                    tac->backpatch($2->falselist, $9);
                    t = merge<unsigned long long>(t, $10->nextlist);
                  }

                  else {
                    t = merge<unsigned long long>(t, $2->falselist);
                  }

                  $$->nextlist = t;
                  table->exitScope(); 
                }
              ;

  N           : /* lambda */
                {
                  $$ = new Node(); 
                  $$->nextlist = {tac->instructions.size()};
                  tac->gen("goto _");
                }

  Cond        : Exp 
                {
                  if ($1->type->toString() != "$Error" && $1->type->toString() != "Bool") {
                    addError(
                      "Condition must be a '\033[1;3mBool\033[0m' but '\033[1;3m" +
                      $1->type->toString() + "\033[0m' found."
                    );
                  }
                  $$ = $1;
                }
              ;

  If          : IF 
                {
                  table->newScope(); 
                }
              ;
  OptElsif    : /* lambda */                    { $$ = NULL; }
              | Elsifs                          { $$ = $1; }
              ;
  Elsifs      : Elsif Cond THEN M I N
                { 
                  $$ = new NodeElsif(NULL, $2, $5); 
                  tac->backpatch($2->truelist, $4);
                  if ($5 != NULL) {
                    $$->truelist = merge<unsigned long long>($5->nextlist, $6->nextlist);
                  }
                  else {
                    $$->truelist = $6->nextlist;
                  }
                  $$->falselist = $2->falselist;
                }

              | Elsifs M Elsif Cond THEN M I N
                { 
                  $$ = new NodeElsif($1, $4, $7); 
                  tac->backpatch($1->falselist, $2);
                  tac->backpatch($4->truelist, $6);
                  if ($7 != NULL) {
                    $$->truelist = merge<unsigned long long>($1->truelist, $7->nextlist);
                  }
                  else {
                  $$->truelist = $1->truelist;
                  }
                  $$->truelist = merge<unsigned long long>($$->truelist, $8->nextlist);
                  $$->falselist = $4->falselist;
                }
              ;

  Elsif       : ELSIF 
                { 
                  table->exitScope();
                  table->newScope(); 
                }
              ;
  OptElse     : /* lambda */                    { $$ = NULL; }
              | Else I
                { 
                  $$ = new NodeElse($2); 
                  if ($2 != NULL) {
                    $$->nextlist = $2->nextlist;
                  }
                }
              ;
  Else        : ELSE  
                { 
                  table->exitScope();
                  table->newScope(); 
                }
              ;


/* ======================= LOOPS ===================================== */
  LoopWhile : While M Cond M W DO I DONE
              { 
                $$ = new NodeWhile($3, $7); 

                // Si Cond da True, ejecutamos la instruccion.
                tac->backpatch($3->truelist, $4);

                // Si Cond da False, pasamos a la siguiente instruccion.
                $$->nextlist = merge<unsigned long long>(
                  $3->falselist, 
                  tac->breaklist.top()
                );
                tac->breaklist.pop();

                // Parcheamos el cuerpo con la siguiente instruccion.
                if ($7 != NULL) {
                  tac->backpatch($7->nextlist, tac->instructions.size());
                }
                // Parcheamos los continues encontrados.
                tac->backpatch(tac->continuelist.top(), tac->instructions.size());
                tac->continuelist.pop();

                // Hacemos una copia de la Condicion para simular un do while, incluyendo
                // copiar su truelist y falselist.
                unsigned long long diff = tac->instructions.size() - $2;
                vector<unsigned long long> truelist, falselist;
                // Copiamos la truelist
                for (unsigned long long instr : $3->truelist) {
                  truelist.push_back(diff + instr);
                }
                // Copiamos la falselist
                for (unsigned long long instr : $3->falselist) {
                  falselist.push_back(diff + instr);
                }
                // Copiamos las instrucciones
                for (unsigned long long i = $2; i < $4; i++) {
                  tac->gen(tac->instructions[i]);
                }
                
                // El nuevo truelist lo parcheamos con el inicio del cuerpo
                tac->backpatch(truelist, *$5);

                // El nuevo falselist se combinara con el nextlist de la instruccion
                // completa
                $$->nextlist = merge<unsigned long long>(
                  $$->nextlist, 
                  falselist
                );
                
                table->exitScope();
              }
            ; 

  While     : WHILE 
              { 
                tac->breaklist.push({});
                tac->continuelist.push({});
                table->newScope(); 
              }
            ;

  LoopFor   : ForSign DO I DONE 
              {
                $$ = new NodeFor($1, $3);

                if ($3 != NULL) {
                  tac->backpatch(
                    merge<unsigned long long>(
                      $3->nextlist, 
                      tac->continuelist.top()
                    ), 
                    tac->instructions.size()
                  );
                }
                else {
                  tac->backpatch(tac->continuelist.top(), tac->instructions.size());
                }
                tac->continuelist.pop();

                if ($1->step != NULL) {
                  tac->gen("add " + $1->addr + " " + $1->addr + " " + $1->step_addr);
                }
                else {
                  tac->gen("add " + $1->addr + " " + $1->addr + " 1");
                }

                tac->gen("goto " + $1->label);
                tac->gen("@label " + $1->label + "_end");

                // Parcheamos los breaks encontrados.
                tac->backpatch(tac->breaklist.top(), $1->label + "_end");
                tac->breaklist.pop();
                
                table->exitScope();
                table->exitScope();
              }

  ForSign   : For OPEN_PAR IdDef SEMICOLON Exp SEMICOLON Exp OptStep CLOSE_PAR 
              { 
                string type1 = $5->type->toString();
                string type2 = $7->type->toString();
                string type3 = $8 == NULL ? "" : $8->type->toString();

                int s = table->currentScope();
                Type *t = predefinedTypes["Int"];

                // Calculamos el offset.
                int offset = table->newOffset(t);

                VarEntry *e = new VarEntry(*$3, s, "Var", t, offset, tac->newTemp());
                table->insert(e); 

                if (type1 != "$Error" && type1 != "Int") {
                  addError(
                    "Initial value in a for loop must be "
                    "'\033[1;3mInt\033[0m' but '\033[1;3m" + type1 + "\033[0m' found."
                  );
                }

                if (type2 != "$Error" && type2 != "Int") {
                  addError(
                    "End value in a for loop must be "
                    "'\033[1;3mInt\033[0m' but '\033[1;3m" + type2 + "\033[0m' found."
                  );
                }

                if ($8 != NULL && type3 != "$Error" && type3 != "Int") {
                  addError(
                    "Step value in a for loop must be "
                    "'\033[1;3mInt\033[0m' but '\033[1;3m" + type3 + "\033[0m' found."
                  );
                }

                $$ = new NodeForSign(*$3, $5, $7, $8);
                $$->addr = tac->newTemp();
                $$->label = tac->newLabel();

                tac->gen("assignw " + $$->addr + " " + $5->addr);
                tac->gen("@label " + $$->label);

                string end_addr;
                if ($7->addr.back() == ']') {
                  end_addr = tac->newTemp();
                  tac->gen("assignw " + end_addr + " " + $7->addr);
                }
                else {
                  end_addr = $7->addr;
                }

                // Verificamos si el step es definido, y n ese caso se verifica si es
                // positivo o negativo
                if ($8 != NULL) {
                  if ($8->addr.back() == ']') {
                    $$->step_addr = tac->newTemp();
                    tac->gen("assignw " + $$->step_addr + " " + $8->addr);
                  }
                  else {
                    $$->step_addr = $8->addr;
                  }

                  tac->gen("lt test " + $$->step_addr + " 0");
                  tac->gen("goif " + $$->label + "_neg test");

                  // Verificacion de iteracion del for
                  tac->gen("geq test " + $$->addr + " " + end_addr);
                  tac->gen("goif " + $$->label + "_end test");
                  tac->gen("goto " + $$->label + "_body");

                  tac->gen("@label " + $$->label + "_neg");
                  tac->gen("leq test " + $$->addr + " " + end_addr);
                  tac->gen("goif " + $$->label + "_end test");

                  tac->gen("@label " + $$->label + "_body");
                }
                else {
                  // Verificacion de iteracion del for
                  tac->gen("geq test " + $$->addr + " " + end_addr);
                  tac->gen("goif " + $$->label + "_end test");
                }
                
                tac->gen("assignw " + e->addr + " " + $$->addr);

                tac->breaklist.push({});
                tac->continuelist.push({});
                table->newScope();
              }
            ;

  For       : FOR  
              { 
                table->newScope(); 
              }
            ;

  OptStep   : /* lambda */                              { $$ = NULL; }
            | SEMICOLON Exp                             { $$ = $2; }
            ;


/* ======================= SUBROUTINES DEFINITION ==================== */
  RoutDef   : M RoutSign OPEN_C_BRACE Actions CLOSE_C_BRACE   
              { 
                string func_size = to_string(table->offsets.back());

                if ($2->is_error) {
                  NodeError *err = (NodeError*) $2;
                  table->exitScope();
                  table->exitScope();
                  if (err->errInfo != "") {
                    table->erase(err->errInfo, table->currentScope());
                  }

                  $$ = new NodeError();
                } 

                else {
                  $$ = new NodeRoutineDef($2, $4); 
                  
                  table->exitScope();
                  table->exitScope();
                  tac->backpatch({(unsigned long long) $1}, func_size);
                }

                table->ret_type = "";
                table->offsets.pop_back();

                if ($4 != NULL) {
                  tac->backpatch($4->nextlist, $2->addr + "_end");
                }

                tac->gen("@label " + $2->addr + "_end");
                tac->gen("assignw lastbase BASE");
                tac->gen("return 0");
                tac->gen("@endfunction " + func_size);
              }
            ; 

  RoutSign  : RoutId OPEN_PAR RoutArgs CLOSE_PAR OptReturn  
              {
                FunctionEntry *fe = NULL;

                if ($3 == NULL || $1->first == "" || $5->toString() == "$Error") {
                  NodeError *err = new NodeError();
                  if ($1->second == NULL) {
                    err->errInfo = $1->first;
                  }
                  else if ($1->first != "") {
                    err->errInfo = "";
                    $1->second->category = "Declaration";
                  }
                  else{
                    err->errInfo = "";
                  }
                  $$ = err;
                } 
                
                else if ($1->second != NULL) {
                  bool error = false;
                  FunctionEntry *fe_dec = $1->second;

                  for (int i = 0; (size_t) i < $3->params.size(); i++) {
                    if (
                      (size_t) i == fe_dec->args.size() ||
                      get<0>($3->params[i]) != get<0>(fe_dec->args[i]) ||
                      get<1>($3->params[i]) != get<1>(fe_dec->args[i]) ||
                      get<2>($3->params[i]) != get<2>(fe_dec->args[i]) || 
                      get<3>($3->params[i]) != get<3>(fe_dec->args[i])
                    ) {
                      addError("Sign of function dont match with the declaration.");
                      error = true;
                      break;
                    }
                  }

                  if ($5->toString() != fe_dec->return_type->toString()) {
                    addError("Sign of function dont match with the declaration.");
                    error = true;
                  }

                  if (error) {
                    NodeError *err = new NodeError();
                    err->errInfo = "";
                    $$ = err;
                  }

                  else {
                    fe = (FunctionEntry*) table->lookup($1->first);
                    fe->args = $3->params;
                    $3->params.clear();
                    
                    $$ = new NodeRoutineSign($1->first, $3, $5);

                    // Verificamos si hay que completar algunas llamadas a esta funcion 
                    // antes de que se definiera.
                    if (tac->functionlist.count(fe->id)) {
                      vector<unsigned long long> instructions = {};
                      int n = tac->functionlist[fe->id].size();

                      for (int j = 0; j < n; j++) {
                        // Verificamos si el scope de definicion esta en la pila de scopes 
                        // de la llamada.
                        for (int s : tac->functionlist[fe->id][j].second) {
                          if (s == fe->scope) {
                            instructions.push_back(tac->functionlist[fe->id][j].first);
                            tac->functionlist[fe->id].erase(
                              tac->functionlist[fe->id].begin() + (j--)
                            );
                            break;
                          }
                        }
                      }

                      tac->backpatch(instructions, fe->addr);

                      // Verificamos si la lista de esta funcion esta vacia
                      if (tac->functionlist[fe->id].size() == 0) {
                        tac->functionlist.erase(fe->id);
                      }
                    }

                    // Repetimos el proceso anterior pero con los parametros opcionales
                    if (tac->calllist.count(fe->id)) {
                      vector<unsigned long long> instructions = {};
                      int n = tac->calllist[fe->id].size();

                      for (int j = 0; j < n; j++) {
                        // Verificamos si el scope de definicion esta en la pila de scopes 
                        // de la llamada.
                        for (int s : tac->calllist[fe->id][j].second) {
                          if (s == fe->scope) {
                            instructions.push_back(tac->calllist[fe->id][j].first);
                            tac->calllist[fe->id].erase(
                              tac->calllist[fe->id].begin() + (j--)
                            );
                            break;
                          }
                        }
                      }

                      tac->backpatch(instructions, "A" + to_string(tac->arrayCount - 1));

                      // Verificamos si la lista de esta funcion esta vacia
                      if (tac->calllist[fe->id].size() == 0) {
                        tac->calllist.erase(fe->id);
                      }
                    }
                  }
                }
                
                else {
                  fe = (FunctionEntry*) table->lookup($1->first);
                  fe->return_type = $5;
                  fe->def_scope = table->currentScope();  
                  fe->args = $3->params;
                  $3->params.clear();
                  
                  $$ = new NodeRoutineSign($1->first, $3, $5);
                }

                if ($5->toString() != "$Error") {
                  table->ret_type = $5->toString();
                }
                table->newScope();

                if (fe != NULL) {
                  $$->nextlist = {tac->instructions.size()};
                  $$->addr = fe->addr;
                  fe->optargs_addr = "A" + to_string(tac->arrayCount - 1);
                }
              }
            ;

  RoutId    : DEF ID 
              {
                Entry *e = table->lookup(*$2);
                int s = table->currentScope();

                if (e != NULL && e->scope == s && e->category != "Declaration") {
                  addError("Redefinition of '\033[1;3m" + *$2 + "\033[0m'.");
                  $$ = new pair<string, FunctionEntry*>("", NULL);
                } 

                else if (e != NULL && e->scope == s && e->category == "Declaration") {
                  FunctionEntry *fe = (FunctionEntry*) e;
                  $$ = new pair<string, FunctionEntry*>(*$2, fe);
                  fe->category = "Function";
                  fe->addr = tac->newFunc();
                  tac->gen("@function " + fe->addr + " _");
                }
                
                else if (e != NULL && e->category == "Declaration") {
                  FunctionEntry *fe_dec = (FunctionEntry*) e;
                  $$ = new pair<string, FunctionEntry*>(*$2, fe_dec); 
                  
                  FunctionEntry *fe = new FunctionEntry(*$2, s, "Function");
                  fe->args = fe_dec->args;
                  fe->return_type = fe_dec->return_type; 
                  fe->addr = tac->newFunc();
                  table->insert(fe);
                  tac->gen("@function " + fe->addr + " _");
                }

                else {
                  $$ = new pair<string, FunctionEntry*>(*$2, NULL);
                  FunctionEntry *fe = new FunctionEntry(*$2, s, "Function");
                  fe->addr = tac->newFunc();
                  table->insert(fe);
                  tac->gen("@function " + fe->addr + " _");
                }
                
                table->newScope();
                table->offsets.push_back(0);
              }
            ;    

  RoutArgs  : /* lambda */ 
              { 
                $$ = new NodeRoutArgs(NULL, NULL); 
              }

            | MandArgs  
              { 
                if ($1 == NULL) {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeRoutArgs($1, NULL); 
                  $$->params = $1->currentParams;
                  $1->currentParams.clear();
                  tac->newArray(0);
                }
              }

            | OptArgs                                       
              {
                if ($1 == NULL) {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeRoutArgs(NULL, $1); 
                  $$->params = $1->currentParams;
                  $1->currentParams.clear();
                  tac->newArray($$->params.size());
                }
              }

            | MandArgs COMMA OptArgs                        
              { 
                if (($1 == NULL) || ($3 == NULL)) {
                  $$ = NULL;
                } 

                else {
                  tac->newArray($3->currentParams.size());
                  for(auto & elem : $3->currentParams) {
                    $1->currentParams.push_back(elem);
                  }

                  $$ = new NodeRoutArgs($1, $3);
                  $$->params = $1->currentParams;
                  $1->currentParams.clear();
                  $3->currentParams.clear();
                }
              }
            ;  

  MandArgs  : Type OptRef IdDef                             
              { 
                if (*$3 == "" || $1->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($1->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }

                else {
                  $$ = new NodeRoutArgDef(NULL, $1, $2, *$3, NULL);
                  $$->currentParams.push_back({*$3, $1->toString(), $2, false});

                  int s = table->currentScope(), offset = table->newOffset($1);

                  Entry *e = new VarEntry(*$3, s, "Var", $1, offset);
                  table->insert(e);
                }
              }
            | MandArgs COMMA Type OptRef IdDef              
              { 
                if ($1 == NULL || *$5 == "" || $3->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($3->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }

                else {
                  $$ = new NodeRoutArgDef($1, $3, $4, *$5, NULL);
                  $$->currentParams = $1->currentParams;
                  $1->currentParams.clear();
                  $$->currentParams.push_back({*$5, $3->toString(), $4, false});

                  int s = table->currentScope(), offset = table->newOffset($3);

                  Entry *e = new VarEntry(*$5, s, "Var", $3, offset);
                  table->insert(e);
                }
              }
            ;   

  OptArgs   : Type OptRef IdDef ASSIGNMENT M CondAssign Exp 
              { 
                string type = $1->toString();
                string rtype = $7->type->toString();

                if (type == "$Error" || rtype == "$Error") {
                  $$ = NULL;
                } 

                else if ($1->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }
                
                else if (type != rtype) {
                  addError(
                    "Can't assign a '\033[1;3m" + rtype +
                    "\033[0m' to a '\033[1;3m" + type + "\033[0m'."
                  );
                  $$ = NULL;
                } 

                else if (*$3 == "") {
                  $$ = NULL;
                }
                
                else {
                  $$ = new NodeRoutArgDef(NULL, $1, $2, *$3, $7);
                  $$->currentParams.push_back({*$3, type, $2, true});

                  if (rtype == "Bool") {
                    $7->addr = tac->newTemp();

                    // Aplicamos backpatching sobre la truelist para realizar la 
                    // asignacion de True, y luego saltamos la asignaicon de False.
                    tac->backpatch($7->truelist, tac->instructions.size());
                    tac->gen("assignb " + $7->addr + " True");
                    string label = "Bool" + to_string(tac->instructions.size() + 2);
                    tac->gen("goto " + label);

                    // Aplicamos backpatching sobre la falselist para realizar la 
                    // asignacion de False, y luego creamos la etiqueta de salto de la
                    // asignacion a True.
                    tac->backpatch($7->falselist, tac->instructions.size());
                    tac->gen("assignb " + $7->addr + " False");
                    tac->gen("@label " + label);
                  }
                  else if (rtype.back() == ']') {
                    $$->type = $7->type;
                  }

                  int s = table->currentScope(), offset = table->newOffset($1);
                  Entry *e = new VarEntry(*$3, s, "Var",$1, offset);
                  table->insert(e);

                  string raddr, assign_type = $1->width == 1 ? "assignb" : "assignw";
                  if ($7->addr.back() == ']') {
                    raddr = rtype == "Float" ? tac->newFloat() : tac->newTemp();
                    tac->gen(assign_type + " " + raddr + " " + $7->addr);
                  } 
                  else {
                    raddr = $7->addr;
                  }

                  tac->gen(assign_type + " BASE[" + to_string(offset) + "] " + raddr);
                  tac->backpatch({$5}, string("0"));
                  tac->gen("@label " + *$6);
                }
              }

            | OptArgs COMMA Type OptRef IdDef ASSIGNMENT M CondAssign Exp   
              { 
                string type = $3->toString();
                string rtype = $9->type->toString();
                
                if (type == "$Error" || rtype == "$Error") {
                  $$ = NULL;
                } 

                else if ($3->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }
                
                else if (type != rtype) {
                  addError(
                    "Can't assign a '\033[1;3m" + rtype +
                    "\033[0m' to a '\033[1;3m" + type + "\033[0m'."
                  );
                  $$ = NULL;
                } 
                
                else if ($1 == NULL || *$5 == "") {
                  $$ = NULL;
                } 
                
                else {
                  $$ = new NodeRoutArgDef($1, $3, $4, *$5, $9);

                  $$->currentParams = $1->currentParams;
                  $1->currentParams.clear();
                  $$->currentParams.push_back({*$5, type, $4, true});

                  if (rtype == "Bool") {
                    $9->addr = tac->newTemp();

                    // Aplicamos backpatching sobre la truelist para realizar la 
                    // asignacion de True, y luego saltamos la asignaicon de False.
                    tac->backpatch($9->truelist, tac->instructions.size());
                    tac->gen("assignb " + $9->addr + " True");
                    string label = "Bool" + to_string(tac->instructions.size() + 2);
                    tac->gen("goto " + label);

                    // Aplicamos backpatching sobre la falselist para realizar la 
                    // asignacion de False, y luego creamos la etiqueta de salto de la
                    // asignacion a True.
                    tac->backpatch($9->falselist, tac->instructions.size());
                    tac->gen("assignb " + $9->addr + " False");
                    tac->gen("@label " + label);
                  }
                  else if (rtype.back() == ']') {
                    $$->type = $9->type;
                  }

                  int s = table->currentScope(), offset = table->newOffset($3);
                  Entry *e = new VarEntry(*$5, s, "Var", $3, offset);
                  table->insert(e);

                  string raddr, assign_type = $3->width == 1 ? "assignb" : "assignw";
                  if ($9->addr.back() == ']') {
                    raddr = rtype == "Float" ? tac->newFloat() : tac->newTemp();
                    tac->gen(assign_type + " " + raddr + " " + $9->addr);
                  } 
                  else {
                    raddr = $9->addr;
                  }

                  tac->gen(assign_type + " BASE[" + to_string(offset) + "] " + raddr);
                  tac->backpatch({$7}, to_string($$->currentParams.size()-1));
                  tac->gen("@label " + *$8);
                }
              }

            ;

  CondAssign: /* lambda */
              {
                string temp = tac->newTemp();
                string array = "A" + to_string(tac->arrayCount);
                $$ = new string(tac->newLabel());
                tac->gen("assignb " + temp + " " + array + "[_]");
                tac->gen("goif " + *$$ + " " + temp);
              }
  
  OptRef    : /* lambda */                { $$ = false; }
            | AT                          { $$ = true; }
            ; 
  
  OptReturn : /* lambda */                { $$ = predefinedTypes["Unit"]; }
            | RIGHT_ARROW Type 
              { 
                if ($2->incomplete != "") {
                  addError("Can't define function that returns incomplete types.");
                  $$ = predefinedTypes["$Error"];
                }
                else {
                  $$ = $2;
                }
              }
            | RIGHT_ARROW T_UNIT 
              {
                $$ = predefinedTypes["Unit"];
              }
            ; 
  
  Actions   : /* lambda */                { $$ = NULL; }
            | Actions M Action                                
              { 
                // Una instruccion puede ser NULL porque dio error o porque no tiene una
                // representacion en el arbol abtracto, como las declaraciones de variables.

                if ($1 == NULL && $3 == NULL) {
                  // Si ambas instrucciones hijas son NULL, esta instruccion es NULL.
                  $$ = NULL;
                } 
                else if ($3 == NULL) {
                  // Si la segunda instruccion es NULL, la instruccion padre sera igual 
                  // a la hija.
                  $$ = $1;
                } 
                else {
                  $$ = new NodeActions($1, $3); 
                  if ($1 != NULL) {
                    // Nos aseguramos que la primera instruccion salte a la segunda.
                    tac->backpatch($1->nextlist, $2);
                  }
                  $$->nextlist = $3->nextlist;
                }
              }
            ;


/* ======================= SUBROUTINES DECLARATION =================== */
  RoutDec   : DecId OPEN_PAR DecArgs CLOSE_PAR OptReturn 
              {
                int s1 = table->currentScope();
                table->exitScope();

                if ($3 != NULL && *$1 != "" && $5->toString() != "$Error") {
                  int s2 = table->currentScope();
                  FunctionDeclarationEntry *e = new FunctionDeclarationEntry(
                    *$1, 
                    s2,
                    "Declaration",
                    $3->params,
                    $5
                  );
                  e->addr = "";
                  e->def_scope = s1; 
                  table->insert(e);
                }
                
                $$ = NULL;
              }
            ;

  DecId     : DEC IdDef   
              {
                table->newScope();
                $$ = $2;
              }
            ;   

  DecArgs   : /* lambda */ 
              { 
                $$ = new NodeRoutDecArgs(NULL, NULL); 
              }

            | MandDecArgs  
              { 
                if ($1 == NULL) {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeRoutDecArgs($1, NULL); 
                  $$->params = $1->currentParams;
                  $1->currentParams.clear();
                }
              }

            | OptDecArgs                                       
              {
                if ($1 == NULL) {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeRoutDecArgs(NULL, $1); 
                  $$->params = $1->currentParams;
                  $1->currentParams.clear();
                }
              }

            | MandDecArgs COMMA OptDecArgs   
              { 
                if (($1 == NULL) || ($3 == NULL)) {
                  $$ = NULL;
                } 

                else {
                  for(auto & elem : $3->currentParams) {
                    $1->currentParams.push_back(elem);
                  }

                  $$ = new NodeRoutDecArgs($1, $3);
                  $$->params = $1->currentParams;
                  $1->currentParams.clear();
                  $3->currentParams.clear();
                }
              }
            ;  

  MandDecArgs : Type OptRef IdDef                             
              { 
                if (*$3 == "" || $1->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($1->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }

                else {
                  $$ = new NodeRoutDecArgDef(NULL, $1, $2, *$3, true);
                  $$->currentParams.push_back({*$3, $1->toString(), $2, false});

                  int s = table->currentScope(), offset = table->newOffset($1);

                  Entry *e = new VarEntry(*$3, s, "Var", $1, offset);
                  table->insert(e);
                }
              }
            | MandDecArgs COMMA Type OptRef IdDef  
              { 
                if ($1 == NULL || *$5 == "" || $3->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($3->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }

                else {
                  $$ = new NodeRoutDecArgDef($1, $3, $4, *$5, false);
                  $$->currentParams = $1->currentParams;
                  $1->currentParams.clear();
                  $$->currentParams.push_back({*$5, $3->toString(), $4, false});

                  int s = table->currentScope(), offset = table->newOffset($3);

                  Entry *e = new VarEntry(*$5, s, "Var", $3, offset);
                  table->insert(e);
                }
              }
            ;   

  OptDecArgs : OPT Type OptRef IdDef
              { 
                string type = $2->toString();

                if (type == "$Error") {
                  $$ = NULL;
                } 

                else if ($2->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }

                else if (*$4 == "") {
                  $$ = NULL;
                }
                
                else {
                  $$ = new NodeRoutDecArgDef(NULL, $2, $3, *$4, true);
                  $$->currentParams.push_back({*$4, type, $3, true});

                  int s = table->currentScope(), offset = table->newOffset($2);
                  Entry *e = new VarEntry(*$4, s, "Var",$2, offset);
                  table->insert(e);
                }
              }

            | OptDecArgs COMMA OPT Type OptRef IdDef 
              { 
                string type = $4->toString();
                if (type == "$Error") {
                  $$ = NULL;
                } 

                else if ($4->incomplete != "") {
                  addError("Can't define arguments with incomplete types.");
                  $$ = NULL;
                }
                
                else if ($1 == NULL || *$6 == "") {
                  $$ = NULL;
                } 
                
                else {
                  $$ = new NodeRoutDecArgDef($1, $4, $5, *$6, true);

                  $$->currentParams = $1->currentParams;
                  $1->currentParams.clear();
                  $$->currentParams.push_back({*$6, type, $5, true});

                  int s = table->currentScope(), offset = table->newOffset($4);
                  Entry *e = new VarEntry(*$6, s, "Var", $4, offset);
                  table->insert(e);
                }
              }

            ;


%%

int main(int argc, char **argv) {
  // Booleans for options
  bool bLexOpt, bParseOpt, bSymbolsOpt, bTACOpt;

  // Creamos las entradas del scope 0
  scope0();

  // Verify all arguments has been passed
  if (argc != 3) {
    cout << "\033[1mSYNOPSIS\n"
      "\t\033[1mmaclang\033[0m lex \033[4mFILE\033[0m\n"
      "\t\033[1mmaclang\033[0m parse \033[4mFILE\033[0m\n"
      "\t\033[1mmaclang\033[0m symbols \033[4mFILE\033[0m\n"
      "\t\033[1mmaclang\033[0m tac \033[4mFILE\033[0m\n";
    return 1;
  } 
  
  // Check if provided method is valid
  bLexOpt = (strcmp(argv[1], "lex") == 0);
  bParseOpt = (strcmp(argv[1], "parse") == 0); 
  bSymbolsOpt = (strcmp(argv[1], "symbols") == 0);
  bTACOpt = (strcmp(argv[1], "tac") == 0);
  if (! (bParseOpt || bSymbolsOpt || bTACOpt || bLexOpt)) {
    cout << "Invalid action: " << argv[1] << endl;

    cout << "\033[1mSYNOPSIS\n"
      "\t\033[1mmaclang\033[0m lex \033[4mFILE\033[0m\n"
      "\t\033[1mmaclang\033[0m parse \033[4mFILE\033[0m\n"
      "\t\033[1mmaclang\033[0m symbols \033[4mFILE\033[0m\n"
      "\t\033[1mmaclang\033[0m tac \033[4mFILE\033[0m\n";

    return 1;
  } 
  
  filename = argv[2];
  // check if file was succesfully opened.
  if ((yyin = fopen(filename, "r")) == 0) {
    cout << "There was an error opening the file" << endl;
    return -1;
  }
  // reset lines and columns
  yylineno = 1; 
  yycolumn = 1;

  // apply lexing if lexing option is passed
  // if not, yyparse will call yylex.
  int tok;
  queue<string> tokens;
  while(bLexOpt && (tok = yylex()))
  {
    tokens.push("\033[0;33m" + to_string(tok) + ":\033[1;36m " + yytext + "\033[0m\n");
  }
  // if were asked just for lexing print the results of it and return
  if (bLexOpt) {
    if(errors.empty()) {
      printf("TOKENS:\n");
      printQueue(tokens);
    }
    else {
      printQueue(errors);
    }
    fclose(yyin);
    return 0;
  }

  // reset lines and columns
  yylineno = 1; 
  yycolumn = 1;

  // Create the type graph
  createTypeGraph();

  // start parsing
  yyparse();

  if (errors.empty()) {
    if (bParseOpt) {
      ast->printTree(NULL);
    } else if (bSymbolsOpt) {
      table->printTable();
    } else if (bTACOpt) {
      tac->print();
    }
  } 
  
  else {
    // print all errors
    printQueue(errors);
    return 1;
  }

  return 0;
}

void scope0(void) {
  // Basic Types.
  vector<string> primitives = {"Unit", "Bool", "Char", "Int", "Float", "String"};
  for (string t : primitives) {
    table->insert(new PrimitiveEntry(t));
  }

  // VARIABLES
  VarEntry *ve;

  // NULL pointer
  ve = new VarEntry("NULL", 0, "Var", new PointerType(predefinedTypes["Unit"]), 0, "NULL");
  table->insert(ve);
  tac->gen("assignw " + ve->addr + " 0");

  // Inicializando la variable lastbase
  tac->gen("assignw lastbase 0");

  // New line
  ExpressionNode *nl = new NodeSTRING("\n");
  ArrayType *t = new ArrayType(predefinedTypes["Char"], new NodeINT(1), true);
  t->size-> addr = tac->newTemp();
  tac->gen("assignw " + t->size-> addr + " 1");
  nl->addr = tac->newStr("\"\\n\"");
  ve = new VarEntry("nl", 0, "Var", t, 0, "nl");
  table->insert(ve);


  // FUNCTIONS.
  FunctionEntry *fe;
  vector<string> temps = vector<string>(12);
  vector<string> labels = vector<string>(7);

  // Read functions
  fe = new FunctionEntry("read", 0, "Function");
  fe->args.push_back({"text", "(Char)[]", true, NULL});
  fe->return_type = predefinedTypes["Unit"];
  fe->addr = "READ";
  fe->optargs_addr = "!";
  fe->def_scope = 0;
  table->insert(fe);
  // Generamos el tac;
  tac->gen("@function " + fe->addr + " 4");
  temps[0] = tac->newTemp();
  tac->gen("assignw " + temps[0] + " BASE[0]");
  tac->gen("read " + temps[0]);
  tac->gen("return 0");
  tac->gen("@endfunction 4");

  fe = new FunctionEntry("readc", 0, "Function");
  fe->return_type = predefinedTypes["Char"];
  fe->addr = "READC";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  // Generamos el tac;
  tac->gen("@function " + fe->addr + " 0");
  temps[0] = tac->newTemp();
  tac->gen("readc " + temps[0]);
  tac->gen("return " + temps[0]);
  tac->gen("@endfunction 0");

  fe = new FunctionEntry("readi", 0, "Function");
  fe->return_type = predefinedTypes["Int"];
  fe->addr = "READI";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  // Generamos el tac
  tac->gen("@function " + fe->addr + " 0");
  temps[0] = tac->newTemp();
  tac->gen("readi " + temps[0]);
  tac->gen("return " + temps[0]);
  tac->gen("@endfunction 0");

  fe = new FunctionEntry("readf", 0, "Function");
  fe->return_type = predefinedTypes["Float"];
  fe->addr = "READF";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  // Generamos el tac
  tac->gen("@function " + fe->addr + " 0");
  temps[0] = tac->newFloat();
  tac->gen("readf " + temps[0]);
  tac->gen("return " + temps[0]);
  tac->gen("@endfunction 0");

  // Adding char to integer function.
  fe = new FunctionEntry("ctoi", 0, "Function");
  fe->args.push_back({"c", "Char", false, NULL});
  fe->return_type = predefinedTypes["Int"];
  fe->addr = "CTOI";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  // Generamos el tac
  tac->gen("@function " + fe->addr + " 1");
  temps[0] = tac->newTemp();
  tac->gen("assignw " + temps[0] + " BASE[0]");
  tac->gen("return " + temps[0]);
  tac->gen("@endfunction 1");

  // Adding integer to char function.
  fe = new FunctionEntry("itoc", 0, "Function");
  fe->args.push_back({"n", "Int", false, NULL});
  fe->return_type = predefinedTypes["Char"];
  fe->addr = "ITOC";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  // Generamos el tac
  tac->gen("@function " + fe->addr + " 4");
  temps[0] = tac->newTemp();
  tac->gen("assignb " + temps[0] + " BASE[0]");
  tac->gen("return " + temps[0]);
  tac->gen("@endfunction 4");

  // Adding float to integer function.
  fe = new FunctionEntry("ftoi", 0, "Function");
  fe->args.push_back({"n", "Float", false, NULL});
  fe->return_type = predefinedTypes["Int"];
  fe->addr = "FTOI";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  // Generamos el tac
  temps[0] = tac->newFloat();
  temps[1] = tac->newTemp();
  tac->gen("@function " + fe->addr + " 4");
  tac->gen("assignw " + temps[0] + " BASE[0]");
  tac->gen("ftoi " + temps[1] + " " + temps[0]);
  tac->gen("return " + temps[1]);
  tac->gen("@endfunction 4");

  // Adding integer to float function.
  fe = new FunctionEntry("itof", 0, "Function");
  fe->args.push_back({"n", "Int", false, NULL});
  fe->return_type = predefinedTypes["Float"];
  fe->addr = "ITOF";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = "!";
  temps[0] = tac->newTemp();
  temps[1] = tac->newFloat();
  tac->gen("@function " + fe->addr + " 4");
  tac->gen("assignw " + temps[0] + " BASE[0]");
  tac->gen("itof " + temps[1] + " " + temps[0]);
  tac->gen("return " + temps[1]);
  tac->gen("@endfunction 4");

  // Adding "print" function.
  // Primero creamos un arreglo vacio
  Type *voidt = new Type();
  voidt->width = 0;
  ArrayType *voidarray = new ArrayType(voidt, new NodeINT(0));
  voidarray->size->addr = "0";
  ExpressionNode *NULLarray = new NodeArray(NULL, voidarray);
  NULLarray->addr = "0";

  fe = new FunctionEntry("print", 0, "Function");
  fe->args.push_back({"buffer", "(Char)[]", false, NULL});
  fe->args.push_back({"chars", "(Char)[]", false, NULLarray});
  fe->args.push_back({"ints", "(Int)[]", false, NULLarray});
  fe->args.push_back({"floats", "(Float)[]", false, NULLarray});
  fe->args.push_back({"strings", "((Char)[])[]", false, NULLarray});
  fe->args.push_back({"end", "(Char)[]", false, nl});
  fe->return_type = predefinedTypes["Unit"];
  fe->addr = "PRINT";
  fe->def_scope = 0;
  table->insert(fe);
  fe->optargs_addr = tac->newArray(5);

  // Generamos el tac
  for (int i = 0; i < 11; i++) temps[i] = tac->newTemp();
  temps[11] = tac->newFloat();
  for (int i = 0; i < 7; i++) labels[i] = tac->newLabel();
  tac->gen("@function " + fe->addr + " 24");
  tac->gen("assignb test " + fe->optargs_addr + "[4]");
  tac->gen("goif " + labels[0] + " test");
  tac->gen("assignw BASE[20] " + nl->addr);
  tac->gen("@label " + labels[0]);
  tac->gen("assignw " + temps[0] + " 4");
  tac->gen("assignw " + temps[1] + " 4");
  tac->gen("assignw " + temps[2] + " 4");
  tac->gen("assignw " + temps[3] + " 4");
  tac->gen("assignw " + temps[4] + " 4");
  tac->gen("assignw " + temps[5] + " BASE[0]");
  tac->gen("@label " + labels[1]);
  tac->gen("assignb " + temps[6] + " " + temps[5] + "[" + temps[0] + "]");
  tac->gen("add " + temps[0] + " " + temps[0] + " 1");
  tac->gen("eq test " + temps[6] + " 0");
  tac->gen("goif " + labels[1] + "_end test");
  tac->gen("eq test " + temps[6] + " 37");
  tac->gen("goif " + labels[2] + " test");
  tac->gen("printc " + temps[6]);
  tac->gen("goto " + labels[1]);
  tac->gen("@label " + labels[2]);
  tac->gen("assignb " + temps[6] + " " + temps[5] + "[" + temps[0] + "]");
  tac->gen("add " + temps[0] + " " + temps[0] + " 1");
  tac->gen("eq test " + temps[6] + " 99");
  tac->gen("goif " + labels[3] + " test");
  tac->gen("eq test " + temps[6] + " 105");
  tac->gen("goif " + labels[4] + " test");
  tac->gen("eq test " + temps[6] + " 102");
  tac->gen("goif " + labels[5] + " test");
  tac->gen("eq test " + temps[6] + " 115");
  tac->gen("goif " + labels[6] + " test");
  tac->gen("goto " + labels[1]);
  tac->gen("@label " + labels[3]);
  tac->gen("assignw " + temps[7] + " BASE[4]");
  tac->gen("assignb " + temps[8] + " " + temps[7] + "[" + temps[1] + "]");
  tac->gen("printc " + temps[8]);
  tac->gen("add " + temps[1] + " " + temps[1] + " 1");
  tac->gen("goto " + labels[1]);
  tac->gen("@label " + labels[4]);
  tac->gen("assignw " + temps[7] + " BASE[8]");
  tac->gen("assignw " + temps[9] + " " + temps[7] + "[" + temps[2] + "]");
  tac->gen("printi " + temps[9]);
  tac->gen("add " + temps[2] + " " + temps[2] + " 4");
  tac->gen("goto " + labels[1]);
  tac->gen("@label " + labels[5]);
  tac->gen("assignw " + temps[7] + " BASE[12]");
  tac->gen("assignw " + temps[11] + " " + temps[7] + "[" + temps[3] + "]");
  tac->gen("printf " + temps[11]);
  tac->gen("add " + temps[3] + " " + temps[3] + " 4");
  tac->gen("goto " + labels[1]);
  tac->gen("@label " + labels[6]);
  tac->gen("assignw " + temps[7] + " BASE[16]");
  tac->gen("assignw " + temps[10] + " " + temps[7] + "[" + temps[4] + "]");
  tac->gen("add " + temps[10] + " " + temps[10] + " 4");
  tac->gen("print " + temps[10]);
  tac->gen("add " + temps[4] + " " + temps[4] + " 4");
  tac->gen("goto " + labels[1]);
  tac->gen("@label " + labels[1] + "_end");
  tac->gen("assignw " + temps[7] + " BASE[20]");
  tac->gen("add " + temps[7] + " " + temps[7] + " 4");
  tac->gen("print " + temps[7]);
  tac->gen("return 0");
  tac->gen("@endfunction 24");
}
