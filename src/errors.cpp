#include "errors.hpp"

/*
  Prints error.
*/
void yyerror(string s) {
  string file = strdup(filename);
    
  // Add syntax error
  string error = "\033[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \033[31mSyntax error:\033[0m Unexpected " +
    "token \"" + yytext + "\".\n\n";

  errors.push(error);

  // read the remaining file for more lexical errors.
  while(yylex());
}

/*
  Add a error to vector errors.
*/
void addError(string error) {
  string file = strdup(filename);

  string err = "\033[1m" + file + " (" + to_string(yylineno) + ", " + 
    to_string(yycolumn) + "): \033[31mError:\033[0m " + error + "\n\n";

  // add the error to the queue
  errors.push(err);
}

/*
  Prints the queue to std.
*/
void printQueue(queue<string> queueToPrint) {
  while (!queueToPrint.empty()) {
    cout << queueToPrint.front();
    queueToPrint.pop();
  }
}