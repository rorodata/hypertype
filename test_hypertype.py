from hypertype import *

def test_simple_types():
    assert String.valid("(↑t)")
    assert not String.valid(5)

    assert Integer.valid(1)
    assert not Integer.valid("(↑t)")

    assert Float.valid(3.14)
    assert not Float.valid("(↑t)")

    assert Boolean.valid(True)
    assert Boolean.valid(False)
    assert not Boolean.valid("(↑t)")
    assert not Boolean.valid(3.14)

    assert Nothing.valid(None)
    assert not Nothing.valid(5)
    assert not Nothing.valid("")

    assert Any.valid(None)
    assert Any.valid("(↑t)")
    assert Any.valid(1)
    assert Any.valid(3.14)
    assert Any.valid(False)
