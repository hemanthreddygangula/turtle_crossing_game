from turtle import Screen
from turtle_body import CrossingTurtle
from cars import Cars
from score_board import Score
import time

screen = Screen()
screen.setup(width=600, height=600 )
screen.tracer(0)

turt = CrossingTurtle()
cars = Cars()
score = Score()

screen.listen()
screen.onkey(turt.move_turtle, key='w')

while 1:
    time.sleep(0.2)
    screen.update()
    
    cars.make_cars()
    cars.move_car()

    for car in cars.all_cars:
        # For collision
        if turt.distance(car)<20:
            turt.pos_reset()
    
    if turt.ycor()>=250:
        print('---------------------')
        score.increment_level()
        turt.pos_reset()

screen.exitonclick()