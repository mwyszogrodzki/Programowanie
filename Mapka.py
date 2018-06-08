rooms = {
    1: {"name": "Hall",
        "east": 2,
        "south": 3,
        "north": 5},
    2: {"name": "Bedroom",
        "west": 1,
        "south": 4},
    3: {"name": "Kitchen",
        "north": 1},
    4: {"name": "Bathroom",
        "north": 2},
    5: {"name": "Porch",
        "south": 1}
}

currentRoom = 5
print("Use command:")
print("> go [direction]")
print("> exit (only in Porch)")
print("Command:")

while True:
    print("You are in " + rooms[currentRoom]["name"])
    move = input("> ").lower().split()
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")
    if move[0] == "exit":
        if currentRoom == 5:
            print("You exit the game!")
            break
        else:
            print("You can't go out from that place.")