#pragma once

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

class StructureEntry;

/*
  Symbols Table implementation.
*/
class SymbolsTable {
  private:
    // Dictionary:  Name -> Entries
    map<string, deque<Entry*>> symTable;
    // Last scope added
    int lastScope;

  public:
    vector<int> scopeStack;
    set<int> globalScopes = {0, 1};
    bool inGlobal = true;
    // Return type in a function definition.
    string ret_type;
    vector<int> offsets;
    // Diccionario:  Scope -> Entries  que se usara para conseguir las entradas de una
    // estructura
    map<int, vector<Entry*>> scopeEntries;
    // Mapeo de nombre de tipos a una lista de pares 
    // <
    //      Tipo incompleto que hay que completar, 
    //      copia del scope stack en el momento en que se realizo la llamada
    // >
    map< string, vector<pair<StructureEntry*, vector<int>>> > incompleteTypesList;

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

    int newOffset(Type* t);

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
      string addr="",
      SymbolsTable *st=NULL
    );
    VarEntry(void) {};

    // Prints the variable information
    void print(void);
};

class VarArrayEntry : public VarEntry {
  public:
    // Access constant for quick retrival of elements
    unsigned low;
    unsigned high;
    int baseConstant;
  
    VarArrayEntry(
        string id, 
        int scope, 
        string category, 
        ArrayType *type, 
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
    int width = -1;
    int incomplete = 0;

    StructureEntry(string id, int scope, string category);

    // Prints the structure information
    void print(void);
};


class FunctionEntry : public Entry {
  public:
    // return type of the function
    Type *return_type;
    // scope for all inner definitions
    int def_scope;
    // every arg is a tuple (name, type, isReference, isOptional)
    vector<tuple<string, string, bool, bool>> args;
    string addr;
    string optargs_addr;

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

