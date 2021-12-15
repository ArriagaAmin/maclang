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
    auto found = this->m_registers.find(id);

    if(found != this->m_registers.end()) 
        return false;
    
    this->m_registers[id] = vector<string>();
    return true;
}

bool Translator::insertVariable(string id, uint16_t type, string value)
{
    auto found = this->m_variables.find(id);

    if(found != this->m_variables.end()) 
        return false;
    
    // Agregar al .data
    string s_type = "word";

    switch (type)
    {
    case 1:
        s_type = "byte";
        break;
    case 2:
        s_type = "@string";
        break;
    default:
        break;
    }

    data.emplace_back(id + decl + mips_instructions.at(s_type) + space + value);
    
    vector<string> locations { id };
    this->m_variables[id] = locations;
    return true;
}

void Translator::insertFlowGraph(FlowGraph* graph)
{
    m_graph = graph;
}

void Translator::print()
{
    cout << ".text" << endl;
    for(string inst : text)
    {
        cout << inst << endl;
    }

    if(functions.size() > 0)
    {
        cout << "\n# ===== Functions Section ====="<< endl;
        for(string inst : functions)
        {
            cout << inst << endl;
        }
    }

    cout << "\n.data" << endl;
    for(string inst : data)
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

        remove(descriptors[current_descriptor.first].begin(), descriptors[current_descriptor.first].end(), element);
    }
}

void Translator::cleanRegistersDescriptor()
{
    for(auto current_register : this->m_registers)
    {
        this->m_registers[current_register.first].clear();
    }
}

bool Translator::assignment(string register_id, string variable_id, bool replace)
{
    return insertElementToDescriptor(this->m_registers, register_id, variable_id, replace);
}

bool Translator::availability(string variable_id, string location, bool replace)
{
    return insertElementToDescriptor(this->m_variables, variable_id, location, replace);
}

vector<string> Translator::getRegisterDescriptor(string id)
{
    return this->m_registers[id];
}

vector<string> Translator::getVariableDescriptor(string id)
{
    return this->m_variables[id];
}

