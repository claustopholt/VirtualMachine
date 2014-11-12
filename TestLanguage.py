from pprint import pprint
from antlr4 import *
from Grammar.TestGrammarLexer import TestGrammarLexer
from Grammar.TestGrammarParser import TestGrammarParser
from Grammar.MyListener import MyListener
from antlr4.error import ErrorListener
from antlr4 import InputStream


class MyErrorListener(ErrorListener.ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("ERROR!!!")
        raise Exception("{0} at line {1}".format(msg, line))


def compile_code(sourcecode):

    # Create a stream for the sourcecode (ANTLR4).
    sourcecode_stream = InputStream.InputStream(sourcecode)

    # Create lexer and parser.
    lexer = TestGrammarLexer(sourcecode_stream)
    stream = CommonTokenStream(lexer)
    parser = TestGrammarParser(stream)

    # Add custom error listener.
    parser.addErrorListener(MyErrorListener())

    # Walk the tree.
    tree = parser.script()
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(my_listener, tree)

    # Return the compiled bytecodes.
    return my_listener.bytecodes



