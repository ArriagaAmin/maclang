#include "translate.hpp"

T_Block::T_Block()
{
    // Agregar los registros de MIPS
    insertRegister("$v0");
    insertRegister("$v1");

    int i = 0;
    while (i < 3)
    {   
        insertRegister("$a" + to_string(i));
        i++;
    }

    i = 0;
    
    while (i < 10)
    {   
        insertRegister("$t" + to_string(i));
        i++;
    }

    i = 0;
    
    while (i < 8)
    {   
        insertRegister("$s" + to_string(i));
        i++;
    }
}

void T_Block::insertInstruction(T_Instruction instruction)
{
    m_instructions.push_back(instruction);
}

bool T_Block::insertRegister(string id)
{
    auto found = m_registers.find(id);

    if(found != m_registers.end()) 
        return false;
    
    m_registers[id] = vector<string>();
    return true;
}

bool T_Block::insertVariable(string id)
{
    auto found = m_variables.find(id);

    if(found != m_variables.end()) 
        return false;
    
    vector<string> locations { id };
    m_variables[id] = locations;
    return true;
}

void T_Block::print()
{
    for(string inst : data)
    {
        cout << inst << endl;
    }

    for(string inst : text)
    {
        cout << inst << endl;
    }

    for(string inst : functions)
    {
        cout << inst << endl;
    }
}

bool T_Block::insertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace)
{
    auto found = descriptors.find(key);

    if(found != descriptors.end()) 
        return false;
    
    if(replace)
        descriptors[key].clear();

    descriptors[key].push_back(element);
    return true;
}

void T_Block::removeElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string current_container)
{   
    for (pair<string, vector<string>> current_descriptor : descriptors) 
    {
        if(current_descriptor.first.compare(current_container) == 0)
            continue;
        
        vector<string> current_elements = current_descriptor.second;
        remove(current_elements.begin(), current_elements.end(), element);
    }
}


bool T_Block::assignment(string register_id, string variable_id, bool replace)
{
    return insertElementToDescriptor(m_registers, register_id, variable_id, replace);
}

bool T_Block::availability(string variable_id, string location, bool replace)
{
    return insertElementToDescriptor(m_variables, variable_id, location, replace);
}

vector<string> T_Block::getRegisterDescriptor(string id)
{
    return m_registers[id];
}

vector<string> T_Block::getVariableDescriptor(string id)
{
    return m_variables[id];
}

string T_Block::findOptimalLocation(vector<string> const &descriptor)
{
    // Por ahora solamente devolver el primero
    return descriptor[0];
}

string T_Block::findElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element)
{   
    for (pair<string, vector<string>> current_descriptor : descriptors) 
    {
        vector<string> current_elements = current_descriptor.second;
        if( find(current_elements.begin(), current_elements.end(), element) != current_elements.end())
            return current_descriptor.first;
    }

    return "";
}

vector<string> T_Block::findFreeRegister()
{
    vector<string> regs;
    for (pair<string, vector<string>> current_register : m_registers) 
    {
        if(current_register.second.empty())
            regs.push_back(current_register.first);
    }

    return regs;
}

string T_Block::recycleRegister(T_Instruction instruction)
{
    // Vamos a recorrer todos los registros e ir verificando cual es el mas viable
    // para reciclar y utilizarlo

    string best_reg = "";

    // Contadores de spills
    map<string, int> spills;
    
    for (pair<string, vector<string>> current_register : m_registers) 
    {
        //bool isSafe = false;
        int current_spills = 0;

        vector<string> descriptor = current_register.second;

        for(string element : descriptor)
        {
            // Primero se verifica que el valor actual este en algun otro lado
            if(m_variables[element].size() > 1)
                // Es seguro el registro
                continue;
            
            // Verificar que el valor actual sea el resultado y si lo es que no sea operando
            bool found = false;
            for(int i = 0; i < 2; i++)
            {
                if(instruction.operands[i].compare(element) == 0)
                {
                    found = true;
                    break;
                }
            }
            if(element.compare(instruction.result) == 0 && found)
                // Es seguro el registro
                continue;

            // Verificar que el valor actual no tenga usos posteriores

            // Si aun este registro no es seguro
            text.push_back("sw " + element + ", " + current_register.first);

            // Mantener descriptores
            availability(element, element);
            
            current_spills += 1;
        }

        spills[current_register.first] = current_spills;
    }

    // Ahora se verifica cual registro tiene el menor numero de spills
    int min_spill = INT32_MAX;
    
    for (pair<string, int> spill : spills) 
    {
        if(spill.second < min_spill)
            best_reg = spill.first;
    }

    return best_reg;
}

void T_Block::selectRegister(string operand, T_Instruction instruction, vector<string> &regs, vector<string> &free_regs)
{
    // Primero se verifica que el operando este guardada en algun registro
    string reg = findElementInDescriptors(m_registers, operand);
    if(!reg.empty())
    {
        regs.push_back(reg);
        return;
    }
    
    // Si no estaba en un registro verificamos si hay registros libres
    if(free_regs.size() > 0)
    {
        regs.push_back(free_regs.front());
        free_regs.erase(free_regs.begin());
        return;
    }
    
    // Si no se cumple nada los casos simples, pasamos a los casos complejos
    // No hay registros disponibles y el operando no esta en ninguno
    reg = recycleRegister(instruction);
    regs.push_back(reg);
}

