#include "tac.hpp"

string TAC::newTemp()
{
    string temp = "T" + to_string(currentTemporalNumber);
    temporals.push_back(temp);
    currentTemporalNumber++;
    return temp;
}

void TAC::gen(
    string currentOp,
    string currentArg1, 
    string currentArg2 )
{
    string temp = newTemp();
    Quad newInstruction(currentOp, currentArg1, currentArg2, temp);
    instructions.push_back(newInstruction);
}

void TAC::print()
{
    for (Quad instruction : instructions)
    {
        instruction.print();
    }
}

Quad::Quad(string op, string arg1, string arg2, string result)
{
    this->op = op;
    this->arg1 = arg1;
    this->arg2 = arg2;
    this->result = result;
}

void Quad::print()
{
    cout << result << " := " << arg1 << " " << op << " " << arg2 << endl;
}