string Translator::findOptimalLocation(string id)
{    
    //vector<string> descriptor = getVariableDescriptor(id);
    // Por ahora solamente devolver el mismo
    return id;
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
    for (pair<string, vector<string>> current_register : this->m_registers) 
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
    
    for (pair<string, vector<string>> current_register : this->m_registers) 
    {
        //bool isSafe = false;
        int current_spills = 0;

        vector<string> descriptor = current_register.second;

        for(string element : descriptor)
        {
            // Primero se verifica que el valor actual este en algun otro lado
            if(this->m_variables[element].size() > 1)
                // Es seguro el registro
                continue;
            
            // Verificar que el valor actual sea el resultado y si lo es que no sea operando
            bool found = false;
            for(size_t i = 0; i < instruction.operands.size(); i++)
            {
                if(instruction.operands[i].name == element)
                {
                    found = true;
                    break;
                }
            }
            if(element == instruction.result.name && found)
                // Es seguro el registro
                continue;

            // Verificar que el valor actual no tenga usos posteriores

            // Si aun este registro no es seguro
            section.emplace_back(mips_instructions.at("store") + space + current_register.first + sep + element);

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
    string reg = findElementInDescriptors(this->m_registers, operand);
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

    for (T_Variable current_operand : instruction.operands)
    {
        selectRegister(current_operand.name, instruction, registers, free_regs, section);
    }
    
    // Si es una instruccion de salto solo es necesario el registro del operando
    if(instruction.id.find("go") != string::npos)
        return registers;

    // Ahora se escoge el registro para el resultado
    if(is_copy && !instruction.result.is_acc)
    {
        string result_reg = registers[0];
        registers.insert(registers.begin(), result_reg);
    }
    else
    {
        // Buscar registro que SOLO contenga al resultado
        string reg = findElementInDescriptors(this->m_registers, instruction.result.name);
        if(!reg.empty() && getRegisterDescriptor(reg).size() < 2)
        {
            registers.insert(registers.begin(), reg);
        }
        // TODO: Si los operandos no tienen usos posteriores se usa alguno de esos registros
        else
        {
            // Sino igual que los operandos
            selectRegister(instruction.result.name, instruction, registers, free_regs, section);
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

        vector<string> aliveVars;

        // Al terminar el bloque basico se actualizan los temporales
        for(auto current_variable : this->m_variables)
        {
            string var_id = current_variable.first;
            vector<string> var_descriptor = current_variable.second;

            if ( find(var_descriptor.begin(), var_descriptor.end(), var_id) == var_descriptor.end() )
            {
                aliveVars.emplace_back(mips_instructions.at("store") + space + var_descriptor[0] + sep + var_id);
                availability(var_id, var_id, true);
            }
        }

        if(aliveVars.size() > 0)
        {
            string lastInstr = "";
            
            // Si la ultima instruccion de un bloque es un salto, se actualizan antes de saltar
            string lastInstrId = currentNodeData->block.back().id;
            if(lastInstrId == "goto" || lastInstrId== "goif" ||
                lastInstrId == "goifnot" || lastInstrId == "call" ||
                lastInstrId== "return")
            {
                lastInstr = section->back();
                section->pop_back();
            }

            (*section).emplace_back("# Updating the temporals");

            for(string line : aliveVars)
            {
                (*section).push_back(line);
            }

            if(!lastInstr.empty())
            {
                (*section).push_back(lastInstr);
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
        section.emplace_back(mips_instructions.at("load") + space + "$a0" + sep + instruction.result.name);
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
            
            section.emplace_back(mips_instructions.at(instruction.id) + space + instruction.result.name);
        }
        else
        {
            vector<string> reg = getReg(instruction, section);
            section.emplace_back(mips_instructions.at(instruction.id) + space + reg[0] + sep + instruction.result.name);
        }
        return;
    }

    // TODO: REWORK TO PARAM Y CALL
    // Instrucciones para llamada de funciones
    if(instruction.id == "param")
    {
        insertVariable(instruction.result.name, 0);
        vector<string> reg = getReg(instruction, section);
        vector<string> reg_descriptor = getRegisterDescriptor(reg[0]);
        if ( find(reg_descriptor.begin(), reg_descriptor.end(), instruction.result.name) == reg_descriptor.end() )
        {
            string best_location = findOptimalLocation(instruction.result.name);

            section.emplace_back(mips_instructions.at("load") + space + reg[0] + sep + best_location);
        }
        section.emplace_back(mips_instructions.at(instruction.id) + space + reg[0] + sep + instruction.operands[0].name + "($sp)");
        return;
    }

    if(instruction.id == "call")
    {
        // TODO: Se hace back up al $sp, $fp y al $ra
        int length = stoi(instruction.operands[1].name);
        length *= 4;
        section.emplace_back("addi $sp, $sp, -" + to_string(length));

        // Crear en donde se guardara el valor de retorno
        insertVariable(instruction.result.name, 0);

        // Se salta hacia la funcion
        section.emplace_back(mips_instructions.at(instruction.id) + space + instruction.operands[0].name);
        return;
    }

    if(instruction.id == "return")
    {
        // TODO: guardar el valor de retorno

        // Se salta de vuelta hacia donde se llamo
        section.emplace_back(mips_instructions.at(instruction.id) + space + "$ra");
        return;
    }

    // Instrucciones para funciones TODO: usar el tamano de la funcion

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

void Translator::translateOperationInstruction(T_Instruction instruction, vector<string>& section, bool is_copy, uint16_t type)
{
    // Intentar crear descriptores de variables
    insertVariable(instruction.result.name, type);

    // Buscar los registros
    vector<string> op_registers = getReg(instruction, section, is_copy);
    int op_index = 1;

    for (T_Variable current_operand : instruction.operands)
    {
        // Verificamos el operando
        string current_reg = op_registers[op_index];
        vector<string> reg_descriptor = getRegisterDescriptor(current_reg);
        if ( find(reg_descriptor.begin(), reg_descriptor.end(), current_operand.name) == reg_descriptor.end() )
        {
            string best_location = findOptimalLocation(current_operand.name);

            section.emplace_back(mips_instructions.at("load") + space + current_reg + sep + best_location);
        }

        // Mantener descriptores
        assignment(current_reg, current_operand.name, true);
        availability(current_operand.name, current_reg);

        if(is_copy)
        {
            assignment(current_reg, instruction.result.name);
            availability(instruction.result.name, current_reg, true);
        }

        op_index++; 
    }
    
    // TODO: Falta manejar BASE, STACK, lastbase
    if(is_copy)
    {
        // Tomar en cuentas las indirecciones
        if(instruction.operands[0].is_acc)
        {
            string op = instruction.operands[0].acc + "(" + op_registers[1] + ")";
            section.emplace_back(mips_instructions.at("load") + space + op_registers[0] + sep + op);
        }
        else if(instruction.result.is_acc)
        {
            // Se carga el la direccion base de lo que se quiere indireccionar si no esta
            vector<string> reg_descriptor = getRegisterDescriptor(op_registers[0]);
            if ( find(reg_descriptor.begin(), reg_descriptor.end(), instruction.result.name) == reg_descriptor.end() )
            {
                string best_location = findOptimalLocation(instruction.result.name);
                section.emplace_back(mips_instructions.at("load") + space + op_registers[0] + sep + best_location);
            }
            // Se almacena el nuevo valor en la direccion nueva
            string op = instruction.result.acc + "(" + op_registers[0] + ")";
            section.emplace_back(mips_instructions.at("store") + space + op_registers[1] + sep + op);
        }
        return;
    }

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
    assignment(op_registers[0], instruction.result.name, true);
    availability(instruction.result.name, op_registers[0], true);
    removeElementFromDescriptors(this->m_variables, op_registers[0], instruction.result.name);
}

void Translator::translateMetaIntruction(T_Instruction instruction)
{
    if(instruction.id == "@string")
    {
        insertVariable(instruction.result.name, 2, instruction.operands[0].name);
        //data.emplace_back(instruction.result.name + decl + mips_instructions.at(instruction.id) + space + instruction.operands[0].name);
        return;
    }
    
    if(instruction.id == "@staticv")
    {
        insertVariable(instruction.result.name, 0, instruction.operands[0].name);
        //data.emplace_back(instruction.result.name + decl + mips_instructions.at("word") + space + instruction.operands[0].name);
        return;
    }
}

void Translator::translateIOIntruction(T_Instruction instruction, vector<string>& section)
{
    if(instruction.id.find("print") != string::npos)
    {
        const char* argRegister = "$a0";
        if(instruction.id.back() != 'f')
        {
            // Se necesita el elemento a imprimir en $a0, se guardan los elementos de ser necesario
            vector<string> regDescriptor = getRegisterDescriptor(argRegister);
            for(string currentVar : regDescriptor)
            {
                section.emplace_back(mips_instructions.at("store") + space + argRegister + sep + currentVar);
                availability(currentVar, currentVar);
            }

            // Se mueve el elemento a $a0
            section.emplace_back(mips_instructions.at("assign") + space + argRegister + sep + instruction.result.name);
            // Se carga el syscall correcto
            section.emplace_back(mips_instructions.at(instruction.id));
        }
        else
        {
            // TODO: falta imprimir los floats
        }
    }
    else    
    {
        if(instruction.id.back() == 'i' || instruction.id.back() == 'c')
        {
            // Se carga el syscall correcto
            section.emplace_back(mips_instructions.at(instruction.id));
        }
        else if(instruction.id.back() == 'f')
        {
            // TODO: falta leer los floats
        }
        else
        {
            const char* addrRegister = "$a0";
            const char* sizeRegister = "$a1";

            // Se necesita el buffer donde guardar el string en $a0
            vector<string> regDescriptor = getRegisterDescriptor(addrRegister);
            for(string currentVar : regDescriptor)
            {
                section.emplace_back(mips_instructions.at("store") + space + addrRegister + sep + currentVar);
                availability(currentVar, currentVar);
            }
            // Se necesita el tamano maximo en $a1
            regDescriptor = getRegisterDescriptor(sizeRegister);
            for(string currentVar : regDescriptor)
            {
                section.emplace_back(mips_instructions.at("store") + space + sizeRegister + sep + currentVar);
                availability(currentVar, currentVar);
            }

            // Se mueve el buffer a $a0
            section.emplace_back(mips_instructions.at("assign") + space + addrRegister + sep + instruction.result.name);
            // TODO: Agregar el tamano de lo que se va a leer
            // Se carga el syscall correcto
            section.emplace_back(mips_instructions.at(instruction.id));
        }
    }
}

void Translator::printVariablesDescriptors()
{
    for(auto vari : this->m_variables)
    {
        cout << vari.first << endl;
        for(auto element : vari.second)
        {
            cout << element << endl;
        }
    }
}