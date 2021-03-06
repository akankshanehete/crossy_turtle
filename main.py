import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 1. create turtle that moves forward when the up key is pressed (no other movements)
# 2. generate random cars along the y axis that are random colors and move from right to left edge of screen
# 3. detect collision with a car, if it occurs then it is game over
# 4. if the turtle reaches the top of screen without collisions, game advances to next level
# 5. scoreboard updates as game advances to next level and speed of the randomly generated cars increases


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

turtle = Player()
cars = CarManager()
sb = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
loop_counter = 0
level_incremented = False

while game_is_on:
    loop_counter += 1
    time.sleep(0.1)

    # generates a new car with every 6 turns of the while loop so car generation isn't too frequent
    if loop_counter % 6 == 0:
        cars.generate_car()
    cars.move_cars()

    # detecting whether turtle has collided with car
    if cars.get_collision_status(turtle) == True:
        game_is_on = False
        sb.game_over_seq()

    level_incremented = False
    # detecting whether turtle has crossed finish line
    if turtle.crossed_line() == True and level_incremented == False:
        time.sleep(2)
        sb.increment_level()
        level_incremented = True
        turtle.reset_player()
        cars.speed += 1

    screen.update()


screen.exitonclick()