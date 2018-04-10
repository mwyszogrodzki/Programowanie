#Sprawdza czy 3 liczby są pitagorejskie

def pitagoras(num1, num2, num3):
    if num1*num1 + num2*num2 == num3*num3:
        result = 1
    else:
        result = 0
    return result

num1 = int(input("Pidaj pierwszą liczbę:"))
num2 = int(input("Podaj drugą liczbę:"))
num3 = int(input("Podaj trzecią liczbę:"))

print("======================")
print("Czy są pitagorejskie?")
if pitagoras(num1, num2, num3) == 1:
    print("Tak")
else:
    print("Nie")