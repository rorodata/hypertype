"""
(↑t) - hypertype
~~~~~~~~~~~~~~~~

Haskell inspired type classes and pattern matching for Python.
"""

class BaseType:
    """Base class for all types.
    """
    def valid(self, value):
        raise NotImplementedError()

    def __or__(self, other):
        return OneOf([self, other])

class SimpleType(BaseType):
    """Type class to the simple types like string, integer etc.
    """
    def __init__(self, type_, label=None):
        self.type_ = type_
        self.label = label or str(type_)

    def valid(self, value):
        return isinstance(value, self.type_)

    def __repr__(self):
        return self.label

class AnyType(BaseType):
    """Type class to match any value.
    """
    def valid(self, value):
        return True

    def __repr__(self):
        return "Any"

class Literal(BaseType):
    """Type class to match a literal value.

        Plus = Literal("+")
        print(Plus.valid("+")) // True
    """
    def __init__(self, value, label=None):
        self.value = value
        self.label = label

    def valid(self, value):
        return self.value == value

    def __repr__(self):
        return self.label or "<{}>".format(self.value)

class List(BaseType):
    """Type class to represent a list of values.

    List is a homogeneous collection and each element of
    the collection must be of the specified type.

        Numbers = List(Integer)
        print(Numbers.valid([1, 2, 3]) # True
    """
    def __init__(self, type_):
        self.type_ = type_

    def valid(self, value):
        return isinstance(value, list) and all(self.type_.valid(v) for v in value)

    def __repr__(self):
        return "List({})".format(self.type_)

class Record(BaseType):
    """Type class to represent a record with fixed keys.

        Point = Record({"x": Integer, "y": Integer})
        print(Point.valid({"x": 1, "y": 2})) // True
    """
    def __init__(self, schema):
        self.schema = schema

    def valid(self, value):
        return isinstance(value, dict) \
            and all(k in value and type_.valid(value[k]) for k, type_ in self.schema.items())

    def __repr__(self):
        return "Record({})".format(self.schema)

class OneOf(BaseType):
    """Type class to match one of the given types.

        Value = Integer | List[Integer]
        print(Value.valid(1)) # True
        print(Value.valid([1, 2, 3])) # True
    """
    def __init__(self, types):
        self.types = types

    def valid(self, value):
        return any(t.valid(value) for t in self.types)

    def __or__(self, other):
        return OneOf(self.types + [other])

    def __repr__(self):
        return " | ".join(str(t) for t in self.types)

String = SimpleType(str, label="String")
Integer = SimpleType(int, label="Integer")
Float = SimpleType(float, label="Float")
Boolean = SimpleType(bool, label="Boolean")
Nothing = SimpleType(type(None), label="Nothing")
Any = AnyType()
