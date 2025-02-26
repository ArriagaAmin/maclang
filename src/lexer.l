/* recognizes the tokens and prints them out */
%option noyywrap
%option yylineno

%{
  #include <string>
  #include <vector>
  #include <queue>
  #include <iostream>
  
  #include "table.hpp"
  #include "parser.tab.h"

  using namespace std;

  // queues for tokens and errors
  queue<string> errors;
  char *filename;
  string line = "";
  
  // count rows and columns to identify errors
  int yycolumn = 1;

  #define YY_USER_ACTION \
    yylloc.first_line = yylloc.last_line = yylineno; \
    yylloc.first_column = yycolumn; yylloc.last_column = yycolumn + yyleng - 1; \
    yycolumn += yyleng; \
    yylval.str = new string(yytext); 

  // add an error to queue
  void pushError(void);

  extern YY_BUFFER_STATE * yy_buffer_stack;
  extern size_t yy_buffer_stack_top;
  YY_BUFFER_STATE current_buffer(void) {
    return yy_buffer_stack ? (yy_buffer_stack)[(yy_buffer_stack_top)] : NULL;
  }
%}

%%
\$\{(\}[^\$]|[^\}])*\}\$      { /* ignore multiline line comment */ }
#.*\n                         { yycolumn = 1; /* ignore single line comment */ }
#.*                           { yycolumn = 1; /* ignore single line comment */ }
";"                           { return SEMICOLON; }
"("                           { return OPEN_PAR; }
")"                           { return CLOSE_PAR; }
"**"                          { return POWER; }
"&&"                          { return AND; }
"||"                          { return OR; }
"!="                          { return NOT_EQUIV; }
"!"                           { return NOT; }
"=="                          { return EQUIV; }
">="                          { return GREATER_EQUAL_THAN; }
"<="                          { return LESS_EQUAL_THAN; }
">"                           { return GREATER_THAN; }
"<"                           { return LESS_THAN; }
"+"                           { return PLUS; }
"-"                           { return MINUS; }
"%"                           { return MODULE; }
"/"                           { return DIV; }
"*"                           { return ASTERISK; }
"="                           { return ASSIGNMENT; } 
"Int"                         { return T_INT; }
"Char"                        { return T_CHAR; }
"Bool"                        { return T_BOOL; }
"Float"                       { return T_FLOAT; }
"Unit"                        { return T_UNIT; }
"String"                      { return T_STRING; }
"False"                       { return FALSE; }
"True"                        { return TRUE; }
"["                           { return OPEN_BRACKET; }
"]"                           { return CLOSE_BRACKET; }
"{"                           { return OPEN_C_BRACE; }  
"}"                           { return CLOSE_C_BRACE; }
","                           { return COMMA; }
"register"                    { return REGISTER; }
"."                           { return DOT; }
"union"                       { return UNION; }
"structure"                   { return STRUCTURE; }
"^"                           { return POINTER; }
"new"                         { return NEW; }
"forget"                      { return FORGET; }
"if"                          { return IF; }
"then"                        { return THEN; }
"elsif"                       { return ELSIF; }
"else"                        { return ELSE; }
"while"                       { return WHILE; }
"do"                          { return DO; }
"done"                        { return DONE; }
"for"                         { return FOR; }
"let"                         { return LET; }
"def"                         { return DEF; }
"dec"                         { return DEC; }
"opt"                         { return OPT; }
"@"                           { return AT; }
"=>"                          { return RIGHT_ARROW; }
"return"                      { return RETURN; }
"break"                       { return BREAK; }
"continue"                    { return CONTINUE; }
"exit"                        { return EXIT; }
"exec"                        { return EXEC; }
"execonce"                    { return EXECONCE; }
[[:alpha:]_][[:alnum:]_]*     { return ID; }
[0-9]+                        { yylval.integer = atoi(yytext); return INT; }
[0-9]+\.[0-9]+                { yylval.flot = atof(yytext); return FLOAT; }
[[:digit:]][[:alnum:]_]*      { 
                                /* add error to queue */
                                pushError(); 
                              }
[\t]                          { yycolumn++; /* ignore tab */ }
[ ]                           { /* ignore whitespace */ }


\'.\'                         { yylval.integer = yytext[1]; return CHAR; }
\'\\\'\'                      { yylval.integer = '\'';      return CHAR; }
\'\\\\\'                      { yylval.integer = '\\';      return CHAR; }
\'\\a\'                       { yylval.integer = '\a';      return CHAR; }
\'\\b\'                       { yylval.integer = '\b';      return CHAR; }
\'\\f\'                       { yylval.integer = '\f';      return CHAR; }
\'\\n\'                       { yylval.integer = '\n';      return CHAR; }
\'\\r\'                       { yylval.integer = '\r';      return CHAR; }
\'\\t\'                       { yylval.integer = '\t';      return CHAR; }
\'\\v\'                       { yylval.integer = '\v';      return CHAR; }
\'\\([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\' { yylval.integer = atoi(&yytext[2]); return CHAR; }

\"(?:[^"\\\n]|\\.)*\"         { return STRING; }
\n                            { yycolumn = 1; /* ignore new line characters */ } 
.                             { 
                                /* add error to queue */
                                pushError(); 
                              }

            
%%

/*
  adds a lexing error to the queue that will be printed on the parsing phase
*/
void pushError() {
  // duplicate the value of yytext
  string token = strdup(yytext);
  string file = strdup(filename);

  string error = "\033[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn - yyleng) + "): \033[31mLexical error:\033[0m Unexpected " +
    "token \"" + token + "\".\n\n";

  // add the error to the queue
  errors.push(error);
}