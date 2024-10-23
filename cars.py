from turtle import Turtle
import random

COLORS=['yellow','red','green','orange']
MOVE=5
SPEED_UP=5

class Car:
    def __init__(self):
        self.all_cars=[]
        self.speed=MOVE


    def create_new_car(self):
        new_car=Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape('square')
        new_car.shapesize(stretch_wid=0.5,stretch_len=1.5)
        new_car.goto(280,random.randint(-250,250))
        new_car.setheading(180)
        self.all_cars.append(new_car)




    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)


    def next_level(self):
        self.speed+=SPEED_UP


