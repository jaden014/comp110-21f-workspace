"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730402799"


def test_invert_empty_dict() -> None:
    """Tests for empty dictionary."""
    words: dict[str, str] = {}
    assert invert(words) == {}


def test_invert_random_test() -> None:
    """Random Test."""
    words: dict[str, str] = {"A": "b"}
    assert invert(words) == {"b": "A"}


def test_invert_another_random_test() -> None:
    """Another random Test."""
    words: dict[str, str] = {"A": "B", "C": "D", "E": "F"}
    assert invert(words) == {"B": "A", "D": "C", "F": "E"}


def test_favorite_color_empty_dictionary() -> None:
    """Tests for empty dictionary."""
    fave_colors: dict[str, str] = {}
    assert favorite_color(fave_colors) is None


def test_favorite_color_random_case() -> None:
    """Tests random case."""
    fave_colors: dict[str, str] = {"A": "Blue", "B": "Blue", "C": "Green"}
    assert favorite_color(fave_colors) == "Blue"


def test_favorite_color_another_random_case() -> None:
    """Another random case."""
    fave_colors: dict[str, str] = {"A": "Blue", "B": "Blue", "C": "Green", "D": "Green"}
    assert favorite_color(fave_colors) == "Blue"


def test_count_empty_list() -> None:
    """Tests for empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_random_case() -> None:
    """Tests random case."""
    xs: list[str] = ["tre", "tre", "ert"]
    assert count(xs) == {"tre": 2, "ert": 1}


def test_count_random_case_2() -> None:
    """Tests another random case."""
    xs: list[str] = ["tre", "tre", "ert", "ert"]
    assert count(xs) == {"tre": 2, "ert": 2}