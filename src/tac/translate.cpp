#include "translate.hpp"

Translator::Translator()
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

void Translator::insertInstruction(T_Instruction* instruction)
{
    m_data_instructions.push_back(instruction);
}

bool Translator::insertRegister(string id)
{
    auto found = m_registers.find(id);

    if(found != m_registers.end()) 
        return false;
    
    m_registers[id] = vector<string>();
    return true;
}

bool Translator::insertVariable(string id)
{
    auto found = m_variables.find(id);

    if(found != m_variables.end()) 
        return false;
    
    vector<string> locations { id };
    m_variables[id] = locations;
    return true;
}

void Translator::insertFlowGraph(FlowGraph* graph)
{
    m_graph = graph;
}

void Translator::print()
{
    cout << ".data" << endl;
    for(string inst : data)
    {
        cout << inst << endl;
    }

    cout << "\n.text" << endl;
    for(string inst : text)
    {
        cout << inst << endl;
    }

    cout << endl;
    for(string inst : functions)
    {
        cout << inst << endl;
    }
}

bool Translator::insertElementToDescriptor(unordered_map<string, vector<string>> &descriptors, string key, string element, bool replace)
{
    auto found = descriptors.find(key);

    if(found == descriptors.end()) 
        return false;
    
    if(replace)
        descriptors[key].clear();

    descriptors[key].push_back(element);
    return true;
}

void Translator::removeElementFromDescriptors(unordered_map<string, vector<string>> &descriptors, string element, string current_container)
{   
    for (pair<string, vector<string>> current_descriptor : descriptors) 
    {
        if(current_descriptor.first == current_container)
            continue;
        
        vector<string> current_elements = current_descriptor.second;
        remove(current_elements.begin(), current_elements.end(), element);
    }
}

void Translator::cleanRegistersDescriptor()
{
    for(auto currentRegister : m_registers)
    {
        currentRegister.second.clear();
    }
}

bool Translator::assignment(string register_id, string variable_id, bool replace)
{
    return insertElementToDescriptor(m_registers, register_id, variable_id, replace);
}

bool Translator::availability(string variable_id, string location, bool replace)
{
    return insertElementToDescriptor(m_variables, variable_id, location, replace);
}

vector<string> Translator::getRegisterDescriptor(string id)
{
    return m_registers[id];
}

vector<string> Translator::getVariableDescriptor(string id)
{
    return m_variables[id];
}

string Translator::findOptimalLocation(string id)
{    
    vector<string> descriptor = getVariableDescriptor(id);
    // Por ahora solamente devolver el primero
    return descriptor[0];
}

string Translator::findElementInDescriptors(unordered_map<string, vector<string>> &descriptors, string element)
{   
    for (pair<string, vector<string>> current_descriptor : descriptors) 
    {
        vector<string> current_elements = current_descriptor.second;
        if( find(current_elements.begin(), current_elements.end(), element) != current_elements.end())
            return current_descriptor.first;
    }

    return "";
}

vector<string> Translator::findFreeRegister()
{
    vector<string> regs;
    for (pair<string, vector<string>> current_register : m_registers) 
    {
        if(current_register.second.empty())
            regs.push_back(current_register.first);
    }

    return regs;
}

string Translator::recycleRegister(T_Instruction instruction, vector<string>& section)
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
            for(int i = 0; i < (int) instruction.operands.size(); i++)
            {
                if(instruction.operands[i] == element)
                {
                    found = true;
                    break;
                }
            }
            if(element == instruction.result && found)
                // Es seguro el registro
                continue;

            // Verificar que el valor actual no tenga usos posteriores

            // Si aun este registro no es seguro
            section.emplace_back(mips_instructions.at("store") + space + element + sep + current_register.first);

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

void Translator::selectRegister(string operand, T_Instruction instruction, vector<string> &regs, vector<string> &free_regs, vector<string>& section)
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
    reg = recycleRegister(instruction, section);
    regs.push_back(reg);
}

vector<string> Translator::getReg(T_Instruction instruction, vector<string>& section, bool is_copy)
{
    vector<string> registers;

    // AGREGAR FUNCIONES

    vector<string> free_regs = findFreeRegister();

    for (string current_operand : instruction.operands)
    {
        selectRegister(current_operand, instruction, registers, free_regs, section);
    }
    
    // Si es una instruccion de salto solo es necesario el registro del operando
    if(instruction.id.find("go") != string::npos)
        return registers;

    // Ahora se escoge el registro para el resultado
    if(is_copy)
    {
        string result_reg = registers[0];
        registers.insert(registers.begin(), result_reg);
    }
    else
    {
        // Buscar registro que SOLO contenga al resultado
        string reg = findElementInDescriptors(m_registers, instruction.result);
        if(!reg.empty() && getRegisterDescriptor(reg).size() < 2)
        {
            registers.insert(registers.begin(), reg);
        }
        // TODO: Si los operandos no tienen usos posteriores se usa alguno de esos registros
        else
        {
            // Sino igual que los operandos
            selectRegister(instruction.result, instruction, registers, free_regs, section);
            string reg = registers.back();
            registers.pop_back();
            registers.insert(registers.begin(), reg);
        }
    } 
    
    return registers;
}

