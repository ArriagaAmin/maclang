#pragma once

#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>

using namespace std;

/*
  "Abstract" class that is parent of all nodes classes in the 
  Abstract Syntax Tree.
*/
class Node {
  public:
    string addr;
    vector<unsigned long long> truelist;
    vector<unsigned long long> falselist;
    vector<unsigned long long> nextlist;
    bool is_error = false;

    Node(void) {};
    // Print a tree representation of the sub-ast.
    virtual void printTree(vector<bool> *identation) {};
};



/* ======================= TYPES ===================================== */
  /* "Abstract" class that is parent of all type classes. */
  class Type {
    public:
      Type(void) {};

      string category;
      int width;
      // Indica que estamos definiendo una variable de un tipo estructura dentro de la
      // definicion de la estructura, y por lo tanto, solo se puede usar como puntero.
      bool danger = false;
      // Indica el nombre de la estructura que hace del tipo incompleto. "" En caso de
      // no tener un tipo incompleto. Una estructura es incompleta si solo ha sido
      // declarada o si tiene un campo incompleto.
      string incomplete = "";

      // Returns a string representation of the sub ast.
      virtual string toString(void) { return ""; };
      // Print a tree representation of the sub-ast.
      virtual void printTree(vector<bool> *identation) {};
  };

  /* Class for defined types. */
  class PrimitiveType : public Type {
    public:
      string id;

      PrimitiveType(string id);

      string toString(void);

      void printTree(vector<bool> *identation);
  };

  /* Representation of  -> ^ Type. */
  class PointerType : public Type {
    public:
      Type *type;

      PointerType(Type *type);

      string toString(void);

      void printTree(vector<bool> *identation);
  };

  /* Representation of  -> Type [ Exp ]. */
  class ExpressionNode;
  class ArrayType : public Type {
    public: 
      bool is_string;
      bool is_pointer;
      ExpressionNode *size;
      Type *type;

      ArrayType(Type *type, ExpressionNode *size, bool is_string=false);

      int getSize();

      string toString(void);

      void printTree(vector<bool> *identation);
  };


/* ======================= BASIC NODES =============================== */
  class ExpressionNode : public Node {
    public: 
      Type *type;
      bool is_lvalue;
      // Indica si la expresion es una constante de uno de los tipos basicos.
      bool is_lit;

      ExpressionNode(void) {};
      
      virtual void printTree(vector<bool> *identation) {};
  };

  class NodeAssign : public ExpressionNode {
    protected:
      Node *lvalue;
      Node *rvalue;

    public:
      NodeAssign(Node *lvalue, Node *rvalue);

      void printTree(vector<bool> *identation);
  };

  class NodeAssignList : public Node {
    protected:
      Node *head;
      Node *assign;

    public:
      NodeAssignList(Node *head, Node *assign);

      void printTree(vector<bool> *identation);
  };

  /* Representacion of  -> I Inst */
  class NodeI : public Node {
    protected:
      Node *head;
      Node *inst;

    public:
      NodeI(Node *head, Node *inst);

      void printTree(vector<bool> *identation);
  };

  /* Root node. */
  class NodeS {
    protected:
      Node *inst;

    public:
      NodeS(Node *inst);

      void printTree(vector<bool> *identation);
  };

  class NodeError : public Node {
    public:
      string errInfo;

      NodeError(void) { this->is_error = true; }
  };


/* ======================= DATA NODES ================================ */
  class NodeBOOL : public ExpressionNode {
    public:
      bool value;

      NodeBOOL(bool value);

      void printTree(vector<bool> *identation);
  };

  class NodeCHAR : public ExpressionNode {
    public:
      char value;

      NodeCHAR(char value);

      void printTree(vector<bool> *identation);
  };

  class NodeINT : public ExpressionNode {
    public:
      int value;

      NodeINT(int value);

      void printTree(vector<bool> *identation);
  };

  class NodeFLOAT : public ExpressionNode {
    public:
      float value;

      NodeFLOAT(float value);

      void printTree(vector<bool> *identation);
  };

  class NodeSTRING : public ExpressionNode {
    public:
      string value;

      NodeSTRING(string value);

      void printTree(vector<bool> *identation);
  };


