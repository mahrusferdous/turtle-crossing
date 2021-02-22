from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    #move forward
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    #if reaches the end line reset
    # def endline(self):
    #     if self.ycor() > FINISH_LINE_Y:
    #         self.goto(STARTING_POSITION)

    #         return True