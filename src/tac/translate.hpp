#pragma once

#include <iostream>
#include <string>

#include <vector>
#include <map>
#include <unordered_map>

#include <algorithm>

using namespace std;

const unsigned NUMBER_OF_REGISTERS = 23;

// TODAVIA FALTAN MUCHAS INSTRUCCIONES
const unordered_map<string, string> mips_instructions ({
    {"assign", "move"},
    {"add", "add"},
    {"sub", "sub"},
    {"mult", "mul"},
    {"div", "div"}, // Esta en el low
    {"mod", "div"}, // Esta en el high
    {"minus", "negu"},
    {"and", "and"},
    {"or", "or"},
    {"not", "not"},
    {"goto", "b"},
    {"goif", "bnez"},
    {"goifnot", "bez"},
    {"param", "sw"},
    {"call", "jal"},
    {"@string", ".asciiz"}
});

struct T_Instruction
{
    string id;
    string result;
    string operands[2];
};

class T_Block
{
private:
    vector<T_Instruction> m_instructions;
    unordered_map<string, vector<string>> m_registers;
    unordered_map<string, vector<string>> m_variables;
    vector<string> data;
    vector<string> text;
    vector<string> functions;
    
    // Funciones para descriptores
    bool insertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace = false);
    void removeElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string current_container);
    string findElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element);
    string findOptimalLocation(vector<string> const &descriptor);
    
    // Funciones para manejar registros
    vector<string> getReg(T_Instruction instruction, bool is_copy = false);
    vector<string> findFreeRegister();
    string recycleRegister(T_Instruction instruction);
    void selectRegister(string operand, T_Instruction instruction, vector<string> &regs, vector<string> &free_regs);
    
    // Funciones para actualizar descriptores
    bool assignment(string register_id, string variable_id, bool replace = false);
    bool availability(string variable_id, string location, bool replace = false);

    // Funciones para instrucciones
    void translateInstruction(T_Instruction instruction);
    void translateMetaIntruction(T_Instruction instruction);
    void translateOperationInstruction(T_Instruction instruction);

public:
    T_Block();
    void translate();
    bool insertRegister(string id);
    bool insertVariable(string id);
    void insertInstruction(T_Instruction instruction);
    vector<string> getRegisterDescriptor(string id);
    vector<string> getVariableDescriptor(string id);
    void print();
};
