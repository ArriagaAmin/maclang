%{
  #include <iostream>
  #include <queue>
  #include <cstring>
  #include <string>
  #include "ast.hpp"

  using namespace std;

  extern int yylex(void);
  extern int yylineno;
  extern int yycolumn;
  extern char *yytext;

  // queues for tokens and errors
  extern queue<string> errors;

  // offsets the columns and the rows for multiline comments
  void setMultiLineOffset(char* text);

  // Prints error;
  void yyerror(char *s);

  // Prints the queue to std.
  void printQueue(queue<string> queueToPrint);

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


%token SEMICOLON
%token OPEN_PAR
%token CLOSE_PAR
%token POWER
%token AND
%token OR
%token NOT_EQUIV
%token NOT
%token EQUIV
%token GREATER_EQUAL_THAN
%token LESS_EQUAL_THAN
%token GREATER_THAN
%token LESS_THAN
%token PLUS
%token MINUS
%token MODULE
%token DIV
%token ASTERISK
%token ASSIGNMENT
%token OPEN_BRACKET
%token CLOSE_BRACKET
%token OPEN_C_BRACE
%token CLOSE_C_BRACE
%token COMMA
%token REGISTER
%token DOT
%token UNION
%token POINTER
%token NEW
%token FORGET
%token IF
%token THEN
%token ELSIF
%token ELSE
%token END
%token WHILE
%token DO
%token DONE
%token FOR
%token LET
%token DEF
%token AT
%token RIGHT_ARROW
%token ERROR

%token <integer>  INT
%token <flot>     FLOAT
%token <str>      ID
%token <chr>      CHAR
%token <str>      STRING
%token <boolean>  TRUE FALSE
%token <str>      T_UNIT T_BOOL T_CHAR T_INT T_FLOAT T_STRING

%type <ast> I Inst Action VarInst VarDef VarDefBody OptAssign Type
%type <nS> S

%% 

/* =================== GLOBAL RULES =================== */
S       : I                   { $$ = new node_S($1); $$->print();  }
        | /* lambda */        { $$ = NULL; }
        ;
I       : Inst                { $$ = new node_I($1); }
        | I Inst              { $$ = new node_I($1, $2); }
        ;
Inst    : Action              { $$ = $1; }
				| Def                 { ; }
        ;
Action  : VarInst SEMICOLON   { $$ = $1; }
				| FuncCall SEMICOLON  { ; }
				| Conditional         { ; }
				| LoopWhile           { ; }
				| LoopFor             { ; }
        ;
Def     : UnionDef            { ; }
				| RegisterDef         { ; }
				| RutineDef           { ; }
        ;

/* ============ VARIABLES DEFINITION ============ */
VarInst     : VarDef                    { $$ = $1; }
						| Assign                    { ; }
            ;
VarDef      : LET VarDefBody            { $$ = $2; }  
            ;
VarDefBody  : Type ID OptAssign         { $$ = new node_VarDef($1, $2, $3); }
            ;   
OptAssign   : /* lambda */              { $$ = NULL; }
						| ASSIGNMENT RValue         { ; }
            ;
Assign      : LValue ASSIGNMENT RValue  { ; }
            ;
RValue      : Exp                       { ; }
            | Array                     { ; }
            | STRING                    { ; }
            ;

/* ======================== TYPES ======================== */
Type	: Type OPEN_BRACKET Exp CLOSE_BRACKET { /*$$ = new node_TypeArrayDef($1, $3)*/; }
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
LValue	:	LValue OPEN_BRACKET Exp CLOSE_BRACKET   { ; }
				|	POINTER LValue                          { ; }
				|	LValue DOT ID                           { ; }
				| OPEN_PAR LValue CLOSE_PAR               { ; }
				|	ID                                      { ; }
        ;

/* ======================= EXPRESSIONS ======================= */
Exp   : Exp EQUIV Exp               { ; }
      | Exp NOT_EQUIV Exp           { ; }
      | Exp OR Exp                  { ; }
      | Exp AND Exp                 { ; }
      | NOT Exp                     { ; }
      | Exp LESS_THAN Exp           { ; }
      | Exp LESS_EQUAL_THAN Exp     { ; }
      | Exp GREATER_THAN Exp        { ; }
      | Exp GREATER_EQUAL_THAN Exp  { ; }
      | Exp PLUS Exp                { ; }
      | Exp MINUS Exp               { ; }
      | Exp ASTERISK Exp            { ; }
      | Exp DIV Exp                 { ; }
      | Exp MODULE Exp              { ; }
      | MINUS Exp                   { ; }
      | PLUS Exp                    { ; }
      | Exp POWER Exp               { ; }
      | OPEN_PAR Exp CLOSE_PAR      { ; }
      | LValue                      { ; }
      | FuncCall                    { ; }
      | TRUE                        { ; }
      | FALSE                       { ; }
      | CHAR                        { ; }
      | INT                         { ; }
      | FLOAT                       { ; }
      ;

/* ====================== ARRAYS ====================== */
Array     : OPEN_BRACKET ArrExp CLOSE_BRACKET
          ;
ArrExp    : /* lambda */
					| ArrElems RValue 
          ;
ArrElems	: /* lambda */ 
					| ArrElems RValue COMMA
          ;

/* ================= FUNCTION CALLS ================= */
FuncCall  : ID OPEN_PAR ArgsExp CLOSE_PAR   { ; }
          ;
ArgsExp   : /* lambda */
					| Args RValue                     { ; }
          ;
Args      : /* lambda */ 
					| Args RValue COMMA               { ; }
          ;

/* ================= UNION DEFINITION ================= */
UnionDef  : UNION ID OPEN_C_BRACE UnionBody CLOSE_C_BRACE   { ; }
          ; 
UnionBody	: Type ID SEMICOLON                               { ; }
					| UnionBody Type ID SEMICOLON                     { ; }
          ;

/* ================ REGISTER DEFINITION ================ */
RegisterDef   : REGISTER ID OPEN_C_BRACE RegisterBody CLOSE_C_BRACE   { ; }
              ;
RegisterBody	: VarDefBody SEMICOLON                                      { ; }
							|	RegisterBody VarDefBody SEMICOLON                         { ; }
              ;

/* ===================== CONDITIONALS ===================== */
Conditional : IF Exp THEN I OptElsif OptElse END   { ; }
            ;
OptElsif    : /* lambda */ 
						| Elsifs                                { ; }
            ;
Elsifs      : ELSIF Exp THEN I                     { ; }
						| Elsifs ELSIF Exp THEN I              { ; }
            ;
OptElse     : /* lambda */ 
						| ELSE I                                { ; }
            ;

/* ======================== LOOPS ======================== */
LoopWhile : WHILE Exp DO I DONE                                            { ; }
          ; 
LoopFor   : FOR OPEN_PAR ID SEMICOLON Exp SEMICOLON 
            Exp OptStep CLOSE_PAR DO I DONE   { ; }
          ;
OptStep   : /* lambda */ 
				  | SEMICOLON Exp                                                  { ; }
          ;

/* =============== SUBROUTINES DEFINITION =============== */
RutineDef   : DEF ID OPEN_PAR RutineArgs CLOSE_PAR 
              OptReturn OPEN_C_BRACE Actions CLOSE_C_BRACE { ; }
            ; 
RutineArgs  : /* lambda */ 
						| ArgsDef                                                      { ; }
            ;
ArgsDef     : Type OptRef ID OptAssign                                     { ; }
						| ArgsDef Type OptRef ID OptAssign                             { ; }
            ;
OptRef      : /* lambda */
						| AT                                                           { ; }
            ;
OptReturn   : /* lambda */ 
						| RIGHT_ARROW Type                                             { ; }
            ;
Actions     : Action                                                       { ; }
						| Actions Action                                               { ; }
            ;

%%

int main(int argc, char **argv)
{
  // Look for input line
  if(argc != 2) 
  {
    cout << "No input file" << endl;
    return -1;
  }

  // open file to extract the tokens
  extern FILE *yyin;
  yyin = fopen(argv[1], "r");
    
  // check if file was succesfully opened.
  if (!yyin) 
  {
    cout << "There was an error opening the file" << endl;
    return -1;
  }

  // apply lexing
  int tok;
  while(tok = yylex());

  fclose(yyin);
  yyin = fopen(argv[1], "r");

  // if there are no errors, apply parsing
  if (errors.empty()) {
    
    // reset lines and columns
    yylineno = 1; 
    yycolumn = 1;

    // start parsing
    yyparse();
  } else {
    printQueue(errors);
  }
  return 0;
}

/*
  Prints error.
*/
void yyerror(char *s)
{
  fprintf(stderr, "error: %s (%d,%d)\n", s, yylineno, yycolumn);
}

/*
  offsets the columns and the rows for multiline comments, as could be the case
  that after a multiline comment could be a valid code statement.
*/
void setMultiLineOffset(char* text)
{ 
  for (int i=0; i < strlen(text); i++)
  {
    char x = text[i];

    // If there is a line break, reset the column and increment the row.
    if(x == '\n')
    {
      yylineno++;
      yycolumn = 0;
    } else {
      yycolumn++;
    }
  }
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