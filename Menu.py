#Funkcja menu

def gamemenu():
    scores = {}
    while True:
        print("==================")
        print("Co chcesz zrobić?")
        print("[1] Nowa gra")
        print("[2] Dodaj wynik")
        print("[3] Wyświetl najlepsze wyniki")
        print("[4] Zakończ")
        choice = input("Wybierz:")
        if choice in ("1", "[1]", "nowa gra", "nowa"):
            print("Rozpoczyna się gra")
            break
        elif choice in ("2", "[2]", "dodaj", "dodaj wynik"):
            player_name = input("Podaj nick gracza:")
            player_score = input("Podaj wynik gracza:")
            scores[player_name] = player_score
        elif choice in ("3", "[3]", "wyświetl", "wyświetl wyniki"):
            print("Wyniki:")
            for i in scores:
                print(i, end=":   ")
                print(scores[i])

gamemenu()