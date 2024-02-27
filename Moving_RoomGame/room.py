class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(f"You are in the {self.name}.")
        print(self.description)


# Creating instances of Room
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
bedroom = Room("Bedroom")

# Adding descriptions to rooms
kitchen.set_description("This is a cozy kitchen.")
ballroom.set_description("This is a grand ballroom.")
dining_hall.set_description("This is a long dining hall with tables for everyone to eat at.")
bedroom.set_description("Cozy warm Bedroom")


# Adding links between rooms
kitchen.linked_rooms["north"] = ballroom
ballroom.linked_rooms["south"] = kitchen
dining_hall.linked_rooms["west"] = kitchen




