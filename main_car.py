import time
from turtle import Screen
from player_turtle import Player
from score_car import Scoreboard
from turtle_car import Car






show = Screen()
mycar =  Car()
my_player = Player()
score = Scoreboard()

show.tracer(0)
show.setup(width=800,height=650)
show.bgcolor("white")
show.title("Race Game by Pramod")




show.listen()
show.onkey(my_player.move,"Up")



game_on = True
score.level()
while game_on:
    time.sleep(0.095)                                   
    mycar.create()                             #create a new car every time 
    mycar.move()                               #Moves a car
    show.update()
    
    for c in mycar.cars:                      #detecting collison with car 
        if c.distance(my_player) < 20:
            score.gameover()
            game_on = False

    if my_player.ycor() > 300:
        score.startlevel+=1
        score.refresh()
        score.level()
        my_player.refresh()
        mycar.car_speeds+=15

show.exitonclick()




