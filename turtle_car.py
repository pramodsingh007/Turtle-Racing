import time
from turtle import Turtle, colormode
import random




colormode(255)

class Car():
    def __init__(self):
        
        self.cars= []
        self.car_speeds = 10

    def create(self):
        chance = random.choice([1,6,5,7])
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.speed("fastest")
            self.r =  random.randint(0,255)
            self.g = random.randint(0,255)
            self.b = random.randint(0,255)
            car.color(self.r,self.g,self.b)
            self.random_x = random.choice([390,400,450,500,600,700,800])
            self.random_y = random.randint(-250,250)
            car.penup()
            car.goto(self.random_x,self.random_y)
            self.cars.append(car)
            
        

    def move(self):
            for c in self.cars:
                c.backward(self.car_speeds)

   


    
    
    



