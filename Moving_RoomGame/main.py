from room import Room

#How to play the game
#If the user is in the kitchen and wants to move to the gameroom, they should input "north".
#If the user is in the gameroom and wants to move back to the kitchen, they should input "south".
#If the user is in the gameroom and wants to move to the dining hall, they should input "west".
#If the user is in the kitchen and wants to move to the bedroom, they should input "east".

# Start the game


def main():
    # Define rooms and their descriptions
    kitchen = Room("Kitchen")
    kitchen.set_description("This is a busy kitchen, if you cant stand the heat get out my kitchen!.")

    gameroom = Room("Gameroom")
    gameroom.set_description("You have entered the game room, get your VR headset.")

    dining_hall = Room("Dining Hall")
    dining_hall.set_description("This is a long dining hall with tables for everyone to eat at.")

    bedroom = Room("Bedroom")
    bedroom.set_description("This is a cozy warm bedroom, you all of a sudden feel sleepy want to take a nap?.")

    # Connect rooms
    kitchen.linked_rooms["north"] = gameroom
    gameroom.linked_rooms["south"] = kitchen
    gameroom.linked_rooms["west"] = dining_hall
    dining_hall.linked_rooms["east"] = gameroom
    dining_hall.linked_rooms["north"] = kitchen
    kitchen.linked_rooms["south"] = dining_hall
    kitchen.linked_rooms["east"] = bedroom
    bedroom.linked_rooms["west"] = kitchen

    # Start the game
    current_room = kitchen
    print(f"You are in the {current_room.name}.")
    current_room.describe()

    while True:
        print("\n")
        command = input("Where do you want to go? (north, south, east, west): ")
        current_room = current_room.move(command)
        current_room.describe()

if __name__ == "__main__":
    main()







