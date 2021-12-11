#include "FlowGraph.hpp"

uint64_t getNextLeader(uint64_t leader, vector<uint64_t> leaders) {
    int begin = 0, end = leaders.size(), index = leaders.size() / 2;

    // Aplicamos binary search para encontrar al lider.
    while (leaders[index] != leader) {
        if (leaders[index] < leader) {
            begin = (begin + end) / 2;
        } 
        else {
            end = (begin + end) / 2;
        }
        index = (begin + end) / 2;
    }

    return leaders[index+1]; 
}

uint64_t getIndexLeader(uint64_t leader, vector<uint64_t> leaders) {
    int begin = 0, end = leaders.size(), index = leaders.size() / 2;

    // Aplicamos binary search para encontrar al lider.
    while (leaders[index] != leader) {
        if (leaders[index] < leader) {
            begin = (begin + end) / 2;
        } 
        else {
            end = (begin + end) / 2;
        }
        index = (begin + end) / 2;
    }

    return index; 
}

FlowNode::FlowNode(uint64_t id, uint64_t leader, T_Function *function, bool is_function) {
    this->id = id;
    this->is_function = is_function;
    this->function_id = function->id;
    this->function_size = function->size;

    // Agregamos las instrucciones que corresponden a este bloque.
    if (leader < function->vec_leaders.back()) {
        uint64_t nextLeader = getNextLeader(leader, function->vec_leaders);
        for (uint64_t i = leader; i < nextLeader; i++) {
            this->block.push_back(function->instructions[i]);
        }
    }
}

string FlowNode::getName(void) {
    string prefix = this->is_function ? "F" + to_string(this->function_id) + "_" : "";
    return prefix + "B" + to_string(this->id);
}

void FlowNode::print(void) {
    string name = this->getName();
    if (this->is_function) {
        cout << "@function " << name << " " << to_string(this->function_size) << "\n";
    } 
    else {
        cout << "@label " << name << "\n";
    }
    for (T_Instruction instr : this->block) {
        cout << "    " << instr.id << " " << instr.result << " ";
        for (string operand : instr.operands) {
            cout << operand << " ";
        }
        cout << "\n";
    }
}

void FlowNode::prettyPrint(void) {
    if (this->is_function) {
        string size = to_string(this->function_size);
        cout << "\033[1;3;34m" << this->getName() << " (" + size << "):\033[0m\n";
    }
    else {
        cout << "\033[1;3m" << this->getName() << ":\033[0m\n";
    }

    string space, max_instr = "assignw";
    for (T_Instruction instr : this->block) {
        space = string(max_instr.size() - instr.id.size() + 1, ' ');
        
        cout << "    \033[3m" << instr.id << "\033[0m" 
            << space << instr.result << " ";

        for (string operand : instr.operands) {
            cout << operand << " ";
        }
        cout << "\n";
    }
}

void FlowGraph::insertArc(uint64_t u, uint64_t v) {
    // Agregamos el arco normal
    if (this->E.count(u)) this->E[u].insert(v);
    else this->E.insert({u, {v}});

    // Agregamos el arco inverso
    if (this->Einv.count(v)) this->Einv[v].insert(u);
    else this->Einv.insert({v, {u}});
}

uint64_t FlowGraph::makeSubGraph(T_Function *function, uint64_t init_id) {
    // Creamos los nodos
    uint64_t last_id = init_id;

    // Agregamos el primer nodo.
    this->V.insert({
        last_id, 
        new FlowNode(last_id, function->vec_leaders[0], function, true && function->id)
    });
    last_id++;

    for (uint64_t i = 1; i < function->vec_leaders.size(); i++) {
        this->V.insert({
            last_id, 
            new FlowNode(last_id, function->vec_leaders[i], function, false)
        });
        last_id++;
    }

    // Creamos los arcos
    FlowNode *u;
    uint64_t other_id, instr_line;
    for (uint64_t id = init_id; id < last_id; id++) {
        u = this->V[id];

        // No hay que procesar bloques vacios (pudiendo ser el ultimo del programa)
        if (u->block.size() == 0) {
            continue;
        }

        if (u->block.back().id == "goto") {
            // Obtenemos el ID del bloque al que se realiza el salto.
            instr_line = function->labels2instr[u->block.back().result];
            other_id = getIndexLeader(instr_line, function->vec_leaders) + init_id;
            u->block.back().result = this->V[other_id]->getName();

            // Agregamos el arco y su inverso hacia el bloque de salto.
            this->insertArc(u->id, other_id);
        }
        else if (u->block.back().id == "goif") {
            // Obtenemos el ID del bloque al que se realiza el salto.
            instr_line = function->labels2instr[u->block.back().result];
            other_id = getIndexLeader(instr_line, function->vec_leaders) + init_id;
            u->block.back().result = this->V[other_id]->getName();

            // Agregamos el arco y su inverso hacia el bloque de salto.
            this->insertArc(u->id, other_id);
            // Agregamos el arco y su inverso al siguiente bloque.
            this->insertArc(u->id, u->id+1);
        }
        else if (u->block.back().id != "return") {
            // Agregamos el arco y su inverso al siguiente bloque.
            this->insertArc(u->id, u->id+1);
        }
    }

    // Aplicamos DFS para saber cuales bloques son alcanzables.
    set<uint64_t> visited = {init_id};
    vector<uint64_t> stack = {init_id};
    uint64_t m;
    // Aplicamos DFS
    while (stack.size() > 0) {
        m = stack.back();
        stack.pop_back();

        for (uint64_t n : this->E[m]) {
            if (visited.count(n) == 0) {
                stack.push_back(n);
                visited.insert(n);
            }
        }
    }

    // Eliminamos aquellos bloques inalcanzables.
    for (uint64_t id = init_id; id < last_id; id++) {
        if (visited.count(id) == 0) {
            this->V.erase(id);
            this->E.erase(id);
            this->Einv.erase(id);
        }
    }

    return last_id;
}

FlowGraph::FlowGraph(vector<T_Function*> functions) {
    uint64_t current_id;

    // Creamos el grafo global
    current_id = this->makeSubGraph(functions[0], 0);
    // Agregamos la instruccion para finalizar el programa al ultimo bloque.
    this->V[current_id-1]->block.push_back({"exit", "0", {}});

    // Creamos el grafo de cada funcion
    map<string, uint64_t> function2block;
    for (uint64_t i = 1; i < functions.size(); i++) {
        function2block[functions[i]->name] = current_id;
        current_id = this->makeSubGraph(functions[i], current_id);
    }

    // Actualizamos las llamadas a las funciones
    FlowNode *f;
    for (pair<uint64_t, FlowNode*> n : this->V) {
        for (uint64_t i = 0; i < n.second->block.size(); i++) {
            if (n.second->block[i].id == "call") {
                f = this->V[function2block[n.second->block[i].operands[0]]];
                n.second->block[i].operands[0] = f->getName();
            }
        }
    }
}

void FlowGraph::print(void) {
    for (pair<uint64_t, FlowNode*> n : this->V) {
        if (n.second->is_function) cout << "\n\n";
        n.second->print();
    }
}

void FlowGraph::prettyPrint(void) {
    for (pair<uint64_t, FlowNode*> n : this->V) {
        if (n.second->is_function) cout << "\n\n";
        n.second->prettyPrint();
    }
}