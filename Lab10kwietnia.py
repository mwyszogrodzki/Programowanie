import math

def roznica(num1, num2):
    result = num1 - num2
    return result

def pierwiastek(num1):
    if num1 >= 100:
        last_number = num1 % 100
    elif num1 < 100:
        last_number = num1 % 10
    num = num1
    if math.sqrt(num) == last_number:
        result = 1
    else:
        result = 0
    return result

def slownik():
    dictionary = {'pies': 'dog', 'kot': 'cat', 'chomik': 'hamster'}
    print("Oto słownik (wyrazy: pies, kot, chomik):")
    word = input("Wybierz słowo do wyświetlenia:")
    print(word.title(), "to po angielsku:", dictionary[word.lower()])


print("Co robić")
print("[1] Różnica")
print("[2] Pierwiastek")
print("[3] Słownik")
wybierz = input("Wybierz:")
if wybierz == "1":
    num1 = input("Podaj pierwszą liczbę: ")
    num2 = input("Podaj drugą liczbę: ")
    print("Wynik: ", roznica(num1, num2))
elif wybierz == "2":
    num1 = int(input("Podaj liczbę:"))
    print("Ta liczba", end=" ")
    if pierwiastek(num1) == 0:
        print("nie", end=" ")
    print("kończy się swoim pierwiastkiem.")
elif wybierz == "3":
    slownik()

