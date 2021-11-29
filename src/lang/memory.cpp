#include "memory.hpp"

/* 
  Reserva memoria para un arreglo.
*/
void allocArray(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  ArrayType *at = (ArrayType*) t;
  string type, typesize_addr, final_addr_aux;

  // Si el arreglo corresponde a un string, no hay que hacer nada.
  if (at->is_string) {
    return;
  }
  
  // Obtenemos el tipo interno
  t = at->type;

  if (at->size->addr.back() == ']') {
    typesize_addr = tac->newTemp();
    tac->gen("assignw " + typesize_addr + " " + at->size->addr);
  }
  else {
    typesize_addr = at->size->addr;
  }

  if (final_addr.back() == ']') {
    final_addr_aux = tac->newTemp();
    tac->gen("assignw " + final_addr_aux + " " + final_addr);
  }
  else {
    final_addr_aux = final_addr;
  }

  // Obtenemos la longitud del hiper arreglo y lo reservamos
  string size_addr = tac->newTemp();
  tac->gen("assignw " + size_addr + " " + to_string(t->width));
  tac->gen("mult " + size_addr + " " + size_addr + " " + typesize_addr);
  tac->gen("malloc " + final_addr_aux + " " + size_addr);

  if (final_addr.back() == ']') {
    tac->gen("assignw " + final_addr + "[0] " + final_addr_aux);
  }

  // Si el tipo base del hiper arreglo no es primitivo ni puntero, es decir, es una
  // estructura, hay que reservar la memoria de cada uno explicitamente.
  type = t->toString();
  if (type.back() == ']' || (! predefinedTypes.count(type) && type[0] != '^')) {

    // Creamos un bucle en el que se reserva memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    if (type.back() == ']') {
      allocArray(t, final_addr_aux + "[" + size_addr + "]");
    }
    else {
      allocStruct(t, final_addr_aux + "[" + size_addr + "]");
    }

    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }
}

/* 
  Reserva memoria para una estructura de datos (union o registro) que tal vez almacene
  un arreglo.
*/
void allocStruct(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  extern SymbolsTable *table;
  string final_addr_aux;

  if (final_addr.back() == ']') {
    final_addr_aux = tac->newTemp();
    tac->gen("assignw " + final_addr_aux + " " + final_addr);
  }
  else {
    final_addr_aux = final_addr;
  }

  // Reservamos la memoria para la estructura completa
  tac->gen("malloc " + final_addr_aux + " " + to_string(t->width));

  if (final_addr.back() == ']') {
    tac->gen("assignw " + final_addr + "[0] " + final_addr_aux);
  }

  // Obtenemos el scope de definicion de la estructura.
  PrimitiveType *pt = (PrimitiveType*) t;
  StructureEntry *se = (StructureEntry*) table->lookup(pt->id);
  int scope = se->def_scope;

  // Si la estructura define algun campo.
  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type;

    // Por cada campo de la estructura.
    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();

      // Reservamos la memoria necesaria para los campos que son arreglos.
      if (type.back() == ']') {
        allocArray(ve->type, final_addr_aux + "[" + to_string(ve->offset) + "]");
      }
      // Y para los campos que son otras estructuras.
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        allocStruct(ve->type, final_addr_aux + "[" + to_string(ve->offset) + "]");
      }
    }
  }
}



/* 
  Copiamos el contenido de un arreglo
*/
void copyArray(Type *t, string dst_addr, string src_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  ArrayType *at = (ArrayType*) t;
  string type, src_addr_aux, dst_addr_aux, typesize_addr;
  
  // Obtenemos el tipo interno
  t = at->type;

  if (at->size->addr.back() == ']') {
    typesize_addr = tac->newTemp();
    tac->gen("assignw " + typesize_addr + " " + at->size->addr);
  }
  else {
    typesize_addr = at->size->addr;
  }

  if (dst_addr.back() == ']') {
    dst_addr_aux = tac->newTemp();
    tac->gen("assign " + dst_addr_aux + " " + dst_addr);
  }
  else {
    dst_addr_aux = dst_addr;
  }

  // Obtenemos la longitud del hiper arreglo y lo reservamos
  string size_addr = tac->newTemp();
  tac->gen("assignw " + size_addr + " " + to_string(t->width));
  tac->gen("mult " + size_addr + " " + size_addr + " " + typesize_addr);
  tac->gen("malloc " + dst_addr_aux + " " + size_addr);

  if (dst_addr.back() == ']') {
    tac->gen("assignw " + dst_addr + "[0] " + dst_addr_aux);
  }

  // Si el tipo base del hiper arreglo no es primitivo ni puntero, es decir, es una
  // estructura, hay que reservar y copiar la memoria de cada uno explicitamente.
  type = t->toString();

  if (src_addr.back() == ']') {
    src_addr_aux = tac->newTemp();
    tac->gen("assignw " + src_addr_aux + " " + src_addr);
  }
  else {
    src_addr_aux = src_addr;
  }

  if (type.back() == ']' || (! predefinedTypes.count(type) && type[0] != '^')) {

    // Creamos un bucle en el que se reserva memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel(), size_addr_aux = tac->newTemp();
    tac->gen("assignw " + size_addr_aux + " " + size_addr);
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr_aux + " " + size_addr_aux + " " + to_string(t->width));
    tac->gen("lt test " + size_addr_aux + " 0");
    tac->gen("goif " + label + "_end test");

    if (type.back() == ']') {
      copyArray(t, dst_addr_aux + "[" + size_addr_aux + "]", src_addr_aux + "[" + size_addr_aux + "]");
    }
    else {
      copyStruct(t, dst_addr_aux + "[" + size_addr_aux + "]", src_addr_aux + "[" + size_addr_aux + "]");
    }

    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }

  // En caso contrario copiamos toda la memoria
  else {
    tac->gen("memcpy " + dst_addr_aux + " " + src_addr_aux + " " + size_addr);
  }
}

