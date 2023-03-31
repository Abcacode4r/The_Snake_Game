from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",18,"bold")
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"score:{self.score} High_score:{self.high_score}",align=ALIGNMENT,font=FONT)
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"score:{self.score} High_score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.clear()
        self.score=0
        self.write(f"score:{self.score} High_score:{self.high_score}", align=ALIGNMENT, font=FONT)


