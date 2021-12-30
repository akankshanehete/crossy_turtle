import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 1. create turtle that moves forward when the up key is pressed (no other movements)
# 2. generate random cars along the y axis that are random colors and move from right to left edge of screen
# 3. detect collision with a car, if it occurs then it is game over
# 4. 


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
