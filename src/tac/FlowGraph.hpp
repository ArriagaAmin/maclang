#pragma once 

#include <map>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

struct T_Variable
{
    string name;
    string acc;
    bool is_acc;
};

struct T_Instruction
{
    string id;
    T_Variable result;
    vector<T_Variable> operands;
};

struct T_Function
{
    string name;
    uint64_t id;
    uint64_t size;
    vector<T_Instruction> instructions;
    map<string, uint64_t> labels2instr;
    set<string> labels_leaders;
    set<uint64_t> leaders = {0};
    vector<uint64_t> vec_leaders;
};

class FlowNode {
    public:
        // Identificador del bloque.
        uint64_t id;
        // Indica si es el bloque inicial de una funcion.
        bool is_function;
        // En caso de ser asi, obtenemos el ID y la memoria necesaria de la funcion.
        uint64_t function_id;
        uint64_t function_size;
        // Nodo a partir del cual ya no forman parte de la funcion.
        uint64_t function_end;
        vector<T_Instruction> block = {};

        FlowNode(uint64_t id, uint64_t leader, T_Function *function, bool is_function);

        // Funcion del analisis de flujo aplicada sobre el bloque entero.
        template <typename T>
        set<T> F(
            map<string, set<T> (*) (set<T>, T_Instruction)> functions, 
            set<T> in,
            bool forward
        );

        string getName(void);
        void print(void);
        void prettyPrint(void);
};

class FlowGraph {
    public:
        // G = (V,E)
        map<uint64_t, FlowNode*> V;
        map<uint64_t, set<uint64_t>> E;
        // Arcos inversos
        map<uint64_t, set<uint64_t>> Einv;
        // Funciones
        map<string, uint64_t> F;
        // Relaciones llamador/llamado
        map<uint64_t, uint64_t> caller;
        map<uint64_t, set<uint64_t>> called;

        FlowGraph(vector<T_Function*> functions);

        void insertArc(uint64_t u, uint64_t v);
        uint64_t makeSubGraph(T_Function *function, uint64_t init_id);

        // ==================== ANALISIS DE FLUJO ==================== //
        // Algoritmo de analisis de flujo generico.
        template <typename T>
        map<uint64_t, vector<set<T>>> flowAnalysis(
            map<uint64_t, vector<set<T>>> (*init) (FlowGraph*),
            set<T> (*initEntryOut) (FlowGraph*),
            set<T> (*initExitIn) (FlowGraph*),
            map<string, set<T> (*) (set<T>, T_Instruction)> functions,
            bool intersection,
            bool forward
        );
        template <typename T>
        void flowPrint(map<uint64_t, vector<set<T>>> sets);

        // Analisis de flujo para variables vivas.
        map<uint64_t, vector<set<string>>> liveVariables(void);


        void print(void);
        void prettyPrint(void);
};


/*
 * Funcion generica F_B 
 */
template <typename T>
set<T> FlowNode::F(
    map<string, set<T> (*) (set<T>, T_Instruction)> functions, 
    set<T> entry,
    bool forward
) {
    if (forward) {

        set<T> out = entry;
        for (T_Instruction instr : this->block) {
            // Aplica la funcion correspondiente al ID de cada instruccion en el bloque.
            out = (*functions[instr.id]) (out, instr);
        }
        return out;
    }
    else {
        set<T> in = entry;
        T_Instruction instr;
        for (int i = this->block.size()-1; i >= 0; i--) {
            // Aplica la funcion correspondiente al ID de cada instruccion en el bloque.
            instr = this->block[i];
            in = (*functions[instr.id]) (in, instr);
        }
        return in;
    }
}

template <typename T>
set<T> setUnion(set<T> U, set<T> V) {
    for (T e : V) U.insert(e);
    return U;
}

template <typename T>
set<T> setIntersec(set<T> U, set<T> V) {
    for (T e : U) 
        if (V.count(e) == 0)
            U.erase(e);
    return U;
}


/*
 * Algoritmo generico de analisis de flujo.
 *
 * Parametros:
 * -----------
 *      * map<uint64_t, vector<set<T>>> (*init) (FlowGraph*) 
 *          Funcion que inicializa los conjuntos dado el grafo de flujo.
 * 
 *      * set<T> (*initEntryOut) (FlowGraph*)
 *          Funcion que inicializa el conjunto OUT del nodo ENTRY.
 * 
 *      * set<T> (*initExitIn) (FlowGraph*)
 *          Funcion que inicializa el conjunto IN del nodo EXIT.
 * 
 *      * map<string, flowFunction> functions
 *          Mapea los ID de las instrucciones del TAC a la funcion transformadora 
 *          correspondiente.
 * 
 *      * bool intersection 
 *          Indica si se realizara una interseccion o una union entre conjuntos al saltar
 *          entro bloques.
 * 
 *      * bool forward
 *          Indica si el analisis es hacia adelante o hacia atras.
 * 
 * Returns:
 * --------
 *      * map<uint64_t, vector<set<T>>>
 *          Diccionario desde los ID de los bloques a sus correspondientes par de 
 *          conjuntos IN, OUT.
 */
