#pragma once

#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <stack>
#include <map>
#include <set>

#include "ast.hpp"

using namespace std;

class TAC
{
private:
    unsigned long long tempVarNumber = 0;
    unsigned long long tempLabelNumber = 0;
    unsigned long long tempFuncNumber = 0;
    vector<pair<string, string>> strings;
    set<unsigned long long> numberLabels;

public:
    vector<string> instructions;
    // Mapeo de nombre de funciones a una lista de pares 
    // <
    //      Instruccion donde se hizo la llamada a funcion, 
    //      copia del scope stack en el momento en que se realizo la llamada
    // >
    map< string, vector<pair<unsigned long long, vector<int>>> > functionlist;
    // Pila de listas de instrucciones que necesitan ser parcheadas
    stack<vector<unsigned long long>> breaklist;
    stack<vector<unsigned long long>> continuelist;
    
    TAC() { }
    string newTemp();
    string newLabel();
    string newFunc();
    string newStr(string str);
    string replaceAll(string text, string to_find, string to_replace);
    void gen(string instr);
    void backpatch(vector<unsigned long long> ps, unsigned long long l);
    void backpatch(vector<unsigned long long> ps, string l);
    void print(void);
    void genTACinstr(string assign, string instr, string addrl, string addr1, string addr2);
};

template <typename T>
vector<T> merge(vector<T> v1, vector<T> v2) {
    vector<T> v(v1);
    v.insert(v.end(), v2.begin(), v2.end());
    return v;
}