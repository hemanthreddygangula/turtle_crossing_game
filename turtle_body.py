from turtle import Turtle

class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
    
    def move_turtle(self):
        self.forward(20)
    
    def pos_reset(self):
        self.goto(0,-280)
