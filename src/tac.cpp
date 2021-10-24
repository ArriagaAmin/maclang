#include "tac.hpp"

string TAC::newTemp()
{
    string temp = "T" + to_string(tempVarNumber);
    tempVarNumber++;
    return temp;
}

string TAC::newLabel()
{
    string temp = "Label" + to_string(tempLabelNumber);
    tempLabelNumber++;
    return temp;
}

void TAC::gen(string instr) 
{
    this->instructions.push_back(instr);
}

string TAC::replace(string text, string to_find, string to_replace) 
{
    std::string::size_type n = 0;
    while ( (n = text.find(to_find, n)) != std::string::npos ) {
        text.replace(n, to_find.size(), to_replace);
        n += to_replace.size();
    }
    return text;
}

void TAC::backpatch(vector<unsigned long long> ps, unsigned long long l) {
    string instr = to_string(l);
    for (unsigned long long i : ps) {
        this->instructions[i] = this->replace(this->instructions[i], "_", instr);
    }
}

void TAC::print(void) {
    unsigned long long index = 0;
    unsigned len = to_string(this->instructions.size()).size();

    for (string instr : this->instructions) {
        printf("%.*llu", len, index, ' ');
        cout << "│ " << instr << "\n";
        index++;
    }
    printf("%.*llu", len, index, ' ');
    cout << "│ " << "\n";
}