/* ======================= OPERATION NODES =========================== */
  class NodeBinaryOperator : public ExpressionNode {
    protected:
      Node *left;
      string op;
      Node *right;

    public:
      NodeBinaryOperator(Node *left, string op, Node *rigth, Type *type);

      void printTree(vector<bool> *identation);
  };

  class NodeUnaryOperator : public ExpressionNode {
    protected:
      string op;
      Node *exp;

    public:
      NodeUnaryOperator(string op, Node *exp, Type *type);

      void printTree(vector<bool> *identation);
  };

  class NodeID : public ExpressionNode {
    protected:
      string id;

    public:
      NodeID(string id, Type *type);

      string getId();

      void printTree(vector<bool> *identation);
  };

  class NodeDot : public ExpressionNode {
    protected:
      Node *structure;
      string id;

    public:
      NodeDot(Node *structure, string id, Type *type);

      void printTree(vector<bool> *identation);
  };

  class NodePointer : public ExpressionNode {
    protected:
      Node *pointer;

    public:
      NodePointer(Node *pointer, Type *type);

      void printTree(vector<bool> *identation);
  };

  class NodeArrayAccess : public ExpressionNode {
    protected:
      Node *array;
      Node *index;

    public:
      NodeArrayAccess(Node *array, Node *index, Type *type);

      void printTree(vector<bool> *identation);
  };


/* ======================= HEAP NODES ================================ */
  /* Representation of  -> new Type. */
  class NodeNew : public ExpressionNode {
    protected:
      Type *type_pointer;

    public:
      NodeNew(Type *type_pointer);

      void printTree(vector<bool> *identation);
  };

  /* Representation of  -> forget Type. */
  class NodeForget : public Node {
    protected:
      Node *lvalue;

    public:
      NodeForget(Node *lvalue);

      void printTree(vector<bool> *identation);
  };


/* ======================= ARRAY NODES =============================== */
  class NodeArray : public ExpressionNode {
    protected:
      Node *elems;

    public:
      NodeArray(Node *elems, Type *type);

      void printTree(vector<bool> *identation);
  };

  /* Representation of  ->  RValue , ArrElems. */
  class NodeArrayElems : public ExpressionNode {
    public:
      NodeArrayElems *head;
      Node *rvalue;
      int current_size;

      NodeArrayElems(NodeArrayElems *head, Type *type, Node *rvalue, int current_size);

      void printTree(vector<bool> *identation);
  };


/* ======================= FUNCTION CALL NODES ======================= */
  /* Representation of function calls. */
  class NodeFunctionCall : public ExpressionNode {
    protected:
      string id;
      Node *args;
      bool bEndInst;

    public:
      NodeFunctionCall(string id, Node *args, bool bEndInst, Type *type);

      void printTree(vector<bool> *identation);

      void setEndInst(void);
  };

  class NodeFunctionCallArgs : public Node {
    protected:
      Node* positional;
      Node* named;

    public:
      vector<ExpressionNode*> positionalArgs;
      map<string, ExpressionNode*> namedArgs;
      set<string> keywords;

      NodeFunctionCallArgs(Node* positional, Node* named);

      void printTree(vector<bool> *identation);
  };

  /* Representation of position arguments when calling a function */
  class NodeFunctionCallPositionalArgs : public Node {
    protected:
      Node *head;
      Node *rvalue;

    public:
      vector<ExpressionNode*> currentArgs;

      NodeFunctionCallPositionalArgs(Node *head, Node *rvalue);

      void printTree(vector<bool> *identation);
  };

  /* Representation of named arguments when calling a function */
  class NodeFunctionCallNamedArgs : public Node {
    protected:
      Node *head;
      string id;
      Node *rvalue;

    public:
      map<string, ExpressionNode*> currentArgs;
      set<string> keywords;

      NodeFunctionCallNamedArgs(Node *head, string id, Node *rvalue);

      void printTree(vector<bool> *identation);
  };


