#pragma once 

#include <map>
#include <set>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct T_Instruction
{
    string id;
    string result;
    vector<string> operands;
};

struct T_Function
{
    string name;
    uint64_t id;
    uint64_t size;
    vector<T_Instruction> instructions;
    map<string, uint64_t> labels2instr;
    set<string> labels_leaders;
    set<uint64_t> leaders = {0};
    vector<uint64_t> vec_leaders;
};

class FlowNode {
    public:
        // Identificador del bloque.
        uint64_t id;
        // Indica si es el bloque inicial de una funcion.
        bool is_function;
        // En caso de ser asi, obtenemos el ID y la memoria necesaria de la funcion.
        uint64_t function_id;
        uint64_t function_size;
        vector<T_Instruction> block = {};

        FlowNode(uint64_t id, uint64_t leader, T_Function *function, bool is_function);
        string getName(void);
        void print(void);
        void prettyPrint(void);
};

class FlowGraph {
    public:
        // G = (V,E)
        map<uint64_t, FlowNode*> V;
        map<uint64_t, set<uint64_t>> E;
        // Arcos inversos
        map<uint64_t, set<uint64_t>> Einv;

        FlowGraph(vector<T_Function*> functions);

        void insertArc(uint64_t u, uint64_t v);
        uint64_t makeSubGraph(T_Function *function, uint64_t init_id);
        void print(void);
        void prettyPrint(void);
};
