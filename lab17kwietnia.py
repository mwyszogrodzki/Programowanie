def printMenu():
  """Funkcja wypisująca menu użytkownika"""
  print("--------------")
  print("--- Menu ---")
  print("--------------")
  print("  [1] Rozpocznij nową grę")
  print("  [2] Zobacz tablicę wyników")
  print("  [3] Pomoc")
  print("  [4] Wyjście")
  print("--------------")

def navigation(choice):
  """Funkcja obsługująca wybór"""
  choice = input(">>>")
  choice = choice.lower()
  if choice in ("1", "[1]", "rozpocznij nową grę", "nowa gra", "rozpocznij"):
      new_game()
  elif choice in ("2", "[2]", "zobacz", "zobacz tablicę wyników", "tablica wyników", "wyniki"):
      leaderboard()
  elif choice in ("3", "[3]", "pomoc", "pomocy", "help"):
      game_help()
  elif choice in ("4", "[4]", "wyjście", "wyjscie", "wyjdź"):
      return


