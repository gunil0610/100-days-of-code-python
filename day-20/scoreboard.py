from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.sety(270)
        self.hideturtle()
        self.color('white')
        self.refresh()

    def add_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
