"""Example of for in syntax."""


names: list[str] = ["Jaden", "Anna", "Whit", "Sam"]


print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1


print("for_in output:")
for name in names:
    print(name)