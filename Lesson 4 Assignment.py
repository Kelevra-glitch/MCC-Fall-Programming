from random import randrange

def main():
    continue_playing = "y"

    while continue_playing == "y":
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()
        determine_winner(user_weapon, opponent_weapon)

        print()
        continue_playing = input("Play again? (y/n): ").lower()
        print()

    print("Thanks for playing!")


def get_user_weapon():
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    weapon = int(input("Enter your choice (1-3): "))
    return weapon


def get_opponent_weapon():
    weapon = randrange(1, 4)
    return weapon

def determine_winner(user, opponent):
    print("You chose:", user)
    print("Opponent chose:", opponent)

    if user == opponent:
        print("It's a tie!")
    elif user == 1 and opponent == 3:
        print("Rock crushes Scissors — You win!")
    elif user == 2 and opponent == 1:
        print("Paper covers Rock — You win!")
    elif user == 3 and opponent == 2:
        print("Scissors cut Paper — You win!")
    else:
        print("Opponent wins!")

if __name__ == "__main__":
    main()
print("Completed by, Jacob Harper")