#pragma once

#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const unsigned NUMBER_OF_REGISTERS = 23;

// TODAVIA FALTAN MUCHAS INSTRUCCIONES
const unordered_map<string, string> instTypes = {
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
    {"goif", "beq"}, //Esto depende del if
    {"param", "sw"},
    {"call", "jal"}
};

struct T_Instruction
{
    string name;
    string result;
    vector<string> operators;
};

class CodeBlock
{
private:
    unordered_map<string, vector<string>> registersDescriptor;
    unordered_map<string, vector<string>> variablesDescriptor;
    vector<string> data;
    vector<string> text;

    bool InsertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace = false);
    void RemoveElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string elementHolder);
    string FindElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element);
    string FindFreeRegister();
    string RecycleRegister(T_Instruction instruction);
    
    vector<string> GetReg(T_Instruction instruction, bool isCopy);
    string FindOptimalLocation(vector<string> const &descriptor);
    bool Assignment(string reg, string var, bool replace = false);
    bool Availability(string var, string location, bool replace = false);
public:
    CodeBlock();
    void Translate(T_Instruction instruction);
    bool InsertRegister(string reg);
    bool InsertVariable(string var);
    vector<string> GetRegisterDescriptor(string key);
    vector<string> GetVariableDescriptor(string key);
};
