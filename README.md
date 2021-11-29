# **MACLang**

*MACLang* is a programming languages developed for course **CI4721 - Programing** 
**Languages II** dictated at Universidad Simón Bolívar (Caracas, Venezuela) in the 
term April-July 2021, by professor Ricardo Monascal.

## Dependencies
* flex *(2.6.4)*
* bison *(3.3.2)*
* g++ *(8.3.0)*

## How to use it

**WIP:** Parsing, Lexing and Symbols Table
The project contains a *Makefile*, thus you just need to run `make` and i1t
will compile the source code. After that, you can execute the program with:

```
&> ./bin/parser.out METHOD [OPTIONS] FILE
```

Where `FILE` represents the path to the file to be parsed and `MEHTOD` could 
have the following values:
  
  * `lex`: prints just the lexical analysis with all tokens recognized by the 
    lexer if there isn't any errors. In case of errors will print the exact 
    position in the input file where there's an invalid token.
  * `parse`: For this method, there're 2 available options, which you need to 
    pick at least one in order to work.
      * `-c`: Prints the represensation with all the asociativities in an 
        explicit way. (All parenthesis). 
      * `-t`: Prints a tree representation of the Absteract Syntax Tree (AST) 
        created by the parser in a redable way. If there're erros, it will
        print just the first one.   
  * `symbols`: Prints the representation of the symbols table. In case there's 
    redeclarations of variables, it will print those redeclarations.

## TAC 

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
      | call    LVal ID
      | printc  Val
      | printi  Val
      | printf  Val
      | print   ID
      | readc   Val
      | readi   Val
      | readf   Val
      | read    ID

F    -> @function ID INT \n Inst @endfunction INT

Inst -> *lambda*
      | I \n Inst

Acc  -> ID [ Val ]
LVal -> ID | Acc
Val  -> TRUE | FALSE | CHAR | INT | FLOAT | ID
RVal -> Val | Acc
```

## Developers
* Amin Arriaga *(16-10072)*
* Manuel Faria *(15-10463)*
* Orlando Chaparro *(12-11499)*   
