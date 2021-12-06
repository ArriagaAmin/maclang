%{  
  #include <iostream>
  #include <string>
  #include <cstring>
  #include <set>
  #include "translate.hpp"

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
%token <str> I_ASSIGNW I_ASSIGNB I_ADD I_SUB I_MULT I_DIV I_MOD I_MINUS I_EQ I_NEQ I_LT 
%token <str> I_LEQ I_GT I_GEQ I_GOTO I_GOIF I_GOIFNOT I_MALLOC I_MEMCPY  I_FREE I_PARAM 
%token <str> I_CALL I_RETURN I_EXIT I_PRINTC I_PRINTI I_PRINTF I_PRINT I_READC I_READI
%token <str> I_READF I_READ
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
          | I_ASSIGNW Acc Val
            {

            }
          | I_ASSIGNW ID RVal
            {
              T_Instruction inst;
              inst.id = "@label";
              inst.result = *$2;
              block->insertInstruction(inst);
            }
          | I_ASSIGNB Acc Val
            {

            }
          | I_ASSIGNB ID RVal
            {
              T_Instruction inst = {"add", *$2, *$3, *$4};
              block->insertInstruction(inst);
            }
          | I_ADD     ID Val Val
            {

            }
          | I_SUB     ID Val Val
            {
              
            }
          | I_MULT    ID Val Val
            {
              
            }
          | I_DIV     ID Val Val
            {
              
            }
          | I_MOD     ID Val Val
            {
              
            }
          | I_MINUS   ID Val
            {
              
            }
          | I_EQ      ID Val Val
            {
              
            }
          | I_NEQ     ID Val Val
            {
              
            }
          | I_LT      ID Val Val
            {
              
            }
          | I_LEQ     ID Val Val
            {
              
            }
          | I_GT      ID Val Val
            {
              
            }
          | I_GEQ     ID Val Val
            {
              
            }
          | I_GOTO    ID
            {
              
            }
          | I_GOIF    ID Val
            {
              
            }
          | I_GOIFNOT ID Val
            {
              
            }
          | I_MALLOC  ID Val
            {
              
            }
          | I_MEMCPY  ID ID Val
            {
              
            }
          | I_FREE    ID
            {
              
            }
          | I_EXIT    Val
            {
              
            }
          | I_PARAM   ID Val
            {
              
            }
          | I_RETURN  Val
            {
              
            }
          | I_CALL    ID ID INT
            {
              
            }
          | I_PRINTC  Val
            {

            }
          | I_PRINTI  Val
            {
              
            }
          | I_PRINTF  Val
            {
              
            }
          | I_PRINT   ID
            {
              
            }
          | I_READC   Val
            {
              $$ = $1;
            }
          | I_READI   Val
            {
              
            }
          | I_READF   Val
            {
              
            }
          | I_READ    ID
            {
              
            }
          ;
       
  F       : MI_FUNCTION ID INT NL Inst MI_ENDFUNCTION INT

  Inst    : /* lambda */
          | I NL Inst 
            {
            }
          ;

  Acc     : ID OPEN_BRACKET Val CLOSE_BRACKET
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
