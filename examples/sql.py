"""A small subset of SQL.
"""
from hypertype import *
import json

Query = Type("Query")
Table = Type("Table")
TableAlias = Type("TableAlias")
Column = Type("Column")
Expression = Type("Expression")
ColumnAlias = Type("ColumnAlias")
FunctionExpr = Type("FunctionExpr")

Query >>= Record({
    "table": Table,
    "columns": List(Column)
})

Table >>= String | TableAlias
TableAlias >>= Record({"name": String, "table": String})

Column >>= Expression | ColumnAlias
Expression >>= String | FunctionExpr
FunctionExpr >>= Record({
    "func": String,
    "args": List(Expression)
})
ColumnAlias >>= Record({"name": String, "expr": Expression})

@method
def compile_query(query: Query):
    table = compile_table(query['table'])
    columns = [compile_column(c) for c in query['columns']]
    return "SELECT {} FROM {}".format(", ".join(columns), table)

@method
def compile_table(table: String):
    return table

@method
def compile_table(table: TableAlias):
    return "{} AS {}".format(table['table'], table['name'])

@method
def compile_column(expr: Expression):
    return compile_expr(expr)

@method
def compile_column(alias: ColumnAlias):
    expr = compile_expr(alias['expr'])
    return "{} AS {}".format(expr, alias['name'])

@method
def compile_expr(name: String):
    return name

@method
def compile_expr(func: FunctionExpr):
    name = func['func']
    args = [compile_expr(arg) for arg in func['args']]
    return "{}({})".format(name, ", ".join(args))

def do_compile(query):
    print(json.dumps(query, indent=2))
    print("---")
    print(compile_query(query))
    print("===")

def main():
    do_compile({
        "table": "sales",
        "columns": ["store", "product", "quantity", "amount"]
    })

    do_compile({
        "table": "sales",
        "columns": [
            {"func": "sum", "args": ["amount"]},
            {
                "name": "max_quantity",
                "expr": {
                    "func": "max",
                    "args": ["quantity"]
                }
            }
        ]
    })

if __name__ == '__main__':
    main()