/* ======================= STRUCTURE DEF NODES ======================= */
  /* Representation of  -> UnionBody Type ID ; */
  class NodeUnionFields : public Node {
    protected:
      Node *head;
      Type *type;
      string id;

    public:
      int max_width;
      vector<string> incompletes = {};
      NodeUnionFields(Node *head, Type *type, string id, int max_width);
  };

  /* Representation of  -> RegisterBody VarDefBody; */
  class NodeRegFields : public Node {
    protected:
      Node *head;
      Type *type;
      string id;
      Node *rvalue;

    public:
      vector<string> incompletes = {};
      NodeRegFields(Node *head, Type *type, string id, Node *rvalue);
  };


/* ======================= CONDITIONAL DEF NODES ===================== */
  /* Representation of if-elsif-else blocks. */
  class NodeConditional : public Node {
    protected:
      Node *cond;
      Node *body;
      Node *elsifs;
      Node *elseDef;

    public:
      NodeConditional(Node *cond, Node *body, Node *elsifs, Node *elseDef);

      void printTree(vector<bool> *identation);
  };

  /* Representation of  -> Elsifs elsif Exp then I. */
  class NodeElsif : public Node {
    protected:
      Node *head;
      Node *cond;
      Node *body;

    public:
      NodeElsif(Node *head, Node *cond, Node *body);

      void printTree(vector<bool> *identation);
  };

  /* Representation of  -> else I. */
  class NodeElse : public Node {
    protected:
      Node *body;

    public:
      NodeElse(Node *body);

      void printTree(vector<bool> *identation);
  };


/* ======================= LOOP NODES ================================ */
  /* Representation of while blocks. */
  class NodeWhile : public Node {
    protected:
      Node *cond;
      Node *body;

    public:
      NodeWhile(Node *cond, Node *body);

      void printTree(vector<bool> *identation);
  };

  /* Representation of for blocks. */
  class NodeFor : public Node {
    protected:
      Node *sign;
      Node *body;

    public:
      NodeFor(Node *sign, Node *body);

      void printTree(vector<bool> *identation);
  };

  class NodeForSign : public Node {
    protected:
      string iter;
      Node *begin;
      Node *end;

    public:
      string label;
      Node *step;

      NodeForSign(string iter, Node *begin, Node *end, Node *step);

      void printTree(vector<bool> *identation);
  };


/* ======================= SUBROUTINE DEF NODES ====================== */
  /* Representation of routine definitions. */
  class NodeRoutineDef : public Node {
    protected:
      Node *sign;
      Node *body;

    public:
      NodeRoutineDef(Node *sign, Node *body);

      void printTree(vector<bool> *identation);
  };

  class NodeRoutineSign : public Node {
    protected:
      string id;
      Node *args;
      Type *ret;

    public:
      NodeRoutineSign(string id, Node *args, Type *ret);

      void printTree(vector<bool> *identation);
  };

  class NodeRoutArgs : public Node {
    protected:
      Node *oblArgs;
      Node *optArgs;

    public:
      vector<tuple<string, string, bool, ExpressionNode*>> params;

      NodeRoutArgs(Node *oblArgs, Node *optArgs);

      void printTree(vector<bool> *identation);
  };

  class NodeRoutArgDef : public Node {
    protected:
      Node *head; 
      Type *type; 
      bool ref; 
      string id; 
      Node *rvalue;

    public:
      vector<tuple<string, string, bool, ExpressionNode*>> currentParams;
      
      NodeRoutArgDef(Node *head, Type *type, bool ref, string id, Node *rvalue);

      void printTree(vector<bool> *identation);
  };

  /* Representacion of  -> Actions Action */
  class NodeActions : public Node {
    protected:
      Node *head;
      Node *inst;

    public:
      NodeActions(Node *head, Node *inst);

      void printTree(vector<bool> *identation);
  };

  class NodeReturn : public Node {
    protected:
      Node *rvalue;

    public:
      NodeReturn(Node *rvalue = NULL);

      void printTree(vector<bool> *identation);
  };

