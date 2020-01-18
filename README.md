# (↑t) - hypertype

Haskell-inspired type system and pattern matching for Python.

## Example

```
from hypertype import *

Circle = Record({
    "type": Literal("circle"),
    "radius": Integer
})
Rectangle = Record({
    "type": Literal("rectangle"),
    "length": Integer,
    "width": Integer
})

Shape = Circle | Rectangle

@method
def area(c: Circle):
    return 3.14*c['radius']*c['radius']

@method
def area(r: Rectangle):
    return r['length']*r['width']

c = {
    "type": "circle",
    "radius": 5
}
r = {
    "type": "rectangle",
    "length": 10,
    "width": 4
}

print(Shape.valid(c), Shape.valid(r))
print(area(c), area(r))
```