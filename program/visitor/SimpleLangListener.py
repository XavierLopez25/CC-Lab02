# Generated from SimpleLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#prog.
    def enterProg(self, ctx:SimpleLangParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#prog.
    def exitProg(self, ctx:SimpleLangParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#stat.
    def enterStat(self, ctx:SimpleLangParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#stat.
    def exitStat(self, ctx:SimpleLangParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Float.
    def enterFloat(self, ctx:SimpleLangParser.FloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Float.
    def exitFloat(self, ctx:SimpleLangParser.FloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDivMod.
    def enterMulDivMod(self, ctx:SimpleLangParser.MulDivModContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDivMod.
    def exitMulDivMod(self, ctx:SimpleLangParser.MulDivModContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Bool.
    def enterBool(self, ctx:SimpleLangParser.BoolContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Bool.
    def exitBool(self, ctx:SimpleLangParser.BoolContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Parens.
    def enterParens(self, ctx:SimpleLangParser.ParensContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Parens.
    def exitParens(self, ctx:SimpleLangParser.ParensContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#String.
    def enterString(self, ctx:SimpleLangParser.StringContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#String.
    def exitString(self, ctx:SimpleLangParser.StringContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSubPow.
    def enterAddSubPow(self, ctx:SimpleLangParser.AddSubPowContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSubPow.
    def exitAddSubPow(self, ctx:SimpleLangParser.AddSubPowContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Int.
    def enterInt(self, ctx:SimpleLangParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Int.
    def exitInt(self, ctx:SimpleLangParser.IntContext):
        pass



del SimpleLangParser