void Translator::translate()
{
    // Traducimos primero las instrucciones que estarian en el .data
    for(T_Instruction* currentInstr : m_data_instructions)
    {
        translateInstruction(*currentInstr, text);
    }

    // Luego traducimos el codigo como tal
    for(auto currentNode : m_graph->V)
    {
        FlowNode* currentNodeData = currentNode.second;
        vector<string>* section = &text;

        if(currentNodeData->is_function)
            section = &functions;
        
        (*section).emplace_back(currentNodeData->getName() + decl);
        for(T_Instruction current_inst : currentNodeData->block)
        {
            translateInstruction(current_inst, *section);
        }

        // Al terminar el bloque basico se actualizan los temporales
        //text.push_back("# Updating the temporals");
        for(auto current_variable : m_variables)
        {
            string var_id = current_variable.first;
            vector<string> var_descriptor = current_variable.second;

            if ( find(var_descriptor.begin(), var_descriptor.end(), var_id) == var_descriptor.end() )
            {
                (*section).emplace_back(mips_instructions.at("store") + space + var_descriptor[0] + sep + var_id);
                availability(var_id, var_id, true);
            }
        }

        // Limpiar los registros
        cleanRegistersDescriptor();
    }
}

void Translator::translateInstruction(T_Instruction instruction, vector<string>& section)
{
    // Verificamos primero si es una meta instruccion para procesarla
    if(instruction.id[0] == '@')
    {
        translateMetaIntruction(instruction);
        return;
    }

    if(instruction.id == "exit")
    {
        section.emplace_back(mips_instructions.at(instruction.id));
        return;
    }

    // Instrucciones de branch
    if(instruction.id.find("go") != string::npos)
    {
        if(instruction.id == "goto")
        {
            if(instruction.id.find("_out") != std::string::npos)
                return;
            
            section.emplace_back(mips_instructions.at(instruction.id) + space + instruction.result);
        }
        else
        {
            vector<string> reg = getReg(instruction, section);
            section.emplace_back(mips_instructions.at(instruction.id) + space + reg[0] + sep + instruction.result);
        }
        return;
    }

    // Instrucciones para llamada de funciones
    if(instruction.id == "param")
    {
        vector<string> reg = getReg(instruction, section);
        section.emplace_back(mips_instructions.at(instruction.id) + space + reg[0] + sep + "0($sp)");
        section.emplace_back("addi $sp, $sp, -4"); // El tamano depende de lo que se le este pasando
        return;
    }

    if(instruction.id == "call")
    {
        // Falta usar el numero de parametros
        section.emplace_back(mips_instructions.at(instruction.id) + space + instruction.result);
        return;
    }

    // Instrucciones para funciones

    // Instrucciones de operaciones
    bool is_copy = false;
    int type = 1;

    if(instruction.id.find("assign") != string::npos)
    {
        is_copy = true;

        if(instruction.id.back() == 'w')
        {
            type = 0;
        }
    }
    else if(instruction.id == "add" || 
            instruction.id == "sub" ||
            instruction.id == "mult" ||
            instruction.id == "div" ||
            instruction.id == "mod" ||
            instruction.id == "minus"
        )
    {
        type = 0;
    }

    translateOperationInstruction(instruction, section, is_copy, type);
}

void Translator::translateOperationInstruction(T_Instruction instruction, vector<string>& section, bool is_copy, int type)
{
    // Intentar crear descriptores de variables
    insertVariable(instruction.result);

    // Agregar al .data
    string s_type = type == 0 ? "word" : "byte";
    data.emplace_back(instruction.result + decl + mips_instructions.at(s_type) + space + "1");

    // Buscar los registros
    vector<string> op_registers = getReg(instruction, section, is_copy);
    int op_index = 1;

    for (string current_operand : instruction.operands)
    {
        // Verificamos el operando
        string current_reg = op_registers[op_index];
        vector<string> reg_descriptor = getRegisterDescriptor(current_reg);
        if ( find(reg_descriptor.begin(), reg_descriptor.end(), current_operand) == reg_descriptor.end() )
        {
            string best_location = current_operand;
            // Si es un temporal se busca en su descriptor la mejor posicion
            if(!isdigit(current_operand[0]))
            {
                // Buscar el y' mas economico
                string best_location = findOptimalLocation(current_operand);
            }

            section.emplace_back(mips_instructions.at("load") + space + current_reg + sep + best_location);
        }

        // Mantener descriptores
        assignment(current_reg, current_operand, true);
        availability(current_operand, current_reg);
        
        if(is_copy)
        {
            assignment(current_reg, instruction.result);
            availability(instruction.result, current_reg, true);
        }

        op_index++; 
    }
    
    if(is_copy)
        return;

    // Emitir codigo dependiendo del operador
    int i = 0;
    if(instruction.id == "div" || instruction.id == "mod")
        i = 1;
    
    string emit = mips_instructions.at(instruction.id) + space;
    for (;i < (int) op_registers.size(); i++)
    {
        if(i == (int) op_registers.size() - 1)
        {
            emit += op_registers[i];
            continue;
        }

        emit += op_registers[i] + sep;
    }
    section.emplace_back(emit);

    // Si son div o mod se agregan la instruccion especial de mips
    if(instruction.id == "div")
        section.emplace_back(mips_instructions.at("low") + space + op_registers[0]);
    else if(instruction.id == "mod")
        section.emplace_back(mips_instructions.at("high") + space + op_registers[0]);

    // Mantener descriptor
    assignment(op_registers[0], instruction.result, true);
    availability(instruction.result, op_registers[0], true);
    removeElementFromDescriptors(m_variables, op_registers[0], instruction.result);
}

void Translator::translateMetaIntruction(T_Instruction instruction)
{
    if(instruction.id == "@string")
    {
        data.emplace_back(instruction.result + decl + mips_instructions.at(instruction.id) + space + instruction.operands[0]);
        return;
    }
    
    if(instruction.id == "@staticv")
    {
        data.emplace_back(instruction.result + decl + mips_instructions.at("word") + space + instruction.operands[0]);
        return;
    }
}

void Translator::printVariablesDescriptors()
{
    for(auto vari : m_variables)
    {
        cout << vari.first << endl;
        for(auto element : vari.second)
        {
            cout << element << endl;
        }
    }
}