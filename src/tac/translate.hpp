#pragma once

#include <iostream>
#include <string>

#include <vector>
#include <map>
#include <unordered_map>

#include <algorithm>
#include <iostream>
#include <ctype.h>

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
    {"assignw", "move"},
    {"assignb", "move"},
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
    {"byte", ".byte"}
});

/*
malloc ID Rval
memcpy ID ID int
free rval
exit rval
printi
printf
print
printc
read
readi
readf
readc
@fun_begin ID SIZE
@fun_end SIZE
li
la
syscall
    */

struct T_Instruction
{
    string id;
    string result;
    vector<string> operands;
};

class T_Block
{
private:
    vector<T_Instruction*> m_instructions;
    unordered_map<string, vector<string>> m_registers;
    unordered_map<string, vector<string>> m_variables;
    vector<string> data;
    vector<string> text;
    
    // Funciones para descriptores
    bool insertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace = false);
    void removeElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string current_container);
    string findElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element);
    string findOptimalLocation(string id);
    
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
    void translateArithmeticOperation(T_Instruction instruction);
    void translateLogicalOperation(T_Instruction instruction);
    void translateOperationInstruction(T_Instruction instruction, bool is_copy = false);

public:
    T_Block();
    void translate();
    bool insertRegister(string id);
    bool insertVariable(string id);
    void insertInstruction(T_Instruction* instruction);
    vector<string> getRegisterDescriptor(string id);
    vector<string> getVariableDescriptor(string id);
    void print();
    void printVariablesDescriptors();
};
