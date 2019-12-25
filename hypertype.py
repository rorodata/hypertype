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

String = Type(str, label="String")
Integer = Type(int, label="Integer")
Float = Type(float, label="Float")
Boolean = Type(bool, label="Boolean")
Nothing = Type(type(None), label="Nothing")
Any = AnyType()
