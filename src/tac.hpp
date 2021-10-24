#include <vector>
#include <tuple>
#include <string>
#include <iostream>

using namespace std;

class TAC
{
private:
    unsigned long long tempVarNumber = 0;
    unsigned long long tempLabelNumber = 0;

public:
    vector<string> instructions;
    
    TAC() { }
    string newTemp();
    string newLabel();
    void gen(string instr);
    string replace(string text, string to_find, string to_replace);
    void backpatch(vector<unsigned long long> ps, unsigned long long l);
    void print(void);
};

