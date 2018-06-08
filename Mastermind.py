# funkcja realizująca grę mastermind

import random

n1 = random.randint(1, 9)
n2 = random.randint(1, 9)
n3 = random.randint(1, 9)
n4 = random.randint(1, 9)
numberswrong = 0
print(n1, n2, n3, n4)
guess1 = input("Podaj pierwszą liczbę: ")
guess2 = input("Podaj pierwszą liczbę: ")
guess3 = input("Podaj pierwszą liczbę: ")
guess4 = input("Podaj pierwszą liczbę: ")
guess1 = int(guess1)
guess2 = int(guess2)
guess3 = int(guess3)
guess4 = int(guess4)
if guess1 != n1:
    numberswrong += 1
else:
    numberswrong += 0
if guess2 != n2:
    numberswrong += 1
else:
    numberswrong += 0
if guess3 != n3:
    numberswrong += 1
else:
    numberswrong += 0
if guess4 != n4:
    numberswrong += 1
else:
    numberswrong += 0
print("Masz", numberswrong, "błędów")
if numberswrong == 0:
    print("Well done")
while numberswrong != 0:
    guess1 = input("Podaj pierwszą liczbę: ")
    guess2 = input("Podaj pierwszą liczbę: ")
    guess3 = input("Podaj pierwszą liczbę: ")
    guess4 = input("Podaj pierwszą liczbę: ")
    guess1 = int(guess1)
    guess2 = int(guess2)
    guess3 = int(guess3)
    guess4 = int(guess4)
    if guess1 != n1:
        numberswrong += 1
    else:
        numberswrong += 0
    if guess2 != n2:
        numberswrong += 1
    else:
        numberswrong += 0
    if guess3 != n3:
        numberswrong += 1
    else:
        numberswrong += 0
    if guess4 != n4:
        numberswrong += 1
    else:
        numberswrong += 0
    print("Masz", numberswrong, "błędów.")
print("Dobra robota")