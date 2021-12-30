from turtle import Turtle
import random
COLORS = ["pale green", "misty rose", "lavender", "navajo white", "light sky blue", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def generate_car(self):
        new = Turtle(shape="square")
        new.color(random.choice(COLORS))
        new.shapesize(stretch_len=2, stretch_wid=1)
        new.penup()
        new.setheading(180)
        new.goto(320, random.randint(-240, 250))
        self.all_cars.append(new)
        self.move_cars()

    def move_cars(self):
        for car in self.all_cars:
            car.speed("slow")
            car.forward(self.speed)
            if car.xcor() <= -330:
                self.all_cars.remove(car)

    def get_collision_status(self, player):
        for car in self.all_cars:
            if (car.distance(player) <= 40) and (player.ycor() >= car.ycor() - 20) and (player.ycor() <= car.ycor() + 20):
                return True
        return False










