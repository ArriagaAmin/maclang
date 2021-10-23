#include <vector>
#include <tuple>
#include <string>
#include <iostream>

using namespace std;

class Quad
{
public:
    Quad(string instr, string result="", string arg1="", string arg2="");
    void print();

    string instr;
    string result;
    string arg1;
    string arg2;
};

class TAC
{
private:
    vector<Quad> instructions;
    unsigned long long currentTemporalNumber = 0;
public:
    TAC() { }
    string newTemp();
    string gen(string instr, string result="", string arg1="", string arg2="");
    void print();
};

