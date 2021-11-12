"""Examples of optional parameters and Union type parameters."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A greeting."""
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + "COMP" + str(name)


# Calling hello with no argument leads to use of default
print(hello())
# Calling hello with argument overrides the default
print(hello("bringle"))
print(hello(110))
print(hello(11.0))