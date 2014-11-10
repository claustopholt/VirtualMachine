from Grammar.TestGrammarListener import TestGrammarListener
from pprint import pprint


class MyListener(TestGrammarListener):

    bytecodes = []

    def enterScript(self, ctx):
        pass

    def exitScript(self, ctx):
        print(self.bytecodes)

    def exitVarAssign(self, ctx):
        name = ctx.ID().getText()
        self.bytecodes.append(name)
        self.bytecodes.append('STFLD')

    def exitIdExpr(self, ctx):
        name = ctx.ID().getText()
        self.bytecodes.append(name)
        self.bytecodes.append("LDFLD")

    def exitIntExpr(self, ctx):
        val = int(ctx.INT().getText())
        self.bytecodes.append(val)

    def exitAddExpr(self, ctx):
        self.bytecodes.append("ADD")

    def exitSubExpr(self, ctx):
        self.bytecodes.append("SUB")

    def exitMulExpr(self, ctx):
        self.bytecodes.append("MUL")

    def exitDivExpr(self, ctx):
        self.bytecodes.append("DIV")

    def exitEqualExpr(self, ctx):
        # TODO!
        pass

    def exitNotEqualExpr(self, ctx):
        # TODO!
        pass

    def exitGtGteExpr(self, ctx):
        # TODO!
        pass

    def exitLtLteExpr(self, ctx):
        # TODO!
        pass

    def exitOutputCall(self, ctx):
        self.bytecodes.append("OUTPUT")

