from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.write(f"Level {self.level}")
    
    def increment_level(self):
        self.level+=1
        self.update_score()
