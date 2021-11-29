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

  CodeBlock *CB;
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

%token <str> MI_STATICV MI_STRING MI_LABEL MI_FUNCTION MI_ENDFUNCTION
%token <str> I_ASSIGN I_ADD I_SUB I_MULT I_DIV I_MOD I_MINUS I_EQ I_NEQ I_LT I_LEQ I_GT 
%token <str> I_GEQ I_GOTO I_GOIF I_MALLOC I_MEMCPY  I_FREE I_PARAM I_CALL I_RETURN I_EXIT
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
              CB->Translate({*$1, *$2, {to_string($3)}});
            }
          | MI_STRING  ID STRING NL
            {
              CB->Translate({*$1, *$2, {*$3}});
            }
          ;

  Text    : /* lambda */
          | T NL Text 
          ;

  T       : I 
            {

            }
          | F 
            {

            }
          ;

  I       : /* lambda */
          | MI_LABEL ID
            {
              CB->Translate({*$1, *$2, {}});
            }
          | I_ASSIGN Acc Val
            {

            }
          | I_ASSIGN ID RVal
            {

            }
          | I_ADD    ID Val Val
            {

            }
          | I_SUB    ID Val Val
            {
              
            }
          | I_MULT   ID Val Val
            {
              
            }
          | I_DIV    ID Val Val
            {
              
            }
          | I_MOD    ID Val Val
            {
              
            }
          | I_MINUS  Acc Val
            {
              
            }
          | I_MINUS  ID RVal
            {
              
            }
          | I_EQ     ID Val Val
            {
              
            }
          | I_NEQ    ID Val Val
            {
              
            }
          | I_LT     ID Val Val
            {
              
            }
          | I_LEQ    ID Val Val
            {
              
            }
          | I_GT     ID Val Val
            {
              
            }
          | I_GEQ    ID Val Val
            {
              
            }
          | I_GOTO   ID
            {
              
            }
          | I_GOIF   ID RVal
            {
              
            }
          | I_MALLOC Acc Val
            {
              
            }
          | I_MALLOC ID RVal
            {
              
            }
          | I_MEMCPY Acc ID
            {
              
            }
          | I_MEMCPY ID RVal
            {
              
            }
          | I_FREE   LVal
            {
              
            }
          | I_EXIT   RVal
            {
              
            }
          | I_PARAM  RVal
            {
              
            }
          | I_RETURN RVal
            {
              
            }
          | I_CALL   ID ID INT
            {
              
            }
          ;
       
  F       : MI_FUNCTION ID INT NL Inst MI_ENDFUNCTION

  Inst    : /* lambda */
          | I NL Inst 
            {

            }
          ;

  Acc     : ID OPEN_BRACKET Val CLOSE_BRACKET
            {

            }
          ;

  LVal    : ID 
            {

            }
          | Acc 
            {

            }
          ;

  Val     : TRUE
            {

            }
          | FALSE 
            {

            }
          | CHAR 
            {

            }
          | INT 
            {

            }
          | FLOAT 
            {

            }
          | ID 
            {

            }
          ;

  RVal    : Val 
            {

            }
          | Acc
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

  CB = new CodeBlock;

  // start parsing
  yyparse();

  if (errors.empty()) {
  } 
  else {
    // print all errors
    printQueue(errors);
    return 1;
  }

  CB->print();

  return 0;
}
