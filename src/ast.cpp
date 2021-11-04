#include "ast.hpp"

/* ======================= AUXILIARY FUNCTIONS ======================= */
  void printIdentation(vector<bool> *identation) {
    for (bool b : *identation) {
      if (b) cout << "│";
      else cout << " ";
      cout << "   ";
    }
  }

  map<string, int> primitiveWidths = {
    {"Unit",    1},
    {"Bool",    1},
    {"Char",    4},   // UTF-8 use 4 bytes
    {"Int",     8},
    {"Float",   8},
    {"Pointer", 8},
    {"$Error",  0}
  };

  // Predefined Types 
  map<string, Type*> predefinedTypes = {
    {"Unit",    new PrimitiveType("Unit")},
    {"Bool",    new PrimitiveType("Bool")},
    {"Char",    new PrimitiveType("Char")},
    {"Int",     new PrimitiveType("Int")},
    {"Float",   new PrimitiveType("Float")},
    {"$Error",  new PrimitiveType("$Error")}
  };


/* ======================= TYPES ===================================== */
  PrimitiveType::PrimitiveType(string id) {
    this->id = id;
    this->width = primitiveWidths[id];
    this->category = "Primitive";
  }
  string PrimitiveType::toString(void) {
    return this->id;
  }
  void PrimitiveType::printTree(vector<bool> *identation) {
    cout << "Primitive Type: " << this->id << "\n";
  }


  PointerType::PointerType(Type *type) {
    this->type = type;
    this->width = primitiveWidths["Pointer"];
    this->category = "Pointer";
  }
  string PointerType::toString(void) {
    return "^(" + this->type->toString() + ")";
  }
  void PointerType::printTree(vector<bool> *identation) {
    cout << "\e[1;34mType Pointer\e[0m\n";

    printIdentation(identation);
    cout << "├── ^\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->type->printTree(identation);
    identation->pop_back();
  }


  ArrayType::ArrayType(Type *type, ExpressionNode *size, bool is_string) {
    this->type = type;
    this->size = size;
    this->is_string = is_string;
    string t_size = type->toString();

    // Si size es un literal, podemos calcular directamente el desplazamiento.
    if (! is_string && size->is_lit) {
      this->width = type->width * ((NodeINT*) size)->value;
      this->is_pointer = false;
    }
    // En caso contrario, se tomara como un puntero.
    else {
      this->width = primitiveWidths["Pointer"];
      this->is_pointer = true;
    }
    this->category = "Array";
  }
  string ArrayType::toString(void) {
    string size = this->is_pointer ? "" : to_string( ((NodeINT*) this->size)->value );
    return "(" + this->type->toString() + ")[" + size + "]";
  }
  void ArrayType::printTree(vector<bool> *identation) {
    cout << "\e[1;34mType Array\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->type->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── \e[1;34mSize: \e[0m";
    this->size->printTree(identation);
    identation->pop_back();
  }

  int ArrayType::getSize()
  {
    // We don't know size if is not a literal so placeholder
    return size->is_lit ? ((NodeINT*) size)->value : 999;
  }


/* ======================= BASIC NODES =============================== */
  NodeAssign::NodeAssign(Node *lvalue, Node *rvalue) {
    this->lvalue = lvalue;
    this->rvalue = rvalue;
    this->is_lvalue = false;
  }
  void NodeAssign::printTree(vector<bool> *identation) {
    cout << "\e[1;34mAssignment\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->lvalue->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    cout << "├── =\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->rvalue->printTree(identation);
    identation->pop_back();
  }


  NodeAssignList::NodeAssignList(Node *head, Node *assign) {
    this->head = head;
    this->assign = assign;
  }
  void NodeAssignList::printTree(vector<bool> *identation) {
    cout << "\e[1;34mAssignment List\e[0m\n";
    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }
    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->assign->printTree(identation);
    identation->pop_back();
  }


  NodeI::NodeI(Node *head, Node *inst) {
    this->head = head;
    this->inst = inst;
  }
  void NodeI::printTree(vector<bool> *identation) {
    cout << "\e[1;34mI\e[0m\n";
    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }
    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->inst->printTree(identation);
    identation->pop_back();
  }


  NodeS::NodeS(Node *inst) {
    this->inst = inst;
  }
  void NodeS::printTree(vector<bool> *identation) {
    cout << "\e[1;34mS\e[0m\n";
    vector<bool> *new_identation = new vector<bool>;
    new_identation->push_back(false);
    if (this->inst != NULL) {
      cout << "└── ";
      this->inst->printTree(new_identation);
    }
  }


