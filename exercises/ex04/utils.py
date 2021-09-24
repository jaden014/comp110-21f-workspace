"""List utility functions."""

__author__ = "730402799"


def all(a: list[int], b: int) -> bool:
    """Tests if every int in a list is the given int."""
    i: int = 0
    if len(a) == 0:
        return False
    while i < len(a):
        if b != a[i]:
            return False
        i += 1
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Tests if 2 lists are deeply equal."""
    i: int = 0
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    while a[i] == b[i] and i < len(a):
        i += 1
        if i == len(a):
            return True
    return False


def max(a: list[int]) -> int:
    """Finds the maximum value of a list of ints."""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    k: int = 0
    while i < len(a):
        if a[i] > k or k == 0:                
            k = a[i]
        i += 1
    return k