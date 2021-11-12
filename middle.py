from turtle import Turtle
from random import randint


class Middle_Line(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 0.2)
        self.penup()
        self.hideturtle()
        self.pensize(10)
        self.color("white")
        self.speed("fastest")
        self.draw_dashed_middle_line()


    # def draw_dashed_middle_line(self):
    #     self.goto(x=0,y=-280)
    #     self.setheading(90)
    #     self.pendown()
    #     self.goto(x=0, y=-240)
    #     # for _ in range(15):
    #     #     self.pendown()
    #     #     self.forward(20)
    #     #     self.penup()
    #     #     self.forward(20)

    def draw_dashed_middle_line(self):
        for _ in range(15):
            self.goto(x=0,y=-275+_*40)
            self.stamp()



