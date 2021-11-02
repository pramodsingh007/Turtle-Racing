from time import sleep
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.goto(-350,280)
        self.startlevel = 1


    def level(self):
        self.write(arg=f"Level {self.startlevel} ",align="left",font=("Courier",24,"normal"))


    def refresh(self):
        self.clear()


    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game Over",align="center",font=("Courier",70,"normal"))