from turtle import Turtle
import random

COLORS=['yellow','red','green','orange']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=0.7,stretch_len=1.5)
        self.color(random.choice(COLORS))
        self.goto(260,random.randrange(-290,290,5))
        self.setheading(180)

    def move(self):
        self.forward(random.randrange(1,80,5))
