"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat


__author__ = "730402799"


def test_only_evens_edge_case_empty_list() -> None:
    """Testing an empty list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_only_evens_only_one_even() -> None:
    """Testing a list with only an even number."""
    a: list[int] = [2]
    assert only_evens(a) == [2]


def test_only_evens_odds_and_evens_in_list() -> None:
    """Tests a list with many odds and evens."""
    a: list[int] = [1, 2, 2, 4, 3]
    assert only_evens(a) == [2, 2, 4]


def test_sub_same_indices() -> None:
    """Tests when indices are the same."""
    a: list[int] = [1, 2, 3]
    j: int = 1
    k: int = 1
    assert sub(a, j, k) == []


def test_sub_empty_list() -> None:
    """Tests empty list."""
    a: list[int] = []
    j: int = 1
    k: int = 2
    assert sub(a, j, k) == []


def test_sub_random_case() -> None:
    """Tests a random case."""
    a: list[int] = [1, 2, 3, 4, 5]
    j: int = 1
    k: int = 4
    assert sub(a, j, k) == [2, 3, 4]


def test_sub_one_int() -> None:
    """Tests a one-element-list where j < 0 and k > len(a)."""
    a: list[int] = [1]
    j: int = -1
    k: int = 2
    assert sub(a, j, k) == []


def test_concat_empty_lists() -> None:
    """Tests two empty lists."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_nonempty_lists() -> None:
    """Tests two nonempty lists."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]


def test_concat_one_empty_list() -> None:
    """Tests one empty list, one nonempty list."""
    a: list[int] = [1, 2]
    b: list[int] = []
    assert concat(a, b) == [1, 2]