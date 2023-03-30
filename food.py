from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed(10)
        self.refresh()
    def refresh(self):
        x_coo=random.randint(-280,280)
        y_coo = random.randint(-280, 280)
        self.goto(x_coo,y_coo)