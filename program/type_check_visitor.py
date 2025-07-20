from visitor.SimpleLangParser import SimpleLangParser
from visitor.SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDivMod(self, ctx: SimpleLangParser.MulDivModContext):
      left_type  = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))
      op = ctx.op.text

      if op in ('*', '/'):
          if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
              return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
          else:
              raise TypeError(f"Unsupported operand types for {op}: {left_type} and {right_type}")

      elif op == '%':
          # sólo Int % Int → Int
          if isinstance(left_type, IntType) and isinstance(right_type, IntType):
              return IntType()
          else:
              raise TypeError(f"Unsupported operand types for %: {left_type} and {right_type}")

      else:
          raise TypeError(f"Unknown operator {op!r}")

  def visitAddSubPow(self, ctx: SimpleLangParser.AddSubPowContext):
        left_type  = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op in ('+', '-'):
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
            else:
                raise TypeError(f"Unsupported operand types for {op}: {left_type} and {right_type}")

        elif op == '^':
            # potencia: sólo numéricos → Float si hay float, Int si ambos enteros
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
            else:
                raise TypeError(f"Unsupported operand types for ^: {left_type} and {right_type}")

        else:
            raise TypeError(f"Unknown operator {op!r}")

  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