/* ======================= DATA NODES ================================ */
  NodeBOOL::NodeBOOL(bool value) {
    this->value = value;
    this->type = predefinedTypes["Bool"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeBOOL::printTree(vector<bool> *identation) {
    cout << "BOOL: " << this->value << "\n";
  }


  NodeCHAR::NodeCHAR(char value) {
    this->value = value;
    this->type = predefinedTypes["Char"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeCHAR::printTree(vector<bool> *identation) {
    cout << "CHAR: " << this->value << "\n";
  }


  NodeINT::NodeINT(int value, bool defineType) {
    this->value = value;
    this->type = predefinedTypes["Int"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeINT::printTree(vector<bool> *identation) {
    cout << "INT: " << this->value << "\n";
  }


  NodeFLOAT::NodeFLOAT(float value) {
    this->value = value;
    this->type = predefinedTypes["Float"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeFLOAT::printTree(vector<bool> *identation) {
    cout << "FLOAT: " << this->value << "\n";
  }


  NodeSTRING::NodeSTRING(string value) {
    this->value = value;
    this->type = new ArrayType(predefinedTypes["Char"], new NodeINT(value.size()), true);
    this->is_lvalue = false;
    this->is_lit = false;
  }
  void NodeSTRING::printTree(vector<bool> *identation) {
    cout << "STRING: " << this->value << "\n";
  }


/* ======================= OPERATTION NODES ========================== */
  NodeBinaryOperator::NodeBinaryOperator(
    Node *left, 
    string op, 
    Node *right, 
    Type *type
  ) {
    this->left = left;
    this->op = op;
    this->right = right;
    this->type = type;
    this->is_lvalue = false;
    this->is_lit = false;
  }
  void NodeBinaryOperator::printTree(vector<bool> *identation) {
    cout << "\e[1;34mBinary Operator\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mLeft: \e[0m";
    this->left->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    cout << "├── Operator: " << this->op << "\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── \e[1;34mRight: \e[0m";
    this->right->printTree(identation);
    identation->pop_back();
  }


  NodeUnaryOperator::NodeUnaryOperator(string op, Node *exp, Type *type) {
    this->op = op;
    this->exp = exp;
    this->type = type;
    this->is_lvalue = false;
    this->is_lit = false;
  }
  void NodeUnaryOperator::printTree(vector<bool> *identation) {
    cout << "\e[1;34mUnary Operator\e[0m\n";

    printIdentation(identation);
    cout << "├── Operator: " << this->op << "\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── \e[1;34mOperating: \e[0m";
    this->exp->printTree(identation);
    identation->pop_back();
  }


  NodeID::NodeID(string id, Type *type) {
    this->id = id;
    this->type = type;
    this->is_lvalue = true;
    this->is_lit = false;
  }
  void NodeID::printTree(vector<bool> *identation) {
    cout << "ID: " << this->id << "\n";
  }

  string NodeID::getId()
  {
    return id;
  }


  NodeDot::NodeDot(Node *structure, string id, Type *type) {
    this->structure = structure;
    this->id = id;
    this->type = type;
    this->is_lvalue = true;
    this->is_lit = false;
  }
  void NodeDot::printTree(vector<bool> *identation) {
    cout << "\e[1;34mField Access\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->structure->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    cout << "└── Field: " << this->id << "\n"; 
  }


  NodePointer::NodePointer(Node *pointer, Type *type) {
    this->pointer = pointer;
    this->type = type;
    this->is_lvalue = true;
    this->is_lit = false;
  }
  void NodePointer::printTree(vector<bool> *identation) {
    cout << "\e[1;34mDesreferentation\e[0m\n";

    printIdentation(identation);
    cout << "├── ^\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->pointer->printTree(identation);
    identation->pop_back();
  }


  NodeArrayAccess::NodeArrayAccess(Node *array, Node *index, Type *type) {
    this->array = array;
    this->index = index;
    this->type = type;
    this->is_lvalue = true;
    this->is_lit = false;
  }
  void NodeArrayAccess::printTree(vector<bool> *identation) {
    cout << "\e[1;34mArray Access\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->array->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->index->printTree(identation);
    identation->pop_back();
  }


/* ======================= HEAP NODES ================================ */
  NodeNew::NodeNew(Type *type_pointer) {
    this->type_pointer = type_pointer;
    this->type = new PointerType(type_pointer);
    this->is_lvalue = false;
    this->is_lit = false;
  }
  void NodeNew::printTree(vector<bool> *identation) {
    cout << "\e[1;34mNew\e[0m\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->type->printTree(identation);
    identation->pop_back();
  }


  NodeForget::NodeForget(Node *lvalue) {
    this->lvalue = lvalue;
  }
  void NodeForget::printTree(vector<bool> *identation) {
    cout << "\e[1;34mForget\e[0m\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->lvalue->printTree(identation);
    identation->pop_back();
  }


/* ======================= ARRAY NODES =============================== */
  NodeArray::NodeArray(Node *elems, Type *type) {
    this->elems = elems;
    this->type = type;
    this->is_lvalue = false;
    this->is_lit = false;
  }
  void NodeArray::printTree(vector<bool> *identation) {
    cout << "\e[1;34mArray\e[0m\n";

    if (this->elems != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->elems->printTree(identation);
      identation->pop_back();
    }
  }


  NodeArrayElems::NodeArrayElems(
    NodeArrayElems *head, 
    Type *type, 
    Node *rvalue, 
    int current_size
  ) {
    this->head = head;
    this->rvalue = rvalue;
    this->type = type;
    this->current_size = current_size;
    this->is_lit = false;
  }
  void NodeArrayElems::printTree(vector<bool> *identation) {
    cout << "\e[1;34mArray Element\e[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->rvalue->printTree(identation);
    identation->pop_back();
  }


/* ======================= FUNCTION CALL NODES ======================= */
  NodeFunctionCall::NodeFunctionCall(
    string id, 
    Node *args, 
    bool bEndInst, 
    Type *type
  ) {
    this->id = id;
    this->args = args;
    this->bEndInst = bEndInst;
    this->type = type;
    this->is_lvalue = true;
    this->is_lit = false;
  }
  void NodeFunctionCall::printTree(vector<bool> *identation) {
    cout << "\e[1;34mFunction Call\e[0m\n";

    printIdentation(identation);
    cout << "├── ID: " << this->id << "\n";

    if (this->args != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->args->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mFunction Call Arguments: \e[0mNULL\n";
    }
  }
  void NodeFunctionCall::setEndInst(void) {
    this->bEndInst = true;
  }


  NodeFunctionCallArgs::NodeFunctionCallArgs(Node* positional, Node* named) {
    this->positional = positional;
    this->named = named;
  }
  void NodeFunctionCallArgs::printTree(vector<bool> *identation) {
    cout << "\e[1;34mRoutine Parameters\e[0m\n";

    if ((this->positional != NULL) && (this->named != NULL)) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->positional->printTree(identation);
      identation->pop_back();

      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->named->printTree(identation);
      identation->pop_back();

    } else if (this->positional != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->positional->printTree(identation);
      identation->pop_back(); 

    } else if (this->named != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->named->printTree(identation);
      identation->pop_back(); 

    }
  }


  NodeFunctionCallPositionalArgs::NodeFunctionCallPositionalArgs(Node *head, Node *rvalue) {
    this->head = head;
    this->rvalue = rvalue;
  }
  void NodeFunctionCallPositionalArgs::printTree(vector<bool> *identation) {
    cout << "\e[1;34mPositional Parameter\e[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->rvalue->printTree(identation);
    identation->pop_back();
  }


  NodeFunctionCallNamedArgs::NodeFunctionCallNamedArgs(
    Node *head, 
    string id, 
    Node *rvalue
  ) {
    this->head = head;
    this->id = id;
    this->rvalue = rvalue;
  }
  void NodeFunctionCallNamedArgs::printTree(vector<bool> *identation) {
    cout << "\e[1;34mNamed Parameter\e[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    cout << "├── ID: " + this->id + "\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->rvalue->printTree(identation);
    identation->pop_back();
  }


/* ======================= STRUCTURE DEF NODES ======================= */
  NodeUnionFields::NodeUnionFields(Node *head, Type *type, string id, int max_width) {
    this->head = head;
    this->type = type;
    this->id = id;
    this->max_width = max_width;
  }

  NodeRegFields::NodeRegFields(Node *head, Type *type, string id, Node *rvalue) {
    this->head = head;
    this->type = type;
    this->id = id;
    this->rvalue = rvalue;
  }


/* ======================= CONDITIONAL DEF NODES ===================== */
  NodeConditional::NodeConditional(Node *cond, Node *body, Node *elsifs, Node *elseDef) {
    this->cond = cond;
    this->body = body;
    this->elsifs = elsifs;
    this->elseDef = elseDef;
  }
  void NodeConditional::printTree(vector<bool> *identation) {
    cout << "\e[1;34mIf\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mCondition: \e[0m";
    this->cond->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── \e[1;34mBody: \e[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \e[1;34mBody: \e[0mNULL\n";
    }

    if (this->elsifs != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->elsifs->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \e[1;34mElsif: \e[0mNULL\n";
    }

    if (this->elseDef != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->elseDef->printTree(identation);
      identation->pop_back();
    }  else {
      printIdentation(identation);
      cout << "└── \e[1;34mElse: \e[0mNULL\n";
    }
  }


  NodeElsif::NodeElsif(Node *head, Node *cond, Node *body) {
    this->head = head;
    this->cond = cond;
    this->body = body;
  }
  void NodeElsif::printTree(vector<bool> *identation) {
    cout << "\e[1;34mElsif\e[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mCondition: \e[0m";
    this->cond->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mBody: \e[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mBody: \e[0mNULL\n";
    }
  }


  NodeElse::NodeElse(Node *body) {
    this->body = body;
  }
  void NodeElse::printTree(vector<bool> *identation) {
    cout << "\e[1;34mElse\e[0m\n";

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mBody: \e[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mBody: \e[0mNULL\n";
    }
  }


/* ======================= LOOP NODES ================================ */
  NodeWhile::NodeWhile(Node *cond, Node *body) {
    this->cond = cond;
    this->body = body;
  }
  void NodeWhile::printTree(vector<bool> *identation) {
    cout << "\e[1;34mWhile\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mCondition: \e[0m";
    this->cond->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mBody: \e[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mBody: \e[0mNULL\n";
    }
  }


  NodeFor::NodeFor(Node *sign, Node *body) {
    this->sign = sign;
    this->body = body;
  }
  void NodeFor::printTree(vector<bool> *identation) {
    cout << "\e[1;34mFor\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mFor Sign: \e[0m";
    this->sign->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mBody: \e[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mBody: \e[0mNULL\n";
    }
  }

  NodeForSign::NodeForSign(string iter, Node *begin, Node *end, Node *step) {
    this->iter = iter;
    this->begin = begin;
    this->end = end;
    this->step = step;
  }
  void NodeForSign::printTree(vector<bool> *identation) {
    printIdentation(identation);
    cout << "├── ITERATOR: " << this->iter << "\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mBegin: \e[0m";
    this->begin->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \e[1;34mEnd: \e[0m";
    this->end->printTree(identation);
    identation->pop_back();

    if (this->step != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── \e[1;34mStep: \e[0m";
      this->step->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \e[1;34mStep: \e[0mNULL\n";
    }
  }


/* ======================= SUBROUTINE DEF NODES ====================== */
  NodeRoutineDef::NodeRoutineDef(Node *sign, Node *body) {
    this->sign = sign;
    this->body = body;
  }
  void NodeRoutineDef::printTree(vector<bool> *identation) {
    cout << "\e[1;34mRoutine Definition\e[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->sign->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mBody: \e[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mBody: \e[0mNULL\n";
    }
  }


  NodeRoutineSign::NodeRoutineSign(string id, Node *args, Type *ret) {
    this->id = id;
    this->args = args;
    this->ret = ret;
  }
  void NodeRoutineSign::printTree(vector<bool> *identation) {
    cout << "\e[1;34mRoutine Sign \e[0m\n";

    printIdentation(identation);
    cout << "├── ID: " << this->id << "\n";

    if (this->args != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->args->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \e[1;34mParameters: \e[0mNULL\n";
    }

    if (this->ret != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mReturn Type: \e[0m";
      this->ret->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \e[1;34mReturn Type: \e[0mNULL\n";
    }
  }


  NodeRoutArgs::NodeRoutArgs(Node *oblArgs, Node *optArgs) {
    this->oblArgs = oblArgs;
    this->optArgs = optArgs;
  }
  void NodeRoutArgs::printTree(vector<bool> *identation) {
    cout << "\e[1;34mRoutine Parameters\e[0m\n";

    if ((this->oblArgs != NULL) && (this->optArgs != NULL)) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── \e[1;34mMandatory Parameters: \e[0m";
      this->oblArgs->printTree(identation);
      identation->pop_back();

      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mOptional Parameters: \e[0m";
      this->optArgs->printTree(identation);
      identation->pop_back();

    } else if (this->oblArgs != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mMandatory Parameters: \e[0m";
      this->oblArgs->printTree(identation);
      identation->pop_back(); 

    } else if (this->optArgs != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \e[1;34mOptional Parameters: \e[0m";
      this->optArgs->printTree(identation);
      identation->pop_back(); 
    }
  }


  NodeRoutArgDef::NodeRoutArgDef(Node *head, Type *type, bool ref, string id, Node *rvalue) {
    this->head = head;
    this->type = type;
    this->ref = ref;
    this->id = id;
    this->rvalue = rvalue;
  }
  void NodeRoutArgDef::printTree(vector<bool> *identation) {
    cout << "\e[1;34mParameter Definition\e[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    } 

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->type->printTree(identation);
    identation->pop_back();

    if (this->ref) {
      printIdentation(identation);
      cout << "├── @\n";
    }

    if (this->rvalue != NULL) {
      printIdentation(identation);
      cout << "├── ID: " << this->id << "\n";

      printIdentation(identation);
      cout << "├── =\n";

      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->rvalue->printTree(identation);
      identation->pop_back();

    } else {
      printIdentation(identation);
      cout << "└── ID: " << this->id << "\n"; 
    }
  }


  NodeActions::NodeActions(Node *head, Node *inst) {
    this->head = head;
    this->inst = inst;
  }
  void NodeActions::printTree(vector<bool> *identation) {
    cout << "\e[1;34mAction\e[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── ";
    this->inst->printTree(identation);
    identation->pop_back();
  }


  NodeReturn::NodeReturn(Node *rvalue) {
    this->rvalue = rvalue;
  }
  void NodeReturn::printTree(vector<bool> *identation) {
    cout << "\e[1;34mReturn\e[0m\n";

    if (this->rvalue != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->rvalue->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── Unit\n";
    }
  }
