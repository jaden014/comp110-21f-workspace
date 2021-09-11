"""Drawing forests in a loop."""

__author__ = "730402799"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
Depth: int = int(input("Depth? "))
i = 1
while i <= Depth:
    print(TREE * i)
    i = i + 1