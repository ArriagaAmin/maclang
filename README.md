<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Eumaclang</h1>

  <p align="center">
    A general-purpose programming language
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#maclang">maclang</a></li>
        <li><a href="#tac2mips">tac2mips</a></li>
      </ul>
    </li>
    <li>
      <a href="#language-specification">Language Specification</a>
      <ul>
        <li><a href="#comments">Comments</a></li>
        <li><a href="#primitive-types-and-variables">Primitive types and variables</a></li>
        <li><a href="#arrays">Arrays</a></li>
        <li><a href="#strings">Strings</a></li>
        <li><a href="#pointers">Pointers</a></li>
        <li><a href="#registers-and-unions">Registers and Unions</a></li>
        <li><a href="#flow-control-instructions">Flow control instructions</a></li>
        <li><a href="#functions">Functions</a></li>
        <li><a href="#input-and-output">I/O</a></li>
        <li><a href="#imports">Imports</a></li>
      </ul>
    </li>
    <li><a href="#tac">TAC</a></li>
    <li><a href="#developers">Developers</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## **About The Project**

*Eumaclang* is a general-purposed programming language developed in the courses **CI4721**
**- Programming Languages II** and **CI4722 - Programming Languages III** in the terms 
April-July 2021 and September-December 2021 respectively at the Universidad Simón Bolívar 
(Caracas, Venezuela), both courses given by Professor Ricardo Monascal. 

### **Built With**

