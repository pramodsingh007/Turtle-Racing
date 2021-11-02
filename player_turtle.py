from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(0,-300)
        self.setheading(90)
        

    def move(self):
        y_move = self.ycor() + 10
        self.goto(0,y_move)

    def refresh(self):
        self.goto(0,-300)


