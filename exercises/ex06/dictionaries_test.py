"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730402799"


def test_invert_empty_dict() -> None:
    """Tests for empty dictionary."""
    words: dict[str, str] = {}
    assert invert(words) == {}


def test_invert_same_key() -> None:
    """Random Test."""
    words: dict[str, str] = {"Hello": "Hola", "One": "No", "Hell": "Bonjour"}
    assert invert(words) == {"Hell": "Bonjour", "One": "No", "Hello": "Hola"}


def test_invert_same_key1() -> None:
    """Another random Test."""
    words: dict[str, str] = {"A": "B", "B": "D", "C": "B"}
    assert invert(words) == {"C": "B", "B": "D", "A": "B"}


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
    xs: list[str] = []
    assert count(xs) == {}


def test_count_random_case() -> None:
    xs: list[str] = ["tre", "tre", "ert"]
    assert count(xs) == {"tre": 2, "ert": 1}


def test_count_random_case_2() -> None:
    xs: list[str] = ["tre", "tre", "ert", "ert"]
    assert count(xs) == {"tre": 2, "ert": 2}