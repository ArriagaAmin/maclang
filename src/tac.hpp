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
    vector<pair<string, unsigned long long>> address;

public:
    vector<string> instructions;
    
    TAC() { }
    string newTemp();
    string newLabel();
    string newAddr(unsigned long long bytes);
    string replaceAll(string text, string to_find, string to_replace);
    void gen(string instr);
    void backpatch(vector<unsigned long long> ps, unsigned long long l);
    void print(void);
};

template <typename T>
vector<T> merge(vector<T> v1, vector<T> v2) {
    vector<T> v(v1);
    v.insert(v.end(), v2.begin(), v2.end());
    return v;
}