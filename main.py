"""
projekt 2: druhý projekt do Engeto Online Python Akademie

author: Kamila Kynčl
email: kamilka.frolikova@gmail.com
"""

import sys
import random

SEPARATOR_LENGTH = 50
NUMBER_LENGTH = 4

def create_secret_number():
    """Vygeneruje náhodné čtyřmístné číslo bez opakování číslic.

    Číslo nezačíná nulou a je vráceno jako řetězec.
    """
    first = random.choice(range(1, 10))
    rest = random.sample(
        [x for x in range(10) if x != first],
        3
    )
    return str(first) + "".join(map(str, rest))

def validate_tip(tip):
    """Ověří vstup uživatele

    Vrací vstupní řetězec pokud je vše v pořádku, jinak chybovou hlášku
    """

    if len(tip) != NUMBER_LENGTH:
        return "Input has not length of 4"

    if not tip.isdigit():
        return "Input is not digits only"
    
    if tip[0] == "0":
        return "First digit cannot be 0"
    
    if len(set(tip)) != NUMBER_LENGTH:
        return "Duplicit numbers are not allowed"
    
    return tip

def resolve(secret, tip):
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

def print_results(bulls, cows):
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
    

SECRET_NUMBER = create_secret_number()

print("Hi there")
print("-" * SEPARATOR_LENGTH)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * SEPARATOR_LENGTH)

while True:
    tip = input("Enter a number :\n" + "-" * SEPARATOR_LENGTH + "\n")
    validated_tip = validate_tip(tip)

    if validated_tip == tip: # Pokud je tip validní
        break
    else:
        print(validated_tip + "\n" + "-" * SEPARATOR_LENGTH + "\n")

bulls_cows = resolve(SECRET_NUMBER, validated_tip)
print_results(bulls_cows[0], bulls_cows[1])
print(SECRET_NUMBER)