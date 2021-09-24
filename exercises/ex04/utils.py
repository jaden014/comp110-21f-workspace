"""List utility functions."""

__author__ = "730402799"


def all(a: list[int], b: int) -> bool:
    i: int = 0
    while i < len(a):
        if b == a[i]:
            return True
        i += 1
    return False


def is_equal(a: list[int], b: list[int]) -> bool:
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
    if len(a) == 0:
        raise ValueError("max() arg is an empty List.")
    i: int = 0
    k: int = 0
    while i < len(a):
        if a[i] > k or k == 0:                
            k = a[i]
        i += 1
        if i == len(a):
            return k


print(max([]))