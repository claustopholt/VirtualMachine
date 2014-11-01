from Grammar.TestGrammarListener import TestGrammarListener


class MyListener(TestGrammarListener):

    def enterScript(self, ctx):
        print("Enter script")

    def exitScript(self, ctx):
        print("Exit script")

    def enterVarAssign(self, ctx):
        print("VarAssign {0} equals {1}".format(ctx.ID(), ctx.INT()))
