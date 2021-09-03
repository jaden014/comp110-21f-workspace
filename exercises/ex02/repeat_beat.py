"""Repeating a beat in a loop."""

__author__ = "730402799"


beat: str = input("Give me a beat!")
amount: int = int(input("How many times should I repeat it?"))
i: int = 1
if amount < 0:
    print("No beat...")
else:
    while i < amount:
        i = i + 1
    print((" " + str(beat)) * i)