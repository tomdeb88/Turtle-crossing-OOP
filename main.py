from turtle import Screen
from main_character import MyCharacter
from cars import Car
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.title('Help Turtle cross the Road')
screen.tracer(0)
screen.listen()

turtle=MyCharacter()

cars=[]
for car in range(25):
    car=Car()
    cars.append(car)

screen.onkey(turtle.go_up,'Up')
screen.onkey(turtle.go_down,'Down')


while True:
    screen.update()
    time.sleep(0.1)
    for car in cars:
        car.move()


























screen.exitonclick()

