from antlr4 import *
from Grammar.TestGrammarLexer import TestGrammarLexer
from Grammar.TestGrammarParser import TestGrammarParser
from Grammar.MyListener import MyListener

def compile(sourcecode):

    print("Compiling.")

    # Create lexer and parser.
    lexer = TestGrammarLexer(sourcecode)
    stream = CommonTokenStream(lexer)
    parser = TestGrammarParser(stream)

    # Walk the tree.
    tree = parser.script()
    myListener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(myListener, tree)


