def twooptions(option1, option2):
    print("[1]", option1, "[2]", option2)
    choiceofto_input = input("Wybierz:")
    if choiceofto_input.lower() in  ("1", "[2]", option1):
        choiceofto = 0
    elif choiceofto_input.lower() in ("2", "[2]", option2):
        choiceofto = 1
    return choiceofto

choice = twooptions("tak", "nie")

print(choice)
