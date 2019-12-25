from hypertype import *

Expr = Reference()
AddExpr = Tuple(Literal("+"), Expr, Expr)
SubExpr = Tuple(Literal("-"), Expr, Expr)
MulExpr = Tuple(Literal("*"), Expr, Expr)
DivExpr = Tuple(Literal("/"), Expr, Expr)

Expr.set(
    Integer
    | AddExpr
    | SubExpr
    | MulExpr
    | DivExpr
    )

@method
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
