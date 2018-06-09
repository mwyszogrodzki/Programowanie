import time
import random

def lotto():
    number1 = random.randint(1, 49)
    number2 = random.randint(1, 49)
    number3 = random.randint(1, 49)
    number4 = random.randint(1, 49)
    number5 = random.randint(1, 49)
    number6 = random.randint(1, 49)

    print("Witaj w grze LOTTO!")
    time.sleep(1)
    print("Liczby podawaj w zakresie od 1 do 49.")
    user1 = input("Podaj pierwszą liczbę:\n>>>")
    user2 = input("Podaj drugą liczbę:\n>>>")
    user3 = input("Podaj trzecią liczbę:\n>>>")
    user4 = input("Podaj czwartą liczbę:\n>>>")

    correct = 0

    if int(user1) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user1 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user1 + " nie szostała wylosowana")

    if int(user2) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user2 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user2 + " nie szostała wylosowana")

    if int(user3) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user3 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user3 + " nie szostała wylosowana")

    if int(user4) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user3 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user3 + " nie szostała wylosowana")

    print("Trafiłeś na " + str(correct) + " spośród 6 liczb")
    print("Szczęśliwe liczby to: ", number1, number2, number3, number4, number5, number6)
    return correct

def zgadywanie():
    number = random.randint(1, 100)
    user_number = ' '
    times = 6
    fails = 0
    succes = 0
    while user_number != number:
        if times > 0:
            user_number = input("Wybierz liczbę od 1 do 100: ")
            if int(user_number) > number:
                print("Wylosowana liczba jest mniejsza")
                times -= 1
                fails += 1
                print("Zostało Ci", times, "prób.\n")
            elif int(user_number) == number:
                print("\n======================")
                print("Bingo!")
                fails += 1
                print("Miałeś", fails, "prób")
                succes = 1
                break
            else:
                print("Wylosowana liczba jest większa")
                times -= 1
                fails += 1
                print("Zostało Ci", times, "prób.\n")
        else:
            print("Game Over!")
            break
    return succes

def decoding():
    coded = "Ipnkdc oydzredntg. Iygiów w podyzd. Oyzraptlj oyzdmpwę."
    decoded = "Koniec prezydenta. Kraków w operze. Przygotuj przemowę."
    number = 0
    for i in coded:
        while True:
            if i == " " or i == ".":
                number += 1
                break
            else:
                print("GA-DE-RY-PO-LU-KI")
                print("Literka:", i)
                letter = input(">>")
                if letter.lower() == decoded[number].lower():
                    print("Dobrze.")
                    number += 1
                    break
                else:
                    continue
    print("Rozszyfrowana wiadomość to:")
    print('"', decoded, '"')

