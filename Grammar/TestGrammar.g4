/*
    Test grammar.
 */

grammar TestGrammar;

// Parser rules.
script
    :	'script' '{' (ID '=' INT)+ '}'
    ;


// Lexer rules.
INT
    :   [0-9]+ ;
ID
    :   [a-zA-Z]+ ;
MUL
    :	'*' ;
DIV
    :	'/' ;
ADD
    :	'+' ;
SUB
    :	'-' ;
GT
    :	'>' ;
GTE
    :	'>=' ;
LT
    :	'<' ;
LTE
    :	'<=' ;
INC
    :   '++' ;
DEC
    :	'--' ;
COMMENT
    :   '#' .*? '\r'? '\n' -> skip ;
WHITESPACE
    :   [ \t\r\n]+ -> skip ;
