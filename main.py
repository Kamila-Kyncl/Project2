"""
projekt 2: druhý projekt do Engeto Online Python Akademie

author: Kamila Kynčl
email: kamilka.frolikova@gmail.com
"""

import random

SEPARATOR_LENGTH = 50
NUMBER_LENGTH = 4


def create_secret_number() -> str:
    """
    Vygeneruje náhodné čtyřmístné číslo bez opakování číslic.
    Číslo nezačíná nulou a je vráceno jako řetězec.
    """
    first = random.choice(range(1, 10))
    rest = random.sample(
        [x for x in range(10) if x != first],
        3
    )
    return str(first) + "".join(map(str, rest))


def validate_tip(tip: str) -> tuple[bool, str]:
    """
    Ověří vstup uživatele.
    Vrací zda je vstup v pořádku, pokud ne, tak i chybovou hlášku
    """

    if len(tip) != NUMBER_LENGTH:
        return False, "Input has not length of 4"

    if not tip.isdigit():
        return False, "Input is not digits only"
    
    if tip[0] == "0":
        return False, "First digit cannot be 0"
    
    if len(set(tip)) != NUMBER_LENGTH:
        return False, "Duplicit numbers are not allowed"
    
    return True, ""


def resolve(secret: str, tip: str) -> tuple[int, int]:
    """
    Vrací počet bulls a cows
    
    :param secret: tajné číslo
    :param tip: tip uživatele
    """
    bulls = 0
    cows = 0

    for i in range(NUMBER_LENGTH):
        if tip[i] == secret[i]:
            bulls += 1
        elif tip[i] in secret:
            cows += 1

    return bulls, cows


def print_results(bulls: int, cows: int) -> None:
    """
    Vypíše počet bulls a cows
    
    :param bulls: počet bulls
    :param cows: počet cows
    """
    bulls_text = "bull"
    cows_text = "cow"

    if bulls != 1:
        bulls_text += "s"

    if cows != 1:
        cows_text += "s"

    print(str(bulls) + " " + bulls_text + ", " + str(cows) + " " + cows_text)
    separator()


def separator() -> None:
    """
    Vypíše oddělovač textu
    """
    print("-" * SEPARATOR_LENGTH)  


def main() -> None:
    """Spustí konzolovou hru Bulls & Cows."""

    secret_number = create_secret_number()

    print("Hi there!")
    separator()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    separator()
    print("Enter a number:")
    separator()

    tips_number = 0

    while True:
        tip = input()
        is_valid, message = validate_tip(tip)

        if not is_valid:
            print(message)
            separator()
            continue

        tips_number += 1
        bulls, cows = resolve(secret_number, tip)

        if bulls == NUMBER_LENGTH:  # Uživatel uhodl číslo
            print("Correct, you've guessed the right number")
            print("in " + str(tips_number) + " guesses!")
            separator()
            print("That's amazing!")
            return
    
        print_results(bulls, cows)


if __name__ == "__main__":
    main()