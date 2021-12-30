from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.refresh()

    def increment_level(self):
        self.level += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.sety(250)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(arg='Level: ' + str(self.level), move=False, align='center', font=FONT)

    def game_over_seq(self):
        self.clear()
        self.sety(250)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(arg='Game Over.', move=False, align='center', font=FONT)


