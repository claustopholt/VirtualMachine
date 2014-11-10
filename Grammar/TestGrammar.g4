/*
    Test grammar.
 */

grammar TestGrammar;


// Parser rules.
script
    :	'script' '{' (statement)+ '}'
    ;

statement
    :	varAssign
    |	ifStatement
    |   outputCall
    |	expr ';'
    ;

varAssign
    :	ID '=' expr ';'
    ;

ifStatement
    :	'if' '(' ifCondition ')' ifTrueBlock ('else' ifFalseBlock)?
    ;

ifCondition
    :	expr
    ;

ifTrueBlock
    :	ifBlock
    ;

ifFalseBlock
    :	ifBlock
    ;

ifBlock
    :	'{' (statement|breakWord)* '}'
    ;

breakWord
    :   'break' ';'
    ;

outputCall
    :   'output' '(' expr ')' ';'
    ;

expr
    :	expr ADD expr			#AddExpr
    |	expr SUB expr			#SubExpr
    |	expr MUL expr			#MulExpr
    |	expr DIV expr			#DivExpr
    |	expr EQUALS expr		#EqualExpr
    |	expr NOTEQUALS expr		#NotEqualExpr
    |	expr GT expr		    #GtExpr
    |	expr LT expr		    #LtExpr
    |	idExpr					#IdExprWrapper
    |	intExpr					#IntExprWrapper
    |	'(' expr ')'			#ParensExpr
    ;

idExpr
	:	ID
	;

intExpr
	:	INT
	;


// Lexer rules.
INT
    :   [0-9]+ ;
ID
    :   [a-zA-Z][a-zA-Z0-9]* ;
MUL
    :	'*' ;
DIV
    :	'/' ;
ADD
    :	'+' ;
SUB
    :	'-' ;
EQUALS
    :   '==';
NOTEQUALS
    :   '!=';
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
