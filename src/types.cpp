#include "types.hpp"

// Esta variable representa un grafo que verifica la correctitud de los tipos para las
// distintas operaciones.
map<string, map<pair<string, string>, Type*>> binaryOpGraph;
map<string, map<string, Type*>> unaryOpGraph;

void createTypeGraph(void) {
  // Creamos los grafos para la verificacion de tipos.

  // Equivalencias.
  binaryOpGraph["=="] = {
    {{"Bool", "Bool"},    predefinedTypes["Bool"]},
    {{"Chat", "Chat"},    predefinedTypes["Bool"]},
    {{"Int", "Int"},      predefinedTypes["Bool"]},
    {{"Float", "Float"},  predefinedTypes["Bool"]},
    {{"Int", "Float"},    predefinedTypes["Bool"]},
    {{"Float", "Int"},    predefinedTypes["Bool"]}
  };
  binaryOpGraph["!="] = binaryOpGraph["=="];

  // Operaciones booleanas.
  binaryOpGraph["||"] = {
    {{"Bool", "Bool"}, predefinedTypes["Bool"]}
  };
  binaryOpGraph["&&"] = binaryOpGraph["||"];

  // Comparacion numerica,
  binaryOpGraph["<"]  = {
    {{"Int", "Int"},      predefinedTypes["Bool"]},
    {{"Float", "Float"},  predefinedTypes["Bool"]},
    {{"Int", "Float"},    predefinedTypes["Bool"]},
    {{"Float", "Int"},    predefinedTypes["Bool"]}
  };
  binaryOpGraph["<="] = binaryOpGraph["<"];
  binaryOpGraph[">"]  = binaryOpGraph["<"];
  binaryOpGraph[">="] = binaryOpGraph["<"];

  // Operaciones aritmeticas
  binaryOpGraph["+"]  = {
    {{"Int", "Int"},      predefinedTypes["Int"]},
    {{"Float", "Float"},  predefinedTypes["Float"]},
    {{"Int", "Float"},    predefinedTypes["Float"]},
    {{"Float", "Int"},    predefinedTypes["Float"]}
  };
  binaryOpGraph["-"] = binaryOpGraph["+"];
  binaryOpGraph["*"] = binaryOpGraph["+"];
  binaryOpGraph["/"] = binaryOpGraph["+"];
  binaryOpGraph["%"] = binaryOpGraph["+"];
  binaryOpGraph["**"] = binaryOpGraph["+"];

  // Operaciones unarias
  unaryOpGraph["!"] = {
    {"Bool", predefinedTypes["Bool"]}
  };
  unaryOpGraph["+"] = {
    {"Int",   predefinedTypes["Int"]},
    {"Float", predefinedTypes["Float"]}
  };
  unaryOpGraph["-"] = unaryOpGraph["+"];
}

/*
  Verfiy that an operand have the correct type for a unary operator.
*/
Type *verifyUnaryOpType(string op, string type) {
  if (type == "$Error") {
    return predefinedTypes["$Error"];
  } 
  else if (unaryOpGraph[op].count(type) == 0) {
     addError(
      (string) "Operator '\e[1;3m" + op + "\e[0m' can't be applied with operand type " +
      "'\e[1;3m" + type + "\e[0m'."
    );
    return predefinedTypes["$Error"];
  } else {
    return unaryOpGraph[op][type];
  }

}

/*
  Verifies that a pair of operators have the correct types for a binary operator.
*/
Type *verifyBinayOpType(string op, string type1, string type2) {
  // Verifies if one of the operands has error type.
  if (type1 == "$Error" || type2 == "$Error") {
    return predefinedTypes["$Error"];
  } 
  // Verificamos que la operacion acepta el par de tipos.
  else if (binaryOpGraph[op].count({type1, type2}) == 0){
    addError(
      "Operator '\e[1;3m" + op + "\e[0m' don't matches with operand types: '\e[1;3m" +
      type1 + "\e[0m' and '\e[1;3m" + type2 + "\e[0m'."
    );
    return predefinedTypes["$Error"];
  }
  // Obtenemos el tipo correspondiente a la operacion.
  else {
    return binaryOpGraph[op][{type1, type2}];
  }
}