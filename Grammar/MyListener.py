from Grammar.TestGrammarListener import TestGrammarListener


class MyListener(TestGrammarListener):

    def enterScript(self, ctx):
        print("Enter script")

    def exitScript(self, ctx):
        print("Exit script")