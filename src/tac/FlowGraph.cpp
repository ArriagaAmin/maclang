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
        cout << "    " << instr.id << " " << instr.result.name << " ";
        if(instr.result.is_acc)
            cout << "[" << instr.result.acc << "]";
        cout << " ";
        for (T_Variable operand : instr.operands) {
            cout << operand.name;
            if(operand.is_acc)
                cout << "[" << operand.acc << "]";
            cout << " ";
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
            << space << instr.result.name;
        if (instr.result.is_acc)
            cout << "[" << instr.result.acc << "]";
        cout << " ";
        for (T_Variable operand : instr.operands) {
            cout << operand.name;
            if (operand.is_acc)
                cout << "[" << operand.acc << "]";
            cout << " ";
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

void FlowGraph::deleteBlock(uint64_t id) {
    // Eliminamos todos los arcos que apuntan hacia el bloque.
    for (uint64_t p : this->Einv[id]) {
        this->E[p].erase(id);
    }
    // Eliminamos todos los arcos inversos que apuntan hacia el bloque.
    for (uint64_t p : this->E[id]) {
        this->Einv[p].erase(id);
    }
    // Eliminamos los arcos desde el bloque.
    this->E.erase(id);
    this->Einv.erase(id);

    // Si el nodo es una funcion, eliminamos su referencia en el grafo
    if (this->V[id]->is_function) {
        this->F.erase(this->V[id]->getName());
    }

    // Eliminamos su posible llamada.
    this->caller.erase(id);

    // Borramos el nodo.
    delete this->V[id];
    this->V.erase(id);
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
    this->V[init_id]->function_end = last_id;

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
            instr_line = function->labels2instr[u->block.back().result.name];
            other_id = getIndexLeader(instr_line, function->vec_leaders) + init_id;
            u->block.back().result.name = this->V[other_id]->getName();

            // Agregamos el arco y su inverso hacia el bloque de salto.
            this->insertArc(u->id, other_id);
        }
        else if (u->block.back().id == "goif" || u->block.back().id == "goifnot") {
            // Obtenemos el ID del bloque al que se realiza el salto.
            instr_line = function->labels2instr[u->block.back().result.name];
            other_id = getIndexLeader(instr_line, function->vec_leaders) + init_id;
            u->block.back().result.name = this->V[other_id]->getName();

            // Agregamos el arco y su inverso hacia el bloque de salto.
            this->insertArc(u->id, other_id);
            // Agregamos el arco y su inverso al siguiente bloque.
            this->insertArc(u->id, u->id+1);
        }
        else if (u->block.back().id != "return" && u->block.back().id != "exit") {
            // Aunque no deberia agregarse un arco tampoco si la instruccion es "call",
            // por ahora es necesario colocarlo.
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
            this->deleteBlock(id);
        }
    }

    // Como el ultimo id pudo haber sido eliminado, obtenemos el ultimo id visitado
    while (visited.count(last_id-1) == 0) {
        last_id--;
    }

    return last_id;
}

FlowGraph::FlowGraph(vector<T_Function*> functions, set<string> staticVars) {
    this->staticVars = staticVars;

    uint64_t current_id;

    // Creamos el grafo global
    current_id = this->makeSubGraph(functions[0], 0);
    // Agregamos la instruccion para finalizar el programa al ultimo bloque.
    this->V[current_id-1]->block.push_back({"exit", {"0", "", false}, {}});

    // Creamos el grafo de cada funcion
    for (uint64_t i = 1; i < functions.size(); i++) {
        this->F[functions[i]->name] = current_id;
        current_id = this->makeSubGraph(functions[i], current_id);
    }

    // Actualizamos las llamadas a las funciones y creamos los arcos correspondientes.
    FlowNode *f;
    for (pair<uint64_t, FlowNode*> n : this->V) {
        for (uint64_t i = 0; i < n.second->block.size(); i++) {
            if (n.second->block[i].id == "call") {
                f = this->V[this->F[n.second->block[i].operands[0].name]];
                n.second->block[i].operands[0].name = f->getName();
                
                // Creamos la relacion de llamada
                this->caller[n.first] = f->id;
            }
        }
    }

    // Eliminamos las funciones que no son llamadas
    // Para ello usamos DFS para obtener todas las posibles llamadas en los bloques.
    set<uint64_t> visited;
    stack<uint64_t> toVisit;
    uint64_t current_b;

    toVisit.push(0);
    visited.insert(0);

    while (toVisit.size() > 0) {
        current_b = toVisit.top();
        toVisit.pop();
        do {
            if (current_b >= current_id) break;

            if (
                this->V.count(current_b) > 0 && 
                this->caller.count(current_b) > 0 &&
                visited.count(this->caller[current_b]) == 0 
            ) {
                visited.insert(this->caller[current_b]);
                toVisit.push(this->caller[current_b]);
            }
            current_b++;

        } while (this->V.count(current_b) == 0 || ! this->V[current_b]->is_function);
    }

    // Eliminamos las funciones que no fueron llamadas.
    current_b = 0;
    while (current_b < current_id) {
        // Si la funcion fue visitada, solo tenemos que pasar a la siguiente funcion.
        if (visited.count(current_b) > 0) {
            do {
                if (current_b >= current_id) break;
                current_b++;
            }
            while (this->V.count(current_b) == 0 || ! this->V[current_b]->is_function);
        }
        // En caso contrario eliminamos todos los bloques de la funcion.
        else {
            do {
                if (current_b >= current_id) break;
                if (this->V.count(current_b) > 0) {
                    this->deleteBlock(current_b);
                }
                current_b++;
            } while (this->V.count(current_b) == 0 || ! this->V[current_b]->is_function);
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
