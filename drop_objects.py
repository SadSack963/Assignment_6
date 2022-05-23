import constants as c
from scoring import ScoreBoard
from bricks import create_bricks_below_paddle

from turtle import Turtle, Screen
from os import listdir


class DropObject(Turtle):
    def __init__(self):
        super(DropObject, self).__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.in_use = False
        self.style = ""

    def move(self):
        self.forward(1)
        if self.ycor() < -(c.EDGE_TB + 20):
            self.reset_state()

    def reset_state(self):
        self.hideturtle()
        self.in_use = False
        self.style = ""

    def destroy(self):
        self.hideturtle()
        self.in_use = False


def get_icons(folder):
    names = []
    for filename in listdir(folder):
        name = filename.split(".")[0]
        names.append(name)
        Screen().addshape(name=f"images/icons/{filename}")
    return names
