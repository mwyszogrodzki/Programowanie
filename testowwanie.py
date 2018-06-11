import random
player = 0
first = 0
second = 0
tries = 0
election = 33

while tries != 10000:
    population = 93
    population = 100 - random.randint(1,9)
    you = (election*1.5)/100 * population
    you_int = you % 1
    you -= you_int
    left = population - you
    firstCandidate = random.randrange(10, left - 5)
    secondCandidate = 100 - you - firstCandidate

    if you > firstCandidate:
        if you > secondCandidate:
            winner = "Gracz"
            player += 1
        else:
            winner = "Drugi kandydat"
            second += 1
    else:
        if firstCandidate > secondCandidate:
            winner = "Pierwszy kandydat"
            first += 1
        else:
            winner = "Drugi kandydat"
            second += 1
    tries += 1


print(player / 10000)
print(first / 10000)
print(second / 10000)
