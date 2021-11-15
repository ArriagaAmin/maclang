#pragma once

#include <string>
#include <map>
#include <set>

#include "ast.hpp"
#include "errors.hpp"

using namespace std;

// Predefined Types 
extern map<string, Type*> predefinedTypes;

void createTypeGraph(void);

bool typecmp(string t1, string t2);

// verifies types for a binary operator
Type *verifyBinayOpType(string op, string type1, string type2);

// verifies type for a unary operator
Type *verifyUnaryOpType(string op, string type);