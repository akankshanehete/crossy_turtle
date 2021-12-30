from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_player()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def crossed_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def reset_player(self):
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POSITION)

