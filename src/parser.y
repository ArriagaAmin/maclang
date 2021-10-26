%{  
  #include <iostream>
  #include <queue>
  #include <string>
  #include <cstring>
  #include <set>
  #include <stack>

  #include "table.hpp"
  #include "tac.hpp"

  using namespace std;

  extern int yylex(void);
  extern int yylineno;
  extern int yycolumn;
  extern char *yytext;
  extern char *filename;

  // queues for tokens and errors
  extern queue<string> errors;
  NodeS *ast;

  // queues for tokens and errors
  queue<string> tokens;
  extern queue<string> errors;

  // Predefined Types 
  extern map<string, Type*> predefinedTypes;

  // Leblanc-Cook's Symbols Table
  SymbolsTable *table = new SymbolsTable;

  // TAC 
  TAC *tac = new TAC;

  // Funciones para reservar memoria para tipos compuestos 
  void allocConstArray(Type *t, string final_addr);
  void allocVarArray(Type *t, string final_addr);
  void allocStruct(Type *t, string final_addr);

  // Funciones para liberar memoria para tipos compuestos 
  void freeConstArray(Type *t, string final_addr);
  void freeVarArray(Type *t, string final_addr);
  void freeStruct(Type *t, string final_addr);

  // Prints error;
  void yyerror(string s);

  // Prints the queue to std.
  void printQueue(queue<string> queueToPrint);

  // add a error.
  void addError(string error);

  /* ==== TYPE VERIFICATION METHODS ==== */

  // verifies the type of an operand
  bool verify(set<string> accepted_types, Type *type);
  // verifies the types of 2 operands
  bool verify(set<pair<string, string>> accepted_types, Type *type1, Type *type2);

  // verifies types for a binary operator
  Type *verifyBinayOpType(
    set<pair<string, string>> accepted_types, 
    set<string> types1,
    set<string> types2,
    Type *type1, 
    Type *type2,
    string op,
    Type *return_type
  );

  // verifies type for a unary operator
  Type *verifyUnaryOpType(
    set<string> accepted_types, 
    Type *type, 
    string op,
    Type *return_type
  );

  // token names for readability on lexer
  string tokenNames [] = {
    "SEMICOLON",
    "OPEN_PAR",
    "CLOSE_PAR",
    "ASSIGNMENT",
    "OPEN_BRACKET",
    "CLOSE_BRACKET",
    "OPEN_C_BRACE",
    "CLOSE_C_BRACE",
    "COMMA",
    "REGISTER",
    "DOT",
    "UNION",
    "POINTER",
    "NEW",
    "FORGET",
    "IF",
    "THEN",
    "ELSIF",
    "ELSE",
    "WHILE",
    "DO",
    "DONE",
    "FOR",
    "LET",
    "DEF",
    "DEC",
    "AT",
    "RIGHT_ARROW",
    "RETURN",
    "INT",
    "FLOAT",
    "CHAR",
    "STRING",
    "ID",
    "TRUE", 
    "FALSE",
    "T_UNIT",
    "T_BOOL",
    "T_CHAR",
    "T_INT",
    "T_FLOAT",
    "T_STRING",
    "POWER",
    "AND",
    "OR",
    "NOT_EQUIV",
    "NOT",
    "EQUIV",
    "GREATER_EQUAL_THAN",
    "LESS_EQUAL_THAN",
    "GREATER_THAN",
    "LESS_THAN",
    "PLUS",
    "MINUS",
    "MODULE", 
    "DIV",
    "ASTERISK"
  };

  Node *global;
%}

%define parse.lac full

%union 
{  
  int    integer;
  float  flot;
  bool   boolean;
  char*  str;
  char   ch;
  Node   *ast;
  NodeS  *nS;
  Type   *t;
  ExpressionNode *expr;
  NodeRoutArgDef *routArgsDef;
  NodeRoutArgs *routArgs;
  NodeArrayElems *arrayElems;
  NodeForSign *forSign;
  NodeFunctionCallArgs *fcArgs;
  NodeFunctionCallPositionalArgs *fcpArgs;
  NodeFunctionCallNamedArgs *fcnArgs;
  vector<pair<string, ExpressionNode*>> *varList;
  tuple<string, int, int> *scopeid;
}

%locations
%start S

%nonassoc   NEW
%right      ASSIGNMENT
%left       EQUIV NOT_EQUIV
%left       OR AND 
%nonassoc   LESS_THAN LESS_EQUAL_THAN GREATER_THAN GREATER_EQUAL_THAN
%right      NOT
%left       PLUS MINUS
%left       ASTERISK DIV MODULE
%right      POWER
%left       OPEN_BRACKET CLOSE_BRACKET
%right      POINTER
%left       DOT
%nonassoc   ID
%left       OPEN_PAR


%token SEMICOLON 1
%token OPEN_PAR 2
%token CLOSE_PAR 3
%token ASSIGNMENT 4
%token OPEN_BRACKET 5
%token CLOSE_BRACKET 6
%token OPEN_C_BRACE 7
%token CLOSE_C_BRACE 8
%token COMMA 9
%token REGISTER 10
%token DOT 11
%token UNION 12
%token POINTER 13
%token NEW 14
%token FORGET 15
%token IF 16
%token THEN 17
%token ELSIF 18
%token ELSE 19
%token WHILE 20
%token DO 21
%token DONE 22
%token FOR 23
%token LET 24
%token DEF 25
%token AT 26
%token RIGHT_ARROW 27
%token RETURN 56
%token DEC 57

