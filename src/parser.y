%{  
  #include <iostream>
  #include <queue>
  #include <string>
  #include <cstring>
  #include <set>

  #include "table.hpp"

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

  // Leblanc-Cook's Symbols Table
  SymbolsTable table;

  // Prints error;
  void yyerror(string s);

  // Prints the queue to std.
  void printQueue(queue<string> queueToPrint);

  // add a error.
  void addError(string error);

  /* ==== TYPE VERIFICATION METHODS ==== */

  // verifies the type of an operand
  bool verify(set<string> accepted_types, string type);
  // verifies the types of 2 operands
  bool verify(set<pair<string, string>> accepted_types, string type1, string type2);

  // verifies types for a binary operator
  string verifyBinayOpType(
    set<pair<string, string>> accepted_types, 
    set<string> types1,
    set<string> types2,
    string type1, 
    string type2,
    string op,
    string return_type
  );

  // verifies type for a unary operator
  string verifyUnaryOpType(
    set<string> accepted_types, 
    string type, 
    string op,
    string return_type
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
  NodeFunctionCallArgs *fcArgs;
  NodeFunctionCallPositionalArgs *fcpArgs;
  NodeFunctionCallNamedArgs *fcnArgs;
}

%locations
%start S

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

%type <ast>           I Inst Action VarInst VarDef Assign UnionDef UnionBody 
%type <ast>           RegBody Conditional OptElsif Elsifs OptElse Def RegDef
%type <ast>           LoopWhile LoopFor RoutDef Actions RoutSign
%type <expr>          Exp LValue RValue FuncCall Array ArrExp ArrElems
%type <expr>          OptAssign Cond OptStep
%type <routArgs>      RoutArgs
%type <routArgsDef>   OptArgs MandArgs
%type <fcArgs>        ArgsExp
%type <fcpArgs>       PositionalArgs
%type <fcnArgs>       NamedArgs
%type <t>             Type OptReturn
%type <boolean>       OptRef
%type <str>           IdDef IdFor UnionId RegId RoutId
%type <nS>            S

%expect 1

%%

/* =================== GLOBAL RULES =================== */
S       : I                   { $$ = new NodeS($1); ast = $$;  }
        ;
I       : /* lambda */        { $$ = NULL; }
        | I Inst              { $$ = new NodeI($1, $2); }
        ;
Inst    : Action              { $$ = $1; }
				| Def                 { $$ = $1; }
        ;
Action  : VarInst SEMICOLON   { $$ = $1; }
				| FuncCall SEMICOLON  { $$ = $1; }
				| Conditional         { $$ = $1; }
				| LoopWhile           { $$ = $1; }
				| LoopFor             { $$ = $1; }
        ;
Def     : UnionDef            { $$ = $1; }
				| RegDef              { $$ = $1; }
				| RoutDef             { $$ = $1; }
        ;

/* ============ VARIABLES DEFINITION ============ */
VarInst     : VarDef                    { $$ = $1; }
						| Assign                    { $$ = $1; }
            | FORGET LValue             { 
                                          if ($2->type == NULL) {
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
                                          }
                                        }
            ;
VarDef      : LET Type IdDef OptAssign  { 
                                          string ltype = $2->toString();

                                          if (
                                            ltype == "$TypeError" || 
                                            $3 == "" ||
                                            ($4 != NULL && $4->type_str == "$ExpressionError") 
                                          ) {
                                            $$ = new NodeError();
                                          } 
                                          
                                          else if ($4 != NULL && ltype != $4->type_str) {
                                            addError(
                                              "Can't assign a '\e[1;3m" + $4->type_str +
                                              "\e[0m' to a '\e[1;3m" + ltype + "\e[0m'."
                                            );
                                            $$ = new NodeError();
                                          } 
                                          
                                          else {
                                            $$ = new NodeVarDef($2, $3, $4);
                                            int s = table.currentScope();
                                            Entry *e = new VarEntry($3, s, "Var", $2);
                                            table.insert(e);
                                          }
                                        }
            ;   
IdDef       : ID                        {
                                          if (! table.verifyInsert($1)) {
                                            addError((string) "Redefinition of '\e[1;3m" + $1 + "\e[0m'.");
                                            $$ = (char*) "";
                                          } else {
                                            $$ = $1; 
                                          }
                                        }
OptAssign   : /* lambda */              { $$ = NULL; }
						| ASSIGNMENT RValue         { $$ = $2; }
            ;
Assign      : LValue ASSIGNMENT RValue  { 
                                          string ltype, rtype = $3->type_str;
                                          if ($1->type == NULL) {
                                            ltype = "$TypeError";
                                          } else {
                                            ltype = $1->type->toString();
                                          }

                                          if (ltype == "$TypeError" || rtype == "$ExpressionError") {
                                            $$ = new NodeError();
                                          } 
                                          
                                          else if (ltype != rtype) {
                                            addError(
                                              "Can't assign a '\e[1;3m" + rtype +
                                              "\e[0m' to a '\e[1;3m" + ltype + "\e[0m'."
                                            );
                                            $$ = new NodeError();
                                          } 
                                          
                                          else {
                                            $$ = new NodeAssign($1, $3); 
                                          }
                                        }
            ;
RValue      : Exp                       { $$ = $1; }
            | Array                     { $$ = $1; }
            | STRING                    { $$ = new NodeSTRING($1); }
            | NEW Type                  { 
                                          if ($2->toString() != "$TypeError") {
                                            $$ = new NodeNew($2); 
                                          }
                                          
                                          else {
                                            $$ = new ExpressionNode();
                                            $$->type_str = "$ExpressionError";
                                          }
                                        }
            ;

/* ======================== TYPES ======================== */
Type	: Type OPEN_BRACKET Exp CLOSE_BRACKET { 
                                              if (
                                                $1->toString() != "$TypeError" &&
                                                $3->type_str != "$ExpressionError"
                                              ) {
                                                $$ = new ArrayType($1, $3);
                                              } else {
                                                $$ = new PrimitiveType("$TypeError");
                                              }
                                            }
			| POINTER Type 	                      { 
                                              if ($2->toString() != "$TypeError") {
                                                $$ = new PointerType($2); 
                                              } else {
                                                $$ = new PrimitiveType("$TypeError");
                                              }
                                            }
			| OPEN_PAR Type CLOSE_PAR             { $$ = $2; }
      | ID                                  {
                                              Entry *e;
                                              if ((e = table.lookup($1)) == NULL) {
                                                addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
                                                $$ = new PrimitiveType("$TypeError");
                                              } 
                                              
                                              else if (e->category != "Type" && e->category != "Structure") {
                                                addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a type.");
                                                $$ = new PrimitiveType("$TypeError");
                                              } 
                                              
                                              else {
                                                $$ = new PrimitiveType($1);
                                              }
                                            }
      | T_UNIT                              { $$ = new PrimitiveType($1); }
			| T_BOOL                              { $$ = new PrimitiveType($1); }
      | T_CHAR                              { $$ = new PrimitiveType($1); }
      | T_INT                               { $$ = new PrimitiveType($1); }
      | T_FLOAT                             { $$ = new PrimitiveType($1); }
      | T_STRING                            { $$ = new ArrayType(new PrimitiveType("Char"), new NodeINT(1)); }
      ;

/* ======================= LVALUES ======================= */
LValue	:	LValue OPEN_BRACKET Exp CLOSE_BRACKET   { 
                                                    if ($1->type == NULL) {
                                                      $$ = new NodeArrayLValue($1, $3, NULL);
                                                    }
                                                     
                                                    else if ($1->type->category != "Array") {
                                                      addError(
                                                        "'\e[1;3m" + $1->type->toString() + 
                                                        "\e[0m' type can't be indexed."
                                                      );
                                                      $$ = new NodeArrayLValue($1, $3, NULL); 
                                                    } 

                                                    else if (
                                                      $3->type_str != "$ExpressionError" &&
                                                      $3->type_str != "Int"
                                                    ) {
                                                      addError(
                                                        "Expected a '\e[1;3mInt\e[0m' but '\e[1;3m" +
                                                        $3->type_str + "\e[0m' found."
                                                      );
                                                      $$ = new NodeArrayLValue($1, $3, NULL); 
                                                    }

                                                    else if ($3->type_str == "$ExpressionError") {
                                                      $$ = new NodeArrayLValue($1, $3, NULL);
                                                    }
                                                    
                                                    else {
                                                      Type *type = ((ArrayType*) $1->type)->type;
                                                      $$ = new NodeArrayLValue($1, $3, type); 
                                                    }
                                                    
                                                  }
				|	POINTER LValue                          { 
                                                    if ($2->type == NULL) {
                                                      $$ = new NodePointerLValue($2, NULL);
                                                    } 
                                                    
                                                    else if ($2->type->category != "Pointer") {
                                                      addError(
                                                        "'\e[1;3m" + $2->type->toString() + 
                                                        "\e[0m' type can't be desreferenced."
                                                      );
                                                      $$ = new NodePointerLValue($2, NULL); 
                                                    } 
                                                    
                                                    else {
                                                      Type *type = ((PointerType*) $2->type)->type;
                                                      $$ = new NodePointerLValue($2, type); 
                                                    }
                                                  }
				|	LValue DOT ID                           { 
                                                    Type *type;
                                                    if ($1->type == NULL) {
                                                      type = NULL;
                                                    } 
                                                    
                                                    else if ($1->type->category != "Primitive") {
                                                      addError(
                                                        "'\e[1;3m" + $1->type->toString() + 
                                                        "\e[0m' type can't be accessed."
                                                      );
                                                      type = NULL;
                                                    } 
                                                    
                                                    else {
                                                      Entry *e = table.lookup($1->type->toString()); 

                                                      if (e->category != "Structure") {
                                                        addError(
                                                          "'\e[1;3m" + $1->type->toString() + 
                                                          "\e[0m' type can't be accessed."
                                                        );
                                                        type = NULL;
                                                      } 
                                                      
                                                      else {
                                                        StructureEntry *se = (StructureEntry*) e;
                                                        VarEntry *field = (VarEntry*) table.lookup($3, se->def_scope);

                                                        if (field == NULL) {
                                                          addError(
                                                            "'\e[1;3m" + $1->type->toString() + 
                                                            "\e[0m' has no member '\e[1;3m" + 
                                                            $3 + "\e[0m'."
                                                          );
                                                          type = NULL;
                                                        } 

                                                        else {
                                                          type = field->type;
                                                        }
                                                      }
                                                    }

                                                    $$ = new NodeDotLValue($1, $3, type); 
                                                  }
				| OPEN_PAR LValue CLOSE_PAR               { $$ = $2; }
				|	ID                                      { 
                                                    Entry *e;
                                                    if ((e = table.lookup($1)) == NULL) {
                                                      addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
                                                      $$ = new NodeIDLValue($1, NULL);
                                                    } 
                                                    
                                                    else if (e->category != "Var") {
                                                      addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a variable.");
                                                      $$ = new NodeIDLValue($1, NULL);
                                                    } 
                                                    
                                                    else {
                                                      VarEntry *ve = (VarEntry*) e;
                                                      $$ = new NodeIDLValue($1, ve->type); 
                                                    }
                                                  }
        ;

/* ======================= EXPRESSIONS ======================= */
Exp   : Exp EQUIV Exp               { 
                                      set<string> types = {"Bool", "Char", "Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Bool", "Bool"},
                                        {"Char", "Char"},
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "==", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp NOT_EQUIV Exp           { 
                                      set<string> types = {"Bool", "Char", "Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Bool", "Bool"},
                                        {"Char", "Char"},
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "!=", "Bool");                                      
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp OR Exp                  { 
                                      set<string> types = {"Bool"};
                                      set<pair<string, string>> tuples = { {"Bool", "Bool"} };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "||", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp AND Exp                 { 
                                      set<string> types = {"Bool"};
                                      set<pair<string, string>> tuples = { {"Bool", "Bool"} };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "&&", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | NOT Exp                     { 
                                      string type = verifyUnaryOpType({"Bool"}, $2->type_str, "!", "Bool");
                                      $$ = new NodeUnaryOperator($1, $2, type); 
                                    }
      | Exp LESS_THAN Exp           { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "<", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp LESS_EQUAL_THAN Exp     { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "<=", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp GREATER_THAN Exp        { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, ">", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp GREATER_EQUAL_THAN Exp  { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, ">=", "Bool");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp PLUS Exp                { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string return_type;
                                      if ((t1 == "Float") || (t2 == "Float")) {
                                        return_type = "Float";
                                      } else {
                                        return_type = "Int";
                                      }
                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "+", return_type);
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp MINUS Exp               { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string return_type;
                                      if ((t1 == "Float") || (t2 == "Float")) {
                                        return_type = "Float";
                                      } else {
                                        return_type = "Int";
                                      }
                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "-", return_type);
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp ASTERISK Exp            { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string return_type;
                                      if ((t1 == "Float") || (t2 == "Float")) {
                                        return_type = "Float";
                                      } else {
                                        return_type = "Int";
                                      }
                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "*", return_type);
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp DIV Exp                 { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "/", "Float");
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | Exp MODULE Exp              { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string return_type;
                                      if ((t1 == "Float") || (t2 == "Float")) {
                                        return_type = "Float";
                                      } else {
                                        return_type = "Int";
                                      }
                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "%", return_type);
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | MINUS Exp                   { 
                                      string return_type;
                                      if ($2->type_str == "Int") {
                                        return_type = "Int";
                                      } else {
                                        return_type = "Float";
                                      }

                                      string type = verifyUnaryOpType({"Int", "Float"}, $2->type_str, "-", return_type);
                                      $$ = new NodeUnaryOperator($1, $2, type); 
                                    }
      | PLUS Exp                    { 
                                      string return_type;
                                      if ($2->type_str == "Int") {
                                        return_type = "Int";
                                      } else {
                                        return_type = "Float";
                                      }

                                      string type = verifyUnaryOpType({"Int", "Float"}, $2->type_str, "+", return_type);
                                      $$ = new NodeUnaryOperator($1, $2, type); 
                                    }
      | Exp POWER Exp               { 
                                      set<string> types = {"Int", "Float"};
                                      set<pair<string, string>> tuples = {
                                        {"Int", "Int"},
                                        {"Float", "Float"},
                                        {"Int", "Float"},
                                        {"Float", "Int"}
                                      };

                                      string t1 = $1->type_str;
                                      string t2 = $3->type_str;

                                      string return_type;
                                      if ((t1 == "Float") || (t2 == "Float")) {
                                        return_type = "Float";
                                      } else {
                                        return_type = "Int";
                                      }
                                      string type = verifyBinayOpType(tuples, types, types, t1, t2, "**", return_type);
                                      $$ = new NodeBinaryOperator($1, $2, $3, type); 
                                    }
      | OPEN_PAR Exp CLOSE_PAR      { $$ = $2; }
      | LValue                      { 
                                      $$ = $1; 
                                      if ($$->type == NULL) {
                                        $$->type_str = "$ExpressionError";
                                      } else {
                                        $$->type_str = $$->type->toString(); 
                                      }
                                    }
      | FuncCall                    { $$ = $1; }
      | TRUE                        { $$ = new NodeBOOL(true); }
      | FALSE                       { $$ = new NodeBOOL(false); }
      | CHAR                        { $$ = new NodeCHAR($1); }
      | INT                         { $$ = new NodeINT($1); }
      | FLOAT                       { $$ = new NodeFLOAT($1); }
      ;

/* ====================== ARRAYS ====================== */
Array     : OPEN_BRACKET ArrExp CLOSE_BRACKET   { 
                                                  if ($2->type_str != "$ExpressionError") {
                                                    $$ = new NodeArray($2, "(" + $2->type_str + ")[]"); 
                                                  } else {
                                                    $$ = new NodeArray($2, "$ExpressionError"); 
                                                  }
                                                }
          ;
ArrExp    : ArrElems RValue                     { 
                                                  string type;
                                                  if ($1 == NULL) {
                                                    type = $2->type_str;
                                                  } 
                                                  
                                                  else if (
                                                    $1->type_str == "$ExpressionError" ||
                                                    $2->type_str == "$ExpressionError"
                                                  ) {
                                                    type = "$ExpressionError";
                                                  } 
                                                  
                                                  else if ($1->type_str != $2->type_str) {
                                                    addError(
                                                      (string) "All elements of an array must have the same type" +
                                                      ", but found '\e[1;3m" + $1->type_str + "\e[0m' and " +
                                                      "'\e[1;3m" + $2->type_str + "\e[0m'."
                                                    );
                                                    type = "$ExpressionError";

                                                  } else {
                                                    type = $2->type_str;
                                                  }
                                                  $$ = new NodeArrayElems($1, type, $2);
                                                }
          ;
ArrElems	: /* lambda */                        { $$ = NULL; }
					| ArrElems RValue COMMA               { 
                                                  string type;
                                                  if ($1 == NULL) {
                                                    type = $2->type_str;

                                                  } else if (
                                                    ($1->type_str == "$ExpressionError") || 
                                                    ($2->type_str == "$ExpressionError")
                                                  ) {
                                                    type = "$ExpressionError";

                                                  } else if ($1->type_str != $2->type_str) {
                                                    addError(
                                                      (string) "All elements of an array must have the same type" +
                                                      ", but found '\e[1;3m" + $1->type_str + "\e[0m' and " +
                                                      "'\e[1;3m" + $2->type_str + "'."
                                                    );
                                                    type = "$ExpressionError";

                                                  } else {
                                                    type = $2->type_str;
                                                  }

                                                  $$ = new NodeArrayElems($1, type, $2);
                                                }
          ;

/* ================= FUNCTION CALLS ================= */
FuncCall  : ID OPEN_PAR ArgsExp CLOSE_PAR   { 
                                              if ($3 == NULL) {
                                                $$ = new ExpressionNode();
                                                $$->type_str = "$ExpressionError";
                                              } 
                                              
                                              else {
                                                string type = "";
                                                Entry *e;
                                                if ((e = table.lookup($1)) == NULL) {
                                                  addError((string) "'\e[1;3m" + $1 + "\e[0m' wasn't declared.");
                                                  type = "$ExpressionError";
                                                } 
                                                
                                                else if (e->category != "Function") {
                                                  addError((string) "'\e[1;3m" + $1 + "\e[0m' isn't a function.");
                                                  type = "$ExpressionError";
                                                } 
                                                
                                                else {
                                                  FunctionEntry *fe = (FunctionEntry*) e;
                                                  bool correctTypes = true, allMand = true;

                                                  int numPositional = $3->positionalArgs.size(), i = 0;
  
                                                  for (tuple<string, string, bool> arg : fe->args) {
                                                    if (i < numPositional) {
                                                      if (get<1>(arg) != $3->positionalArgs[i]) {
                                                        addError(
                                                          (string) "Argument '\e[1;3m" + get<0>(arg) + "\e[0m' " +
                                                          "must be '\e[1;3m" + get<1>(arg) + "\e[0m' but '\e[1;3m" +
                                                          $3->positionalArgs[i] + "\e[0m' found."
                                                        );
                                                        correctTypes = false;
                                                      }

                                                      if ($3->keywords.count(get<0>(arg))) {
                                                        addError(
                                                          (string) "Got multiple values of '\e[1;3m" + get<0>(arg) + "\e[0m'."
                                                        );
                                                        correctTypes = false;
                                                      }
                                                    } 
                                                    
                                                    else if ($3->keywords.count(get<0>(arg))) {
                                                      if (get<1>(arg) != $3->namedArgs[get<0>(arg)]) {
                                                        addError(
                                                          (string) "Argument '\e[1;3m" + get<0>(arg) + "\e[0m' " +
                                                          "must be '\e[1;3m" + get<1>(arg) + "\e[0m' but '\e[1;3m" +
                                                          $3->namedArgs[get<0>(arg)] + "\e[0m' found."
                                                        );
                                                        correctTypes = false;
                                                      }
                                                      $3->keywords.erase(get<0>(arg));
                                                    } 
                                                    
                                                    else if (get<2>(arg) && allMand) {
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
                                                    type = "$ExpressionError";
                                                  }
                                                }

                                                if (type != "$ExpressionError") {
                                                  FunctionEntry *fe = (FunctionEntry*) e;

                                                  Type *pt = (Type*) fe->return_type;
                                                  type = pt->toString();
                                                }

                                                $$ = new NodeFunctionCall($1, $3, false, type); 
                                              }
                                            }
          ;
ArgsExp         : /* lambda */                                { $$ = new NodeFunctionCallArgs(NULL, NULL); }
                | PositionalArgs                              { 
                                                                if ($1 == NULL) {
                                                                  $$ = NULL;
                                                                } else {
                                                                  $$ = new NodeFunctionCallArgs($1, NULL);
                                                                  $$->positionalArgs = $1->currentArgs;
                                                                  $1->currentArgs.clear();
                                                                }
                                                              }
                | NamedArgs                                   { 
                                                                if ($1 == NULL) {
                                                                  $$ = NULL;
                                                                } else {
                                                                  $$ = new NodeFunctionCallArgs(NULL, $1);
                                                                  $$->namedArgs = $1->currentArgs;
                                                                  $$->keywords = $1->keywords;

                                                                  $1->currentArgs.clear();
                                                                  $1->keywords.clear();
                                                                }
                                                              }
                | PositionalArgs COMMA NamedArgs              { 
                                                                if ($1 == NULL || $3 == NULL) {
                                                                  $$ = NULL;
                                                                } else {
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
PositionalArgs  : RValue                                      { 
                                                                if ($1->type_str == "$ExpressionError") {
                                                                  $$ = NULL;
                                                                } else {
                                                                  $$ = new NodeFunctionCallPositionalArgs(NULL, $1);
                                                                  $$->currentArgs.push_back($1->type_str);  
                                                                }
                                                              }
                | PositionalArgs COMMA RValue                 { 
                                                                if ($3->type_str == "$ExpressionError" || $1 == NULL) {
                                                                  $$ = NULL;
                                                                } else {
                                                                  $$ = new NodeFunctionCallPositionalArgs($1, $3);

                                                                  $$->currentArgs = $1->currentArgs;
                                                                  $1->currentArgs.clear();
                                                                  $$->currentArgs.push_back($3->type_str);
                                                                }
                                                              }
                ;
NamedArgs       : ID ASSIGNMENT RValue                        { 
                                                                if ($3->type_str == "$ExpressionError") {
                                                                  $$ = NULL;
                                                                } else {
                                                                  $$ = new NodeFunctionCallNamedArgs(NULL, $1, $3);
                                                                  $$->currentArgs[$1] = $3->type_str; 
                                                                  $$->keywords.insert($1);
                                                                }
                                                              }
                | NamedArgs COMMA ID ASSIGNMENT RValue        { 
                                                                $$ = new NodeFunctionCallNamedArgs($1, $3, $5); 
                                                                if ($1 != NULL && $1->currentArgs.count($3)) {
                                                                  addError(
                                                                    (string) "Got multiple values of '\e[1;3m" + $3 + "\e[0m'."
                                                                  );
                                                                  $$ = NULL;
                                                                } 
                                                                
                                                                else if (
                                                                  ($1 == NULL) || 
                                                                  ($5->type_str == "$ExpressionError")
                                                                )  {
                                                                  $$ = NULL;
                                                                } 
                                                                
                                                                else {
                                                                  $$->currentArgs = $1->currentArgs;
                                                                  $$->currentArgs[$3] = $5->type_str;
                                                                  $1->currentArgs.clear();

                                                                  $$->keywords = $1->keywords;
                                                                  $$->keywords.insert($3);
                                                                  $1->keywords.clear();
                                                                }
                                                              }
                ;

/* ================= UNION DEFINITION ================= */
UnionDef  : UnionId OPEN_C_BRACE UnionBody CLOSE_C_BRACE  { 
                                                            if ($1 == "" || $3 == NULL) {
                                                              $$ = new NodeError();
                                                            } else {
                                                              $$ = new NodeUnionDef($1, $3);

                                                              int def_s = table.currentScope();
                                                              table.exitScope(); 
                                                              int s = table.currentScope();

                                                              Entry *e = new StructureEntry($1, s, "Structure", def_s);
                                                              table.insert(e);
                                                            }
                                                          }
          ;
UnionId   : UNION IdDef                                   { table.newScope(); $$ = $2; }
          ;  
UnionBody	: Type IdDef SEMICOLON                          { 
                                                            if ($2 == "" || $1->toString() == "$TypeError") {
                                                              $$ = NULL;
                                                            } else {
                                                              $$ = new NodeUnionFields(NULL, $1, $2); 
                                                              int s = table.currentScope();
                                                              Entry *e = new VarEntry($2, s, "Field", $1);
                                                              table.insert(e);
                                                            }
                                                          }
					| UnionBody Type IdDef SEMICOLON                { 
                                                            if ($1 == NULL || $3 == "" || $2->toString() == "$TypeError") {
                                                              $$ = NULL;
                                                            } else {
                                                              $$ = new NodeUnionFields($1, $2, $3); 
                                                              int s = table.currentScope();
                                                              Entry *e = new VarEntry($3, s, "Field", $2);
                                                              table.insert(e);
                                                            }
                                                          }
          ;

/* ================ REGISTER DEFINITION ================ */
RegDef    : RegId OPEN_C_BRACE RegBody CLOSE_C_BRACE  { 
                                                        if ($1 == "" || $3 == NULL) {
                                                          $$ = new NodeError();
                                                        } else {
                                                          $$ = new NodeRegDef($1, $3);

                                                          int def_s = table.currentScope();
                                                          table.exitScope();
                                                          int s = table.currentScope();

                                                          Entry *e = new StructureEntry($1, s, "Structure", def_s);
                                                          table.insert(e);
                                                        }
                                                      }
          ;   
RegId     : REGISTER IdDef                            { table.newScope(); $$ = $2; }
          ; 
RegBody	  : Type IdDef OptAssign SEMICOLON            { 
                                                        if (
                                                          $2 == "" || $1->toString() == "$TypeError" ||
                                                          ($3 != NULL && $3->type_str == "$ExpressionError")
                                                        ) {
                                                          $$ = NULL;
                                                        } 

                                                        else if ($3 != NULL && $1->toString() != $3->type_str) {
                                                          addError(
                                                            "Can't assign a '\e[1;3m" + $3->type_str +
                                                            "\e[0m' to a '\e[1;3m" + $1->toString() + "\e[0m'."
                                                          );
                                                          $$ = NULL;
                                                        }
                                                        
                                                        else {
                                                          $$ = new NodeRegFields(NULL, $1, $2, $3);
                                                          int s = table.currentScope();
                                                          Entry *e = new VarEntry($2, s, "Field", $1);
                                                          table.insert(e);
                                                        }
                                                      }
				  |	RegBody Type IdDef OptAssign SEMICOLON    { 
                                                        if ($3 == "" || $2->toString() == "$TypeError") {
                                                          $$ = NULL;
                                                        } 

                                                        else if ($4 != NULL && $2->toString() != $4->type_str) {
                                                          addError(
                                                            "Can't assign a '\e[1;3m" + $4->type_str +
                                                            "\e[0m' to a '\e[1;3m" + $2->toString() + "\e[0m'."
                                                          );
                                                          $$ = NULL;
                                                        }

                                                        else if ($1 == NULL) {
                                                          $$ = NULL;
                                                        }
                                                        
                                                        else {
                                                          $$ = new NodeRegFields($1, $2, $3, $4);
                                                          int s = table.currentScope();
                                                          Entry *e = new VarEntry($3, s, "Field", $2);
                                                          table.insert(e);
                                                        }
                                                      }
          ;

/* ===================== CONDITIONALS ===================== */
Conditional : If Cond THEN I OptElsif OptElse DONE  { 
                                                      $$ = new NodeConditional($2, $4, $5, $6);
                                                      table.exitScope(); 
                                                    }
            ;
Cond        : RValue                                {
                                                      if ($1->type_str != "$ExpressionError" && $1->type_str != "Bool") {
                                                        addError(
                                                          "Condition must be a '\e[1;3mBool\e[0m' but '\e[1;3m" +
                                                          $1->type_str + "\e[0m' found."
                                                        );
                                                      }
                                                      $$ = $1;
                                                    }
            ;
If          : IF                                    { table.newScope(); }
            ;
OptElsif    : /* lambda */                          { $$ = NULL; }
						| Elsifs                                { $$ = $1; }
            ;
Elsifs      : Elsif Cond THEN I                     { $$ = new NodeElsif(NULL, $2, $4); }
						| Elsifs Elsif Cond THEN I              { $$ = new NodeElsif($1, $3, $5); }
            ;
Elsif       : ELSIF                                 { 
                                                      table.exitScope();
                                                      table.newScope(); 
                                                    }
            ;
OptElse     : /* lambda */                          { $$ = NULL; }
						| Else I                                { $$ = new NodeElse($2); }
            ;
Else        : ELSE                                  { 
                                                      table.exitScope();
                                                      table.newScope(); 
                                                    }
            ;

/* ======================== LOOPS ======================== */
LoopWhile : While Cond DO I DONE                       { 
                                                        $$ = new NodeWhile($2, $4); 
                                                        table.exitScope();
                                                      }
          ; 
While     : WHILE                                     { table.newScope(); }
          ;
LoopFor   : For OPEN_PAR IdFor SEMICOLON RValue SEMICOLON   
            RValue OptStep CLOSE_PAR DO I DONE        { 
                                                        if (
                                                          $5->type_str != "$ExpressionError" &&
                                                          $5->type_str != "Float" && 
                                                          $5->type_str != "Int"
                                                        ) {
                                                          addError(
                                                            "Initial value in a for loop must be "
                                                            "'\e[1;3mInt\e[0m' or '\e[1;3mFloat\e[0m' "
                                                            "but '\e[1;3m" + $5->type_str + "\e[0m' found."
                                                          );
                                                        }

                                                        if (
                                                          $7->type_str != "$ExpressionError" &&
                                                          $7->type_str != "Float" && 
                                                          $7->type_str != "Int"
                                                        ) {
                                                          addError(
                                                            "End value in a for loop must be "
                                                            "'\e[1;3mInt\e[0m' or '\e[1;3mFloat\e[0m' "
                                                            "but '\e[1;3m" + $7->type_str + "\e[0m' found."
                                                          );
                                                        }

                                                        if (
                                                          $8 != NULL &&
                                                          $8->type_str != "$ExpressionError" &&
                                                          $8->type_str != "Float" && 
                                                          $8->type_str != "Int"
                                                        ) {
                                                          addError(
                                                            "Step value in a for loop must be "
                                                            "'\e[1;3mInt\e[0m' or '\e[1;3mFloat\e[0m' "
                                                            "but '\e[1;3m" + $8->type_str + "\e[0m' found."
                                                          );
                                                        }

                                                        $$ = new NodeFor($3, $5, $7, $8, $11);
                                                        table.exitScope();
                                                      }
          ;
IdFor     : IdDef                                     { 
                                                        int s = table.currentScope();
                                                        Type *t = new PrimitiveType("Float");
                                                        Entry *e = new VarEntry($1, s, "Var", t);
                                                        table.insert(e); 
                                                        $$ = $1; 
                                                      }
          ;
For       : FOR                                       { table.newScope(); }
          ;
OptStep   : /* lambda */                              { $$ = NULL; }
				  | SEMICOLON RValue                          { $$ = $2; }
          ;

/* =============== SUBROUTINES DEFINITION =============== */
RoutDef   : RoutSign OPEN_C_BRACE Actions CLOSE_C_BRACE   { 
                                                            if ($1->toString() == "Error") {
                                                              NodeError *err = (NodeError*) $1;
                                                              table.exitScope();
                                                              table.exitScope();
                                                              table.erase(err->errInfo, table.currentScope());

                                                              $$ = new NodeError();

                                                            } else {
                                                              table.exitScope();
                                                              table.exitScope();

                                                              $$ = new NodeRoutineDef($1, $3); 
                                                            }

                                                            table.ret_type = "";
                                                          }
          ;  
RoutSign  : RoutId OPEN_PAR RoutArgs CLOSE_PAR OptReturn  {
                                                            if ($3 == NULL || $5->toString() == "$TypeError") {
                                                              NodeError *err = new NodeError();
                                                              err->errInfo = $1;
                                                              $$ = err;

                                                            } else {
                                                              FunctionEntry *e;
                                                              e = (FunctionEntry*) table.lookup($1);
                                                              e->return_type = $5;
                                                              e->def_scope = table.currentScope();                                                              
                                                              e->args = $3->params;
                                                              $3->params.clear();
                                                              
                                                              table.newScope();
                                                              $$ = new NodeRoutineSign($1, $3, $5);
                                                            }

                                                            if ($5->toString() != "$TypeError") {
                                                              table.ret_type = $5->toString();
                                                            }
                                                          }
          ;
RoutId    : DEF IdDef                                     {
                                                            int s = table.currentScope();
                                                            Entry *e = new FunctionEntry($2, s, "Function");
                                                            table.insert(e);
                                                            table.newScope();
                                                            $$ = $2;
                                                          }
          ;    
RoutArgs  : /* lambda */                                  { $$ = new NodeRoutArgs(NULL, NULL); }
          | MandArgs                                      { 
                                                            if ($1 == NULL) {
                                                              $$ = NULL;
                                                            } else {
                                                              $$ = new NodeRoutArgs($1, NULL); 
                                                              $$->params = $1->currentParams;
                                                              $1->currentParams.clear();
                                                            }
                                                          }
          | OptArgs                                       {
                                                            if ($1 == NULL) {
                                                              $$ = NULL;
                                                            } else {
                                                              $$ = new NodeRoutArgs(NULL, $1); 
                                                              $$->params = $1->currentParams;
                                                              $1->currentParams.clear();
                                                            }
                                                          }
          | MandArgs COMMA OptArgs                        { 
                                                            if (($1 == NULL) || ($3 == NULL)) {
                                                              $$ = NULL;
                                                            } else {
                                                              for(auto & elem : $3->currentParams)
                                                              {
                                                                $1->currentParams.push_back(elem);
                                                              }

                                                              $$ = new NodeRoutArgs($1, $3);
                                                              $$->params = $1->currentParams;
                                                              $1->currentParams.clear();
                                                              $3->currentParams.clear();
                                                            }
                                                          }
          ;   
MandArgs  : Type OptRef IdDef                             { 
                                                            if ($3 == "" || $1->toString() == "$TypeError") {
                                                              $$ = NULL;
                                                            } else {
                                                              $$ = new NodeRoutArgDef(
                                                                NULL, $1, $2, $3, NULL
                                                              );
                                                              $$->currentParams.push_back({$3, $1->toString(), true});

                                                              int s = table.currentScope();
                                                              Entry *e = new VarEntry($3, s, "Var", $1);
                                                              table.insert(e);
                                                            }
                                                          }
          | MandArgs COMMA Type OptRef IdDef              { 
                                                            if (
                                                              $1 == NULL || $5 == "" ||
                                                              $3->toString() == "$TypeError"
                                                            ) {
                                                              $$ = NULL;
                                                            } else {
                                                              $$ = new NodeRoutArgDef(
                                                                $1, $3, $4, $5, NULL
                                                              );
                                                              $$->currentParams = $1->currentParams;
                                                              $1->currentParams.clear();
                                                              $$->currentParams.push_back({$5, $3->toString(), true});

                                                              int s = table.currentScope();
                                                              Entry *e = new VarEntry($5, s, "Var", $3);
                                                              table.insert(e);
                                                            }
                                                          }
          ;   
OptArgs   : Type OptRef IdDef ASSIGNMENT RValue           { 
                                                            if (
                                                              $1->toString() == "$TypeError" ||
                                                              $5->type_str == "$ExpressionError"
                                                            ) {
                                                              $$ = NULL;
                                                            } 
                                                            
                                                            else if ($1->toString() != $5->type_str) {
                                                              addError(
                                                                "Can't assign a '\e[1;3m" + $5->type_str +
                                                                "\e[0m' to a '\e[1;3m" + $1->toString() + "\e[0m'."
                                                              );
                                                              $$ = NULL;
                                                            } 

                                                            else if ($3 == "") {
                                                              $$ = NULL;
                                                            }
                                                            
                                                            else {
                                                              $$ = new NodeRoutArgDef(
                                                                NULL, $1, $2, $3, $5
                                                              );

                                                              $$->currentParams.push_back({$3, $1->toString(), false});

                                                              int s = table.currentScope();
                                                              Entry *e = new VarEntry($3, s, "Var", $1);
                                                              table.insert(e);
                                                            }
                                                          }
          | OptArgs COMMA Type OptRef IdDef 
            ASSIGNMENT RValue                             { 
                                                            if (
                                                              $3->toString() == "$TypeError" ||
                                                              $7->type_str == "$ExpressionError"
                                                            ) {
                                                              $$ = NULL;
                                                            } 
                                                            
                                                            else if ($3->toString() != $7->type_str) {
                                                              addError(
                                                                "Can't assign a '\e[1;3m" + $7->type_str +
                                                                "\e[0m' to a '\e[1;3m" + $3->toString() + "\e[0m'."
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
                                                              $$->currentParams.push_back({$5, $3->toString(), false});

          
                                                              int s = table.currentScope();
                                                              Entry *e = new VarEntry($5, s, "Var", $3);
                                                              table.insert(e);
                                                            }
                                                          }
          ;
OptRef    : /* lambda */                                  { $$ = false; }
					| AT                                            { $$ = true; }
          ; 
OptReturn : /* lambda */                                  { $$ = new PrimitiveType("Unit"); }
				  | RIGHT_ARROW Type                              { $$ = $2; }
          ; 
Actions   : /* lambda */                                  { $$ = NULL; }
				  | Actions Action                                { $$ = new NodeActions($1, $2); }
          | Actions RETURN RValue SEMICOLON               {
                                                            if (
                                                              table.ret_type != "" &&
                                                              $3->type_str != table.ret_type
                                                            ) {
                                                              addError(
                                                                "Expected return type '\e[1;3m" + 
                                                                table.ret_type + "\e[0m' but " +
                                                                "'\e[1;3m" + $3->type_str + "\e[0m' found."
                                                              );
                                                              $$ = new NodeError();
                                                            } else {
                                                              $$ = new NodeReturn($3);
                                                            }
                                                          }
          | Actions RETURN SEMICOLON                      {
                                                            if (
                                                              table.ret_type != "" &&
                                                              "Unit" != table.ret_type
                                                            ) {
                                                              addError(
                                                                "Expected return type '\e[1;3m" + 
                                                                table.ret_type + "\e[0m' but " +
                                                                "'\e[1;3mUnit\e[0m' found ."
                                                              );
                                                              $$ = new NodeError();
                                                            } else {
                                                              $$ = new NodeReturn();
                                                            }
                                                          }
          ;

%%

int main(int argc, char **argv)
{
  // Adding scope 0 elements.
  vector<string> primitives = {"Unit", "Bool", "Char", "Int", "Float", "String"};
  for (string t : primitives) {
    table.insert(new PrimitiveEntry(t));
  }

  // Booleans for options
  bool bLexOpt = false;
  bool bParseOpt = false;
  bool bSymbolsOpt = false;
  bool bTreeOpt = false;
  bool bRepOpt = false;

  // Verify all arguments has been passed
  if (argc < 3 || argc > 4) {
    cout << "\e[1mSYNOPSIS\n"
      "\t\e[1mmaclang\e[0m lex \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m parse -t \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m parse -c \e[4mFILE\e[0m\n"
      "\t\e[1mmaclang\e[0m symbols \e[4mFILE\e[0m\n";
    return 1;
  } 
  
  // Check if provided method is valid
  if (strcmp(argv[1], "lex") && strcmp(argv[1], "parse") && strcmp(argv[1], "symbols")) {
    cout << "Invalid action: " << argv[1] << endl;
    return 1;

  } else if (strcmp(argv[1], "parse") == 0) {
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

  } else {
    // Sumbols table 

    bSymbolsOpt = true;
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
    } else {
      table.printTable();
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
bool verify(set<string> accepted_types, string type) {
  return accepted_types.count(type);
}

/*
  Verifies that the types correspond with an accepted pair of types.
*/
bool verify(set<pair<string, string>> accepted_types, string type1, string type2) {
  return accepted_types.count({type1, type2});
}

/*
  Verfiy that an operand have the correct type for a unary operator.
*/
string verifyUnaryOpType(
  set<string> accepted_types, 
  string type, 
  string op,
  string return_type
) {
  if (type == "$ExpressionError") {
    return "$ExpressionError";

  } else if (verify(accepted_types, type)) {
    return return_type;

  } else {
    addError(
      (string) "Operator '\e[1;3m" + op + "\e[0m' can't be applied with operand type " +
      "'\e[1;3m" + type + "\e[0m'."
    );
    return "$ExpressionError";
  }

}

/*
  Verifies that a pair of operators have the correct types for a binary operator.
*/
string verifyBinayOpType(
  set<pair<string, string>> accepted_types, 
  set<string> types1,
  set<string> types2,
  string type1, 
  string type2,
  string op,
  string return_type
) {
  // Verifies if one of the operands has error type.
  if (type1 == "$ExpressionError" || type2 == "$ExpressionError") {
    return "$ExpressionError";

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
        type1 + "\e[0m' and '\e[1;3m" + type2 + "\e[0m'."
      );
      return "$ExpressionError";
    }
  }
}
