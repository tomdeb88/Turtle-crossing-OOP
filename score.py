from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-230,250)
        self.level=1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center",font=('Arial', 20, 'bold'))

    def level_up(self):
        self.level+=1
        self.show_level()