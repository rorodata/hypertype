from hypertype import *

Expr = Type()
BinOp = Type()

Expr >>= Integer | Tuple(BinOp, Expr, Expr)
BinOp >>= Literal("+") | Literal("-") | Literal("*") | Literal("/")

@method
def compute(expr: Integer):
    return expr

@method
def compute(expr: Tuple(BinOp, Expr, Expr)):
    op, left, right = expr
    return compute_op(op, left, right)

@method
def compute_op(op: Literal("+"), left: Expr, right: Expr):
    return compute(left) + compute(right)

@method
def compute_op(op: Literal("-"), left: Expr, right: Expr):
    return compute(left) - compute(right)

@method
def compute_op(op: Literal("*"), left: Expr, right: Expr):
    return compute(left) * compute(right)

@method
def compute_op(op: Literal("/"), left: Expr, right: Expr):
    return compute(left) / compute(right)

e = ["+", 2, ["*", 3, 4]]
print(compute(e))
