"""Practice with dictionaries."""


__author__ = "730402799"


def invert(words: dict[str, str]) -> dict[str, str]:
    """Function to invert a dictionary."""
    z: int = 0
    values: list[str] = []
    keys: list[str] = []
    inverted_dict: dict[str, str] = {}
    for x in words:
        k: int = 0
        for word in words:
            if word == x and k != z:
                raise KeyError("nuh-uh")
            k += 1
        z += 1
        keys.append(x)
        values.append(words[x])
    i: int = len(keys) - 1
    while i >= 0:
        inverted_dict[keys[i]] = values[i]
        i -= 1
    return inverted_dict


def favorite_color(names_n_colors: dict[str, str]) -> str:
    """Function to find most repeated color."""
    colors: dict[str, int] = {}
    count: int = 0
    for name in names_n_colors:
        colors[names_n_colors[name]] = 0
        colors[names_n_colors[name]] += 1
    for each in colors:
        if colors[each] > count:
            count = colors[each]
        if count == colors[each]:
            return each


def count(xs: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for each in xs:
        if each in counts:
            counts[each] += 1
        else: counts[each] = 1
    return counts