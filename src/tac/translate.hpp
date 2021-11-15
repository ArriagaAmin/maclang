#pragma once

#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const unsigned NUMBER_OF_REGISTERS = 23;

class CodeBlock
{
private:
    unordered_map<string, string> operators;
    unordered_map<string, vector<string>> registersDescriptor;
    unordered_map<string, vector<string>> variablesDescriptor;
    vector<string> instructions;

    bool InsertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace = false);
    void RemoveElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string elementHolder);
    string FindElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element);
    string FindFreeRegister();
    string RecycleRegister(string instruction);
public:
    CodeBlock();
    vector<string> GetReg(string instruction); // For now is a string but we need the reference to the structure parsed
    void Translate(string instruction); // For now is a string but we need the reference to the structure parsed
    bool InsertRegister(string reg);
    bool InsertVariable(string var);
    vector<string> GetRegisterDescriptor(string key);
    vector<string> GetVariableDescriptor(string key);
    string FindOptimalLocation(vector<string> const &descriptor);
    bool Assignment(string reg, string var, bool replace = false);
    bool Availability(string var, string location, bool replace = false);
};
