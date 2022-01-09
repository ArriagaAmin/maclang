#pragma once

#include <string>
#include <stack>

#include "ast.hpp"
#include "table.hpp"
#include "tac.hpp"
#include "errors.hpp"

using namespace std;

// Predefined Types 
extern map<string, Type*> predefinedTypes;

// Funciones para reservar memoria de tipos compuestas.
void allocArray(Type *t, string final_addr);

void allocStruct(Type *t, string final_addr);

// Funciones para copiar tipos compuestos.
void copyArray(Type *t, string dst_addr, string src_addr);

void copyStruct(Type *t, string dst_addr, string src_addr);

// Funciones para liberar memoria para tipos compuestos 
void freeArray(Type *t, string final_addr);

void freeStruct(Type *t, string final_addr);

