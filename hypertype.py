"""
(↑t) - hypertype
~~~~~~~~~~~~~~~~

Haskell inspired type classes and pattern matching for Python.
"""

class BaseType:
    def valid(self, value):
        raise NotImplementedError()

class Type(BaseType):
    def __init__(self, type_, label=None):
        self.type_ = type_
        self.label = label or str(type_)

    def valid(self, value):
        return isinstance(value, self.type_)

    def __repr__(self):
        return self.label

class AnyType(BaseType):
    def valid(self, value):
        return True

    def __repr__(self):
        return "Any"

class List(BaseType):
    def __init__(self, node):
        self.node = node

    def valid(self, value):
        return isinstance(value, list) and all(self.node.valid(v) for v in value)

    def __repr__(self):
        return "List({})".format(self.node)

class Record(BaseType):
    def __init__(self, schema):
        self.schema = schema

    def valid(self, value):
        return isinstance(value, dict) \
            and all(k in value and type_.valid(value[k]) for k, type_ in self.schema.items())

    def __repr__(self):
        return "Record({})".format(self.schema)

String = Type(str, label="String")
Integer = Type(int, label="Integer")
Float = Type(float, label="Float")
Boolean = Type(bool, label="Boolean")
Nothing = Type(type(None), label="Nothing")
Any = AnyType()
