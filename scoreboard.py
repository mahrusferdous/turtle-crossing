FONT = ("Courier", 14, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-240, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)


    def level_up(self):
        self.score += 1
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)        


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)         