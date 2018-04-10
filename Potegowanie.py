#Użytkownik podaje liczbę i potęgę

number1 = int(input("Podaj liczbę, którą chcesz potęgować"))
number2 = int(input("Do której potęgi chcesz ją podnieść?"))
result = number1
for i in range(0, number2-1):
    result *= number1

print("WynikL", result)