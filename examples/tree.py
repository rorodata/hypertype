"""
data Tree a             = Leaf a | Branch (Tree a) (Tree a)

fringe                     :: Tree a -> [a]
fringe (Leaf x)            =  [x]
fringe (Branch left right) =  fringe left ++ fringe right
"""

from hypertype import *

Leaf = Type()
Branch = Type()
Tree = Type()

Tree >>= Leaf | Branch
Leaf >>= Integer
Branch >>= Tuple(Tree, Tree)

@method
def flatten(node: Leaf):
    return [node]

@method
def flatten(node: Branch):
    return flatten(node[0]) + flatten(node[1])

def main():
    tree = [1, [2, 3]]
    print(flatten(tree))

if __name__ == '__main__':
    main()
