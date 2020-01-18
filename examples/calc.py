from hypertype import *

Expr = Type()
BinOp = Type()

Expr >>= Integer | Tuple(BinOp, Expr, Expr)
BinOp >>= Literal("+") | Literal("-") | Literal("*") | Literal("/")

@method(Expr)
def compute(expr: Integer):
    return expr

@method
def compute(expr: AddExpr):
    return compute(expr[1]) + compute(expr[2])

@method
def compute(expr: SubExpr):
    return compute(expr[1]) - compute(expr[2])

@method
def compute(expr: MulExpr):
    return compute(expr[1]) * compute(expr[2])

@method
def compute(expr: DivExpr):
    return compute(expr[1]) / compute(expr[2])

e = ["+", 2, ["*", 3, 4]]
print(compute(e))
