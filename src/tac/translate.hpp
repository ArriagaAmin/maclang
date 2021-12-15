#pragma once

#include <map>
#include <string>
#include <vector>
#include <ctype.h>
#include <iostream>
#include <algorithm>
#include <unordered_map>

#include "FlowGraph.hpp"

using namespace std;

const string space = "  ";
const string sep = ", ";
const string decl = ": ";

const unordered_map<string, string> mips_instructions ({
    // Operaciones aritmeticas
    {"add", "add"},
    {"sub", "sub"},
    {"mult", "mul"},
    {"div", "div"}, // Esta en el low
    {"mod", "div"}, // Esta en el high
    {"minus", "negu"},

    //Operaciones logicas
    {"not", "not"},
    {"and", "and"},
    {"or", "or"},
    {"eq", "beq"},
    {"neq", "bne"},
    {"geq", "bge"},
    {"gt", "bgt"},
    {"leq", "ble"},
    {"lt", "blt"},

    // Saltos y accesos a memoria
    {"goto", "j"},
    {"assign", "move"},
    {"goif", "bnez"},
    {"goifnot", "bez"},
    {"param", "sw"},
    {"call", "jal"},
    {"return", "jr"},
    {"low", "mflow"},
    {"high", "mfhi"},
    {"load", "lw"},
    {"store", "sw"},

    // Registros especiales
    {"ra", "$ra"},
    {"sp", "$sp"},
    {"zero", "$zero"},

    // .Data
    {"@string", ".asciiz"},
    {"word", ".word"},
    {"byte", ".byte"},

    // Syscalls
    {"exit", "li  $v0, 10 \nsyscall"},
    {"printi", "li  $v0, 1 \nsyscall"},
    {"printf", "li  $v0, 2 \nsyscall"},
    {"printc", "li  $v0, 11 \nsyscall"},
    {"print", "li  $v0, 4 \nsyscall"},
    {"readi", "li  $v0, 5 \nsyscall"},
    {"readf", "li  $v0, 6 \nsyscall"},
    {"readc", "li  $v0, 12 \nsyscall"},
    {"read", "li  $v0, 8 \nsyscall"}

});

/*
malloc ID Rval
memcpy ID ID int
free rval
*/

class Translator
{
private:
    vector<T_Instruction*> m_data_instructions;
    FlowGraph* m_graph;
    unordered_map<string, vector<string>> m_registers;
    unordered_map<string, vector<string>> m_variables;
    vector<string> data;
    vector<string> text;
    vector<string> functions;
    
    // Funciones para descriptores
    bool insertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace = false);
    void removeElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string current_container);
    string findElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element);
    string findOptimalLocation(string id);
    
    // Funciones para manejar registros
    vector<string> getReg(T_Instruction instruction, vector<string>& section, bool is_copy = false);
    vector<string> findFreeRegister();
    string recycleRegister(T_Instruction instruction, vector<string>& section);
    void selectRegister(string operand, T_Instruction instruction, vector<string> &regs, vector<string> &free_regs, vector<string>& section);
    void cleanRegistersDescriptor();
    
    // Funciones para actualizar descriptores
    bool assignment(string register_id, string variable_id, bool replace = false);
    bool availability(string variable_id, string location, bool replace = false);

    // Funciones para instrucciones
    void translateInstruction(T_Instruction instruction, vector<string>& section);
    void translateMetaIntruction(T_Instruction instruction);
    void translateOperationInstruction(T_Instruction instruction, vector<string>& section, bool is_copy = false, uint16_t type = 0);
    void translateIOIntruction(T_Instruction instruction, vector<string>& section);
public:
    Translator();
    void translate();
    bool insertRegister(string id);
    bool insertVariable(string id, uint16_t type, string value = "1");
    void insertInstruction(T_Instruction* instruction);
    void insertFlowGraph(FlowGraph* graph);
    vector<string> getRegisterDescriptor(string id);
    vector<string> getVariableDescriptor(string id);
    void print();
    void printVariablesDescriptors();
};
