from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",18,"normal")
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"score:{self.score}",align=ALIGNMENT,font=FONT)
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 24, "normal"))

