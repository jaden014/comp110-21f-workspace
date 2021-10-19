"""Example of functions imported elsewhere."""

THE_ANSWER: int = 42

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n

if __name__ == "__main__":
    # Usually call main here.
    print(f"helpers.py: {__name__}")
else:
    # Usually don't do anything.
    print("evaluated as an imported module.")