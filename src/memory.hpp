#pragma once

#include <string>
#include <stack>

#include "ast.hpp"
#include "table.hpp"
#include "tac.hpp"

using namespace std;

// Funciones para reservar memoria para tipos compuestos 
void allocConstArray(Type *t, string final_addr);

void allocVarArray(Type *t, string final_addr);

void allocStruct(Type *t, string final_addr);

// Funciones para liberar memoria para tipos compuestos 
void freeConstArray(Type *t, string final_addr);

void freeVarArray(Type *t, string final_addr);

void freeStruct(Type *t, string final_addr);