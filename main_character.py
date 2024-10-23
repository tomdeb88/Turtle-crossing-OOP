from turtle import Turtle

class MyCharacter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("blue")
        self.penup()
        self.starting_position()
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def starting_position(self):
        self.goto(0, -280)

