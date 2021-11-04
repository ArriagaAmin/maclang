#include "memory.hpp"

/* 
  Reserva memoria para un arreglo de longitud constante que tal vez tenga arreglos
  de longitud variable.
*/
void allocConstArray(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;

  stack<ArrayType*> arrayStack;
  ArrayType* at;
  string type;
  
  // Recorremos el tipo arreglo hasta conseguir un tipo que no es un arreglo o es un 
  // arreglo de longitud variable.
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']' && ! ((ArrayType*) t)->is_pointer);

  // Si nos conseguimos con un arreglo o una estructura
  type = t->toString();
  if (type.back() == ']' || (! predefinedTypes.count(type) && type[0] != '^')) {
    // Obtenemos la longitud del hiper arreglo
    string size_addr = tac->newTemp();
    tac->gen("assign " + size_addr + " " + to_string(t->width));
    while (! arrayStack.empty()) {
      tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
      arrayStack.pop();
    }

    // Creamos un bucle en el que se reserva memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    // Dependiendo de si el tipo "base" es un arreglo de longitud variable o una 
    // estructura, realizamos la reserva de memoria correspondiente.
    if (type.back() == ']') {
      allocVarArray(t, final_addr + "[" + size_addr + "]");
    } 
    else {
      allocStruct(t, final_addr + "[" + size_addr + "]");
    }

    // Final del bucle.
    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }
}

/* 
  Reserva memoria para un arreglo de longitud variable.
*/
void allocVarArray(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;

  stack<ArrayType*> arrayStack;
  ArrayType *at;

  // Si el arreglo corresponde a un string, no hay que hacer nada.
  if (((ArrayType*) t)->is_string) {
    return;
  }
  
  // Recorremos el tipo arreglo hasta conseguir un tipo que no es un arreglo.
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']');

  // Creamos un bucle para obtener la longitud del hiper arreglo.
  string size_addr = tac->newTemp();
  tac->gen("assign " + size_addr + " " + to_string(t->width));
  while (! arrayStack.empty()) {
    tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
    arrayStack.pop();
  }
  
  tac->gen("malloc " + final_addr + " " + size_addr);

  // Si el tipo base del hiper arreglo no es primitivo ni puntero, es decir, es una
  // estructura, hay que reservar la memoria de cada uno explicitamente.
  if (! predefinedTypes.count(t->toString()) && t->toString()[0] != '^') {

    // Creamos un bucle en el que se reserva memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");
    allocStruct(t, final_addr + "[" + size_addr + "]");
    tac->gen("goto " + label);
    tac->gen("goto " + label + "_end");
  }
}

/* 
  Reserva memoria para una estructura de datos (union o registro) que tal vez almacene
  un arreglo de longitud variable.
*/
void allocStruct(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  extern SymbolsTable *table;

  // Obtenemos el scope de definicion de la estructura.
  PrimitiveType *pt = (PrimitiveType*) t;
  StructureEntry *se = (StructureEntry*) table->lookup(pt->id);
  int scope = se->def_scope;

  // Si la estructura define algun campo.
  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type;
    ArrayType *at;

    // Por cada campo de la estructura.
    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();

      // Reservamos la memoria necesaria para los campos que son arreglos.
      if (type.back() == ']') {
        at = (ArrayType*) ve->type;
        // Ya sean de longitud variable
        if (at->is_pointer) {
          allocVarArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
        }
        // O longitud constante.
        else {
          allocConstArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");

        }
      }
      // Y para los campos que son otras estructuras.
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        allocStruct(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
      }
    }
  }
}

/* 
  Libera memoria para un arreglo de longitud constante que tal vez tenga arreglos
  de longitud variable.
*/
void freeConstArray(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;

  stack<ArrayType*> arrayStack;
  ArrayType* at;
  string type;
  
  // Recorremos el hiper arreglo hasta conseguir un tipo que no es un arreglo o es un 
  // arreglo de longitud variable.
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']' && ! ((ArrayType*) t)->is_pointer);

  // Si nos conseguimos con un arreglo o una estructura
  type = t->toString();
  if (type.back() == ']' || (! predefinedTypes.count(type) && type[0] != '^')) {
    // Obtenemos la longitud del hiper arreglo
    string size_addr = tac->newTemp();
    tac->gen("assign " + size_addr + " " + to_string(t->width));
    while (! arrayStack.empty()) {
      tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
      arrayStack.pop();
    }

    // Creamos un bucle en el que se libera memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    // Dependiendo de si el tipo "base" es un arreglo de longitud variable o una 
    // estructura, realizamos la liberacion de memoria correspondiente.
    if (type.back() == ']') {
      freeVarArray(t, final_addr + "[" + size_addr + "]");
    } 
    else {
      freeStruct(t, final_addr + "[" + size_addr + "]");
    }

    // Final del bucle.
    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }
}

/* 
  Libera memoria para un arreglo de longitud variable.
*/
void freeVarArray(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;

  stack<ArrayType*> arrayStack;
  ArrayType *at;

  // Si el arreglo corresponde a un string, no hay que hacer nada.
  if (((ArrayType*) t)->is_string) {
    return;
  }
  
  // Recorremos el tipo arreglo hasta conseguir un tipo que no es un arreglo.
  do {
    at = (ArrayType*) t;
    arrayStack.push(at);
    t = at->type;
  } while (t->toString().back() == ']');

  // Si el tipo base del hiper arreglo no es primitivo ni puntero, es decir, es una
  // estructura, hay que liberar la memoria de cada uno explicitamente.
  if (! predefinedTypes.count(t->toString()) && t->toString()[0] != '^') {

    // Creamos un bucle para reservar la memoria del hiper arreglo.
    string size_addr = tac->newTemp();
    tac->gen("assign " + size_addr + " " + to_string(t->width));
    while (! arrayStack.empty()) {
      tac->gen("mult " + size_addr + " " + size_addr + " " + arrayStack.top()->size->addr);
      arrayStack.pop();
    }

    // Creamos un bucle en el que se libera memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");
    freeStruct(t, final_addr + "[" + size_addr + "]");
    tac->gen("goto " + label);
    tac->gen("goto " + label + "_end");
  }
  
  // Liberamos la memoria del arreglo entero.
  tac->gen("free " + final_addr);
}

/* 
  Libera memoria para una estructura de datos (union o registro) que tal vez almacene
  un arreglo de longitud variable.
*/
void freeStruct(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  extern SymbolsTable *table;

  // Obtenemos el scope de definicion de la estructura.
  PrimitiveType *pt = (PrimitiveType*) t;
  StructureEntry *se = (StructureEntry*) table->lookup(pt->id);
  int scope = se->def_scope;

  // Si la estructura define algun campo.
  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type;
    ArrayType *at;

    // Por cada campo de la estructura.
    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();

      // Liberamos la memoria necesaria para los campos que son arreglos.
      if (type.back() == ']') {
        at = (ArrayType*) ve->type;
        // Ya sean de longitud variable
        if (at->is_pointer) {
          freeVarArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
        }
        // O longitud constante.
        else {
          freeConstArray(ve->type, final_addr + "[" + to_string(ve->offset) + "]");

        }
      }
      // Y para los campos que son otras estructuras.
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        freeStruct(ve->type, final_addr + "[" + to_string(ve->offset) + "]");
      }
    }
  }
}

