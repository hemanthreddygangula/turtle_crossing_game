from turtle import Turtle
import random, time

POS = [x for x in range(-240, 250, 50)]
colors = ['red', 'blue', 'yellow', 'green', 'violet', 'indigo', 'orange']

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def make_cars(self):
        choice = random.randint(1,4)
        if choice == 1:
            start = random.choice(POS)
            col = random.choice(colors)
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(col)
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.goto(280,start)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(10)
            
