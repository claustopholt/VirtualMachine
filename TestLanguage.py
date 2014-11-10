from antlr4 import *
from Grammar.TestGrammarLexer import TestGrammarLexer
from Grammar.TestGrammarParser import TestGrammarParser
from Grammar.MyListener import MyListener


def compile_code(sourcecode):

    print("Compiling...")

    # Create lexer and parser.
    lexer = TestGrammarLexer(sourcecode)
    stream = CommonTokenStream(lexer)
    parser = TestGrammarParser(stream)

    # Walk the tree.
    tree = parser.script()
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(my_listener, tree)

    print("Compilation done.")


