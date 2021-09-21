def logical(n: int) -> str:
    if n <= 0:
        return "a"

    if n == 0:
        return "b"
    else:
        if n < 10:
            return "c"
        else:
            if n > 10:
                return "d"
            else:
                return "e"


choice: int = int(input("Enter a number: "))
print(logical(choice))