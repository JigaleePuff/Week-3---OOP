import random
from turtle import Screen, Turtle

WIDTH, HEIGHT = 1000, 400
COLORS = ["crimson", "blue", "olive", "yellow", "black", "cyan", "purple", "orange", "light salmon", "magenta"]

class Racer(Turtle):
    def __init__(self, name, color, y_position):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.goto(-WIDTH // 2 + 20, y_position)
        self.pendown()
        self.name = name

def init_turtle():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing Beta 2.0')

def race(turtles):
    while True:
        for racer in turtles:
            if racer.xcor() >= WIDTH // 2 - 50:
                return racer.name  # Return the winner's name directly
            distance = random.randint(1, 5)
            racer.forward(distance)

def get_number_of_racers():
    """Asks the user how many racers they want and returns it as an integer."""
    while True:
        try:
            num = int(input("Enter a number for racers from (1-10): "))
            if num < 1 or num > 10:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input! Please enter a whole number between 1 and 10.")

def main():
    racers = get_number_of_racers()
    init_turtle()
    colors = random.sample(COLORS, racers)  # Randomly select colors for the specified number of racers
    turtles = create_turtles(colors)  # Create turtles with random colors
    
    # Adjust the speed of each racer
    for racer in turtles:
        racer.speed("slow")  # Adjust speed as needed

    winner_name = race(turtles)
    print(f"The winner is {winner_name}")

    Screen().exitonclick()  # Keep the screen open

def create_turtles(colors):
    turtles = []
    spacingy = HEIGHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = Racer(f"Racer {i+1}", color, HEIGHT // 2 - (i + 1) * spacingy)
        turtles.append(racer)
    return turtles

if __name__ == "__main__":
    main()
