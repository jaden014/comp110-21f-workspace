"""Counting letters in a string."""

__author__ = "730402799"


letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i: int = 0
Count: int = 0
while i + 1 <= len(word):
    if letter == word[i]:
        Count = Count + 1
        i = i + 1
    else:
        i = i + 1
print("Count: " + str(Count))