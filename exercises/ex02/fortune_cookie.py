"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730402799"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
i: int = randint(0, 3)
if i == 0:
    print("It is not our abilities that determine who we really are, it is our choices.")
else:
    if i == 1:
        print("HARRY DID YOU PUT YOUR NAME IN THE GOBLET OF FIRE?!")
    else:
        if i == 2:
            print("Would you care for a lemon drop?")
        else:
            if i == 3:
                print("To have been loved so deeply, even though the person who loved us is gone, will give us some protection forever.")
print("Now, go spread positive vibes!")
