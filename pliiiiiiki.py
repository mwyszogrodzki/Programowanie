import os

uprawnienia = 1

location_name = "las"

sciezkaDoPliku = location_name + ".txt"

if os.path.isfile(sciezkaDoPliku):
    file_read = open(sciezkaDoPliku, "r")
    print(file_read.readline())
else:
    if uprawnienia == 1:
        wybor = input("Czy chcesz stworzyć plik?")
        if wybor.lower() == "tak":
            f = open(sciezkaDoPliku, "w")
            print("Tworzę plik")
            text = input("Podaj treść, oddziel linijki średnikami")
            lines = list(text.split(";"))
            f.writelines(lines)
            f.close()
        elif wybor.lower() == "nie":
            print("Trudno")
        else:
            print("Nie ma takiej opcji")
    else:
        print("Nie ma takiego pliku")