%token <integer>  INT 28
%token <flot>     FLOAT 29
%token <ch>       CHAR 30
%token <str>      STRING 31
%token <str>      ID 32
%token <boolean>  TRUE 33 
%token <boolean>  FALSE 34
%token <str>      T_UNIT 35
%token <str>      T_BOOL 36
%token <str>      T_CHAR 37
%token <str>      T_INT 38
%token <str>      T_FLOAT 39
%token <str>      T_STRING 40
%token <str>      POWER 41
%token <str>      AND 42
%token <str>      OR 43
%token <str>      NOT_EQUIV 44
%token <str>      NOT 45
%token <str>      EQUIV 46
%token <str>      GREATER_EQUAL_THAN 47
%token <str>      LESS_EQUAL_THAN 48
%token <str>      GREATER_THAN 49
%token <str>      LESS_THAN 50
%token <str>      PLUS 51
%token <str>      MINUS 52
%token <str>      MODULE 53 
%token <str>      DIV 54
%token <str>      ASTERISK 55

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
%type <scopeid>       RoutId
%type <integer>       M

%%

/* ======================= GLOBAL RULES ============================== */
  S       : I 
            { 
              $$ = new NodeS($1); 
              ast = $$; 

              if ($1 != NULL) {
                tac->backpatch($1->nextlist, tac->instructions.size());
              }
            }
          ;
  M       : /* lambda */        { $$ = tac->instructions.size(); }
  I       : /* lambda */        { $$ = NULL; }
          | I M Inst 
            { 
              if ($1 == NULL && $3 == NULL) {
                $$ = NULL;
              } else if ($3 == NULL) {
                $$ = $1;
              } else {
                $$ = new NodeI($1, $3); 
                if ($1 != NULL) {
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
              $$ = $1;
              if ($1->type->toString() == "Bool") {
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
                    $$ = new NodeError();
                  } 

                  else if ($2->type->category != "Pointer") {
                    addError(
                      "Expected a pointer but '\e[1;3m" + 
                      $2->type->toString() + "\e[0m' found."
                    );
                    $$ = new NodeError();
                  }

                  else {
                    $$ = new NodeForget($2);
                    Type *t = ((PointerType*) ($2->type))->type;
                    string type = t->toString();
                    string addr = $2->addr;
                    
                    // Si el tipo es un arreglo de longitud constante
                    if (type.back() == ']' && ((ArrayType*) t)->size->is_lit) {
                      freeConstArray(t, addr);
                    }

                    // En cambio si es un arreglo de longitud variable
                    else if (type.back() == ']') {
                      freeVarArray(t, addr);
                    }

                    // En cambio si es una estructura
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
                    $$ = new ExpressionNode();
                  } 

                  else if (! $1->is_lvalue) {
                    addError("Can't assign to a R-Value.");
                    $$ = new ExpressionNode();
                  }

                  else if (ltype != rtype) {
                    addError(
                      "Can't assign a '\e[1;3m" + rtype +
                      "\e[0m' to a '\e[1;3m" + ltype + "\e[0m'."
                    );
                    $$ = new ExpressionNode();
                  } 

                  else {
                    $$ = new NodeAssign($1, $3);

                    if (rtype != "Bool") {
                      // Handling arrays
                      if(ltype.find("[]") != string::npos)
                      {
                        tac->gen("assign base["+ $1->addr + "] " + $3->addr);
                      }
                      else
                        tac->gen("assign " + $1->addr + " " + $3->addr);
                    }
                    else {
                      tac->backpatch($3->truelist, tac->instructions.size());
                      tac->gen("assign " + $1->addr + " True");
                      tac->gen("goto " + to_string(tac->instructions.size() + 2));
                      tac->backpatch($3->falselist, tac->instructions.size());
                      tac->gen("assign " + $1->addr + " False");
                    }
                  }
                }
              ;
  VarDef      : LET Type VarDefList
                { 
                  string type = $2->toString();
                  $$ = NULL;

                  if (type != "$Error") {
                    for (pair<string, ExpressionNode*> vardef : *$3) {
                      string rtype = vardef.second == NULL ?
                        "" : vardef.second->type->toString();

                      if (vardef.second != NULL && type != rtype) {
                        addError(
                          "Can't assign a '\e[1;3m" + rtype +
                          "\e[0m' to a '\e[1;3m" + type + "\e[0m'."
                        );
                      } 

                      else {
                        int s = table->currentScope();
                        string addr;

                        // Si el tipo es un arreglo de longitud constante
                        if (type.back() == ']' && ((ArrayType*) $2)->size->is_lit) {
                          addr = tac->newAddr($2->width);
                          allocConstArray($2, addr);
                        }

                        // En cambio si es un arreglo de longitud variable
                        else if (type.back() == ']') {
                          addr = tac->newTemp();
                          allocVarArray($2, addr);
                        }

                        // En cambio si es una estructura
                        else if (! predefinedTypes.count(type) && type[0] != '^') {
                          addr = tac->newAddr($2->width);
                          allocStruct($2, addr);
                        }

                        // En caso contrario, usamos un temporal comun.
                        else {
                          addr = tac->newTemp();
                        }

                        int offset = table->offsets.back();
                        Entry *e;
                        if(type.back() == ']') {
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
                          e = new VarArrayEntry(
                            vardef.first, 
                            s, 
                            "Var", 
                            current, 
                            offset,
                            addr
                          );
                        }

                        table->insert(e);
                        table->offsets.back() += $2->width;

                        if (vardef.second != NULL) {
                          $$ = new NodeAssignList(
                            $$, 
                            new NodeAssign(new NodeID(vardef.first, $2), vardef.second)
                          );

                          if (rtype != "Bool") {
                            tac->gen("assign " + addr + " " + vardef.second->addr);
                          }
                          else {
                            tac->backpatch(vardef.second->truelist, tac->instructions.size());
                            tac->gen("assign " + addr + " True");
                            tac->gen("goto " + to_string(tac->instructions.size() + 2));

                            tac->backpatch(vardef.second->falselist, tac->instructions.size());
                            tac->gen("assign " + addr + " False");
                          }
                        }
                      }

                      if ($$ != NULL) {
                        $$->nextlist = {};
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
            $$ = new ArrayType(predefinedTypes["Char"], new NodeINT(8), true); 
          }
        ;


/* ======================= EXPRESSIONS =============================== */
  Exp   : Exp EQUIV Exp 
          { 
            set<string> types = {"Bool", "Char", "Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Bool", "Bool"},
              {"Char", "Char"},
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "==", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            tac->gen("eq test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp NOT_EQUIV Exp 
          { 
            set<string> types = {"Bool", "Char", "Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Bool", "Bool"},
              {"Char", "Char"},
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "!=", 
              predefinedTypes["Bool"]
            );                                      
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            tac->gen("neq test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp OR M Exp 
          { 
            set<string> types = {"Bool"};
            set<pair<string, string>> tuples = { {"Bool", "Bool"} };

            Type *t1 = $1->type;
            Type *t2 = $4->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "||", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeBinaryOperator($1, $2, $4, type); 

            tac->backpatch($1->falselist, $3);
            $$->truelist = merge<unsigned long long>($1->truelist, $4->truelist);
            $$->falselist = $4->falselist;
          }

        | Exp AND M Exp 
          { 
            set<string> types = {"Bool"};
            set<pair<string, string>> tuples = { {"Bool", "Bool"} };

            Type *t1 = $1->type;
            Type *t2 = $4->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "&&", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeBinaryOperator($1, $2, $4, type); 

            tac->backpatch($1->truelist, $3);
            $$->falselist = merge<unsigned long long>($1->falselist, $4->falselist);
            $$->truelist = $4->truelist;
          }

        | NOT Exp 
          { 
            Type *type = verifyUnaryOpType(
              {"Bool"}, 
              $2->type, 
              "!", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeUnaryOperator($1, $2, type); 
            $$->truelist = $2->falselist;
            $$->falselist = $2->truelist;
          }

        | Exp LESS_THAN Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "<", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            tac->gen("lt test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp LESS_EQUAL_THAN Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "<=", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            tac->gen("leq test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp GREATER_THAN Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              ">", 
              predefinedTypes["Bool"]
            );
            $$ = new NodeBinaryOperator($1, $2, $3, type);

            tac->gen("gt test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _"); 
          }

        | Exp GREATER_EQUAL_THAN Exp  
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              ">=", 
              predefinedTypes["Bool"]
            );

            $$ = new NodeBinaryOperator($1, $2, $3, type); 

            tac->gen("geq test " + $1->addr + " " + $3->addr);
            $$->truelist = {tac->instructions.size()};
            $$->falselist = {tac->instructions.size() + 1};
            tac->gen("goif test _");
            tac->gen("goto _");
          }

        | Exp PLUS Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *return_type;
            if (t1->toString() == "Float" || t2->toString() == "Float") {
              return_type = predefinedTypes["Float"];
            } 
            else {
              return_type = predefinedTypes["Int"];
            }

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "+", 
              return_type
            );

            $$ = new NodeBinaryOperator($1, $2, $3, type); 
            $$->addr = tac->newTemp();
            tac->gen("add " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp MINUS Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *return_type;

            if ((t1->toString() == "Float") || (t2->toString() == "Float")) {
              return_type = predefinedTypes["Float"];
            } 
            else {
              return_type = predefinedTypes["Int"];
            }

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "-", 
              return_type
            );

            $$ = new NodeBinaryOperator($1, $2, $3, type); 
            $$->addr = tac->newTemp();
            tac->gen("sub " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp ASTERISK Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *return_type;
            if ((t1->toString() == "Float") || (t2->toString() == "Float")) {
              return_type = predefinedTypes["Float"];
            } else {
              return_type = predefinedTypes["Int"];
            }
            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "*", 
              return_type
            );

            $$ = new NodeBinaryOperator($1, $2, $3, type); 
            $$->addr = tac->newTemp();
            tac->gen("mult " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp DIV Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "/", 
              predefinedTypes["Float"]
            );
            $$ = new NodeBinaryOperator($1, $2, $3, type);

            $$->addr = tac->newTemp();
            tac->gen("div " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | Exp MODULE Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Float"},
              {"Int", "Float"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *return_type;
            if ((t1->toString() == "Float") || (t2->toString() == "Float")) {
              return_type = predefinedTypes["Float"];
            } 
            else {
              return_type = predefinedTypes["Int"];
            }
            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "%", 
              return_type
            );

            $$ = new NodeBinaryOperator($1, $2, $3, type); 
            $$->addr = tac->newTemp();
            tac->gen("mod " + $$->addr + " " + $1->addr + " " + $3->addr);
          }

        | MINUS Exp  
          { 
            Type *return_type;
            if ($2->type->toString() == "Int") {
              return_type = predefinedTypes["Int"];
            } else {
              return_type = predefinedTypes["Float"];
            }

            Type *type = verifyUnaryOpType({"Int", "Float"}, $2->type, "-", return_type);

            $$ = new NodeUnaryOperator($1, $2, type); 

            $$->addr = tac->newTemp();
            tac->gen("minus " + $$->addr + $2->addr);
          }

        | PLUS Exp              { $$ = $2; }

        | Exp POWER Exp 
          { 
            set<string> types = {"Int", "Float"};
            set<pair<string, string>> tuples = {
              {"Int", "Int"},
              {"Float", "Int"}
            };

            Type *t1 = $1->type;
            Type *t2 = $3->type;

            Type *return_type;

            if ((t1->toString() == "Float")) {
              return_type = predefinedTypes["Float"];
            } 
            else {
              return_type = predefinedTypes["Int"];
            }

            Type *type = verifyBinayOpType(
              tuples, 
              types, 
              types, 
              t1, 
              t2, 
              "**", 
              return_type
            );

            $$ = new NodeBinaryOperator($1, $2, $3, type); 
            $$->addr = tac->newTemp();

            // Generamos el codigo para la exponencial.
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

            if (ltype == "$Error") {
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]);
            }
              
            else if ($1->type->category != "Array") {
              addError("'\e[1;3m" + ltype + "\e[0m' type can't be indexed.");
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]); 
            } 

            else if (itype != "$Error" && itype != "Int") {
              addError(
                "Expected a '\e[1;3mInt\e[0m' but '\e[1;3m" +
                itype + "\e[0m' found."
              );
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]); 
            }

            else if (itype == "$Error") {
              $$ = new NodeArrayAccess($1, $3, predefinedTypes["$Error"]);
            }
            
            else {
              Type *type = ((ArrayType*) $1->type)->type;
              $$ = new NodeArrayAccess($1, $3, type);
              if(type->toString().find("[]") != string::npos)
              {
                $$->addr = tac->newTemp();
                tac->gen("assign " + $$->addr + " " + $3->addr + "*" + to_string(type->width));
              }
              else
              {
                string t = tac->newTemp();
                $$->addr = tac->newTemp();
                tac->gen("assign " + t + " " + $3->addr + "*" + to_string(type->width));
                tac->gen("assign " + $$->addr + " " + $1->addr + "+" + t);
              } 
            }
          }

        | POINTER Exp  
          { 
            if ($2->type->toString() == "$Error") {
              $$ = new NodePointer($2, predefinedTypes["$Error"]);
            } 
            
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
              $$->addr = tac->newTemp();
              tac->gen("deref " + $$->addr + " " + $2->addr);
            }
          }

        | Exp DOT ID 
          { 
            if ($1->type->toString() == "$Error") {
              $$ = new NodeDot($1, $3, predefinedTypes["$Error"]);
            } 
            
            else if ($1->type->category != "Primitive") {
              addError(
                "'\e[1;3m" + $1->type->toString() + 
                "\e[0m' type can't be accessed."
              );
              $$ = new NodeDot($1, $3, predefinedTypes["$Error"]);
            } 
            
            else {
              Entry *e = table->lookup($1->type->toString()); 

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
                  $$->addr = $1->addr + "[" + to_string(field->offset) + "]";

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
            if ((e = table->lookup($1)) == NULL) {
              addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
              $$ = new NodeID($1, predefinedTypes["$Error"]);
            } 
            
            else if (e->category != "Var") {
              addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a variable.");
              $$ = new NodeID($1, predefinedTypes["$Error"]);
            } 
            
            else {
              VarEntry *ve = (VarEntry*) e;
              $$ = new NodeID($1, ve->type); 

              if (table->ret_type == "") {
                $$->addr = ve->addr;
              }
              else {
                $$->addr = "base[" + to_string(ve->offset) + "]";
              }

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
              tac->gen("malloc " + $$->addr + " " + to_string($2->width));
              string type = $2->toString();

              // Si el tipo es un arreglo de longitud constante
              if (type.back() == ']' && ((ArrayType*) $2)->size->is_lit) {
                allocConstArray($2, $$->addr);
              }

              // En cambio si es un arreglo de longitud variable
              else if (type.back() == ']') {
                allocVarArray($2, $$->addr);
              }

              // En cambio si es una estructura
              else if (! predefinedTypes.count(type) && type[0] != '^') {
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

              if (ltype == "$Error" || rtype == "$Error") {
                $$ = new ExpressionNode();
                $$->type = predefinedTypes["$Error"];
              } 

              else if (! $2->is_lvalue) {
                addError(
                  "Can't assign to a R-Value."
                );
                $$ = new ExpressionNode();
                $$->type = predefinedTypes["$Error"];
              }
              
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
                  $$->addr = tac->newTemp();
                  tac->gen("assign " + $2->addr + " " + $4->addr);
                  tac->gen("assign " + $$->addr + " " + $4->addr);
                }
                else {
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
            $$->addr = tac->newTemp();
            int n = strlen($1);
            tac->gen("malloc " + $$->addr + " " + to_string(4 * (n - 1)));

            // Almacenamos cada caracter
            unsigned i = 0;
            for (int j = 1; j < n-1; j++) {
              tac->gen(
                "assign " + $$->addr + "[" + to_string(i) + "] '" + $1[j] + "'"
              );
              i += predefinedTypes["Char"]->width;
            }
            tac->gen("assign " + $$->addr + "[" + to_string(i) + "] '\\0'");
          }
        ;


/* ======================= ARRAYS ==================================== */
  Array     : OPEN_BRACKET ArrExp CLOSE_BRACKET   
              { 
                if ($2->type->toString() != "$Error") {
                  int size = ((NodeArrayElems*) $2)->current_size;
                  $$ = new NodeArray($2, new ArrayType($2->type, new NodeINT(size))); 
                  $$->addr = tac->newAddr(size * $2->type->width);
                  NodeArrayElems *exp = $2;

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
                  $2->addr = tac->newTemp();

                  tac->backpatch($2->truelist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " True");
                  tac->gen("goto " + to_string(tac->instructions.size() + 2));
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " False");
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
                  $2->addr = tac->newTemp();

                  tac->backpatch($2->truelist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " True");
                  tac->gen("goto " + to_string(tac->instructions.size() + 2));
                  tac->backpatch($2->falselist, tac->instructions.size());
                  tac->gen("assign " + $2->addr + " False");
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
                          bool correctTypes = true, allMand = true;
                          string type_str;

                          int numPositional = $3->positionalArgs.size(), i = 0;

                          for (tuple<string, string, bool, bool> arg : fe->args) {
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

                              if (correctTypes) {
                                tac->gen("param " + $3->positionalArgs[i]->addr);
                              }
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

                              if (correctTypes) {
                                tac->gen("param " + $3->namedArgs[get<0>(arg)]->addr);
                              }
                            } 
                            
                            else if (get<3>(arg) && allMand) {
                              addError(
                                (string) "Missing required positional arguments."
                              );
                              correctTypes = false;
                              allMand = false;
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
                          tac->gen("call " + $$->addr + " " + to_string(fe->args.size()));

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
                          $1->addr = tac->newTemp();

                          tac->backpatch($1->truelist, tac->instructions.size());
                          tac->gen("assign " + $1->addr + " True");
                          tac->gen("goto " + to_string(tac->instructions.size() + 2));
                          tac->backpatch($1->falselist, tac->instructions.size());
                          tac->gen("assign " + $1->addr + " False");
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
                          $3->addr = tac->newTemp();

                          tac->backpatch($3->truelist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " True");
                          tac->gen("goto " + to_string(tac->instructions.size() + 2));
                          tac->backpatch($3->falselist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " False");
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
                          $3->addr = tac->newTemp();

                          tac->backpatch($3->truelist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " True");
                          tac->gen("goto " + to_string(tac->instructions.size() + 2));
                          tac->backpatch($3->falselist, tac->instructions.size());
                          tac->gen("assign " + $3->addr + " False");
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
                          $5->addr = tac->newTemp();

                          tac->backpatch($5->truelist, tac->instructions.size());
                          tac->gen("assign " + $5->addr + " True");
                          tac->gen("goto " + to_string(tac->instructions.size() + 2));
                          tac->backpatch($5->falselist, tac->instructions.size());
                          tac->gen("assign " + $5->addr + " False");
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
                  t = merge<unsigned long long>($5->nextlist, $6->nextlist);

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
                  $$->truelist = merge<unsigned long long>($5->nextlist, $6->nextlist);
                  $$->falselist = $2->falselist;
                }

              | Elsifs M Elsif Cond THEN M I N
                { 
                  $$ = new NodeElsif($1, $4, $7); 
                  tac->backpatch($1->falselist, $2);
                  tac->backpatch($4->truelist, $6);
                  $$->truelist = merge<unsigned long long>($1->truelist, $7->nextlist);
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
                  $$->nextlist = $2->nextlist;
                }
              ;
  Else        : ELSE                             
                { 
                  table->exitScope();
                  table->newScope(); 
                }
              ;


/* ======================= LOOPS ===================================== */
  LoopWhile : While M Cond M DO I DONE                      
              { 
                $$ = new NodeWhile($3, $6); 
                table->exitScope();

                tac->backpatch($6->nextlist, $2);
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

                tac->backpatch($3->nextlist, tac->instructions.size());

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
                if ($1->toString() == "Error") {
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
              }
            ; 

  RoutSign  : RoutId OPEN_PAR RoutArgs CLOSE_PAR OptReturn  
              {
                if ($3 == NULL || get<0>(*$1) == "" || $5->toString() == "$Error") {
                  NodeError *err = new NodeError();
                  if (get<1>(*$1) == -1)
                    err->errInfo = get<0>(*$1);
                  else 
                    err->errInfo = "";
                  $$ = err;
                } 
                
                else if (get<1>(*$1) != -1) {
                  bool error = false;
                  FunctionEntry *fe;
                  fe = (FunctionEntry*) table->lookup(get<0>(*$1), get<1>(*$1));

                  for (int i = 0; i < $3->params.size(); i++) {
                    if (
                      i == fe->args.size() ||
                      get<0>($3->params[i]) != get<0>(fe->args[i]) ||
                      get<1>($3->params[i]) != get<1>(fe->args[i]) ||
                      get<2>($3->params[i]) != get<2>(fe->args[i])
                    ) {
                      addError(
                        (string) "Sign of function dont match with "
                        "the declaration."
                      );
                      error = true;
                      break;
                    }

                    if (! get<3>($3->params[i])) {
                      addError(
                        (string) "Default values must be in declaration."
                      );
                      error = true;
                      break;
                    }
                  }

                  if ($5->toString() != fe->return_type->toString()) {
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

                  else if (get<1>(*$1) == get<2>(*$1)) {
                    fe->category = "Function";
                    fe->def_scope = table->currentScope();
                    $3->params.clear();

                    $$ = new NodeRoutineSign(get<0>(*$1), $3, $5);
                  }

                  else {
                    FunctionEntry *e;
                    e = (FunctionEntry*) table->lookup(get<0>(*$1));
                    e->return_type = $5;
                    e->def_scope = table->currentScope();                  
                    e->args = fe->args;
                    $3->params.clear();
                    
                    $$ = new NodeRoutineSign(get<0>(*$1), $3, $5);
                  }
                }
                
                else {
                  FunctionEntry *e;
                  e = (FunctionEntry*) table->lookup(get<0>(*$1));
                  e->return_type = $5;
                  e->def_scope = table->currentScope();  
                  e->args = $3->params;
                  $3->params.clear();
                  
                  $$ = new NodeRoutineSign(get<0>(*$1), $3, $5);
                }

                if ($5->toString() != "$Error") {
                  table->ret_type = $5->toString();
                }

                table->newScope();
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
                  $$ = new tuple<string, int, int>("", -1, -1);
                } 
                
                else if (e != NULL && e->category == "Declaration") {
                  $$ = new tuple<string, int, int>(
                    $2, e->scope, table->currentScope()
                  ); 
                }

                else {
                  int s = table->currentScope();
                  Entry *e = new FunctionEntry($2, s, "Function");
                  table->insert(e);
                  $$ = new tuple<string, int, int>((string) $2, -1, -1);
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
                  $$->currentParams.push_back({$3, $1->toString(), $2, true});

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
                  $$->currentParams.push_back({$5, $3->toString(), $4, true});

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
                  $$->currentParams.push_back({$3, type, $2,false});

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
                  $$->currentParams.push_back({$5, type, $4,false});

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
                }
              }
            ;


/* ======================= SUBROUTINES DECLARATION =================== */
  RoutDec   : DecId OPEN_PAR RoutArgs CLOSE_PAR OptReturn 
              {
                table->exitScope();

                if ($3 != NULL && $1 != "" && $5->toString() != "$Error") {
                  int s = table->currentScope();
                  Entry *e = new FunctionDeclarationEntry(
                    $1, 
                    s,
                    "Declaration",
                    $3->params,
                    $5
                  );
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

int main(int argc, char **argv)
{
  // Adding scope 0 elements.
  vector<string> primitives = {"Unit", "Bool", "Char", "Int", "Float", "String"};
  for (string t : primitives) {
    table->insert(new PrimitiveEntry(t));
  }
  FunctionEntry *fe = new FunctionEntry("read", 0, "Function");
  fe->return_type = new ArrayType(predefinedTypes["Char"], new NodeINT(1));
  fe->def_scope = 0;
  table->insert(fe);

  fe = new FunctionEntry("print", 0, "Function");
  fe->args.push_back({"text", "(Char)[]", false, true});
  fe->return_type = predefinedTypes["Unit"];
  fe->def_scope = 0;
  table->insert(fe);

  // Booleans for options
  bool bLexOpt = false;
  bool bParseOpt = false;
  bool bSymbolsOpt = false;
  bool bTreeOpt = false;
  bool bRepOpt = false;
  bool bTACOpt = false;

  // Verify all arguments has been passed
  if (argc < 3 || argc > 4) {
    cout << "\e[1mSYNOPSIS\n"
      "\t\e[1mmaclang\e[0m lex \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m parse -t \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m parse -c \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m symbols \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m tac \e[4mFILE\e[0m\n";
    return 1;
  } 
  
  // Check if provided method is valid
  if (
    strcmp(argv[1], "lex") && strcmp(argv[1], "parse") && strcmp(argv[1], "symbols") &&
    strcmp(argv[1], "tac")
    ) {
    cout << "Invalid action: " << argv[1] << endl;
    return 1;
  } 
  
  else if (strcmp(argv[1], "parse") == 0) {
    // Parsing.

    bParseOpt = true;
    // Print tree
    if (strcmp(argv[2], "-t") == 0) { bTreeOpt = true; }
    // Print code representation
    else if (strcmp(argv[2], "-c") == 0) { bRepOpt = true; }
    else {
      cout << "Invalid flag: " << argv[2] << endl;
      return 1;
    }
    filename = argv[3];

  } else if (strcmp(argv[1], "lex") == 0) {
    // Lexing.

    bLexOpt = true;
    filename = argv[2];

  } else if (strcmp(argv[1], "symbols") == 0) {
    // Sumbols table 

    bSymbolsOpt = true;
    filename = argv[2];

  } else if (strcmp(argv[1], "tac") == 0) {
    // TAC

    bTACOpt = true;
    filename = argv[2];
  }
  
  // open file to extract the tokens
  extern FILE *yyin;
  yyin = fopen(filename, "r");
    
  // check if file was succesfully opened.
  if (!yyin) 
  {
    cout << "There was an error opening the file" << endl;
    return -1;
  }

  // apply lexing if lexing option is passed
  // if not, yyparse will call yylex.
  int tok;
  while(bLexOpt && (tok = yylex()))
  {
    // if token can have multiple values, also print the value of the token
    switch(tok) {
      case INT:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;34m " + 
                    tokenNames[tok-1] + "\e[0m = \e[1;36m" + 
                    to_string(yylval.integer) + "\n");
        break;
      case FLOAT:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;32m " + 
                    tokenNames[tok-1] + "\e[0m = \e[1;36m" + 
                    to_string(yylval.flot) + "\n");
        break;
      case CHAR:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;35m " + 
                    tokenNames[tok-1] + "\e[0m = \e[1;36m" + yylval.ch + "\n");
        break;
      case STRING:
      case ID:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;31m " + 
                    tokenNames[tok-1] + "\e[0m = \e[1;36m" + yylval.str + "\n");
        break;
      default:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;37m " + 
                    tokenNames[tok-1] + "\e[0m\n");
    }
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

  // parsing
  yyin = fopen(filename, "r");

  // reset lines and columns
  yylineno = 1; 
  yycolumn = 1;

  // start parsing
  yyparse();

  if (errors.empty()) {
    if (bParseOpt) {
      if (bTreeOpt) {
        ast->printTree(NULL);
      } else {
        ast->print();
      }

    } else if (bSymbolsOpt) {
      table->printTable();

    } else if (bTACOpt) {
      tac->print();
    }

  } else {
    // print all errors
    printQueue(errors);

    return 1;
  }

  return 0;
}

/*
  Prints error.
*/
void yyerror(string s)
{
  string file = strdup(filename);
    
  // Add syntax error
  string error = "\e[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \e[31mSyntax error:\e[0m Unexpected " +
    "token \"" + yytext + "\".\n\n";

  errors.push(error);

  // read the remaining file for more lexical errors.
  while(yylex());
}

/*
  Prints the queue to std.
*/
void printQueue(queue<string> queueToPrint)
{
  while (!queueToPrint.empty()) {
    cout << queueToPrint.front();
    queueToPrint.pop();
  }
}

/*
  Add a error to vector errors.
*/
void addError(string error) {
  string file = strdup(filename);

  string err = "\e[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \e[31mError:\e[0m " + error + "\n\n";

  // add the error to the queue
  errors.push(err);
}

/*
  Verifies of the type is one of the accepted_types.
*/
bool verify(set<string> accepted_types, Type *type) {
  return accepted_types.count(type->toString());
}

/*
  Verifies that the types correspond with an accepted pair of types.
*/
bool verify(set<pair<string, string>> accepted_types, Type *type1, Type *type2) {
  return accepted_types.count({type1->toString(), type2->toString()});
}

/*
  Verfiy that an operand have the correct type for a unary operator.
*/
Type *verifyUnaryOpType(
  set<string> accepted_types, 
  Type *type, 
  string op,
  Type *return_type
) {
  if (type->toString() == "$Error") {
    return predefinedTypes["$Error"];

  } else if (verify(accepted_types, type)) {
    return return_type;

  } else {
    addError(
      (string) "Operator '\e[1;3m" + op + "\e[0m' can't be applied with operand type " +
      "'\e[1;3m" + type->toString() + "\e[0m'."
    );
    return predefinedTypes["$Error"];
  }

}

/*
  Verifies that a pair of operators have the correct types for a binary operator.
*/
Type *verifyBinayOpType(
  set<pair<string, string>> accepted_types, 
  set<string> types1,
  set<string> types2,
  Type *type1, 
  Type *type2,
  string op,
  Type *return_type
) {
  // Verifies if one of the operands has error type.
  if (type1->toString() == "$Error" || type2->toString() == "$Error") {
    return predefinedTypes["$Error"];

  // If there are no errors in the operands.
  } else {
    bool st1 = verify(types1, type1);
    bool st2 = verify(types2, type2);

    // Verify that both types are supported.
    if ((st1 && st2) && verify(accepted_types, type1, type2)) {
      return return_type;

    // If one of the types isn't supported.
    } else {
      addError(
        "Operator '\e[1;3m" + op + "\e[0m' don't matches with operand types: '\e[1;3m" +
        type1->toString() + "\e[0m' and '\e[1;3m" + type2->toString() + "\e[0m'."
      );
      return predefinedTypes["$Error"];
    }
  }
}


void allocConstArray(Type *t, string final_addr) {
  stack<ArrayType*> arrayStack;
  ArrayType* at;
  
  // Recorremos el hiper arreglo hasta conseguir un tipo que no es un arreglo o es un 
  // arreglo de longitud variable.
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']' && ((ArrayType*) t)->size->is_lit);

  // Si nos conseguimos con un arreglo o una estructura
  if (
    t->toString().back() == ']' || 
    (! predefinedTypes.count(t->toString()) && t->toString()[0] != '^')
  ) {
    // Obtenemos la longitud del hiper arreglo
    string size_addr = tac->newTemp();
    tac->gen("assign " + size_addr + " " + to_string(t->width));

    while (! arrayStack.empty()) {
      tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
      arrayStack.pop();
    }

    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    if (t->toString().back() == ']') {
      allocVarArray(t, final_addr + "[" + size_addr + "]");
    } 
    else {
      allocStruct(t, final_addr + "[" + size_addr + "]");
    }

    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }
}

void allocVarArray(Type *t, string final_addr) {
  stack<ArrayType*> arrayStack;
  ArrayType *at;
  
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']');

  string size_addr = tac->newTemp();
  tac->gen("assign " + size_addr + " " + to_string(t->width));

  while (! arrayStack.empty()) {
    tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
    arrayStack.pop();
  }

  tac->gen("malloc " + final_addr + " " + size_addr);

  // Si el tipo base del hiper arreglo no es primitivo ni puntero
  if (! predefinedTypes.count(t->toString()) && t->toString()[0] != '^') {
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    allocStruct(t, final_addr + "[" + size_addr + "]");

    tac->gen("goto " + label);
    tac->gen("goto " + label + "_end");
  }
}

void allocStruct(Type *t, string final_addr) {
  // Obtenemos el scope de definicion de la estructura.
  PrimitiveType *pt = (PrimitiveType*) t;
  StructureEntry *se = (StructureEntry*) table->lookup(pt->id);
  int scope = se->def_scope;

  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type;
    ArrayType *at;

    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();

      if (type.back() == ']') {
        at = (ArrayType*) ve->type;
        if (! at->size->is_lit) {
          allocVarArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
        }
        else {
          allocConstArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");

        }
      }
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        allocStruct(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
      }
    }
  }
}

