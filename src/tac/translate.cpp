#include "translate.hpp"

CodeBlock::CodeBlock()
{
    // Agregar los registros de MIPS
    InsertRegister("$v0");
    InsertRegister("$v1");

    int i = 0;
    while (i < 3)
    {   
        InsertRegister("$a" + to_string(i));
        i++;
    }

    i = 0;
    
    while (i < 10)
    {   
        InsertRegister("$t" + to_string(i));
        i++;
    }

    i = 0;
    
    while (i < 8)
    {   
        InsertRegister("$s" + to_string(i));
        i++;
    }
}

bool CodeBlock::InsertRegister(string reg)
{
    auto found = registersDescriptor.find(reg);

    if(found == registersDescriptor.end()) 
        return false;
    
    registersDescriptor[reg] = vector<string>();
    return true;
}

bool CodeBlock::InsertVariable(string var)
{
    auto found = variablesDescriptor.find(var);

    if(found == variablesDescriptor.end()) 
        return false;
    
    vector<string> locations {var};
    variablesDescriptor[var] = locations;
    return true;
}

bool CodeBlock::InsertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace = false)
{
    auto found = descriptors.find(key);

    if(found == descriptors.end()) 
        return false;
    
    if(replace)
        descriptors[key].clear();

    descriptors[key].push_back(element);
    return true;
}

void CodeBlock::RemoveElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string elementHolder)
{
    unordered_map<string, vector<string>>::iterator it = descriptors.begin();
    
    for (pair<string, vector<string>> currentDescriptor : descriptors) 
    {
        if(currentDescriptor.first.compare(elementHolder))
            continue;
        
        vector<string> currentElements = currentDescriptor.second;
        remove(currentElements.begin(), currentElements.end(), element);
    }
}


bool CodeBlock::Assignment(string reg, string var, bool replace)
{
    return InsertElementToDescriptor(registersDescriptor, reg, var, replace);
}

bool CodeBlock::Availability(string var, string location, bool replace)
{
    return InsertElementToDescriptor(variablesDescriptor, var, location, replace);
}

vector<string> CodeBlock::GetRegisterDescriptor(string key)
{
    return registersDescriptor[key];
}

vector<string> CodeBlock::GetVariableDescriptor(string key)
{
    return variablesDescriptor[key];
}

string CodeBlock::FindOptimalLocation(vector<string> const &descriptor)
{
    // Por ahora solamente devolver el primero
    return descriptor[0];
}

vector<string> GetReg(string instruction);

void CodeBlock::Translate(string instruction)
{
    // Por ahora simplemente se hara un esbozo de los tipos de traducciones
    
    /* ---------- Operaciones generales x := y + z ----------- */
    // Placeholders
    string result = "x";
    string op1 = "y";
    string op2 = "z";
    vector<string> currentRegisters = GetReg(instruction);

    // Verificamos para el primer operador
    string firstRegister = currentRegisters[1];
    vector<string> firstRegDescriptor = GetRegisterDescriptor(firstRegister);
    if ( find(firstRegDescriptor.begin(), firstRegDescriptor.end(), op1) == firstRegDescriptor.end() )
    {
        // Buscar el y' mas economico
        string econLocation = FindOptimalLocation(GetVariableDescriptor(op1));
        instructions.push_back("lw " + firstRegister + ", " + econLocation);

        // Mantener descriptores
        Assignment(firstRegister, op1, true);
        Availability(op1, firstRegister);
    }

    // Verificamos para el segundo operador
    string secondRegister = currentRegisters[2];
    vector<string> secondRegDescriptor = GetRegisterDescriptor(secondRegister);
    if ( find(secondRegDescriptor.begin(), secondRegDescriptor.end(), op2) == secondRegDescriptor.end() )
    {
        // Buscar el z' mas economico
        string econLocation = FindOptimalLocation(GetVariableDescriptor(op2));
        instructions.push_back("lw " + secondRegister + ", " + econLocation);

        // Mantener descriptores
        Assignment(secondRegister, op2, true);
        Availability(op2, secondRegister);
    }

    // Emitir codigo dependiendo del operador
    instructions.push_back("add " + currentRegisters[0] + ", " + firstRegister + ", " + secondRegister);

    // Mantener descriptor
    Assignment(currentRegisters[0], result, true);
    Availability(result, currentRegisters[0], true);
    RemoveElementFromDescriptors(variablesDescriptor, currentRegisters[0], result);

    /* ---------- Operaciones de copia x := y ----------- */
    op1 = "y";
    vector<string> currentRegisters = GetReg(instruction);
    string copyRegister = currentRegisters[1];
    vector<string> copyDescriptor = GetRegisterDescriptor(copyRegister);
    if ( find(copyDescriptor.begin(), copyDescriptor.end(), op1) == firstRegDescriptor.end() )
    {
        // Buscar el y' mas economico
        string econLocation = FindOptimalLocation(GetVariableDescriptor(op1));
        instructions.push_back("lw " + firstRegister + ", " + econLocation);

        // Mantener descriptores
        Assignment(copyRegister, op1, true);
        Availability(op1, copyRegister);

        Assignment(copyRegister, result);
        Availability(result, copyRegister, true);
    }


}