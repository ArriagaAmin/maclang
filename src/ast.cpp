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
    {"Unit",    0},
    {"Bool",    1},
    {"Char",    1},   // ASCII
    {"Int",     4},
    {"Float",   4},
    {"Pointer", 4},
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
    cout << "\033[1;34mType Pointer\033[0m\n";

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
    this->width = primitiveWidths["Pointer"];
    this->category = "Array";
  }
  string ArrayType::toString(void) {
    return "(" + this->type->toString() + ")[]";
  }
  void ArrayType::printTree(vector<bool> *identation) {
    cout << "\033[1;34mType Array\033[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->type->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── \033[1;34mSize: \033[0m";
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
    cout << "\033[1;34mAssignment\033[0m\n";

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
    cout << "\033[1;34mAssignment List\033[0m\n";
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
    cout << "\033[1;34mI\033[0m\n";
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

  NodeExec::NodeExec(string filename, Node *ast) {
    this->filename = filename;
    this->ast = ast;
  }
  void NodeExec::printTree(vector<bool> *identation) {
    cout << "\033[1;34mExec \033[0m(\033[1m" + this->filename + "\033[0m)\n";
    if (this->ast != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->ast->printTree(identation);
      identation->pop_back();
    }
  }


  NodeS::NodeS(Node *inst) {
    this->inst = inst;
  }
  void NodeS::printTree(vector<bool> *identation) {
    cout << "\033[1;34mS\033[0m\n";
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
    cout << "BOOL: \033[1;36m" << (this->value ? "True" : "False") << "\033[0m\n";
  }


  NodeCHAR::NodeCHAR(char value) {
    this->value = value;
    this->type = predefinedTypes["Char"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeCHAR::printTree(vector<bool> *identation) {
    cout << "CHAR: \033[1;36m" << this->value << "\033[0m\n";
  }


  NodeINT::NodeINT(int value) {
    this->value = value;
    this->type = predefinedTypes["Int"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeINT::printTree(vector<bool> *identation) {
    cout << "INT: \033[1;36m" << this->value << "\033[0m\n";
  }


  NodeFLOAT::NodeFLOAT(float value) {
    this->value = value;
    this->type = predefinedTypes["Float"];
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeFLOAT::printTree(vector<bool> *identation) {
    cout << "FLOAT: \033[1;36m" << this->value << "\033[0m\n";
  }


  NodeSTRING::NodeSTRING(string value) {
    value.erase(0, 1);
    value[value.size() - 1] = '\0';
    this->value = value;
    this->type = new ArrayType(predefinedTypes["Char"], new NodeINT(value.size()), true);
    this->is_lvalue = false;
    this->is_lit = true;
  }
  void NodeSTRING::printTree(vector<bool> *identation) {
    cout << "STRING: \033[1;36m" << this->value << "\033[0m\n";
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
    cout << "\033[1;34mBinary Operator\033[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \033[1;34mLeft: \033[0m";
    this->left->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    cout << "├── Operator: " << this->op << "\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── \033[1;34mRight: \033[0m";
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
    cout << "\033[1;34mUnary Operator\033[0m\n";

    printIdentation(identation);
    cout << "├── Operator: " << this->op << "\n";

    printIdentation(identation);
    identation->push_back(false);
    cout << "└── \033[1;34mOperating: \033[0m";
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
    cout << "ID: \033[1;3m" << this->id << "\033[0m\n";
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
    cout << "\033[1;34mField Access\033[0m\n";

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
    cout << "\033[1;34mDesreferentation\033[0m\n";

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
    cout << "\033[1;34mArray Access\033[0m\n";

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
    cout << "\033[1;34mNew\033[0m\n";

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
    cout << "\033[1;34mForget\033[0m\n";

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
    cout << "\033[1;34mArray\033[0m\n";

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
    cout << "\033[1;34mArray Element\033[0m\n";

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
    cout << "\033[1;34mFunction Call\033[0m\n";

    printIdentation(identation);
    cout << "├── \033[1;3m" << this->id << "\033[0m\n";

    if (this->args != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->args->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mFunction Call Arguments: \033[0mNULL\n";
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
    cout << "\033[1;34mRoutine Parameters\033[0m\n";

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
    cout << "\033[1;34mPositional Parameter\033[0m\n";

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
    cout << "\033[1;34mNamed Parameter\033[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    cout << "├── ID: \033[1;3m" + this->id + "\033[0m\n";

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
    cout << "\033[1;34mIf\033[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \033[1;34mCondition: \033[0m";
    this->cond->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── \033[1;34mBody: \033[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \033[1;34mBody: \033[0mNULL\n";
    }

    if (this->elsifs != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->elsifs->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \033[1;34mElsif: \033[0mNULL\n";
    }

    if (this->elseDef != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->elseDef->printTree(identation);
      identation->pop_back();
    }  else {
      printIdentation(identation);
      cout << "└── \033[1;34mElse: \033[0mNULL\n";
    }
  }


  NodeElsif::NodeElsif(Node *head, Node *cond, Node *body) {
    this->head = head;
    this->cond = cond;
    this->body = body;
  }
  void NodeElsif::printTree(vector<bool> *identation) {
    cout << "\033[1;34mElsif\033[0m\n";

    if (this->head != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->head->printTree(identation);
      identation->pop_back();
    }

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \033[1;34mCondition: \033[0m";
    this->cond->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mBody: \033[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mBody: \033[0mNULL\n";
    }
  }


  NodeElse::NodeElse(Node *body) {
    this->body = body;
  }
  void NodeElse::printTree(vector<bool> *identation) {
    cout << "\033[1;34mElse\033[0m\n";

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mBody: \033[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mBody: \033[0mNULL\n";
    }
  }


/* ======================= LOOP NODES ================================ */
  NodeWhile::NodeWhile(Node *cond, Node *body) {
    this->cond = cond;
    this->body = body;
  }
  void NodeWhile::printTree(vector<bool> *identation) {
    cout << "\033[1;34mWhile\033[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \033[1;34mCondition: \033[0m";
    this->cond->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mBody: \033[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mBody: \033[0mNULL\n";
    }
  }


  NodeFor::NodeFor(Node *sign, Node *body) {
    this->sign = sign;
    this->body = body;
  }
  void NodeFor::printTree(vector<bool> *identation) {
    cout << "\033[1;34mFor\033[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \033[1;34mFor Sign: \033[0m";
    this->sign->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mBody: \033[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mBody: \033[0mNULL\n";
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
    cout << "├── \033[1;34mBegin: \033[0m";
    this->begin->printTree(identation);
    identation->pop_back();

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── \033[1;34mEnd: \033[0m";
    this->end->printTree(identation);
    identation->pop_back();

    if (this->step != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "└── \033[1;34mStep: \033[0m";
      this->step->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mStep: \033[0m 1\n";
    }
  }


/* ======================= SUBROUTINE DEF NODES ====================== */
  NodeRoutineDef::NodeRoutineDef(Node *sign, Node *body) {
    this->sign = sign;
    this->body = body;
  }
  void NodeRoutineDef::printTree(vector<bool> *identation) {
    cout << "\033[1;34mRoutine Definition\033[0m\n";

    printIdentation(identation);
    identation->push_back(true);
    cout << "├── ";
    this->sign->printTree(identation);
    identation->pop_back();

    if (this->body != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mBody: \033[0m";
      this->body->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mBody: \033[0mNULL\n";
    }
  }


  NodeRoutineSign::NodeRoutineSign(string id, Node *args, Type *ret) {
    this->id = id;
    this->args = args;
    this->ret = ret;
  }
  void NodeRoutineSign::printTree(vector<bool> *identation) {
    cout << "\033[1;34mRoutine Sign \033[0m\n";

    printIdentation(identation);
    cout << "├── ID: \033[1;3m" << this->id << "\033[0m\n";

    if (this->args != NULL) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── ";
      this->args->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "├── \033[1;34mParameters: \033[0mNULL\n";
    }

    if (this->ret != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mReturn Type: \033[0m";
      this->ret->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── \033[1;34mReturn Type: \033[0mNULL\n";
    }
  }


  NodeRoutArgs::NodeRoutArgs(Node *oblArgs, Node *optArgs) {
    this->oblArgs = oblArgs;
    this->optArgs = optArgs;
  }
  void NodeRoutArgs::printTree(vector<bool> *identation) {
    cout << "\033[1;34mRoutine Parameters\033[0m\n";

    if ((this->oblArgs != NULL) && (this->optArgs != NULL)) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── \033[1;34mMandatory Parameters: \033[0m";
      this->oblArgs->printTree(identation);
      identation->pop_back();

      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mOptional Parameters: \033[0m";
      this->optArgs->printTree(identation);
      identation->pop_back();

    } else if (this->oblArgs != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mMandatory Parameters: \033[0m";
      this->oblArgs->printTree(identation);
      identation->pop_back(); 

    } else if (this->optArgs != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mOptional Parameters: \033[0m";
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
    cout << "\033[1;34mParameter Definition\033[0m\n";

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

    if (this->rvalue != NULL) {
      printIdentation(identation);
      cout << "├── " << (this->ref ? "@" : "") << "ID: \033[1;3m" << this->id << "\033[0m\n";

      printIdentation(identation);
      cout << "├── =\n";

      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->rvalue->printTree(identation);
      identation->pop_back();

    } else {
      printIdentation(identation);
      cout << "└── " << (this->ref ? "@" : "") << "ID: \033[1;3m" << this->id << "\033[0m\n"; 
    }
  }


  NodeActions::NodeActions(Node *head, Node *inst) {
    this->head = head;
    this->inst = inst;
  }
  void NodeActions::printTree(vector<bool> *identation) {
    cout << "\033[1;34mAction\033[0m\n";

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
    cout << "\033[1;34mReturn\033[0m\n";

    if (this->rvalue != NULL) {
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── ";
      this->rvalue->printTree(identation);
      identation->pop_back();
    } else {
      printIdentation(identation);
      cout << "└── Unit\n";
    }
  }


/* ======================= SUBROUTINE DEC NODES ====================== */
  NodeRoutDecArgs::NodeRoutDecArgs(Node *oblArgs, Node *optArgs) {
    this->oblArgs = oblArgs;
    this->optArgs = optArgs;
  }
  void NodeRoutDecArgs::printTree(vector<bool> *identation) {
    cout << "\033[1;34mRoutine Declaration Parameters\033[0m\n";

    if ((this->oblArgs != NULL) && (this->optArgs != NULL)) {
      printIdentation(identation);
      identation->push_back(true);
      cout << "├── \033[1;34mMandatory Parameters: \033[0m";
      this->oblArgs->printTree(identation);
      identation->pop_back();

      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mOptional Parameters: \033[0m";
      this->optArgs->printTree(identation);
      identation->pop_back();

    } else if (this->oblArgs != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mMandatory Parameters: \033[0m";
      this->oblArgs->printTree(identation);
      identation->pop_back(); 

    } else if (this->optArgs != NULL){
      printIdentation(identation);
      identation->push_back(false);
      cout << "└── \033[1;34mOptional Parameters: \033[0m";
      this->optArgs->printTree(identation);
      identation->pop_back(); 
    }
  }


  NodeRoutDecArgDef::NodeRoutDecArgDef(Node *head, Type *type, bool ref, string id, bool opt) {
    this->head = head;
    this->type = type;
    this->ref = ref;
    this->id = id;
    this->opt = opt;
  }
  void NodeRoutDecArgDef::printTree(vector<bool> *identation) {
    cout << "\033[1;34mParameter Definition\033[0m\n";

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

    printIdentation(identation);
    cout << "└── " << (this->opt ? "optional " : "") << (this->ref ? "@" : "") 
      << "ID: \033[1;3m" << this->id << "\033[0m\n"; 
  }