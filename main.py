from turtle import Screen
from main_character import MyCharacter
from score import Score
from cars import Car
import time
import random

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


turtle=MyCharacter()
car=Car()
score=Score()

screen.listen()
screen.onkey(turtle.go_up,'Up')

game_over=False
while not game_over:
    time.sleep(0.1)
    screen.update()
    random_num=random.randint(1,6)
    if random_num==1:
        car.create_new_car()
    car.move()

    for auto in car.all_cars:
        if auto.distance(turtle)<20:
            game_over=True
    if turtle.ycor()>290:
        score.level_up()
        turtle.starting_position()
        car.next_level()































screen.exitonclick()