* [Flex *(2.6.4)*](https://github.com/westes/flex)
* [Bison *(3.3.2)*](https://www.gnu.org/software/bison/)
* [g++ *(8.3.0)*](https://gcc.gnu.org/onlinedocs/)

<!-- GETTING STARTED -->
## **Getting Started**

The project contains a *Makefile*, thus you just need to run: 

```bash
$ make
``` 

and i1t will compile the source code.

## **Usage**

### **eumaclang**

To process the original source code use:

```bash
$ ./bin/maclang ACTION FILE
```

Where `FILE` represents the path to the file to be parsed and `ACTION` could 
have the following values:
  
  * `lex`: prints just the lexical analysis with all tokens recognized by the lexer if 
      there isn't any errors. In case of errors will print the exact position in the 
      input file where there's an invalid token.
  * `symbols`: Prints the representation of the symbols table. In case there's 
      redeclarations of variables, it will print those redeclarations.
  * `parse`: Prints a tree representation of the Absteract Syntax Tree (AST) created by 
      the parser in a redable way. If there're erros, it will print just the first one.  
  * `tac`: Generate and print the three-address code (TAC) that represents the original 
      code. 

### **tac2mips**

Translate the generated TAC code to MIPS code

```bash
$ ./bin/tac2mips FILE
```

Where `FILE` represents the path to the file to translate

## **Language Specification**

### **Comments**

Line comments will start with the character `#`, while comments multilines will be 
started and ended by `$ {` and `} $` respectively. For example

```
# Line comment.
${
  Multi
  lines
  comment
}$
```

### **Primitive types and variables**

The language will have 5 primitive types:

  * `Int` (Integers 2's complement)
  * `Char` (Characters ASCII). Character literals are enclosed in single quotes. You can 
      define the i-th ASCII character using `\` followed by i, for example `'\42'`. The 
      following special characters can also be used: `'\''`, `'\\'`, `'\a'`, `'\b'`, 
      `'\f'`, `'\n'`, `'\r'`, `'\t'` and `'\v'`.
  * `Bool` (Booleans `True` and` False`)
  * `Float` (Floating point numbers, IEEE 754, single precision)
  * `Unit` (Type of functions that do not return any value)

To initialize a variable the following syntax is used

```
let TYPE VARLIST [= EXPLIST];
```

Where VARLIST is a list of identifiers that represent the variables, and EXPLIST is a 
list of expressions that will be assigned to the variables. Both VARLIST and EXPLIST must 
be the same length. The i-th variable will be assigned the i-th expression. Each 
expression must correspond to the indicated type. Cannot declare variable of type `Unit`.
For example:

```
let Int x, y, z = 0, 42 + 69, -1 * 1;
```

Operations between basic types:

  * `==` and `!=` can be used to compare basic types with each other, it also works 
      between integers and floats.
  * `<`, `<=`, `>` and `>=` can be used to compare integers, floats and characters with 
      each other, it also works between integers and floats. A character `c0` is less 
      than another `c1` iff the ASCII representation of `c0` is less than that of `c1`.
  * `+`, `-`, `*` and `/` represent the operations of addition, subtraction, 
      multiplication and division respectively between integers and floats. If both 
      operands are integers, the result will be an integer, otherwise the result will 
      be a float.
  * `%` is the mod operation between integers.
  * `**` is the power operation such that the base can be integer or float but the 
      exponent must be integer.
  * `=` is used to assign an expression to an l-value, in addition to the fact that the
      complete expression will be equal to the one assigned. For example `i = (j = 0)` 
      assign 0 to both j and i.

There are the following functions to convert between basic types:

|      |Int                                |Float                                |String                       |
|------|-----------------------------------|-------------------------------------|-----------------------------|
|Char  |`ctoi(Char c) => Int`              |                                     |                             |
|Int   |                                   |`itof(Int n) => Float`               |`itos(String @text, Int n)`  |
|Float |`ftoi(Float n) => Int`             |                                     |`ftos(String @text, Float n)`|
|String|`stoi(String text, Int @n) => Bool`|`stof(String text, Float @n) => Bool`|                             |

where `ctoi` convert a char to its ASCII representation.

### **Arrays**

To declare a variable of type array we use the type `TYPE[N]` where `TYPE` is the type of
elements, which must be different from` Unit`, and `N` the number of elements that the 
array will have. Since arrays are dynamic, they can also be declared using the type 
`TYPE[]` such that the variable will be an array of `TYPE` but empty. For example:

```
let Int[42] A;
let Float[] F;
```

Array of arrays can also be declared

```
let Char[100][][42] S;
```

You can also declare literal arrays, like `[0,1,2,42,4]`. The operations defined on 
arrays are: 

  * Assignment `=`
  * Indexing `[]`
  * Assignment indexing `[]=`

### **Strings**

Strings will be defined as arrays of characters. However, the language will include 
syntactic sugar to declare it as a `String` type, which would be equivalent to the 
`Char[]` type. For instance:

```
let String hello = "world";
let String aja = ['a', 'y', ' ', 'n', 'o', '\n'];
let Char[] ohno = "ohwell";
let Char[] press = ['F'];
```

Therefore, the `String` type has the same operations defined as arrays. It is important 
to note that single quotes (`'`) will be used for the characters, while for strings 
double quotes (`"`) will be used. It should be noted that for strings the assumption is 
made that they end with the character `'\0'`, therefore, if an array is used as a string,
the character `'\0'` should be manually placed at the end.

### **Pointers**

Pointer types are defined as `^TYPE` and have the following properties:

  * `TYPE` cannot by `Unit`.
  * The only operations that pointers support are assigning `=` and dereferencing `^`.
  * When specifying a type, `^` references take precedence over `[]` arrays, that is, 
      `^TYPE[]` is equivalent to `(^TYPE)[]`.
  * Similarly, dereference has higher precedence than indexing or indexed assignment.
      That is, `^VAR[i]` isequivalent to `(^VAR)[i]`.
  * As we have already seen, this precedence can be modified using parentheses. 
      For example `^(TYPE[])` indicates the type pointer to an array of variables of 
      type `TYPE`.
  * To create a reference of a type use the keyword `new`, for example:
```
let ^Int ref = new Int;
```
  * The type `^Unit` has only one instance: `NULL`. It can be assigned to any pointer. 
      `NULL` cannot be assigned, except for itself. Dereferencing `NULL` raises an error.
  * As a counterpart to `new`, there will be the `forget` keyword to free the memory 
      occupied by a reference. For instance:
```
forget ref;
```

### **Registers and Unions**

The definition of registers will follow the following structure:

```
register NAME {
  TYPE FIELD [= DEFAULT];
  ...
}
```

While the definition of unions follows the following structure:

```
union NAME {
  TYPE FIELD;
  ...
}
```

Once defined, they can be used as one more type of language. The only operations defined 
on them are field access (`.`) and assignment. For instance:

```
union NodeVal {
  Int i;
  Float f;
  Char c;
}

register Node {
  ^Node next = NULL;
  String ID;
  NodeVal val;
}
let Node[10] N;
N[0].ID = "lorem";
N[0].val.i = -1;
```

Registers or unions can be declared before defining them using the `structure` 
declaration, which follows the syntax:

```
structure NAME;
```

They can then be used in the definition of other unions or registers before being 
defined. You must be careful because an incomplete structure, which is defined as those 
that have only been declared or have an incomplete type field, cannot be used in 
variable declarations, function arguments or function returns. Also, an incomplete 
structure can only be used as a field if it is "wrapped" by a pointer. Example:

```
structure NodeList;
structure NodeVal;

register Node {
  ^NodeList succs;
  ^NodeVal val;
  String ID;
}

union NodeVal {
  Int i;
  Float f;
  Char c;
}

register NodeList {
  Node[] nodes;
}
```

You cannot declare or define records or unions within the definition of a function, but 
in the rest of scopes and their scope works the same as that of variables. Therefore, 
there can be multiple definitions for the same declaration. For example:

```
structure A;

if var then
  register A {
    Int a;
  }
else 
  union A {
    Int a;
  }
done 
```

### **Flow control instructions**

Conditionals:

```
if CONDITION then
  INSTRUCTION
  ...
[elsif CONDITION then
  INSTRUCTION
  ...]
...
[else
  INSTRUCTION
  ...]
done
```

Undetermined loops:

```
while CONDITION do
  INSTRUCTIONS
  ...
done
```

Determined loops:

```
for (ID; BEGIN; END [; STEP]) do
  INSTRUCTIONS
  ...
done
```

where `BEGIN`, `END` and `STEP` must be integers.

### **Functions**

Function definition syntax:

```
def FUNCTION(TYPE [@]ID [=EXP], ...) [=> TYPE] {
  INSTRUCTIONS;
  ...
}
```

Where `@` indicates that the argument is passed by reference, otherwise a copy of the 
argument is passed, even if it is of type compound. Optional values must be the last to 
be declared. Cannot define functions within the definition of other functions. Example:

```
def F(
    Int a, 
    Char @c, 
    ^Int i = new Int, 
    String @w = "tf?", 
    Bool[1] b = [False]
) => ^Int {
  return i;
}
```

Function call syntax

```
FUNCTION([ID=] EXP, ...)
```

Where named parameters should be placed at the end of the call. Example:

```
let Char c;
F(0, w="hat?", c=c);
```

You can also declare functions before they are defined using the `dec` declaration:

```
dec FUNCTION(TYPE [@]ID [=EXP], ...) [=> TYPE];
```

Like structures, as a function can be defined in different scopes (except within the 
definition of another function), then there can be definitions of the same declaration.
The scope of the definitions of the functions is equal to that of the variables. For
example:

```
dec A(Int i);

if var then
  def B() {
    A(0);
  }
  def A(Int i) {
    return i;
  }
else 
  def A(Int i) {
    return -1;
  }
done

def A(Int i) {
  return 0;
}
```

### **Input and output**

To print, the `print` function is used which has the following signature (the empty 
array cannot actually be used in the language):

```
def print(
  String buffer, 
  Char[] chars=[], 
  Int[] inst=[], 
  Float[] floats=[], 
  String[] strings=[],
  String end=['\n']
)
```

where `buffer` is the text to be printed and allows the following symbols to be used to 
replace them with an expression:

  * `"%c"` will be replaced by a character in the array `chars`.
  * `"%i"` will be replaced by a integer in the array `ints`.
  * `"%f"` will be replaced by a float in the array `floats`.
  * `"%s"` will be replaced by a string in the array `strings`.
  * `"%%"` will be replaced by `"%"`.

The replacements are done in order, that is, the first occurrence of `"%i"` will be 
replaced by the first element of `ints`. And `end` is what will be printed at the end.
Example:

```
print(
  "%c%cThe ID and value of the %i-th node is: %c%s%c%f%c",
  chars=['\t', '\t', '\n', '\n', '\n'],
  ints=[42],
  strings=["Mynode"],
  floats=[3.1415],
  end="."
)
```

Would print

```
        The ID and value of the 42-th node is: 
Mynode
3.1415
.
```

Then we have the following reading functions:

  * `read(String buffer)`
  * `readc() => Char`
  * `readi() => Int`
  * `readf() => Float`

### **Imports**

Although the language does not have an import statement, it does have an execute
statement that allows executing a specified file:

```
exec STRING;
execonce STRING;
```

`exec` executes the indicated file, it is equivalent to placing said file on the line 
where the `exec` is placed. Whereas `execonce` only executes the file if it has not been 
executed before. Example:

```
exec "myfile";
execonce "myfile2";
```

## **TAC**

The grammar that defines the TAC generated in the project is

```
S    -> Data Text

Data -> *lambda* 
      | D Data

D    -> @staticv INT \n
      | @string  STRING \n

Text -> *lambda*
      | T \n Text 

T    -> I 
      | F

I    -> *lambda*
      | @label ID
      | assignw Acc Val
      | assignw ID RVal
      | assignb Acc Val
      | assignb ID RVal
      | add     ID Val Val
      | sub     ID Val Val
      | mult    ID Val Val
      | div     ID Val Val
      | mod     ID Val Val
      | minus   ID Val
      | eq      ID Val Val
      | neq     ID Val Val
      | lt      ID Val Val
      | leq     ID Val Val
      | gt      ID Val Val
      | geq     ID Val Val
      | goto    ID
      | goif    ID Val
      | goifnot ID Val
      | malloc  ID Val
      | memcpy  ID ID INT
      | free    ID
      | exit    Val
      | param   ID Val
      | return  Val
      | call    ID ID
      | printc  Val
      | printi  Val
      | printf  Val
      | print   ID
      | readc   ID
      | readi   ID
      | readf   ID
      | read    ID

F    -> @function ID INT \n Inst @endfunction INT

Inst -> *lambda*
      | I \n Inst

Acc  -> ID [ Val ]
Val  -> TRUE | FALSE | CHAR | INT | FLOAT | ID
RVal -> Val | Acc
```

## **Developers**

* Amin Arriaga *(16-10072)*
* Kevin Mena *(13-10869)*
* Manuel Faria *(15-10463)*
* Orlando Chaparro *(12-11499)*
* Ricardo Monascal