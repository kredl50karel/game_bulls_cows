# Import modulu
import random


# Hlavni fce programu
def main():
    tisk_uvodu()
    # Definovani promenne
    my_num = generate_num(4)

    # Smycka while pro spravnou definici vstupu
    while True:
        vstup = input('Enter your number: ')

        if overeni_input(vstup):
            continue

        bulls, cows = count_bulls_cows(vstup, my_num)

        if check_game_over(bulls, cows):
            break


# Predstaveni hry
def tisk_uvodu():
    print('''
-----------------------------------------------
Hi there!

A computer will create a 4-digit number.
This number should have no repeated digits.
Upon making a guess, 2 hints will 
be provided- Cows and Bulls.
Bulls indicate the number of correct
digits in the correct position and cows indicates 
the number of correct digits in the wrong position.
For example, if the secret code is 1234
and the guessed number
is 1246 then we have 2 BULLS
(for the exact matches of digits 1 and 2) and 1 COW
(for the match of digit 4 in the wrong position)
The player keeps on guessing until
the secret code isn't cracked. 
-----------------------------------------------
    ''')


# Generovani 4-mistneho cisla

def generate_num(length):
    # Pomocna promenna
    num = ''

    # Tvoreni ctyrmistného cisla
    while len(set(num)) != length or num[0] == 0:
        # Generuj cislo od 1000 do 9999
        num = str(random.randint(1000, 9999))

    return num


# Overeni vstupu
def overeni_input(vstup):
    result = False

    # Je vstup spravny?
    if len(set(vstup)) != 4 or \
            not vstup.isdecimal() or len(vstup) != 4:
        print("Please enter true input")
        result = True

    return result


# Porovnavani
def count_bulls_cows(inp, secret_num):
    # Overeni bulls a cows, definovani promennych
    bulls = 0
    cows = 0

    for index, num in enumerate(inp):
        if num == secret_num[index]:
            bulls += 1
        elif num in secret_num:
            cows += 1
    return bulls, cows


# Ukonceni hry
def check_game_over(bulls, cows):
    # Prevod do j.c. a mn c. a vycet cows a bulls

    if bulls == 1:
        singularb = "bull"
    else:
        singularb = "bulls"

    if cows == 1:
        singularc = "cow"
    else:
        singularc = "cows"

    game_over = False

    # Konec hry
    if bulls == 4:
        print(f"Congratulation, you won!")
        game_over = True

    # Tisk aktualniho stavu
    else:
        print(
            f"{singularb} = {bulls}, {singularc} = {cows}"
        )
    return game_over


main()
