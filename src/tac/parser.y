%{  
  #include <iostream>
  #include <string>
  #include <cstring>
  #include <set>

  #include "errors.hpp"

  using namespace std;

  extern int yylineno;
  extern int yycolumn;
  extern char *filename;
  extern queue<string> errors;
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

%token MI_STATICV MI_STRING MI_LABEL MI_FUNCTION MI_ENDFUNCTION MI_DECLARED
%token I_ASSIGN I_ADD I_SUB I_MULT I_DIV I_MOD I_MINUS I_EQ I_NEQ I_LT I_LEQ I_GT I_GEQ 
%token I_GOTO I_GOIF I_MALLOC I_FREE I_PARAM I_CALL I_RETURN
%token OPEN_BRACKET CLOSE_BRACKET NL

%token <integer>  INT
%token <flot>     FLOAT 
%token <chr>      CHAR
%token <str>      STRING 
%token <boolean>  TRUE 
%token <boolean>  FALSE
%token <str>      ID

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

  T       : I 
          | F  
          ;

  F       : MI_FUNCTION ID NL Inst MI_ENDFUNCTION NL
            {

            }
          ;

  Inst    : /* lambda */
          | I Inst 
          ;

  I       : NL { /* ignore */ }
          | MI_LABEL ID NL
            {

            }
          | MI_DECLARED Lvalue ID NL 
            {

            }
          | I_ASSIGN Lvalue Rvalue NL
            {

            }
          | I_ADD Lvalue Rvalue Rvalue NL
            {

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
          ;
       
  Lvalue  : ID 
            {

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

  printf("OK!\n");

  return 0;
}
