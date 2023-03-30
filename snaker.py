STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
Up=90
Down=270
Right=0
Left=180
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.Create_Snake()
        self.Slice=[]
    def Create_Snake(self):
        for ten in STARTING_POSITIONS:
           self.add_segment(ten)
    def add_segment(self,ten):
        ted = Turtle("square")
        ted.color("white")
        ted.pu()
        ted.goto(ten)
        self.segments.append(ted)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_com = self.segments[seg_num - 1].xcor()
            y_com = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_com, y_com)
        self.segments[0].forward(MOVE_FORWARD)

    def up(self):
        if self.segments[0].heading()!=Down:
            self.segments[0].setheading(Up)
    def down(self):
        if self.segments[0].heading() != Up:
            self.segments[0].setheading(Down)
    def right(self):
        if self.segments[0].heading() != Left:
            self.segments[0].setheading(Right)
    def left(self):
        if self.segments[0].heading() != Right:
         self.segments[0].setheading(Left)