vector<string> T_Block::getReg(T_Instruction instruction, bool is_copy)
{
    vector<string> registers;

    // AGREGAR BUSCAR REGISTRO PARA GOIF Y GOIFNOT

    // AGREGAR FUNCIONES

    vector<string> free_regs = findFreeRegister();

    for (string current_operand : instruction.operands)
    {
        selectRegister(current_operand, instruction, registers, free_regs);
    }
    
    bool result_reg_added = false;

    // Ahora se escoge el registro para el resultado
    if(is_copy)
    {
        string result_reg = registers[0];
        registers.insert(registers.begin(), result_reg);
        result_reg_added = true;
    }

    if(!result_reg_added)
    {
        // Buscar registro que SOLO contenga al resultado
        string reg = findElementInDescriptors(m_registers, instruction.result);
        if(!reg.empty() && getRegisterDescriptor(reg).size() < 2)
        {
            registers.insert(registers.begin(), reg);
            result_reg_added = true;
        }
    }

    // Si los operandos no tienen usos posteriores se usa alguno de esos registros

    // Mismo tema que los operandos
    if(!result_reg_added)
    {
        selectRegister(instruction.result, instruction, registers, free_regs);
        string reg = registers.back();
        registers.pop_back();
        registers.insert(registers.begin(), reg);
    }

    return registers;
}

void T_Block::translate()
{
    for(T_Instruction current_inst : m_instructions)
    {
        translateInstruction(current_inst);
    }
}

void T_Block::translateInstruction(T_Instruction instruction)
{
    // Verificamos primero si es una meta instruccion para procesarla
    if(instruction.id[0] == '@')
    {
        translateMetaIntruction(instruction);
        return;
    }

    // Instrucciones de branch
    if(instruction.id[0] == 'g')
    {
        if(instruction.id.compare("goto") == 0)
        {
            if(instruction.id.find("_out") != std::string::npos)
                return;
            
            text.push_back(mips_instructions.at(instruction.id) + " " + instruction.result);
        }
        else
        {
            vector<string> reg = getReg(instruction);
            text.push_back(mips_instructions.at(instruction.id) + " " + reg[0] + ", " + instruction.result);
        }
        return;
    }

    // Instrucciones para llamada de funciones
    if(instruction.id.compare("param") == 0)
    {
        vector<string> reg = getReg(instruction);
        text.push_back(mips_instructions.at(instruction.id) + " " + reg[0] + ", 0($sp)");
        text.push_back("addi $sp, $sp, -4"); // El tamano depende de lo que se le este pasando
        return;
    }

    if(instruction.id.compare("call") == 0)
    {
        // Falta usar el numero de parametros
        text.push_back(mips_instructions.at(instruction.id) + instruction.result);
        return;
    }

    // Instrucciones para funciones

    // Instrucciones de operadores
    translateOperationInstruction(instruction);
}

void T_Block::translateOperationInstruction(T_Instruction instruction)
{
    // Intentar crear descriptores de variables
    insertVariable(instruction.result);
    for(string op : instruction.operands)
        insertVariable(op);
    
    // Verificamos si es una instruccion de copia para luego actualizar los descriptores
    bool is_copy = instruction.id.compare("assign") == 0 ? true : false;
    vector<string> op_registers = getReg(instruction, is_copy);
    int op_index = 1;

    for (string current_operand : instruction.operands)
    {
        // Verificamos el operando
        string current_reg = op_registers[op_index];
        vector<string> reg_descriptor = getRegisterDescriptor(current_reg);
        if ( find(reg_descriptor.begin(), reg_descriptor.end(), current_operand) == reg_descriptor.end() )
        {
            // Buscar el y' mas economico
            string best_location = findOptimalLocation(getVariableDescriptor(current_operand));
            text.push_back("lw " + current_reg + ", " + best_location);

            // Mantener descriptores
            assignment(current_reg, current_operand, true);
            availability(current_operand, current_reg);

            if(is_copy)
            {
                assignment(current_reg, instruction.result);
                availability(instruction.result, current_reg, true);
            }
        }    
        op_index++; 
    }
    

    // Emitir codigo dependiendo del operador
    string emit = mips_instructions.at(instruction.id) + " ";
    for (int i = 0; i < (int) op_registers.size(); i++)
    {
        if(i == (int) op_registers.size() - 1)
        {
            emit += op_registers[i];
            continue;
        }

        emit += op_registers[i] + ", ";
    }
    text.push_back(emit);

    // Mantener descriptor
    assignment(op_registers[0], instruction.result, true);
    availability(instruction.result, op_registers[0], true);
    removeElementFromDescriptors(m_variables, op_registers[0], instruction.result);
}

void T_Block::translateMetaIntruction(T_Instruction instruction)
{
    if(instruction.id.compare("@label") == 0)
    {
        text.push_back(instruction.result + ": ");
        return;
    }

    if(instruction.id.compare("@string") == 0)
    {
        string instruction_type = mips_instructions.at(instruction.id);
        data.push_back(instruction.result + ": " + instruction_type + " " + instruction.operands[0]);
        return;
    }
    
    if(instruction.id.compare("@staticv") == 0)
    {
        data.push_back(instruction.result + ": " + instruction.operands[0]);
        return;
    }
}