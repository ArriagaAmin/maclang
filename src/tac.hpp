#include <vector>
#include <tuple>
#include <string>
#include "ast.hpp"

using namespace std;

class TAC
{
private:
    vector<Quad> instructions;
    vector<string> temporals;
    int currentTemporalNumber = 1;
public:
    TAC() { }
    string newTemp();
    void gen(string currentOp, string currentArg1 = "", string currentArg2 = "");
    void print();
};

class Quad
{
public:
    Quad(string op, string arg1, string arg2, string result);
    void print();

    string op;
    string arg1;
    string arg2;
    string result;
};
