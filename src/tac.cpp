#include "tac.hpp"

string TAC::newTemp()
{
    string temp = "T" + to_string(currentTemporalNumber);
    currentTemporalNumber++;
    return temp;
}

string TAC::gen(string instr, string result, string arg1, string arg2)
{
    Quad newInstruction(instr, result, arg1, arg2);
    instructions.push_back(newInstruction);
    return instr + " " + result + " " + arg1 + " " + arg2;
}

void TAC::print()
{
    for (Quad instruction : instructions)
    {
        instruction.print();
    }
}

Quad::Quad(string instr, string result, string arg1, string arg2)
{
    this->instr = instr;
    this->result = result;
    this->arg1 = arg1;
    this->arg2 = arg2;
}

void Quad::print()
{
    cout << instr << " " << result << " " << arg1 << " " << arg2 << endl;
}