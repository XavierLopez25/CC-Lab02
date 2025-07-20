from listener.SimpleLangListener import SimpleLangListener
from listener.SimpleLangParser import SimpleLangParser
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckListener(SimpleLangListener):

  def __init__(self):
    self.errors = []
    self.types = {}

  def enterMulDivMod(self, ctx: SimpleLangParser.MulDivModContext):
    pass

  def exitMulDivMod(self, ctx: SimpleLangParser.MulDivModContext):
        left_type  = self.types[ctx.expr(0)]
        right_type = self.types[ctx.expr(1)]
        op = ctx.op.text

        if op in ('*', '/'):
            if not self.is_valid_arithmetic_operation(left_type, right_type):
                self.errors.append(f"Unsupported operand types for {op}: {left_type} and {right_type}")
            result = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        elif op == '%':
            if not (isinstance(left_type, IntType) and isinstance(right_type, IntType)):
                self.errors.append(f"Unsupported operand types for %: {left_type} and {right_type}")
            result = IntType()

        else:
            self.errors.append(f"Unknown operator {op}")
            return

        self.types[ctx] = result

  def enterAddSubPow(self, ctx: SimpleLangParser.AddSubPowContext):
    pass

  def exitAddSubPow(self, ctx: SimpleLangParser.AddSubPowContext):
        left_type  = self.types[ctx.expr(0)]
        right_type = self.types[ctx.expr(1)]
        op = ctx.op.text

        if op in ('+', '-'):
            if not self.is_valid_arithmetic_operation(left_type, right_type):
                self.errors.append(f"Unsupported operand types for {op}: {left_type} and {right_type}")
            result = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        elif op == '^':
            if not self.is_valid_arithmetic_operation(left_type, right_type):
                self.errors.append(f"Unsupported operand types for ^: {left_type} and {right_type}")
            result = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        else:
            self.errors.append(f"Unknown operator {op}")
            return

        self.types[ctx] = result

  def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

  def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

  def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

  def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

  def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

  def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

  def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return True
    return False