template <typename T>
map<uint64_t, vector<set<T>>> FlowGraph::flowAnalysis(
    map<uint64_t, vector<set<T>>> (*init) (FlowGraph*),
    set<T> (*initEntryOut) (FlowGraph*),
    set<T> (*initExitIn) (FlowGraph*),
    map<string, set<T> (*) (set<T>, T_Instruction)> functions,
    bool intersection,
    bool forward
) {
    // Inicializamos el IN y OUT de cada bloque.
    map<uint64_t, vector<set<T>>> sets = (*init)(this);
    // Inicializamos el OUT e IN de ENTRY y EXIT respectivamente.
    set<T> entry_out = (*initEntryOut)(this);
    set<T> exit_in = (*initExitIn)(this);
    set<T> aux, base;
    set<uint64_t> R;

    bool change = true, first;
    uint64_t id;

    vector<uint64_t> ids;
    for (pair<uint64_t, FlowNode*> n : this->V) {
        ids.push_back(n.first);
    }
    if (! forward) {
        reverse(ids.begin(), ids.end());
    }

    // Ejecutamos hasta alcanzar un punto fijo
    while (change) {
        change = false;
        for (uint64_t i : ids) {
            id = this->V[i]->id;
            aux = sets[id][!forward];

            // Obtenemos la entrada del bloque.
            sets[id][!forward] = set<T>();
            // Calculamos la union/intercepcion de los predecesores/sucesores.
            R = forward ? this->Einv[id] : this->E[id];
            if (intersection) {
                first = true;
                for (uint64_t u_id : R) {
                    if (first) {
                        sets[id][!forward] = sets[u_id][forward];
                        first = false;
                    }
                    else {
                        sets[id][!forward] = setIntersec<T>(sets[id][!forward], sets[u_id][forward]);
                    }
                }
                // Agregamos los llamador o llamadores en caso de ser necesario
                if (forward && this->caller.count(id-1) > 0) {
                    sets[id][0] = setIntersec<T>(sets[id][0], sets[this->caller[id-1]][1]);
                }
                else if (! forward && this->caller.count(id) > 0) {
                    sets[id][1] = setIntersec<T>(sets[id][1], sets[this->caller[id]][0]);
                }

                // Si es el primer nodo del grafo y estamos en forward
                if ((id == 0 || this->V[id]->is_function) && forward) {
                    sets[id][0] = setIntersec<T>(sets[id][0], entry_out);
                }
                // En cambio, si es un nodo final y estamos en backward
                else if (! forward && this->Einv.count(id) == 0) {
                    sets[id][1] = setIntersec<T>(sets[id][1], exit_in);
                }
            }
            else {
                for (uint64_t u_id : R) {
                    sets[id][!forward] = setUnion<T>(sets[id][!forward], sets[u_id][forward]);
                }
                // Agregamos los llamador o llamadores en caso de ser necesario
                if (forward && this->caller.count(id-1) > 0) {
                    sets[id][0] = setUnion<T>(sets[id][0], sets[this->caller[id-1]][1]);
                }
                else if (! forward && this->caller.count(id) > 0) {
                    sets[id][1] = setUnion<T>(sets[id][1], sets[this->caller[id]][0]);
                }

                // Si es el primer nodo del grafo y estamos en forward
                if ((id == 0 || this->V[id]->is_function) && forward) {
                    sets[id][0] = setUnion<T>(sets[id][0], entry_out);
                }
                // En cambio, si es un nodo final y estamos en backward
                else if (! forward && this->Einv.count(id) == 0) {
                    sets[id][1] = setUnion<T>(sets[id][1], exit_in);
                }
            }
            // Ignoramos la variable BASE
            sets[id][!forward].erase("BASE");
            change = change || sets[id][!forward] != aux;

            // Calculamos el out del bloque
            aux = sets[id][forward];
            sets[id][forward] = this->V[i]->F<T>(functions, sets[id][!forward], forward);
            // Ignoramos la variable BASE
            sets[id][forward].erase("BASE");
            // Verificamos si hubo un cambio
            change = change || sets[id][forward] != aux;
        }
    }

    return sets;
}


/*
 * Imprime de forma bonita el resultado de un analisis de flujo.
 */
template <typename T>
void FlowGraph::flowPrint(map<uint64_t, vector<set<T>>> sets) {
    for (pair<uint64_t, FlowNode*> n : this->V) {
        // Nombre del nodo.
        if (n.second->is_function) {
            string size = to_string(n.second->function_size);
            cout << "\n\033[1;3;34m" << n.second->getName() << " (" + size << "):\033[0m\n";
        }
        else {
            cout << "\033[1;3m" << n.second->getName() << ":\033[0m\n";
        }

        // Predecesores del nodo.
        cout << "    \033[1mPREDS:\033[0m {";
        for (uint64_t v : this->Einv[n.first]) {
            cout << this->V[v]->getName() << ", ";
        }
        if (n.first == 0 || this->V[n.first]->is_function) {
            cout << "ENTRY, ";
        }
        cout << "}\n";

        // IN del nodo.
        cout << "    \033[1mIN:\033[0m    {";
        for (T elem : sets[n.first][0]) {
            cout << elem << ", ";
        }
        cout << "}\n";

        // BLOQUE
        cout << "    \033[1mBLOCK:\033[0m\n";
        string space, max_instr = "assignw";
        for (T_Instruction instr : n.second->block) {
            space = string(max_instr.size() - instr.id.size() + 1, ' ');
            
            cout << "        | \033[3m" << instr.id << "\033[0m" 
                << space << instr.result.name << " ";

            for (T_Variable operand : instr.operands) {
                cout << operand.name << " ";
            }
            cout << "\n";
        }

        // OUT del nodo.
        cout << "    \033[1mOUT:\033[0m   {";
        for (T elem : sets[n.first][1]) {
            cout << elem << ", ";
        }
        cout << "}\n";

        // Sucesores del nodo.
        cout << "    \033[1mSUCCS:\033[0m {";
        if (this->E.count(n.first) == 0 || this->E[n.first].size() == 0) {
            cout << "EXIT, ";
        }
        else {
            for (uint64_t v : this->E[n.first]) {
                cout << this->V[v]->getName() << ", ";
            }
        }
        cout << "}\n\n";
    }
}
