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

  using namespace std;

  extern int yylineno;
  extern int yycolumn;
  extern char *filename;
  extern queue<string> errors;

  // AST and TAC 
  TAC *tac = new TAC;
  NodeS *ast;

  // Predefined Types 
  extern map<string, Type*> predefinedTypes;

  // Leblanc-Cook's Symbols Table
  SymbolsTable *table = new SymbolsTable;
%}

%define parse.lac full

%union 
{  
  int                                   integer;
  float                                 flot;
  bool                                  boolean;
  char*                                 str;
  char                                  ch;
  Node                                  *ast;
  NodeS                                 *nS;
  Type                                  *t;
  ExpressionNode                        *expr;
  NodeRoutArgDef                        *routArgsDef;
  NodeRoutArgs                          *routArgs;
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
%right      <str> POINTER
%left       <str> DOT
%nonassoc   <str> ID
%left       <str> OPEN_PAR

%token SEMICOLON
%token CLOSE_PAR
%token OPEN_C_BRACE 
%token CLOSE_C_BRACE
%token COMMA
%token REGISTER 
%token UNION
%token FORGET 
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
%token AT 
%token RIGHT_ARROW
%token RETURN 
%token DEC

%token <integer>  INT
%token <flot>     FLOAT 
%token <ch>       CHAR
%token <str>      STRING 
%token <boolean>  TRUE 
%token <boolean>  FALSE
%token <str>      T_UNIT
%token <str>      T_BOOL
%token <str>      T_CHAR 
%token <str>      T_INT 
%token <str>      T_FLOAT
%token <str>      T_STRING 

%type <ast>           I Inst Action VarInst VarDef UnionDef UnionBody 
%type <ast>           RegBody Conditional OptElsif Elsifs OptElse Def RegDef
%type <ast>           LoopWhile LoopFor RoutDef Actions RoutSign RoutDec N 
%type <expr>          Exp FuncCall Array
%type <expr>          OptAssign Cond OptStep
%type <arrayElems>    ArrExp ArrElems
%type <forSign>       ForSign
%type <routArgs>      RoutArgs
%type <routArgsDef>   OptArgs MandArgs
%type <fcArgs>        ArgsExp
%type <fcpArgs>       PositionalArgs
%type <fcnArgs>       NamedArgs
%type <t>             Type OptReturn
%type <boolean>       OptRef
%type <str>           IdDef UnionId RegId DecId
%type <nS>            S
%type <varList>       VarDefList
%type <funcEntry>     RoutId
%type <integer>       M W

%%

/* ======================= GLOBAL RULES ============================== */
  S       : I 
            { 
              $$ = new NodeS($1); 
              ast = $$; 

              // Verificamos que no quedaron llamadas a funciones de solo declaraciones.
              for (pair<string, vector<pair<unsigned long long, vector<int>>>> f : tac->functionlist) {
                addError("Function '\e[1;3m" + f.first + "\e[0m' undefined.");
              }

              if ($1 != NULL) {
                tac->backpatch($1->nextlist, tac->instructions.size());
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
  Action  : Exp SEMICOLON 
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
          | VarInst SEMICOLON   { $$ = $1; }
          | Conditional         { $$ = $1; }
          | LoopWhile           { $$ = $1; }
          | LoopFor             { $$ = $1; }
          ;
  Def     : UnionDef            { $$ = $1; }
          | RegDef              { $$ = $1; }
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
                    addError("Expected a pointer but '\e[1;3m" + t + "\e[0m' found.");
                    $$ = NULL;
                  }

                  else {
                    $$ = new NodeForget($2);
                    Type *t = ((PointerType*) ($2->type))->type;
                    string type = t->toString();
                    string addr = $2->addr;
                    
                    // Si el tipo es un arreglo o estructura, llamamos a la funcion
                    // para liberar memoria correspondiente
                    if (type.back() == ']' && ! ((ArrayType*) t)->is_pointer) {
                      freeConstArray(t, addr);
                    }
                    else if (type.back() == ']') {
                      freeVarArray(t, addr);
                    }
                    else if (! predefinedTypes.count(type) && type[0] != '^') {
                      freeStruct(t, addr);
                    }

                    tac->gen("free " + addr);
                  }
                }

              | Exp ASSIGNMENT Exp 
                { 
                  string ltype = $1->type->toString();
                  string rtype = $3->type->toString();

                  if (ltype == "$Error" || rtype == "$Error") {
                    $$ = NULL;
                  } 

                  else if (! $1->is_lvalue) {
                    addError("Can't assign to a R-Value.");
                    $$ = NULL;
                  }

                  else if (ltype != rtype) {
                    addError(
                      "Can't assign a '\e[1;3m" + rtype +
                      "\e[0m' to a '\e[1;3m" + ltype + "\e[0m'."
                    );
                    $$ = NULL;
                  } 

                  else {
                    $$ = new NodeAssign($1, $3);

                    if (rtype != "Bool") {
                      // Si el rtype no es booleano, se hace la asignacion comun.
                      tac->gen("assign " + $1->addr + " " + $3->addr);
                    }
                    else {
                      // En caso contrario hay que usar backpatching para realizar una
                      // asignacion del booleano.

                      // Aplicamos backpatching sobre la truelist para realizar la 
                      // asignacion de True, y luego saltamos la asignaicon de False.
                      tac->backpatch($3->truelist, tac->instructions.size());
                      tac->gen("assign " + $1->addr + " True");
                      string label = "E" + to_string(tac->instructions.size() + 2);
                      tac->gen("goto " + label);

                      // Aplicamos backpatching sobre la falselist para realizar la 
                      // asignacion de False, y luego creamos la etiqueta de salto de la
                      // asignacion a True.
                      tac->backpatch($3->falselist, tac->instructions.size());
                      tac->gen("assign " + $1->addr + " False");
                      tac->gen("@label " + label);
                    }
                  }
                }
              ;
  VarDef      : LET Type VarDefList
                { 
                  string type = $2->toString();
                  $$ = NULL;

                  if (type != "$Error") {
                    // Por cada variable en la lista de definicion.
                    for (pair<string, ExpressionNode*> vardef : *$3) {
                      ExpressionNode* exp = vardef.second;
                      string rtype = exp == NULL ? "" : exp->type->toString();

                      // Verificamos que el tipo de la definicion y el tipo de la 
                      // expresion (en caso de haberla) son iguales.
                      if (exp != NULL && type != rtype) {
                        addError(
                          "Can't assign a '\e[1;3m" + rtype +
                          "\e[0m' to a '\e[1;3m" + type + "\e[0m'."
                        );
                      } 

                      else {
                        int s = table->currentScope();
                        string addr;

                        // Verificamos si nos encontramos dentro de una funcion.
                        if (table->ret_type != "") {
                          addr = "base[" + to_string(table->offsets.back()) + "]";
                        }

                        // En caso de que el tipo sea un arreglo o estructura (registro
                        // o union) reservamos la memoria necesaria. Tambien obtenemos
                        // la direccion de memoria correspondiente a la variable.

                        // Si es un arreglo de longitud constante.
                        if (type.back() == ']' && ! ((ArrayType*) $2)->is_pointer) {
                          if (table->ret_type != "") {
                            // Si nos encontramos dentro de una funcion, el arreglo sera
                            // almacenado dinamicamente a pesar de ser constante.
                            allocVarArray($2, addr);
                          } else {
                            addr = tac->newAddr($2->width);
                            allocConstArray($2, addr);
                          }
                        }
                        // Si es un arreglo de longitud variable.
                        else if (type.back() == ']') {
                          if (table->ret_type == "") {
                            addr = tac->newTemp();
                          }
                          allocVarArray($2, addr);
                        }
                        // En cambio si es una estructura excepto un puntero.
                        else if (! predefinedTypes.count(type) && type[0] != '^') {
                          if (table->ret_type != "") {
                            // Si nos encontramos dentro de una funcion, la estructura
                            // sera almacenada dinamicamente.
                            tac->gen("malloc " + addr + " " + to_string($2->width));
                            allocStruct($2, addr);
                          } else {
                            addr = tac->newAddr($2->width);
                            allocStruct($2, addr);
                          }
                        }
                        // En cambio, si no estamos dentro de una funcion
                        else if (table->ret_type == "") {
                          addr = tac->newTemp();
                        }

                        // Declaramos la variable.
                        tac->gen("@declared " + addr + " " + vardef.first);

                        // Almacenamos la entrada.
                        int offset = table->offsets.back();
                        Entry *e;
                        if(type.back() != ']') {
                          e = new VarEntry(
                            vardef.first, 
                            s, 
                            "Var", 
                            $2, 
                            offset,
                            addr
                          );
                        }
                        else{
                          ArrayType *current = (ArrayType*) $2;
                          e = new VarArrayEntry(vardef.first, s, "Var", current, offset, addr);
                        }
                        table->insert(e);
                        table->offsets.back() += $2->width;

                        // En caso de haber una expresion, se realiza la asignacion.
                        if (exp != NULL) {
                          $$ = new NodeAssignList(
                            $$, 
                            new NodeAssign(new NodeID(vardef.first, $2), exp)
                          );

                          if (rtype != "Bool") {
                            // Si la expresion no es booleana, se realiza una asignacion 
                            // comun.
                            tac->gen("assign " + addr + " " + exp->addr);
                          }
                          else {
                            // En caso contrario se utiliza backpatching para realizar
                            // la asignacion correcta segun los distintos saltos.
                            
                            // Backpatching sobre la truelist.
                            tac->backpatch(exp->truelist, tac->instructions.size());
                            tac->gen("assign " + addr + " True");
                            string label = "E" + to_string(tac->instructions.size() + 2);
                            // Salto para evitar la asignacion de False.
                            tac->gen("goto " + label);
                            // Backpatching sobre la falselist.
                            tac->backpatch(exp->falselist, tac->instructions.size());
                            tac->gen("assign " + addr + " False");
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
                  if ($1 != "" && ($2 == NULL || $2->type->toString() != "$Error")) {
                    $$->push_back({$1, $2});
                  }
                }  

              | VarDefList COMMA IdDef OptAssign  
                {
                  $$ = $1;
                  if ($3 != "" && ($4 == NULL || $4->type->toString() != "$Error")) {
                    $$->push_back({$3, $4});
                  } 
                }
              ;   
  
  IdDef       : ID 
                {
                  // Verificamos que no hay otro identificador igual en este scope.
                  if (! table->verifyInsert($1)) {
                    addError((string) "Redefinition of '\e[1;3m" + $1 + "\e[0m'.");
                    $$ = (char*) "";
                  } 
                  else {
                    $$ = $1; 
                  }
                }
  
  OptAssign   : /* lambda */                { $$ = NULL; }
              | ASSIGNMENT Exp              { $$ = $2; }
              ;


/* ======================= TYPES ===================================== */
  Type  : Type OPEN_BRACKET Exp CLOSE_BRACKET 
          { 
            // Verificamos que la expresion interna sea un entero.
            if ($1->toString() != "$Error" && $3->type->toString() == "Int") {
              $$ = new ArrayType($1, $3);
            } else {
              $$ = predefinedTypes["$Error"];
            }
          }

        | POINTER Type 
          { 
            if ($2->toString() != "$Error") {
              $$ = new PointerType($2); 
            } else {
              $$ = predefinedTypes["$Error"];
            }
          }

        | ID 
          {
            Entry *e;
            // Verificamos que el identificador existe y corresponde a una estructura.
            if ((e = table->lookup($1)) == NULL) {
              addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
              $$ = predefinedTypes["$Error"];
            } 
            else if (e->category != "Type" && e->category != "Structure") {
              addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a type.");
              $$ = predefinedTypes["$Error"];
            } 
            else {
              $$ = new PrimitiveType($1);
              $$->width = ((StructureEntry*) e)->width;
            }
          }

        | OPEN_PAR Type CLOSE_PAR             { $$ = $2; }
        | T_UNIT                              { $$ = predefinedTypes["Unit"]; }
        | T_BOOL                              { $$ = predefinedTypes["Bool"]; }
        | T_CHAR                              { $$ = predefinedTypes["Char"]; }
        | T_INT                               { $$ = predefinedTypes["Int"]; }
        | T_FLOAT                             { $$ = predefinedTypes["Float"]; }
        | T_STRING                            
          { 
            $$ = new ArrayType(predefinedTypes["Char"], new NodeINT(1), true); 
          }
        ;


/* ======================= EXPRESSIONS =============================== */
  W     : /* lambda */        
          { 
            $$ = tac->instructions.size(); 
            tac->gen("@label E" + to_string($$));
          }

  Exp   : Exp EQUIV W Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $4->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $4, type); 

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
              tac->gen("assign " + $1->addr + " True");
              label = "E" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);
              
              // Usamos backpatching sobre la falselist de la primera expresion para 
              // realizar un salto a la asignacion de False y luego crear la etiqueta
              // de salto de la asignacion del True.
              tac->backpatch($1->falselist, tac->instructions.size());
              tac->gen("assign " + $1->addr + " False");
              tac->gen("@label " + label);

              // Saltamos a la segunda expresion
              tac->gen("goto E" + to_string($3));

              // Repetimos el mismo proceso de la primera expresion.
              $4->addr = tac->newTemp();
              tac->backpatch($4->truelist, tac->instructions.size());
              tac->gen("assign " + $4->addr + " True");
              label = "E" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);
              tac->backpatch($4->falselist, tac->instructions.size());
              tac->gen("assign " + $4->addr + " False");
              tac->gen("@label " + label);

            }

            // Como el resultado es booleano, creamos la truelist y falselist 
            // correspondiente.
            tac->gen("eq test " + $1->addr + " " + $4->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp NOT_EQUIV W Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $4->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $4, type); 

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
              tac->gen("assign " + $1->addr + " True");
              label = "E" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);

              // Usamos backpatching sobre la falselist de la primera expresion para 
              // realizar un salto a la asignacion de False y luego crear la etiqueta
              // de salto de la asignacion del True.
              tac->backpatch($1->falselist, tac->instructions.size());
              tac->gen("assign " + $1->addr + " False");
              tac->gen("@label " + label);

              // Saltamos a la segunda expresion
              tac->gen("goto E" + to_string($3));

              // Repetimos el mismo proceso de la primera expresion.
              $4->addr = tac->newTemp();
              tac->backpatch($4->truelist, tac->instructions.size());
              tac->gen("assign " + $4->addr + " True");
              label = "E" + to_string(tac->instructions.size() + 2);
              tac->gen("goto " + label);
              tac->backpatch($4->falselist, tac->instructions.size());
              tac->gen("assign " + $4->addr + " False");
              tac->gen("@label " + label);
            }

            // Como el resultado es booleano, creamos la truelist y falselist 
            // correspondiente.
            tac->gen("neq test " + $1->addr + " " + $4->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp OR M Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $4->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $4, type); 

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
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $4, type); 

            // Aplicamos backpatching.
            tac->backpatch($1->truelist, $3);
            $$->falselist = merge<unsigned long long>($1->falselist, $4->falselist);
            $$->truelist = $4->truelist;
          }

        | NOT Exp 
          { 
            // Verificamos que el tipo coincide con la operacion.
            Type *type = verifyUnaryOpType($1, $2->type->toString());
            $$ = new NodeUnaryOperator($1, $2, type); 

            // Aplicamos backpatching.
            $$->truelist = $2->falselist;
            $$->falselist = $2->truelist;
          }

        | Exp LESS_THAN Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type);  

            // Aplicamos backpatching.
            tac->gen("lt test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp LESS_EQUAL_THAN Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Aplicamos backpatching.
            tac->gen("leq test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp GREATER_THAN Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Aplicamos backpatching.
            tac->gen("gt test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _"); 
          }

        | Exp GREATER_EQUAL_THAN Exp  
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Aplicamos backpatching.
            tac->gen("geq test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp PLUS Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->gen("add " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp MINUS Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->gen("sub " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp ASTERISK Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->gen("mult " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp DIV Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->gen("div " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp MODULE Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->gen("mod " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | MINUS Exp  
          { 
            // Verificamos que el tipo coincide con la operacion
            Type *type = verifyUnaryOpType($1, $2->type->toString());
            $$ = new NodeUnaryOperator($1, $2, type); 

            // Agregamos las instrucciones del TAC.
            $$->addr = tac->newTemp();
            tac->gen("minus " + $$->addr + " " + $2->addr);
          }

        | PLUS Exp
          { 
            // Verificamos que el tipo coincide con la operacion.
            Type *type = verifyUnaryOpType($1, $2->type->toString());
            $$ = $2; 
          }

        | Exp POWER Exp 
          { 
            // Verificamos que los tipos coinciden con la operacion
            Type *t1 = $1->type;
            Type *t2 = $3->type;
            Type *type = verifyBinayOpType($2, t1->toString(), t2->toString());
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            // Generamos el codigo TAC para la exponencial.
            $$->addr = tac->newTemp();
            // Inicializamos el resultado en 1
            tac->gen("assign " + $$->addr + " 1");

            // Creamos una etiqueta para el loop
            string loop_name = tac->newLabel();
            tac->gen("@label " + loop_name);

            // Verificamos si el exponente es menor o igual a 0, en ese caso salimos del
            // bucle
            tac->gen("leq test " + $3->addr + " 0");
            tac->gen("goif " + loop_name + "_end test");

            // Siguiente iteracion
            tac->gen("mult " + $$->addr + " " + $$->addr + " " + $1->addr);
            tac->gen("sub " + $3->addr + " " + $3->addr + " 1");
            tac->gen("goto " + loop_name);

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
              addError("'\e[1;3m" + ltype + "\e[0m' type can't be indexed.");
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]); 
            } 
            // O que la expresion de acceso no sea entera.
            else if (itype != "$Error" && itype != "Int") {
              addError(
                "Expected a '\e[1;3mInt\e[0m' but '\e[1;3m" +
                itype + "\e[0m' found."
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

              // Si el tipo base es un arreglo constante, entonces no accedemos a memoria 
              // si no que nos movemos a traves de ella sumando el numero de elementos
              // correspondiente a la base.
              if(type->toString().back() == ']' && ! ((ArrayType*) type)->is_pointer) {
                string t = tac->newTemp();
                $$->addr = tac->newTemp();
                tac->gen("mult " + t + " " + $3->addr + " " + to_string(type->width));
                tac->gen("add " + $$->addr + " " + $1->addr + t);
              }

              // En caso contrario, se hace un acceso a memoria.
              else {
                string t = tac->newTemp();
                $$->addr = tac->newTemp();
                tac->gen("mult " + $$->addr + " " + $3->addr + " " + to_string(type->width));

                // Si el tipo base es booleano, aplicamos el backpatching correspondiente.
                if (type->toString() == "Bool") {
                  $$->truelist = {tac->instructions.size()};
                  tac->gen("goif " + $$->addr + " _");
                  $$->falselist = {tac->instructions.size()};
                  tac->gen("goto _");
                }
              }
            }
          }
        | POINTER Exp  
          { 
            // Verificamos que el tipo base no sea erroneo.
            if ($2->type->toString() == "$Error") {
              $$ = new NodePointer($2, predefinedTypes["$Error"]);
            } 
            // O no sea un puntero.
            else if ($2->type->category != "Pointer") {
              addError(
                "'\e[1;3m" + $2->type->toString() + 
                "\e[0m' type can't be desreferenced."
              );
              $$ = new NodePointer($2, predefinedTypes["$Error"]); 
            } 
            else {
              Type *type = ((PointerType*) $2->type)->type;
              $$ = new NodePointer($2, type); 
              // La desreferenciacion es equivalente al acceso de memoria sin 
              // desplazamiento
              $$->addr = $2->addr + "[0]";
            }
          }

        | Exp DOT ID 
          { 
            // Verificamos que el tipo base no es erronea.
            if ($1->type->toString() == "$Error") {
              $$ = new NodeDot($1, $3, predefinedTypes["$Error"]);
            } 
            // O no sea un tipo "primitivo" (extendiendo a las estructuras).
            else if ($1->type->category != "Primitive") {
              addError(
                "'\e[1;3m" + $1->type->toString() + 
                "\e[0m' type can't be accessed."
              );
              $$ = new NodeDot($1, $3, predefinedTypes["$Error"]);
            } 
            else {
              Entry *e = table->lookup($1->type->toString()); 
              // O no sea una estructura.
              if (e->category != "Structure") {
                addError(
                  "'\e[1;3m" + $1->type->toString() + 
                  "\e[0m' type can't be accessed."
                );
                $$ = new NodeDot($1, $3, predefinedTypes["$Error"]);
              } 
              
              else {
                StructureEntry *se = (StructureEntry*) e;
                VarEntry *field = (VarEntry*) table->lookup($3, se->def_scope);

                // O no tenga el campo indicado.
                if (field == NULL) {
                  addError(
                    "'\e[1;3m" + $1->type->toString() + 
                    "\e[0m' has no member '\e[1;3m" + 
                    $3 + "\e[0m'."
                  );
                  $$ = new NodeDot($1, $3, predefinedTypes["$Error"]);
                } 

                else {
                  $$ = new NodeDot($1, $3, field->type);

                  // El acceso a campo es equivalente al acceso a memoria desplazado
                  // por el offset del campo.
                  $$->addr = $1->addr + "[" + to_string(field->offset) + "]";

                  // Si el campo es booleano agregamos el backpatching correspondiente.
                  if (field->type->toString() == "Bool") {
                    $$->truelist = {tac->instructions.size()};
                    tac->gen("goif " + $$->addr + " _");
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
            if ((e = table->lookup($1)) == NULL) {
              addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
              $$ = new NodeID($1, predefinedTypes["$Error"]);
            } 
            // Y sea una variable.
            else if (e->category != "Var") {
              addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a variable.");
              $$ = new NodeID($1, predefinedTypes["$Error"]);
            } 
            else {
              VarEntry *ve = (VarEntry*) e;
              $$ = new NodeID($1, ve->type); 

              // Si nos encontramos fuera de una funcion, usamos la etiqueta de la 
              // variable.
              if (table->ret_type == "") {
                $$->addr = ve->addr;
              }
              // Si no, usamos desplazamiento en memoria.
              else {
                $$->addr = "base[" + to_string(ve->offset) + "]";
              }

              // Si la variable es booleana agregamos el backpatching correspondiente.
              if (ve->type->toString() == "Bool") {
                $$->truelist = {tac->instructions.size()};
                tac->gen("goif " + $$->addr + " _");
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
              if (type.back() == ']' && ! ((ArrayType*) $2)->is_pointer) {
                tac->gen("malloc " + $$->addr + " " + to_string($2->width));
                allocConstArray($2, $$->addr);
              }
              else if (type.back() == ']') {
                allocVarArray($2, $$->addr);
              }
              else if (! predefinedTypes.count(type) && type[0] != '^') {
                tac->gen("malloc " + $$->addr + " " + to_string($2->width));
                allocStruct($2, $$->addr);
              }
            }

            else {
              $$ = new ExpressionNode();
              $$->type = predefinedTypes["$Error"];
            }
          }

        | OPEN_PAR Exp ASSIGNMENT Exp CLOSE_PAR         
            { 
              string ltype = $2->type->toString();
              string rtype = $4->type->toString();

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
              else if (ltype != rtype) {
                addError(
                  "Can't assign a '\e[1;3m" + rtype +
                  "\e[0m' to a '\e[1;3m" + ltype + "\e[0m'."
                );
                $$ = new ExpressionNode();
                $$->type = predefinedTypes["$Error"];
              } 
              
              else {
                $$ = new NodeAssign($2, $4); 
                $$->type = $4->type;

                if (rtype != "Bool") {
                  // Si la expresion no es booleana, se realiza la asignacion al L-Value
                  // y a la expresion que retorna la asignacion.
                  $$->addr = tac->newTemp();
                  tac->gen("assign " + $2->addr + " " + $4->addr);
                  tac->gen("assign " + $$->addr + " " + $4->addr);
                }
                else {
                  // En caso contrario tenemos que usar backpatching para hacer la 
                  // asignacion correspondiente.
                  tac->backpatch($4->truelist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " True");
                  $$->truelist = {tac->instructions.size()};
                  tac->gen("goto _");

                  tac->backpatch($4->falselist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " False");
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
            tac->gen("assign " + $$->addr + " '" + $1 + "'"); 
          }

        | INT
          { 
            $$ = new NodeINT($1); 
            $$->addr = tac->newTemp();
            tac->gen("assign " + $$->addr + " " + to_string($1));
          }

        | FLOAT 
          { 
            $$ = new NodeFLOAT($1); 
            $$->addr = tac->newTemp();
            tac->gen("assign " + $$->addr + " " + to_string($1));
          }

        | STRING 
          { 
            $$ = new NodeSTRING($1); 
            $$->addr = tac->newStr($1);
          }
        ;


/* ======================= ARRAYS ==================================== */
  Array     : OPEN_BRACKET ArrExp CLOSE_BRACKET   
              { 
                // Verificamos que no hubo errores en las expresiones que conforman el
                // arreglo.
                if ($2->type->toString() != "$Error") {
                  int size = ((NodeArrayElems*) $2)->current_size;
                  $$ = new NodeArray($2, new ArrayType($2->type, new NodeINT(size)));

                  // Creamos una nueva etiqueta para reservar memoria estaticamente. 
                  $$->addr = tac->newAddr(size * $2->type->width);
                  NodeArrayElems *exp = $2;

                  // Realizamos la asignacion de cada expresion del arreglo.
                  while (--size >= 0) {
                    tac->gen(
                      "assign " + $$->addr + "[" + 
                      to_string(size * $2->type->width) + "] " + exp->rvalue->addr
                    );
                    exp = exp->head;
                  }

                } 
                else {
                  $$ = new NodeArray($2, predefinedTypes["$Error"]); 
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
                
                else if (type1 != type2) {
                  addError(
                    (string) "All elements of an array must have the same type" +
                    ", but found '\e[1;3m" + type1 + "\e[0m' and " +
                    "'\e[1;3m" + type2 + "\e[0m'."
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
                  tac->gen("assign " + $2->addr + " True");

                  label = "E" + to_string(tac->instructions.size() + 2);
                  tac->gen("goto " + label);
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " False");
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
                    (string) "All elements of an array must have the same type" +
                    ", but found '\e[1;3m" + type1 + "\e[0m' and " +
                    "'\e[1;3m" + type2 + "\e[0m'."
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
                  tac->gen("assign " + $2->addr + " True");

                  label = "E" + to_string(tac->instructions.size() + 2);
                  tac->gen("goto " + label);
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " False");
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

                        if ((e = table->lookup($1)) == NULL) {
                          addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
                          type = predefinedTypes["$Error"];
                        } 
                        
                        else if (e->category!="Function" && e->category!="Declaration") {
                          addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a function.");
                          type = predefinedTypes["$Error"];
                        } 
                        
                        else {
                          FunctionEntry *fe = (FunctionEntry*) e;
                          bool correctTypes = true;
                          string type_str;

                          int numPositional = $3->positionalArgs.size(), i = 0;

                          for (tuple<string, string, bool, ExpressionNode*> arg : fe->args) {
                            if (i < numPositional) {
                              type_str = $3->positionalArgs[i]->type->toString();

                              if (get<1>(arg) != type_str) {
                                addError(
                                  (string) "Argument '\e[1;3m" + get<0>(arg) + 
                                  "\e[0m' " + "must be '\e[1;3m" + get<1>(arg) + 
                                  "\e[0m' but '\e[1;3m" + type_str + 
                                  "\e[0m' found."
                                );
                                correctTypes = false;
                              }

                              if ($3->keywords.count(get<0>(arg))) {
                                addError(
                                  (string) "Got multiple values of '\e[1;3m" + 
                                  get<0>(arg) + "\e[0m'."
                                );
                                correctTypes = false;
                              }

                              tac->gen("param " + $3->positionalArgs[i]->addr);
                            } 
                            
                            else if ($3->keywords.count(get<0>(arg))) {
                              type_str = $3->namedArgs[get<0>(arg)]->type->toString();

                              if (get<1>(arg) != type_str) {
                                addError(
                                  (string) "Argument '\e[1;3m" + get<0>(arg) + 
                                  "\e[0m' " + "must be '\e[1;3m" + get<1>(arg) + 
                                  "\e[0m' but '\e[1;3m" + type_str + 
                                  "\e[0m' found."
                                );
                                correctTypes = false;
                              }
                              $3->keywords.erase(get<0>(arg));

                              tac->gen("param " + $3->namedArgs[get<0>(arg)]->addr);
                            } 
                            
                            else if (get<3>(arg) == NULL) {
                              addError(
                                (string) "Missing required positional arguments."
                              );
                              correctTypes = false;
                            }

                            else {
                              tac->gen("param " + get<3>(arg)->addr);
                            }

                            i++;
                          }

                          if ($3->keywords.size()) {
                            string err = "Got unexpected keywords: ";
                            for (string k : $3->keywords) {
                              err += "'\e[1;3m" + k + "\e[0m', ";
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
                          $$ = new NodeFunctionCall($1, $3, false, type); 
                          $$->addr = tac->newTemp();

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

                            tac->gen(
                              "call " + $$->addr + " _ " + to_string(fe->args.size())
                            );
                          }

                          else {
                            tac->gen(
                              "call " + $$->addr + " " + fe->addr + " " + 
                              to_string(fe->args.size())
                            );
                          }

                          if (type->toString() == "Bool") {
                            $$->truelist = {tac->instructions.size()};
                            tac->gen("goif " + $$->addr + " _");
                            $$->falselist = {tac->instructions.size()};
                            tac->gen("goto _");
                          }
                        } 
                        else {
                          $$ = new NodeFunctionCall($1, $3, false, type); 
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

                        if ($1->type->toString() == "Bool") {
                          string label;

                          $1->addr = tac->newTemp();

                          tac->backpatch($1->truelist, tac->instructions.size());
                          tac->gen("assign " + $1->addr + " True");

                          label = "E" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($1->falselist, tac->instructions.size());
                          tac->gen("assign " + $1->addr + " False");
                          tac->gen("@label " + label);
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

                        if ($3->type->toString() == "Bool") {
                          string label;

                          $3->addr = tac->newTemp();

                          tac->backpatch($3->truelist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " True");

                          label = "E" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($3->falselist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " False");
                          tac->gen("@label " + label); 
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
                        $$ = new NodeFunctionCallNamedArgs(NULL, $1, $3);

                        if ($3->type->toString() == "Bool") {
                          string label;

                          $3->addr = tac->newTemp();

                          tac->backpatch($3->truelist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " True");

                          label = "E" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($3->falselist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " False");
                          tac->gen("@label " + label);
                        }

                        $$->currentArgs[$1] = $3; 
                        $$->keywords.insert($1);
                      }
                    }

                  | NamedArgs COMMA ID ASSIGNMENT Exp           
                    { 
                      $$ = new NodeFunctionCallNamedArgs($1, $3, $5); 
                      if ($1 != NULL && $1->currentArgs.count($3)) {
                        addError(
                          (string) "Got multiple values of '\e[1;3m" + $3 + "\e[0m'."
                        );
                        $$ = NULL;
                      } 
                      
                      else if ($1 == NULL || $5->type->toString() == "$Error") {
                        $$ = NULL;
                      } 
                      
                      else {
                        $$->currentArgs = $1->currentArgs;

                        if ($5->type->toString() == "Bool") {
                          string label;

                          $5->addr = tac->newTemp();

                          tac->backpatch($5->truelist, tac->instructions.size());
                          tac->gen("assign " + $5->addr + " True");

                          label = "E" + to_string(tac->instructions.size() + 2);
                          tac->gen("goto " + label);
                          tac->backpatch($5->falselist, tac->instructions.size());
                          tac->gen("assign " + $5->addr + " False");
                          tac->gen("@label " + label);
                        }

                        $$->currentArgs[$3] = $5;
                        $1->currentArgs.clear();

                        $$->keywords = $1->keywords;
                        $$->keywords.insert($3);
                        $1->keywords.clear();
                      }
                    }
                  ;


/* ======================= UNION DEFINITION ========================== */
  UnionDef  : UnionId OPEN_C_BRACE UnionBody CLOSE_C_BRACE  
              { 
                if ($1 != "" && $3 != NULL) {
                  int def_s = table->currentScope();
                  table->exitScope(); 
                  int s = table->currentScope();

                  Entry *e = new StructureEntry(
                    $1, 
                    s, 
                    "Structure", 
                    def_s,
                    ((NodeUnionFields*) $3)->max_width
                  );
                  table->insert(e);
                }

                $$ = NULL;
                table->offsets.pop_back();
              }
            ;

  UnionId   : UNION IdDef   
              { 
                table->newScope(); 
                $$ = $2; 
                table->offsets.push_back(0);
              }
            ;  

  UnionBody  : Type IdDef SEMICOLON                          
              { 
                if ($2 == "" || $1->toString() == "$Error") {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeUnionFields(NULL, $1, $2, $1->width); 
                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $2, 
                    s, 
                    "Field", 
                    $1, 
                    table->offsets.back(),
                    "",
                    table
                  );
                  table->insert(e);
                }
              }

            | UnionBody Type IdDef SEMICOLON 
              { 
                if ($1 == NULL || $3 == "" || $2->toString() == "$Error") {
                  $$ = NULL;
                } 

                else {
                  int max_width = ((NodeUnionFields*) $1)->max_width;
                  max_width = max_width > $2->width ? max_width : $2->width;
                  $$ = new NodeUnionFields($1, $2, $3, max_width); 
                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $3, 
                    s, 
                    "Field", 
                    $2, 
                    table->offsets.back(),
                    "",
                    table
                  );
                  table->insert(e);
                }
              }
            ;


/* ======================= REGISTER DEFINITION ======================= */
  RegDef    : RegId OPEN_C_BRACE RegBody CLOSE_C_BRACE  
              { 
                if ($1 != "" && $3 != NULL) {
                  int def_s = table->currentScope();
                  table->exitScope();
                  int s = table->currentScope();

                  Entry *e = new StructureEntry(
                    $1, 
                    s, 
                    "Structure", 
                    def_s,
                    table->offsets.back()
                  );
                  table->insert(e);
                }

                $$ = NULL;
                table->offsets.pop_back();
              }
            ;   

  RegId     : REGISTER IdDef 
              { 
                table->newScope(); 
                $$ = $2; 
                table->offsets.push_back(0);
              }
            ; 

  RegBody    : Type IdDef OptAssign SEMICOLON            
              { 
                bool cond = $2 == "" || $1->toString() == "$Error" ||
                  ($3 != NULL && $3->type->toString() == "$Error");

                if (cond) {
                  $$ = NULL;
                } 

                else if ($3 != NULL && $1->toString() != $3->type->toString()) {
                  addError(
                    "Can't assign a '\e[1;3m" + $3->type->toString() +
                    "\e[0m' to a '\e[1;3m" + $1->toString() + "\e[0m'."
                  );
                  $$ = NULL;
                }
                
                else {
                  $$ = new NodeRegFields(NULL, $1, $2, $3);
                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $2, 
                    s, 
                    "Field", 
                    $1, 
                    table->offsets.back(),
                    "",
                    table
                  );
                  table->insert(e);
                  table->offsets.back() += $1->width; 
                }
              }

            |  RegBody Type IdDef OptAssign SEMICOLON    
              { 
                if ($3 == "" || $2->toString() == "$Error") {
                  $$ = NULL;
                } 

                else if ($4 != NULL && $2->toString() != $4->type->toString()) {
                  addError(
                    "Can't assign a '\e[1;3m" + $4->type->toString() +
                    "\e[0m' to a '\e[1;3m" + $2->toString() + "\e[0m'."
                  );
                  $$ = NULL;
                }

                else if ($1 == NULL) {
                  $$ = NULL;
                }
                
                else {
                  $$ = new NodeRegFields($1, $2, $3, $4);
                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $3, 
                    s, 
                    "Field", 
                    $2, 
                    table->offsets.back(),
                    "",
                    table
                  );
                  table->insert(e);
                  table->offsets.back() += $2->width; 
                }
              }
            ;


/* ======================= CONDITIONALS ============================== */
  Conditional : If Cond THEN M I N M OptElsif M OptElse DONE  
                { 
                  $$ = new NodeConditional($2, $5, $8, $10);
                  table->exitScope(); 

                  tac->backpatch($2->truelist, $4);
                  tac->backpatch($2->falselist, $7);

                  vector<unsigned long long> t;
                  if ($5 != NULL) {
                    t = merge<unsigned long long>($5->nextlist, $6->nextlist);
                  }
                  else {
                    t = $6->nextlist;
                  }

                  if ($8 != NULL && $10 != NULL) {
                    t = merge<unsigned long long>(t, $8->truelist);
                    t = merge<unsigned long long>(t, $10->nextlist);
                    tac->backpatch($8->falselist, $9);
                  }
                  
                  else if ($8 != NULL) {
                    t = merge<unsigned long long>(t, $8->truelist);
                    t = merge<unsigned long long>(t, $8->falselist);
                  }

                  else if ($10 != NULL) {
                    t = merge<unsigned long long>(t, $10->nextlist);
                  }

                  $$->nextlist = t;
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
                      "Condition must be a '\e[1;3mBool\e[0m' but '\e[1;3m" +
                      $1->type->toString() + "\e[0m' found."
                    );
                  }
                  $$ = $1;
                }
              ;

  If          : IF                              { table->newScope(); }
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
  LoopWhile : While W Cond M DO I DONE                      
              { 
                $$ = new NodeWhile($3, $6); 
                table->exitScope();

                if ($6 != NULL) {
                  tac->backpatch($6->nextlist, $2);
                }
                tac->backpatch($3->truelist, $4);
                $$->nextlist = $3->falselist;
                tac->gen("goto " + to_string($2));
              }
            ; 

  While     : WHILE                { table->newScope(); }
            ;

  LoopFor   : ForSign DO I DONE 
              {
                $$ = new NodeFor($1, $3);

                if ($3 != NULL) {
                  tac->backpatch($3->nextlist, tac->instructions.size());
                }

                if ($1->step != NULL) {
                  tac->gen("add " + $1->addr + " " + $1->addr + " " + $1->step->addr);
                }
                else {
                  tac->gen("add " + $1->addr + " " + $1->addr + " 1");
                }

                tac->gen("goto " + $1->label);
                tac->gen("@label " + $1->label + "_end");
                table->exitScope();
              }

  ForSign   : For OPEN_PAR IdDef SEMICOLON Exp SEMICOLON Exp OptStep CLOSE_PAR 
              { 
                string type1 = $5->type->toString();
                string type2 = $7->type->toString();
                string type3 = $8 == NULL ? "" : $8->type->toString();

                int s = table->currentScope();
                Type *t = predefinedTypes["Float"];
                VarEntry *e = new VarEntry(
                  $3, 
                  s, 
                  "Var", 
                  t, 
                  table->offsets.back(),
                  tac->newTemp()
                );
                table->insert(e); 
                table->offsets.back() += predefinedTypes["Float"]->width;

                if (type1 != "$Error" && type1 != "Float" && type1 != "Int") {
                  addError(
                    "Initial value in a for loop must be "
                    "'\e[1;3mInt\e[0m' or '\e[1;3mFloat\e[0m' "
                    "but '\e[1;3m" + type1 + "\e[0m' found."
                  );
                }

                if (type2 != "$Error" && type2 != "Float" && type2 != "Int") {
                  addError(
                    "End value in a for loop must be "
                    "'\e[1;3mInt\e[0m' or '\e[1;3mFloat\e[0m' "
                    "but '\e[1;3m" + type2 + "\e[0m' found."
                  );
                }

                if ($8 != NULL && type3 != "$Error" && type3 != "Float" && type3 != "Int") {
                  addError(
                    "Step value in a for loop must be "
                    "'\e[1;3mInt\e[0m' or '\e[1;3mFloat\e[0m' "
                    "but '\e[1;3m" + type3 + "\e[0m' found."
                  );
                }

                $$ = new NodeForSign($3, $5, $7, $8);
                $$->addr = tac->newTemp();
                $$->label = tac->newLabel();

                tac->gen("assign " + $$->addr + " " + $5->addr);
                tac->gen("@label " + $$->label);

                // Verificacion de iteracion del for
                tac->gen("geq test " + $$->addr + " " + $7->addr);
                tac->gen("goif " + $$->label + "_end test");
                
                tac->gen("assign " + e->addr + " " + $$->addr);
              }
            ;

  For       : FOR                                       { table->newScope(); }
            ;

  OptStep   : /* lambda */                              { $$ = NULL; }
            | SEMICOLON Exp                             { $$ = $2; }
            ;


/* ======================= SUBROUTINES DEFINITION ==================== */
  RoutDef   : RoutSign OPEN_C_BRACE Actions CLOSE_C_BRACE   
              { 
                if ($1->is_error) {
                  NodeError *err = (NodeError*) $1;
                  table->exitScope();
                  table->exitScope();
                  if (err->errInfo != "")
                    table->erase(err->errInfo, table->currentScope());

                  $$ = new NodeError();
                } 

                else {
                  table->exitScope();
                  table->exitScope();

                  $$ = new NodeRoutineDef($1, $3); 
                }

                table->ret_type = "";
                table->offsets.pop_back();

                tac->gen("@endfunction");
                tac->backpatch($1->nextlist, tac->instructions.size());
              }
            ; 

  RoutSign  : RoutId OPEN_PAR RoutArgs CLOSE_PAR OptReturn  
              {
                FunctionEntry *fe;

                if ($3 == NULL || $1->first == "" || $5->toString() == "$Error") {
                  NodeError *err = new NodeError();
                  if ($1->second == NULL)
                    err->errInfo = $1->first;
                  else 
                    err->errInfo = "";
                  $$ = err;
                } 
                
                else if ($1->second != NULL) {
                  bool error = false;
                  FunctionEntry *fe_dec = $1->second;

                  for (int i = 0; i < $3->params.size(); i++) {
                    if (
                      i == fe_dec->args.size() ||
                      get<0>($3->params[i]) != get<0>(fe_dec->args[i]) ||
                      get<1>($3->params[i]) != get<1>(fe_dec->args[i]) ||
                      get<2>($3->params[i]) != get<2>(fe_dec->args[i])
                    ) {
                      addError(
                        (string) "Sign of function dont match with "
                        "the declaration."
                      );
                      error = true;
                      break;
                    }

                    if (get<3>($3->params[i]) != NULL) {
                      addError(
                        (string) "Default values must be in declaration."
                      );
                      error = true;
                      break;
                    }
                  }

                  if ($5->toString() != fe_dec->return_type->toString()) {
                    addError(
                      (string) "Sign of function dont match with "
                      "the declaration."
                    );
                    error = true;
                  }

                  if (error) {
                    NodeError *err = new NodeError();
                    err->errInfo = "";
                    $$ = err;
                  }

                  else {
                    fe = (FunctionEntry*) table->lookup($1->first);
                    fe->args = fe_dec->args;
                    fe->addr = tac->newFunc();
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
                  }
                }
                
                else {
                  fe = (FunctionEntry*) table->lookup($1->first);
                  fe->return_type = $5;
                  fe->def_scope = table->currentScope();  
                  fe->args = $3->params;
                  fe->addr = tac->newFunc();
                  $3->params.clear();
                  
                  $$ = new NodeRoutineSign($1->first, $3, $5);
                }

                if ($5->toString() != "$Error") {
                  table->ret_type = $5->toString();
                }

                table->newScope();

                $$->nextlist = {tac->instructions.size()};
                tac->gen("goto _");
                $$->addr = fe->addr;
                tac->gen("@function " + $$->addr);
              }
            ;

  RoutId    : DEF ID 
              {
                Entry *e = table->lookup($2);

                if (
                  e != NULL &&
                  e->scope == table->currentScope() &&
                  e->category != "Declaration"
                ) {
                  addError(
                    (string) "Redefinition of '\e[1;3m" 
                    + $2 + "\e[0m'."
                  );
                  $$ = new pair<string, FunctionEntry*>("", NULL);
                } 
                
                else if (e != NULL && e->category == "Declaration") {
                  FunctionEntry *fe_dec = (FunctionEntry*) e;
                  $$ = new pair<string, FunctionEntry*>($2, fe_dec); 
                  
                  int s = table->currentScope();
                  FunctionEntry *fe = new FunctionEntry($2, s, "Function");
                  fe->args = fe_dec->args;
                  fe->return_type = fe_dec->return_type; 
                  table->insert(fe);
                }

                else {
                  $$ = new pair<string, FunctionEntry*>($2, NULL);
                  int s = table->currentScope();
                  Entry *e = new FunctionEntry($2, s, "Function");
                  table->insert(e);
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
                }
              }

            | MandArgs COMMA OptArgs                        
              { 
                if (($1 == NULL) || ($3 == NULL)) {
                  $$ = NULL;
                } 

                else {
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
                if ($3 == "" || $1->toString() == "$Error") {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeRoutArgDef(NULL, $1, $2, $3, NULL);
                  $$->currentParams.push_back({$3, $1->toString(), $2, NULL});

                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $3, 
                    s, 
                    "Var", 
                    $1, 
                    table->offsets.back()
                  );
                  table->insert(e);
                  table->offsets.back() += $1->width; 
                }
              }
            | MandArgs COMMA Type OptRef IdDef              
              { 
                if ($1 == NULL || $5 == "" || $3->toString() == "$Error") {
                  $$ = NULL;
                } 

                else {
                  $$ = new NodeRoutArgDef(
                    $1, $3, $4, $5, NULL
                  );
                  $$->currentParams = $1->currentParams;
                  $1->currentParams.clear();
                  $$->currentParams.push_back({$5, $3->toString(), $4, NULL});

                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $5, 
                    s, 
                    "Var", 
                    $3, 
                    table->offsets.back()
                  );
                  table->insert(e);
                  table->offsets.back() += $3->width; 
                }
              }
            ;   

  OptArgs   : Type OptRef IdDef ASSIGNMENT Exp 
              { 
                string type = $1->toString();
                string rtype = $5->type->toString();

                if (type == "$Error" || rtype == "$Error") {
                  $$ = NULL;
                } 
                
                else if (type != rtype) {
                  addError(
                    "Can't assign a '\e[1;3m" + rtype +
                    "\e[0m' to a '\e[1;3m" + type + "\e[0m'."
                  );
                  $$ = NULL;
                } 

                else if ($3 == "") {
                  $$ = NULL;
                }
                
                else {
                  $$ = new NodeRoutArgDef(NULL, $1, $2, $3, $5);
                  $$->currentParams.push_back({$3, type, $2, (ExpressionNode*) $5});

                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $3, 
                    s, 
                    "Var",
                    $1, 
                    table->offsets.back()
                  );
                  table->insert(e);
                  table->offsets.back() += $1->width; 
                }
              }

            | OptArgs COMMA Type OptRef IdDef ASSIGNMENT Exp                                
              { 
                string type = $3->toString();
                string rtype = $7->type->toString();
                if (type == "$Error" || rtype == "$Error") {
                  $$ = NULL;
                } 
                
                else if (type != rtype) {
                  addError(
                    "Can't assign a '\e[1;3m" + rtype +
                    "\e[0m' to a '\e[1;3m" + type + "\e[0m'."
                  );
                  $$ = NULL;
                } 
                
                else if ($1 == NULL || $5 == "") {
                  $$ = NULL;
                } 
                
                else {
                  $$ = new NodeRoutArgDef(
                    $1, $3, $4, $5, $7
                  );

                  $$->currentParams = $1->currentParams;
                  $1->currentParams.clear();
                  $$->currentParams.push_back({$5, type, $4, (ExpressionNode*) $7});

                  int s = table->currentScope();
                  Entry *e = new VarEntry(
                    $5, 
                    s, 
                    "Var", 
                    $3, 
                    table->offsets.back()
                  );
                  table->insert(e);
                  table->offsets.back() += $3->width; 
                }
              }

            ;
  
  OptRef    : /* lambda */                { $$ = false; }
            | AT                          { $$ = true; }
            ; 
  
  OptReturn : /* lambda */                { $$ = predefinedTypes["Unit"]; }
            | RIGHT_ARROW Type            { $$ = $2; }
            ; 
  
  Actions   : /* lambda */                { $$ = NULL; }
            | Actions Action                                
              { 
                if ($1 == NULL && $2 == NULL) {
                  $$ = NULL;
                }

                else if ($2 == NULL) {
                  $$ = $1;
                }

                else {
                  $$ = new NodeActions($1, $2); 
                }
              }

            | Actions RETURN Exp SEMICOLON                  
              {
                if (table->ret_type != "" && $3->type->toString() != table->ret_type) {
                  addError(
                    "Expected return type '\e[1;3m" + 
                    table->ret_type + "\e[0m' but " +
                    "'\e[1;3m" + $3->type->toString() + "\e[0m' found."
                  );
                  $$ = new NodeError();
                } 

                else {
                  $$ = new NodeReturn($3);
                  tac->gen("return " + $3->addr);
                }
              }

            | Actions RETURN SEMICOLON                      
              {
                if (table->ret_type != "" && "Unit" != table->ret_type) {
                  addError(
                    "Expected return type '\e[1;3m" + 
                    table->ret_type + "\e[0m' but " +
                    "'\e[1;3mUnit\e[0m' found ."
                  );
                  $$ = new NodeError();
                } 

                else {
                  $$ = new NodeReturn();
                  tac->gen("return 0");
                }
              }
            ;


/* ======================= SUBROUTINES DECLARATION =================== */
  RoutDec   : DecId OPEN_PAR RoutArgs CLOSE_PAR OptReturn 
              {
                table->exitScope();

                if ($3 != NULL && $1 != "" && $5->toString() != "$Error") {
                  int s = table->currentScope();
                  FunctionDeclarationEntry *e = new FunctionDeclarationEntry(
                    $1, 
                    s,
                    "Declaration",
                    $3->params,
                    $5
                  );
                  e->addr = "";
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


%%

int main(int argc, char **argv) {
  FunctionEntry *fe;
  // Booleans for options
  bool bLexOpt, bParseOpt, bSymbolsOpt, bTACOpt;
  // open file to extract the tokens
  extern FILE *yyin;

  // Adding scope 0 elements.
  vector<string> primitives = {"Unit", "Bool", "Char", "Int", "Float", "String"};
  for (string t : primitives) {
    table->insert(new PrimitiveEntry(t));
  }

  // Adding "read" function.
  fe = new FunctionEntry("read", 0, "Function");
  fe->return_type = new ArrayType(predefinedTypes["Char"], new NodeINT(1), true);
  fe->addr = "READ";
  fe->def_scope = 0;
  table->insert(fe);

  // Adding "print" function.
  fe = new FunctionEntry("print", 0, "Function");
  fe->args.push_back({"text", "(Char)[]", false, NULL});
  fe->return_type = predefinedTypes["Unit"];
  fe->addr = "PRINT";
  fe->def_scope = 0;
  table->insert(fe);


  // Verify all arguments has been passed
  if (argc != 3) {
    cout << "\e[1mSYNOPSIS\n"
      "\t\e[1mmaclang\e[0m lex \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m parse \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m symbols \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m tac \e[4mFILE\e[0m\n";
    return 1;
  } 
  
  // Check if provided method is valid
  bLexOpt = (strcmp(argv[1], "lex") == 0);
  bParseOpt = (strcmp(argv[1], "parse") == 0); 
  bSymbolsOpt = (strcmp(argv[1], "symbols") == 0);
  bTACOpt = (strcmp(argv[1], "tac") == 0);
  if (! (bParseOpt || bSymbolsOpt || bTACOpt || bLexOpt)) {
    cout << "Invalid action: " << argv[1] << endl;

    cout << "\e[1mSYNOPSIS\n"
      "\t\e[1mmaclang\e[0m lex \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m parse \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m symbols \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m tac \e[4mFILE\e[0m\n";

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
    tokens.push("\e[0;33m" + to_string(tok) + ":\e[1;36m " + yytext + "\e[0m\n");
  }
  fclose(yyin);
  // if were asked just for lexing print the results of it and return
  if (bLexOpt) {
    if(errors.empty())
      printQueue(tokens);
    else
      printQueue(errors);
    return 0;
  }

  // check if file was succesfully opened.
  if ((yyin = fopen(filename, "r")) == 0) {
    cout << "There was an error opening the file" << endl;
    return -1;
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
