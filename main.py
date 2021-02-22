import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, 'Up')

speed = 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #randomize car
    number = random.randint(1,8)
    if number == 3:
        cars.append(CarManager())

    for c in cars:
        #Detect collision
        if c.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
        c.move_car(speed)

        if player.ycor() > 280:
            player.goto(0, -280)
            scoreboard.level_up()
            speed += 5


screen.exitonclick()