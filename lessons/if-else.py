"""Challenge Question #1."""
__author__ = "730402799"
choice: int = int(input("Enter a number: "))
# A if choice <25
# B if choice >=25 less than 50
# C if over 75
# D if >=50 less than equal 75
if choice >= 50:
    if choice > 75:
        print("C")
    else:
        print("D")
else:
    if choice < 25:
        print("A")
    else:
        print("B")
