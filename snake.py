from turtle import Turtle


STARTING_POSITION = [(0,0),(-20,0), (-40,0)]
MOVE = 20
UP = 90
DOWN = 180
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle('square')
            new_segment.color('black')
            new_segment.penup()
            new_segment.shapesize(stretch_wid=0.9, stretch_len=0.9)
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend_snake(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        new_segment = Turtle('square')
        new_segment.color('black')
        new_segment.penup()
        new_segment.shapesize(stretch_wid=0.9, stretch_len=0.9)
        new_segment.goto(x,y)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
