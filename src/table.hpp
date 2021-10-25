#include <map>
#include <deque>
#include <vector>
#include <iostream>
#include "ast.hpp"

using namespace std;

/*
  "Abstract" class that is parent of all entries classes in the Symbols Table.
*/
class Entry {
  public:
    // Variable identification.
    string id;
    // Scope where variable was defined.
    int scope;
    int offset;
    // Category of the entry
    string category;
  
    Entry(void) {};

    // Prints the variable information
    virtual void print(void) {};
};

/*
  Symbols Table implementation.
*/
class SymbolsTable {
  private:
    // Dictionary:  Name -> Entries
    map<string, deque<Entry*>> symTable;
    vector<int> scopeStack;
    // Last scope added
    int lastScope;

  public:
    // Return type in a function definition.
    string ret_type;
    vector<int> offsets;

    SymbolsTable(void);

    // Insert a new entry
    void insert(Entry *e);

    int currentScope(void);

    // Verify if a ID can be added
    bool verifyInsert(string id);

    // Find a variable
    Entry* lookup(string id);

    // Find a variable in a scope
    Entry* lookup(string id, int scope);

    // Erase a variable in a scope
    void erase(string id, int scope);

    // Add a new scope
    int newScope(void);

    // Delete the last scope
    void exitScope(void);

    // Prints representation of the symbols table
    void printTable(void);

    // Prints representation of the scope stack 
    void printScopeStack(void);
};


class PrimitiveEntry : public Entry {
  public:
    PrimitiveEntry(string id);

    Type *type;

    void print(void);
};


class VarEntry : public Entry {
  public:
    // Variable type
    Type *type;
    // Nombre temporal para el TAC
    string addr;
  
    VarEntry(
      string id, 
      int scope, 
      string category, 
      Type *type, 
      int offset, 
      string addr=""
    );

    // Prints the variable information
    void print(void);
};


class StructureEntry : public Entry {
  public:
    // scope where the entry was defined.
    int def_scope;  
    int width;

    StructureEntry(string id, int scope, string category, int def_scope, int width);

    // Prints the structure information
    void print(void);
};


class FunctionEntry : public Entry {
  public:
    // return type of the function
    Type *return_type;
    // scope for all inner definitions
    int def_scope;
    // every arg is a tuple (name, type, isReference, isMandatory)
    vector<tuple<string, string, bool, bool>> args;

    FunctionEntry(string id, int scope, string category);
    FunctionEntry(void) {};

    // Prints the function information
    void print(void);
};


class FunctionDeclarationEntry : public FunctionEntry {
  public:
    FunctionDeclarationEntry(
      string id, 
      int scope,
      string category, 
      vector<tuple<string, string, bool, bool>> args, 
      Type *return_type
    );

    // Prints the function information
    void print(void);
};

