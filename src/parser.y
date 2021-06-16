%{
  #include <iostream>
  #include <queue>
  #include <string>
  #include <cstring>
  #include "ast.hpp" 
  #include "table.hpp"

  using namespace std;

  extern int yylex(void);
  extern int yylineno;
  extern int yycolumn;
  extern char *yytext;
  extern char *filename;
  // queues for tokens and errors
  extern queue<string> errors;
  node_S *ast;

  // queues for tokens and errors
  queue<string> tokens;
  extern queue<string> errors;

  symbols_table table;

  // Prints error;
  void yyerror(string s);

  // Prints the queue to std.
  void printQueue(queue<string> queueToPrint);

  // main method for parsing.
  int parser_main(int argc, char **argv);

  // main method for lexing.
  int lexer_main(int argc, char **argv);

  // add redefinitions errors.
  void redefinition_error(string id);

  // add undefined error.
  void undefined_error(string id);

  // token names for readability on lexer
  string token_names [] = {
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

  node* global;
%}

%define parse.lac full

%union 
{	
  int   integer;
  float flot;
  bool  boolean;
  char  *str;
  char  ch;
  node  *ast;
  node_S *nS;
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

%type <ast>       I Inst Action VarInst VarDef OptAssign Type OptReturn
%type <ast>       LValue Exp Array ArrExp ArrElems FuncCall ArgsExp
%type <ast>       Args RValue Assign UnionDef UnionBody Def RegDef
%type <ast>       RegBody Conditional OptElsif Elsifs OptElse 
%type <ast>       LoopWhile LoopFor OptStep RoutDef OptArgs OblArgs 
%type <ast>       RoutArgs Actions 
%type <boolean>   OptRef
%type <str>       IdDef IdFor UnionId RegId RoutId
%type <nS>        S

%expect 1

%%

/* =================== GLOBAL RULES =================== */
S       : I                   { $$ = new node_S($1); ast = $$;  }
        | /* lambda */        { $$ = NULL; }
        ;
I       : Inst                { $$ = new node_I(NULL, $1); }
        | I Inst              { $$ = new node_I($1, $2); }
        ;
Inst    : Action              { $$ = $1; }
				| Def                 { $$ = $1; }
        ;
Action  : VarInst SEMICOLON   { $$ = $1; }
				| FuncCall SEMICOLON  { $$ = $1; ((node_FunctionCall*) $$)->set_end_inst(); }
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
            | FORGET LValue             { $$ = new node_Forget($2); }
            ;
VarDef      : LET Type IdDef OptAssign  { 
                                          $$ = new node_VarDef($2, $3, $4);
                                          int s = table.current_scope();
                                          entry *e = new entry($3, s, "");
                                          table.insert(e);
                                        }
            ;   
IdDef       : ID                        {
                                          if (! table.verify_insert($1)) {
                                            redefinition_error($1);
                                          }
                                          $$ = $1; 
                                        }
OptAssign   : /* lambda */              { $$ = NULL; }
						| ASSIGNMENT RValue         { $$ = $2; }
            ;
Assign      : LValue ASSIGNMENT RValue  { $$ = new node_Assign($1, $3); }
            ;
RValue      : Exp                       { $$ = $1; }
            | Array                     { $$ = $1; }
            | STRING                    { $$ = new node_STRING($1); }
            | NEW Type                  { $$ = new node_New($2); }
            ;

/* ======================== TYPES ======================== */
Type	: Type OPEN_BRACKET Exp CLOSE_BRACKET { $$ = new node_TypeArrayDef($1, $3); }
			| POINTER Type 	                      { $$ = new node_TypePointerDef($2); }
			| OPEN_PAR Type CLOSE_PAR             { $$ = $2; }
      | T_UNIT                              { $$ = new node_TypePrimitiveDef($1); }
			| T_BOOL                              { $$ = new node_TypePrimitiveDef($1); }
      | T_CHAR                              { $$ = new node_TypePrimitiveDef($1); }
      | T_INT                               { $$ = new node_TypePrimitiveDef($1); }
      | T_FLOAT                             { $$ = new node_TypePrimitiveDef($1); }
      | T_STRING                            { $$ = new node_TypePrimitiveDef($1); }
      ;

/* ======================= LVALUES ======================= */
LValue	:	LValue OPEN_BRACKET Exp CLOSE_BRACKET   { $$ = new node_ArrayLValue($1, $3); }
				|	POINTER LValue                          { $$ = new node_PointerLValue($2); }
				|	LValue DOT ID                           { $$ = new node_DotLValue($1, $3); }
				| OPEN_PAR LValue CLOSE_PAR               { $$ = $2; }
				|	ID                                      { 
                                                    if (table.lookup($1) == NULL) {
                                                      undefined_error($1);
                                                    }
                                                    $$ = new node_IDLValue($1); 
                                                  }
        ;

/* ======================= EXPRESSIONS ======================= */
Exp   : Exp EQUIV Exp               { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp NOT_EQUIV Exp           { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp OR Exp                  { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp AND Exp                 { $$ = new node_BinaryOperator($1, $2, $3); }
      | NOT Exp                     { $$ = new node_UnaryOperator($1, $2); }
      | Exp LESS_THAN Exp           { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp LESS_EQUAL_THAN Exp     { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp GREATER_THAN Exp        { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp GREATER_EQUAL_THAN Exp  { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp PLUS Exp                { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp MINUS Exp               { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp ASTERISK Exp            { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp DIV Exp                 { $$ = new node_BinaryOperator($1, $2, $3); }
      | Exp MODULE Exp              { $$ = new node_BinaryOperator($1, $2, $3); }
      | MINUS Exp                   { $$ = new node_UnaryOperator($1, $2); }
      | PLUS Exp                    { $$ = new node_UnaryOperator($1, $2); }
      | Exp POWER Exp               { $$ = new node_BinaryOperator($1, $2, $3); }
      | OPEN_PAR Exp CLOSE_PAR      { $$ = $2; }
      | LValue                      { $$ = $1; }
      | FuncCall                    { $$ = $1; }
      | TRUE                        { $$ = new node_BOOL(true); }
      | FALSE                       { $$ = new node_BOOL(false); }
      | CHAR                        { $$ = new node_CHAR($1); }
      | INT                         { $$ = new node_INT($1); }
      | FLOAT                       { $$ = new node_FLOAT($1); }
      ;

/* ====================== ARRAYS ====================== */
Array     : OPEN_BRACKET ArrExp CLOSE_BRACKET   { $$ = new node_Array($2); }
          ;
ArrExp    : /* lambda */                        { $$ = NULL; }
					| ArrElems RValue                     { $$ = new node_ArrayElems($1, $2); }
          ;
ArrElems	: /* lambda */                        { $$ = NULL; }
					| ArrElems RValue COMMA               { $$ = new node_ArrayElems($1, $2); }
          ;

/* ================= FUNCTION CALLS ================= */
FuncCall  : ID OPEN_PAR ArgsExp CLOSE_PAR   { 
                                              if (table.lookup($1) == NULL) {
                                                undefined_error($1);
                                              }
                                              $$ = new node_FunctionCall($1, $3, false); 
                                            }
          ;
ArgsExp   : /* lambda */                    { $$ = NULL; }
					| Args RValue                     { $$ = new node_FunctionCallArgs($1, $2); }
          ;
Args      : /* lambda */                    { $$ = NULL; }
					| Args RValue COMMA               { $$ = new node_FunctionCallArgs($1, $2); }
          ;

/* ================= UNION DEFINITION ================= */
UnionDef  : UnionId OPEN_C_BRACE UnionBody CLOSE_C_BRACE  { 
                                                            $$ = new node_UnionDef($1, $3);
                                                            table.exit_scope(); 
                                                            int s = table.current_scope();
                                                            entry *e = new entry($1, s, "");
                                                            table.insert(e);
                                                          }
          ;
UnionId   : UNION IdDef                                   { table.new_scope(); $$ = $2; }
          ;  
UnionBody	: Type IdDef SEMICOLON                          { 
                                                            $$ = new node_UnionFields(NULL, $1, $2); 
                                                            int s = table.current_scope();
                                                            entry *e = new entry($2, s, "");
                                                            table.insert(e);
                                                          }
					| UnionBody Type IdDef SEMICOLON                { 
                                                            $$ = new node_UnionFields($1, $2, $3); 
                                                            int s = table.current_scope();
                                                            entry *e = new entry($3, s, "");
                                                            table.insert(e);
                                                          }
          ;

/* ================ REGISTER DEFINITION ================ */
RegDef    : RegId OPEN_C_BRACE RegBody CLOSE_C_BRACE  { 
                                                        $$ = new node_RegDef($1, $3);
                                                        table.exit_scope();
                                                        int s = table.current_scope();
                                                        entry *e = new entry($1, s, "");
                                                        table.insert(e);
                                                      }
          ;   
RegId     : REGISTER IdDef                            { table.new_scope(); $$ = $2; }
          ; 
RegBody	  : Type IdDef OptAssign SEMICOLON            { 
                                                        $$ = new node_RegFields(NULL, $1, $2, $3);
                                                        int s = table.current_scope();
                                                        entry *e = new entry($2, s, "");
                                                        table.insert(e);
                                                      }
				  |	RegBody Type IdDef OptAssign SEMICOLON    { 
                                                        $$ = new node_RegFields($1, $2, $3, $4);
                                                        int s = table.current_scope();
                                                        entry *e = new entry($3, s, "");
                                                        table.insert(e);
                                                      }
          ;



/* ===================== CONDITIONALS ===================== */
Conditional : If Exp THEN I OptElsif OptElse DONE   { 
                                                      $$ = new node_Conditional($2, $4, $5, $6);
                                                      table.exit_scope(); 
                                                    }
            ;
If          : IF                                    { table.new_scope(); }
            ;
OptElsif    : /* lambda */                          { $$ = NULL; }
						| Elsifs                                { $$ = $1; }
            ;
Elsifs      : Elsif Exp THEN I                      { $$ = new node_Elsif(NULL, $2, $4); }
						| Elsifs Elsif Exp THEN I               { $$ = new node_Elsif($1, $3, $5); }
            ;
Elsif       : ELSIF                                 { 
                                                      table.exit_scope();
                                                      table.new_scope(); 
                                                    }
            ;
OptElse     : /* lambda */                          { $$ = NULL; }
						| Else I                                { $$ = new node_Else($2); }
            ;
Else        : ELSE                                  { 
                                                      table.exit_scope();
                                                      table.new_scope(); 
                                                    }
            ;

/* ======================== LOOPS ======================== */
LoopWhile : While Exp DO I DONE                       { 
                                                        $$ = new node_While($2, $4); 
                                                        table.exit_scope();
                                                      }
          ; 
While     : WHILE                                     { table.new_scope(); }
          ;
LoopFor   : For OPEN_PAR IdFor SEMICOLON Exp SEMICOLON   
            Exp OptStep CLOSE_PAR DO I DONE           { 
                                                        $$ = new node_For($3, $5, $7, $8, $11);
                                                        table.exit_scope();
                                                      }
          ;
IdFor     : IdDef                                     { 
                                                        int s = table.current_scope();
                                                        entry *e = new entry($1, s, "");
                                                        table.insert(e); 
                                                        $$ = $1; 
                                                      }
          ;
For       : FOR                                       { table.new_scope(); }
          ;
OptStep   : /* lambda */                              { $$ = NULL; }
				  | SEMICOLON Exp                             { $$ = $2; }
          ;

/* =============== SUBROUTINES DEFINITION =============== */
RoutDef   : RoutId OPEN_PAR RoutArgs CLOSE_PAR OptReturn 
            OPEN_C_BRACE Actions CLOSE_C_BRACE            { 
                                                            $$ = new node_RoutineDef(
                                                              $1, $3, $5, $7
                                                            ); 
                                                            table.exit_scope();
                                                          }
          ;  
RoutId    : DEF IdDef                                     {
                                                            int s = table.current_scope();
                                                            entry *e = new entry($2, s, "");
                                                            table.insert(e);
                                                            table.new_scope();
                                                          }
          ;    
RoutArgs  : /* lambda */                                  { $$ = NULL; }
          | OblArgs                                       { $$ = new node_RoutArgs($1, NULL); }
          | OptArgs                                       { $$ = new node_RoutArgs(NULL, $1); }
          | OblArgs COMMA OptArgs                         { $$ = new node_RoutArgs($1, $3); }
          ;   
OblArgs   : Type OptRef IdDef                             { 
                                                            $$ = new node_RoutArgDef(
                                                              NULL, $1, $2, $3, NULL
                                                            );
                                                            int s = table.current_scope();
                                                            entry *e = new entry($3, s, "");
                                                            table.insert(e);
                                                          }
          | OblArgs COMMA Type OptRef IdDef               { 
                                                            $$ = new node_RoutArgDef(
                                                              $1, $3, $4, $5, NULL
                                                            );
                                                            int s = table.current_scope();
                                                            entry *e = new entry($5, s, "");
                                                            table.insert(e);
                                                          }
          ;   
OptArgs   : Type OptRef IdDef ASSIGNMENT RValue           { 
                                                            $$ = new node_RoutArgDef(
                                                              NULL, $1, $2, $3, $5
                                                            );
                                                            int s = table.current_scope();
                                                            entry *e = new entry($3, s, "");
                                                            table.insert(e);
                                                          }
          | OptArgs COMMA Type OptRef IdDef 
            ASSIGNMENT RValue                             { 
                                                            $$ = new node_RoutArgDef(
                                                              $1, $3, $4, $5, $7
                                                            );
                                                            int s = table.current_scope();
                                                            entry *e = new entry($5, s, "");
                                                            table.insert(e);
                                                          }
          ;
OptRef    : /* lambda */                                  { $$ = false; }
					| AT                                            { $$ = true; }
          ; 
OptReturn : /* lambda */                                  { $$ = NULL; }
				  | RIGHT_ARROW Type                              { $$ = $2; }
          ; 
Actions   : /* lambda */                                  { $$ = NULL; }
				  | Actions Action                                { $$ = new node_Actions($1, $2); }
          ;

%%

int main(int argc, char **argv)
{
  bool lex_opt = false;
  bool parse_opt = false;
  bool symbols_opt = false;
  bool tree_opt = false;
  bool rep_opt = false;

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

    parse_opt = true;
    // Print tree
    if (strcmp(argv[2], "-t") == 0) { tree_opt = true; }
    // Print code representation
    else if (strcmp(argv[2], "-c") == 0) { rep_opt = true; }
    else {
      cout << "Invalid flag: " << argv[2] << endl;
      return 1;
    }
    filename = argv[3];

  } else if (strcmp(argv[1], "lex") == 0) {
    // Lexing.

    lex_opt = true;
    filename = argv[2];

  } else {
    // Sumbols table 

    symbols_opt = true;
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

  // apply lexing
  int tok;
  while(tok = yylex())
  {
    // if token can have multiple values, also print the value of the token
    switch(tok) {
      case INT:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;34m " + 
                    token_names[tok-1] + "\e[0m = \e[1;36m" + 
                    to_string(yylval.integer) + "\n");
        break;
      case FLOAT:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;32m " + 
                    token_names[tok-1] + "\e[0m = \e[1;36m" + 
                    to_string(yylval.flot) + "\n");
        break;
      case CHAR:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;35m " + 
                    token_names[tok-1] + "\e[0m = \e[1;36m" + yylval.ch + "\n");
        break;
      case STRING:
      case ID:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;31m " + 
                    token_names[tok-1] + "\e[0m = \e[1;36m" + yylval.str + "\n");
        break;
      default:
        tokens.push("\e[0;33m" + to_string(tok) + ":\t\e[0m\e[1;37m " + 
                    token_names[tok-1] + "\e[0m\n");
    }
  }

  fclose(yyin);

  // if were asked just for lexing print the results of the lexer_main
  // and return
  if (lex_opt) {
    if(errors.empty())
      printQueue(tokens);
    else
      printQueue(errors);

    return 0;
  }

  // parsing
  yyin = fopen(filename, "r");

  // if there are no errors, apply parsing
  if (errors.empty()) {
    
    // reset lines and columns
    yylineno = 1; 
    yycolumn = 1;

    // start parsing
    yyparse();

    if (errors.empty()) {
      if (parse_opt) {
        if (tree_opt) {
          ast->print_tree(NULL);
        } else {
          ast->print();
        }
      } else {
        table.print_table();
      }

    } else {
      printQueue(errors);
    }

  } else {
    printQueue(errors);
  }

  return 0;
}

/*
  Prints error.
*/
void yyerror(string s)
{
  string file = strdup(filename);

  cout << "\e[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \e[31mSyntax error:\e[0m Unexpected " +
    "token \"" + yytext + "\".\n\n";
  exit(1);
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
  Add a redefinition error to vector errors.
*/
void redefinition_error(string id) {
  string file = strdup(filename);

  string error = "\e[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \e[31mError:\e[0m Redefinition of " +
    "\"" + id + "\".\n\n";

  // add the error to the queue
  errors.push(error);
}

/*
  Add a undefined error to vector errors.
*/
void undefined_error(string id) {
  string file = strdup(filename);

  string error = "\e[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \e[31mError:\e[0m \"" + id + "\" was not " +
    "declared.\n\n";

  // add the error to the queue
  errors.push(error);
}

