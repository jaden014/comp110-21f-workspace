"""Examples of optional parameters and Union type parameters."""


def hello(name: str = "World") -> str:
    """A greeting."""
    result: str = "Hello, "
    return result + name


print(hello())
print(hello("bringle"))