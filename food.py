from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
        self.color('purple')
        self.penup()
        self.speed('fastest')
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)