/* 
  Copiamos el contenido de una estructura de datos (union o registro).
*/
void copyStruct(Type *t, string dst_addr, string src_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  extern SymbolsTable *table;
  string src_addr_aux, dst_addr_aux;

  if (dst_addr.back() == ']') {
    dst_addr_aux = tac->newTemp();
    tac->gen("assignw " + dst_addr_aux + " " + dst_addr);
  }
  else {
    dst_addr_aux = dst_addr;
  }

  // Reservamos la memoria para la estructura completa
  tac->gen("malloc " + dst_addr + " " + to_string(t->width));

  if (dst_addr.back() == ']') {
    tac->gen("assignw " + dst_addr + "[0] " + dst_addr_aux);
  }

  if (src_addr.back() == ']') {
    src_addr_aux = tac->newTemp();
    tac->gen("assignw " + src_addr_aux + " " + src_addr);
  }
  else {
    src_addr_aux = src_addr;
  }
  tac->gen("memcpy " + dst_addr_aux + " " + src_addr_aux + " " + to_string(t->width));

  // Obtenemos el scope de definicion de la estructura.
  PrimitiveType *pt = (PrimitiveType*) t;
  StructureEntry *se = (StructureEntry*) table->lookup(pt->id);
  int scope = se->def_scope;

  // Si la estructura define algun campo.
  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type, offset;

    // Por cada campo de la estructura.
    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();
      offset = to_string(ve->offset);

      // Reservamos la memoria necesaria para los campos que son arreglos.
      if (type.back() == ']') {
        copyArray(ve->type, dst_addr_aux + "[" + offset + "]", src_addr_aux + "[" + offset + "]");
      }
      // Y para los campos que son otras estructuras.
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        copyStruct(ve->type, dst_addr_aux + "[" + offset + "]", src_addr_aux + "[" + offset + "]");
      }
    }
  }
}



/* 
  Libera memoria para un arreglo.
*/
void freeArray(Type *t, string final_addr) {
  extern TAC *tac;
  extern map<string, Type*> predefinedTypes;
  ArrayType *at = (ArrayType*) t;
  string type, final_addr_aux;

  // Si el arreglo corresponde a un string, no hay que hacer nada.
  if (at->is_string) {
    return;
  }
  
  // Obtenemos el tipo interno
  t = at->type;

  if (final_addr.back() == ']') {
    final_addr_aux = tac->newTemp();
    tac->gen("assignw " + final_addr_aux + " " + final_addr);
  }
  else {
    final_addr_aux = final_addr;
  }

  // Si el tipo base del hiper arreglo no es primitivo ni puntero, es decir, es una
  // estructura, hay que liberar la memoria de cada uno explicitamente.
  type = t->toString();
  if (type.back() == ']' || (! predefinedTypes.count(type) && type[0] != '^')) {
    string typesize_addr;
    if (at->size->addr.back() == ']') {
      typesize_addr = tac->newTemp();
      tac->gen("assignw " + typesize_addr + " " + at->size->addr);
    }
    else {
      typesize_addr = at->size->addr;
    }

    // Obtenemos la longitud del hiper arreglo.
    string size_addr = tac->newTemp();
    tac->gen("assignw " + size_addr + " " + to_string(t->width));
    tac->gen("mult " + size_addr + " " + size_addr + " " + typesize_addr);

    // Creamos un bucle en el que se reserva memoria para cada elemento del hiper arreglo.
    string label = tac->newLabel();
    tac->gen("@label " + label);
    tac->gen("sub " + size_addr + " " + size_addr + " " + to_string(t->width));
    tac->gen("lt test " + size_addr + " 0");
    tac->gen("goif " + label + "_end test");

    if (type.back() == ']') {
      freeArray(t, final_addr_aux + "[" + size_addr + "]");
    }
    else {
      freeStruct(t, final_addr_aux + "[" + size_addr + "]");
    }

    tac->gen("goto " + label);
    tac->gen("@label " + label + "_end");
  }

  // Liberamos la memoria total
  tac->gen("free " + final_addr_aux);
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

  string final_addr_aux;

  if (final_addr.back() == ']') {
    final_addr_aux = tac->newTemp();
    tac->gen("assignw " + final_addr_aux + " " + final_addr);
  }
  else {
    final_addr_aux = final_addr;
  }

  // Si la estructura define algun campo.
  if (table->scopeEntries.count(scope)) {
    VarEntry *ve;
    string type;

    // Por cada campo de la estructura.
    for (Entry *e : table->scopeEntries[scope]) {
      ve = (VarEntry*) e;
      type = ve->type->toString();

      // Liberamos la memoria necesaria para los campos que son arreglos.
      if (type.back() == ']') {
        freeArray(ve->type, final_addr_aux + "[" + to_string(ve->offset) + "]");
      }
      // Y para los campos que son otras estructuras.
      else if (! predefinedTypes.count(type) && type[0] != '^') {
        freeStruct(ve->type, final_addr_aux + "[" + to_string(ve->offset) + "]");
      }
    }
  }

  // Liberamos la memoria de la estructura completa
  tac->gen("free " + final_addr_aux);
}

