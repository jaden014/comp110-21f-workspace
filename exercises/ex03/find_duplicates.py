"""Finding duplicate letters in a word."""

__author__ = "730402799"


word: str = input("Enter a word: ")
i: int = 0
k: int = 0
b: int = 0
while i < len(word):
    while k < len(word):
        if i != k:
            if word[i] == word[k]:
                b = 1
                k = i = len(word)
        k = k + 1
    i = i + 1
    k = 0


if b == 1:
    print("Found duplicate: " + str(True))
else:
    print("Found duplicate: " + str(False))