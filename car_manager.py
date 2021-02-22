from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1,2)
        self.random_position()


    def random_position(self):
        self.y_pos = random.randint(-250, 250)
        self.goto(320, self.y_pos)
        self.color(random.choice(COLORS))


    def move_car(self, moving):
        new_x = self.xcor() - moving
        self.goto(new_x, self.y_pos)


