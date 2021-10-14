"""Practice with dictionaries."""


__author__ = "730402799"


def invert(words: dict[str, str]) -> dict[str, str]:
    """Function to invert a dictionary."""
    inverted_dict: dict[str, str] = {}
    for each in words:
        inverted_dict[words[each]] = each
    if len(words) != len(inverted_dict):
        raise KeyError("nuh-uh")
    return inverted_dict


def favorite_color(names_n_colors: dict[str, str]) -> str:
    """Function to find most repeated color."""
    colors: dict[str, int] = {}
    count: int = 0
    for name in names_n_colors:
        colors[names_n_colors[name]] = 0
    for name in names_n_colors:
        colors[names_n_colors[name]] += 1
    for each in colors:
        if colors[each] > count:
            count = colors[each]
    for each in colors:
        if count == colors[each]:
            return each
    return ""


def count(xs: list[str]) -> dict[str, int]:
    """Function to count the number of times something appears on the list."""
    counts: dict[str, int] = {}
    for each in xs:
        if each in counts:
            counts[each] += 1
        else:
            counts[each] = 1
    return counts