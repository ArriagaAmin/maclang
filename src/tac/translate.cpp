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

bool CodeBlock::InsertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace)
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

string CodeBlock::FindElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element)
{   
    for (pair<string, vector<string>> currentDescriptor : descriptors) 
    {
        vector<string> currentElements = currentDescriptor.second;
        if( find(currentElements.begin(), currentElements.end(), element) != currentElements.end())
            return currentDescriptor.first;
    }

    return "";
}

string CodeBlock::FindFreeRegister()
{
    
    for (pair<string, vector<string>> currentRegister : registersDescriptor) 
    {
        if(currentRegister.second.empty())
            return currentRegister.first;
    }

    return "";
}

string CodeBlock::RecycleRegister(T_Instruction instruction)
{
    // Vamos a recorrer todos los registros e ir verificando cual es el mas viable
    // para reciclar y utilizarlo

    string bestReg = "";

    // Contadores de spills
    map<string, int> spills;
    
    for (pair<string, vector<string>> currentRegister : registersDescriptor) 
    {
        //bool isSafe = false;
        int currentSpills = 0;

        vector<string> descriptor = currentRegister.second;

        for(string element : descriptor)
        {
            // Primero se verifica que el valor actual este en algun otro lado
            if(variablesDescriptor[element].size() > 1)
                // Es seguro el registro
                continue;
            
            // Verificar que el valor actual sea el resultado y si lo es que no sea operando
            if(element.compare(instruction.result) && 
                find(instruction.operators.begin(), instruction.operators.end(), element) != instruction.operators.end())
                // Es seguro el registro
                continue;

            // Verificar que el valor actual no tenga usos posteriores

            // Si aun este registro no es seguro
            text.push_back("sw " + element + ", " + currentRegister.first);

            // Mantener descriptores
            Availability(element, element);
            
            currentSpills += 1;
        }

        spills[currentRegister.first] = currentSpills;
    }

    // Ahora se verifica cual registro tiene el menor numero de spills
    int current = INT32_MAX;
    
    for (pair<string, int> currentRegister : spills) 
    {
        if(currentRegister.second < current)
            bestReg = currentRegister.first;
    }

    return bestReg;
}

vector<string> CodeBlock::GetReg(T_Instruction instruction, bool isCopy)
{
    vector<string> registers;

    // AGREGAR BUSCAR REGISTRO PARA GOIF Y GOIFNOT

    // AGREGAR FUNCIONES

    for (string currentOp : instruction.operators)
    {
        // Primero se verifica que el operando este guardada en algun registro
        string reg = FindElementInDescriptors(registersDescriptor, currentOp);
        if(!reg.empty())
        {
            registers.push_back(reg);
            continue;
        }
        
        // Si no estaba en un registro verificamos si hay registros libres
        reg = FindFreeRegister();

        if(!reg.empty())
        {
            registers.push_back(reg);
            continue;
        }
        
        // Si no se cumple nada los casos simples, pasamos a los casos complejos
        // No hay registros disponibles y el operando no esta en ninguno
        reg = RecycleRegister(instruction);
        registers.push_back(reg);
    }
    
    bool resultRegAdded = false;

    // Ahora se escoge el registro para el resultado
    if(isCopy)
    {
        string resultReg = registers[0];
        registers.insert(registers.begin(), resultReg);
        resultRegAdded = true;
    }

    if(!resultRegAdded)
    {
        // Buscar registro que SOLO contenga al resultado
        string reg = FindElementInDescriptors(registersDescriptor, instruction.result);
        if(!reg.empty())
        {
            if(GetRegisterDescriptor(reg).size() < 2)
            {
                registers.insert(registers.begin(), reg);
                resultRegAdded = true;
            }
        }
    }

    // Si los operandos no tienen usos posteriores se usa alguno de esos registros
    
    return registers;
}

void CodeBlock::Translate(T_Instruction instruction)
{
    // Verificamos primero si es una meta instruccion para procesarla
    if(instruction.name[0] == '@')
    {
        TranslateMetaIntruction(instruction);
        return;
    }

    // Instrucciones de branch
    if(instruction.name[0] == 'g')
    {
        if(instruction.name.compare("goto"))
        {
            if(instruction.name.find("_out") != std::string::npos)
                return;
            
            text.push_back(instTypes[instruction.name] + " " + instruction.result);
        }
        else
        {
            vector<string> reg = GetReg(instruction);
            text.push_back(instTypes[instruction.name] + " " + reg[0] + ", " + instruction.result);
        }
        return;
    }

    // Instrucciones para llamada de funciones
    if(instruction.name.compare("param"))
    {
        vector<string> reg = GetReg(instruction);
        text.push_back(instTypes[instruction.name] + " " + reg[0] + ", 0($sp)");
        text.push_back("addi $sp, $sp, -4"); // El tamano depende de lo que se le este pasando
        return;
    }

    if(instruction.name.compare("call"))
    {
        // Falta usar el numero de parametros
        text.push_back(instTypes[instruction.name] + instruction.result);
        return;
    }

    // Instrucciones para funciones

    // Instrucciones de operadores
    TranslateOperationInstruction(instruction);
}

void CodeBlock::TranslateOperationInstruction(T_Instruction instruction)
{
        // Verificamos si es una instruccion de copia para luego actualizar los descriptores
    bool isCopy = instruction.name.compare("assign") ? true : false;
    
    vector<string> opRegisters = GetReg(instruction, isCopy);
    int opIndex = 1;

    for (string currentOp : instruction.operators)
    {
        // Verificamos el operando
        string currentReg = opRegisters[opIndex];
        vector<string> regDescriptor = GetRegisterDescriptor(currentReg);
        if ( find(regDescriptor.begin(), regDescriptor.end(), currentOp) != regDescriptor.end() )
        {
            // Buscar el y' mas economico
            string econLocation = FindOptimalLocation(GetVariableDescriptor(currentOp));
            text.push_back("lw " + currentReg + ", " + econLocation);

            // Mantener descriptores
            Assignment(currentReg, currentOp, true);
            Availability(currentOp, currentReg);

            if(isCopy)
            {
                Assignment(currentReg, instruction.result);
                Availability(instruction.result, currentReg, true);
            }
        }    
        opIndex++;
    }

    // Emitir codigo dependiendo del operador
    string emit = instTypes[instruction.name] + " ";
    for (string reg : opRegisters)
    {
        emit += reg + ", ";
    }
    text.push_back(emit);

    // Mantener descriptor
    Assignment(opRegisters[0], instruction.result, true);
    Availability(instruction.result, opRegisters[0], true);
    RemoveElementFromDescriptors(variablesDescriptor, opRegisters[0], instruction.result);
}

void CodeBlock::TranslateMetaIntruction(T_Instruction instruction)
{
    if(instruction.name.compare("@label"))
    {
        text.push_back(instruction.result + ": ");
        return;
    }

    if(instruction.name.compare("@string"))
    {
        string instructionType = instTypes[instruction.name];
        data.push_back(instruction.result + ": " + instructionType + " " + instruction.operators[0]);
        return;
    }
    
    if(instruction.name.compare("@staticv"))
    {
        data.push_back(instruction.result + ": " + instruction.operators[0]);
        return;
    }
}