"""Harry Potter Experience."""

__author__ = "730402799"

player: str
points: int 
OWL_EMOJI: str = "\U0001F989"
CAT_EMOJI: str = "\U0001F431"
TOAD_EMOJI: str = "\U0001F438"
i: int = 1


def greet() -> None:
    """Friendly greeting."""
    global player
    player = input("What's your name? ")
    print(f"Dear {player}, we are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.")


def choice1() -> None:
    """What Harry did."""
    print("Good choice. Hagrid knows his stuff and he'll definitely be able to help you out. You got an adventure point!")
    global player
    global points
    points = points + 1
    print(f"Hagrid has decided to buy you a pet, {player}! Do you want 1. An owl {OWL_EMOJI}, 2. A cat {CAT_EMOJI}, or 3. A toad {TOAD_EMOJI}?")
    pet: int = int(input("Enter the number of the pet you want: "))
    if pet == 2:
        while pet == 2:
            print("Try again. Cats are terrible.")
            pet = int(input("Enter the number of the pet you want: "))
    if pet == 1:
        pet1()
    if pet == 3:
        pet3()


def choice2(a: int) -> int:
    """Voldemort arc."""
    SNAKE_MULTIPLIER: int = 10
    return a * int(input("How old are you? ")) * SNAKE_MULTIPLIER
    

def choice3() -> None:
    """Experience ender."""
    print("You must be the most boring person ever. Literally who would ever turn this down. You lose 100 adventure points and are officially lame.")
    global points
    points = points - 100
    print(f"Game over. You ended with {points} adventure points.")


def pet1() -> None:
    """Harry's pet."""
    print(f"Excellent choice! Owls are really useful (they can carry your mail!) and they're very friendly and loyal. {OWL_EMOJI}")
    global points
    points = points + 1
    print("You got an adventure point!")


def pet3() -> None:
    """Neville's pet."""
    print(f"Uninspired. Toads are lame. You lose 1 adventure point. {TOAD_EMOJI}")
    global points
    points = points - 1


def main() -> None:
    """Main Gameplay"""
    greet()
    global i
    while i == 1:
        print("You have 3 options: 1. You may accompany Hagrid to Diagon Alley to buy your school supplies. 2. You may spurn Hagrid's assistance, and shop in Diagon Alley alone. 3. You may decline your invitation to Hogwarts.")
        choice: int = int(input("Enter the number of the option you chose: "))
        if choice == 1:
            choice1()
        if choice == 2:
            print("Interesting decision. You are a stangely independent lad/lass. You got 2 adventure points!")
            global points
            points = points + 2
            n: int = choice2(points)
            print(f"Oh no! {n} snakes have suddenly surrounded you in Diagon Alley! You can either: 1. run, or 2. try and talk to them.")
            Snake_fight: int = int(input("Enter the number of the option you chose: "))
            if Snake_fight == 1:
                print(f"Solid decision. I would do that too if I were surrounded by {n} snakes. You get an adventure point by virtue of surviving this harrowing experience.")
                points = points + 1
                print(f"Game over. You finished with {points} adventure points. Enjoy your 7 years at Hogwarts!")
            if Snake_fight == 2:
                from random import randint
                K = randint(-1, 2)
                if K >= 1:
                    print(f"Oh no, looks like you're a Parselmouth. You are almost guaranteed to be evil. You get {n} adventure points cause you'd probably kill me if I don't. I'm getting the hell out of here, peace out.")
                    points = points + n
                    print(f"You finished with {points} adventure points. Enjoy your 7 years at Hogwarts!")
                else:
                    print(f"Ha, moron. You died, game over. You finished with {points} adventure points.")
        if choice == 3:
            choice3()
        i = int(input("Would you like to continue exploring the other branches of the game? You can keep your adventure points until you're finished. Enter 1 if you want to keep playing. Enter 0 if you want to quit: "))
    print(f"Thanks for playing! You finished with {points} adventure ponits.")


if __name__ == "__main__":
    print("__name__ is '__main__'")
    main()