void freeConstArray(Type *t, string final_addr) {
  stack<ArrayType*> arrayStack;
  ArrayType* at;
  
  // Recorremos el hiper arreglo hasta conseguir un tipo que no es un arreglo o es un 
  // arreglo de longitud variable.
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']' && ((ArrayType*) t)->size->is_lit);

  // Si nos conseguimos con un arreglo o una estructura
  if (
    t->toString().back() == ']' || 
    (! predefinedTypes.count(t->toString()) && t->toString()[0] != '^')
  ) {
    // Obtenemos la longitud del hiper arreglo
    string size_addr = tac->newTemp();
    tac->gen("assign " + size_addr + " " + to_string(t->width));

    while (! arrayStack.empty()) {
      tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
      arrayStack.pop();
    }

    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    if (t->toString().back() == ']') {
      freeVarArray(t, final_addr + "[" + size_addr + "]");
    } 
    else {
      freeStruct(t, final_addr + "[" + size_addr + "]");
    }

    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }
}

void freeVarArray(Type *t, string final_addr) {
  stack<ArrayType*> arrayStack;
  ArrayType *at;
  
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']');

  // Si el tipo base del hiper arreglo no es primitivo ni puntero
  if (! predefinedTypes.count(t->toString()) && t->toString()[0] != '^') {
    string size_addr = tac->newTemp();
    tac->gen("assign " + size_addr + " " + to_string(t->width));

    while (! arrayStack.empty()) {
      tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
      arrayStack.pop();
    }
    
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    freeStruct(t, final_addr + "[" + size_addr + "]");

    tac->gen("goto " + label);
    tac->gen("goto " + label + "_end");
  }
  
  tac->gen("free " + final_addr);
}

void freeStruct(Type *t, string final_addr) {
  // Obtenemos el scope de definicion de la estructura.
  PrimitiveType *pt = (PrimitiveType*) t;
  StructureEntry *se = (StructureEntry*) table->lookup(pt->id);
  int scope = se->def_scope;

  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type;
    ArrayType *at;

    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();

      if (type.back() == ']') {
        at = (ArrayType*) ve->type;
        if (! at->size->is_lit) {
          freeVarArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
        }
        else {
          freeConstArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");

        }
      }
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        freeStruct(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
      }
    }
  }
}