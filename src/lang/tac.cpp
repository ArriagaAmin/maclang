#include "tac.hpp"

string TAC::newTemp()
{
    string temp = "T" + to_string(tempVarNumber);
    tempVarNumber++;
    return temp;
}

string TAC::newLabel()
{
    string temp = "L" + to_string(tempLabelNumber);
    tempLabelNumber++;
    return temp;
}

string TAC::newFunc()
{
    string temp = "F" + to_string(tempFuncNumber);
    tempFuncNumber++;
    return temp;
}

string TAC::newStr(string str)
{
    str.erase(0, 1);
    str.erase(str.size() - 1, 1);
    str = "0000" + str;
    string temp = "S" + to_string(this->strings.size());
    this->strings.push_back({temp, str});
    return temp;
}

string TAC::replaceAll(string text, string to_find, string to_replace) 
{
    std::string::size_type n = 0;
    while ( (n = text.find(to_find, n)) != std::string::npos ) {
        text.replace(n, to_find.size(), to_replace);
        n += to_replace.size();
    }
    return text;
}

void TAC::gen(string instr) 
{
    this->instructions.push_back(instr);
}

void TAC::backpatch(vector<unsigned long long> ps, unsigned long long l) {
    string instr = "B" + to_string(l);
    bool replace = false;
    for (unsigned long long i : ps) {
        this->instructions[i] = replaceAll(this->instructions[i], "_", instr);
        replace = true;
    }
    if (replace) {
        this->numberLabels.insert(l);
    }
}

void TAC::backpatch(vector<unsigned long long> ps, string l) {
    for (unsigned long long i : ps) {
        this->instructions[i] = replaceAll(this->instructions[i], "_", l);
    }
}

void TAC::print(void) {
    unsigned long long index = 0;

    for (pair<string, string> str : this->strings) {
        cout << "@string " << str.first << " \"" << str.second << "\"\n";
    }

    for (string instr : this->instructions) {
        if (this->numberLabels.count(index) != 0) {
            cout << "@label B" << index << "\n";
        }
        cout << instr << "\n";
        index++;
    }
    
    if (this->numberLabels.count(index) != 0) {
        cout << "@label B" << index << "\n";
    }
}

void TAC::genTACinstr(string assign, string instr, string addrl, string addr1, string addr2) {
    string addr1_aux, addr2_aux;

    if (addr1.back() == ']') {
        addr1_aux = this->newTemp();
        this->gen(assign + " " + addr1_aux + " " + addr1);
    }
    else {
        addr1_aux = addr1;
    }
    if (addr2.back() == ']') {
        addr2_aux = this->newTemp();
        this->gen(assign + " " + addr2_aux + " " + addr2);
    }
    else {
        addr2_aux = addr2;
    }
    this->gen(instr + " " + addrl + " " + addr1_aux + " " + addr2_aux);
}