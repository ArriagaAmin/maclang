%{  
  #include <iostream>
  #include <string>
  #include <cstring>
  #include <set>
  #include "translate.hpp"

  #include "errors.hpp"

  using namespace std;

  extern int yylineno;
  extern int yycolumn;
  extern char *filename;
  extern queue<string> errors;
  T_Block *block = new T_Block;
%}

%define parse.lac full

%union 
{  
  int          integer;
  float        flot;
  bool         boolean;
  char         chr;
  std::string  *str;
}

%locations
%start S

%token MI_STATICV MI_STRING MI_LABEL
%token I_ASSIGN I_ADD I_SUB I_MULT I_DIV I_MOD I_MINUS I_EQ I_NEQ I_LT I_LEQ I_GT I_GEQ 
%token I_GOTO I_GOIF I_MALLOC I_FREE I_PARAM I_CALL I_RETURN I_EXIT
%token OPEN_BRACKET CLOSE_BRACKET NL

%token <integer>  INT
%token <flot>     FLOAT 
%token <chr>      CHAR
%token <str>      STRING 
%token <boolean>  TRUE 
%token <boolean>  FALSE
%token <str>      ID

%type <str> T Lvalue Rvalue

%%
  S       : Data Text
          ;

  Data    : /* lambda */
          | D Data
          ;

  D       : 
            MI_STATICV ID INT NL 
            {

            }
          | MI_STRING ID STRING NL
            {

            }
          ;

  Text    : /* lambda */
          | T Text 
          ;
  T       : NL { /* ignore */ }
          | MI_LABEL ID NL
            {
              T_Instruction inst;
              inst.id = "@label";
              inst.result = *$2;
              block->insertInstruction(inst);
            }
          | I_ASSIGN Lvalue Rvalue NL
            {

            }
          | I_ADD Lvalue Rvalue Rvalue NL
            {
              T_Instruction inst = {"add", *$2, *$3, *$4};
              block->insertInstruction(inst);
            }
          | I_SUB Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_MULT Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_DIV Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_MOD Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_MINUS Lvalue Rvalue NL
            {
              
            }
          | I_EQ Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_NEQ Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_LT Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_LEQ Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_GT Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_GEQ Lvalue Rvalue Rvalue NL
            {
              
            }
          | I_GOTO ID NL
            {
              
            }
          | I_GOIF ID Rvalue NL
            {
              
            }
          | I_MALLOC Lvalue Rvalue NL
            {
              
            }
          | I_FREE Rvalue NL
            {
              
            }
          | I_PARAM Rvalue NL
            {
              
            }
          | I_CALL Lvalue ID Rvalue NL
            {
              
            }
          | I_RETURN Rvalue NL
            {
              
            }
          | I_EXIT Rvalue NL
            {
              
            }
          ;
       
  Lvalue  : ID 
            {
              $$ = $1;
            }
          | Lvalue OPEN_BRACKET INT CLOSE_BRACKET
            {
            }
          | Lvalue OPEN_BRACKET ID CLOSE_BRACKET
            {

            }
          ;

  Rvalue  : Lvalue 
            {
              $$ = $1;
            }
          | FLOAT
            {
              
            }
          | INT
            {

            }
          | CHAR
            {

            }
          | TRUE
            {

            }
          | FALSE
            {

            }
          ;
%%

int main(int argc, char **argv) {
  // open file to extract the tokens
  extern FILE *yyin;

  // Verify all arguments has been passed
  if (argc != 2) {
    cout << "\033[1mSYNOPSIS\n"
      "\t\033[1mtac2mips\033[0m \033[4mFILE\033[0m\n";
    return 1;
  } 
  
  filename = argv[1];
  // check if file was succesfully opened.
  if ((yyin = fopen(filename, "r")) == 0) {
    cout << "There was an error opening the file" << endl;
    return -1;
  }
  // reset lines and columns
  yylineno = 1; 

  // start parsing
  yyparse();

  if (errors.empty()) {
  } 
  else {
    // print all errors
    printQueue(errors);
    return 1;
  }

  block->translate();
  block->print();

  //printf("OK!\n");

  return 0;
}
