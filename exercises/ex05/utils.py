"""List utility functions part 2."""


__author__ = "730402799"


def only_evens(a: list[int]) -> list[int]:
    """Returns only the even numbers in a list."""
    i: int = 0
    evens: list[int] = []
    while i < len(a):
        if a[i] % 2 == 0:
            evens.append(a[i])
        i += 1
    return evens


def sub(a: list[int], j: int, k: int) -> list[int]:
    """Returns the piece of a list lying between 2 indices."""
    if a == [] or j > len(a) or k <= 0:
        return []
    i: int = j
    sublist: list[int] = []
    if j < 0:
        i = 0
    if k > len(a):
        k = len(a) - 1
    while j <= i and i < k:
        sublist.append(a[i])
        i += 1
    return sublist


def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns both lists in a bigger list."""
    i: int = 0
    biglist: list[int] = []
    while i < len(a):
        biglist.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        biglist.append(b[i])
        i += 1
    return biglist