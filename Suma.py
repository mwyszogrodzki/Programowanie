#Suma

def suma(input_numbers):
    number1, number2 = input_numbers.split("+")
    number1 = int(number1)
    number2 = int(number2)
    sum = number1 + number2
    return sum

print("Witaj w programie do dodawania!")
input_numbers = input("Potaj dwie liczby oddzielone znakiem +:")
print("Wynik:", suma(input_numbers))