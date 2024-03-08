from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Consolas", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Consolas", 60, "normal"))

    def l_update(self):
        self.l_score += 1
        self.update()

    def r_update(self):
        self.r_score += 1
        self.update()

