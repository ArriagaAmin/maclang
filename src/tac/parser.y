%{  
  #include <iostream>
  #include <string>
  #include <cstring>
  #include <set>

  #include "translate.hpp"
  #include "errors.hpp"
  #include "FlowGraph.hpp"

  using namespace std;

  extern int yylineno;
  extern int yycolumn;
  extern char *filename;
  extern queue<string> errors;

  T_Function *global = new T_Function, *current_function;
  vector<T_Function*> functions = {global};
  // Indica que funciones han sido llamadas.
  set<string> calls;
  bool err = false;

  Translator *CB;
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
%token <str> I_READF I_READ I_FTOI I_ITOF I_OR I_AND
%token OPEN_BRACKET CLOSE_BRACKET NL

%token <integer>  INT
%token <flot>     FLOAT 
%token <chr>      CHAR
%token <str>      STRING 
%token <boolean>  TRUE 
%token <boolean>  FALSE
%token <str>      ID

%type <str> T Val RVal Acc

%%
  S       : Data Text
            {
              // Agregamos el lider que representa EXIT
              global->leaders.insert(global->instructions.size());

              // Agregamos los lideres generados debido a gotos
              for (string label : global->labels_leaders) {
                if (global->labels2instr.count(label) == 0) {
                  cout << "\033[1;31mError\033[0m: Undefined label \033[1;3m" + 
                    label + "\033[0m.\n";
                  err = true;
                }
                else {
                  global->leaders.insert(global->labels2instr[label]);
                }
              }

              // Pasamos del conjunto de lideres al vector de lideres.
              for (uint64_t leader : global->leaders) {
                global->vec_leaders.push_back(leader);
              }
              global->leaders.clear();

              // Filtramos aquellas funciones que nunca fueron llamadas.
              vector<T_Function*> filtered_functions = {global};
              for (T_Function *f : functions) {
                if (calls.count(f->name)) {
                  filtered_functions.push_back(f);
                }
              }

              if (! err) {
                FlowGraph fg = FlowGraph(filtered_functions);
                cout << "Graph flow created" << endl;
                CB->insertFlowGraph(&fg);
                fg.prettyPrint();
                CB->translate();
                CB->print();
              }
            }
          ;

  Data    : /* lambda */
          | D Data
          ;

  D       : 
            MI_STATICV ID INT NL 
            {
              CB->insertInstruction(new T_Instruction{*$1, *$2, {to_string($3)}});
            }
          | MI_STRING  ID STRING NL
            {
              CB->insertInstruction(new T_Instruction{*$1, *$2, {*$3}});
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
              //CB->insertInstruction(new T_Instruction{*$1, *$2, {}});
              current_function->labels2instr[*$2] = current_function->instructions.size();
            }
          | I_ASSIGNW Acc Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_ASSIGNW ID RVal
            { 
              //CB->insertInstruction(new T_Instruction{*$1, *$2, {*$3}});
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_ASSIGNB Acc Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_ASSIGNB ID RVal
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_ADD     ID Val Val
            {
              //CB->insertInstruction(new T_Instruction{*$1, *$2, {*$3, *$4}});
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_SUB     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_MULT    ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_DIV     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_MOD     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_MINUS   ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_FTOI    ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_ITOF    ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_EQ      ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_NEQ     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_LT      ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_LEQ     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_GT      ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_GEQ     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_OR      ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_AND     ID Val Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_GOTO    ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
              current_function->leaders.insert(current_function->instructions.size());
              current_function->labels_leaders.insert(*$2);
            }
          | I_GOIF    ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
              current_function->leaders.insert(current_function->instructions.size());
              current_function->labels_leaders.insert(*$2);
            }
          | I_GOIFNOT ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
              current_function->leaders.insert(current_function->instructions.size());
              current_function->labels_leaders.insert(*$2);
            }
          | I_MALLOC  ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_MEMCPY  ID ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, *$4}});
            }
          | I_FREE    ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_EXIT    Val
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_PARAM   ID Val
            {
              current_function->instructions.push_back({*$1, *$2, {*$3}});
            }
          | I_RETURN  Val
            {
              current_function->instructions.push_back({*$1, *$2, {}});
              current_function->leaders.insert(current_function->instructions.size());
            }
          | I_CALL    ID ID INT
            {
              current_function->instructions.push_back({*$1, *$2, {*$3, to_string($4)}});
              calls.insert(*$3);
            }
          | I_PRINTC  Val
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_PRINTI  Val
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_PRINTF  Val
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_PRINT   ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_READC   ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_READI   ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_READF   ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          | I_READ    ID
            {
              current_function->instructions.push_back({*$1, *$2, {}});
            }
          ;
       
  F       : Function NL Inst MI_ENDFUNCTION INT
            {
              // Agregamos los lideres generados debido a gotos
              for (string label : current_function->labels_leaders) {
                if (current_function->labels2instr.count(label) == 0) {
                  cout << "\033[1;31mError\033[0m: Undefined label \033[1;3m" + 
                    label + "\033[0m.\n";
                  err = true;
                }
                else {
                  current_function->leaders.insert(current_function->labels2instr[label]);
                }
              }

              // Agregamos el lider que representa EXIT
              current_function->leaders.insert(current_function->instructions.size());

              // Pasamos del conjunto de lideres al vector de lideres.
              for (uint64_t leader : current_function->leaders) {
                current_function->vec_leaders.push_back(leader);
              }
              current_function->leaders.clear();

              current_function = global;
            }

  Function: MI_FUNCTION ID INT
            {
              current_function = new T_Function;
              current_function->id = functions.size();
              functions.push_back(current_function);

              current_function->size = $3;
              current_function->name = *$2;
              current_function->labels2instr[*$2] = current_function->instructions.size();
              current_function->leaders.insert(current_function->instructions.size());
            }

  Inst    : /* lambda */
          | I NL Inst 
            {
            }
          ;

  Acc     : ID OPEN_BRACKET Val CLOSE_BRACKET
            {
              $$ = new string(*$1 + "[" + *$3 + "]");
            }
          ;


  Val     : TRUE
            {
              $$ = new string(to_string($1));
            }
          | FALSE 
            {
              $$ = new string(to_string($1));
            }
          | CHAR 
            {
              $$ = new string(to_string($1));
            }
          | INT 
            {
              $$ = new string(to_string($1));
            }
          | FLOAT 
            {
              $$ = new string(to_string($1));
            }
          | ID 
            {
              $$ = $1;
            }
          ;

  RVal    : Val 
            {
              $$ = $1;
            }
          | Acc
            {
              $$ = $1;
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

  CB = new Translator;

  // start parsing
  global->id = 0;
  current_function = global;
  yyparse();

  if (errors.empty()) {
  } 
  else {
    // print all errors
    printQueue(errors);
    return 1;
  }

  //CB->translate();
  //CB->print();
  //CB->printVariablesDescriptors();

  return 0;
}
