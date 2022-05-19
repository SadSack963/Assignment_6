import constants as c

from turtle import Turtle
from random import randint


class Brick(Turtle):
    def __init__(self, color_index, location, row, col):
        super(Brick, self).__init__()
        self.color_index = color_index
        self.fillcolor(c.COLORS[self.color_index])
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=c.STRETCH)
        self.penup()
        self.goto(location)
        self.style = 2
        self.id = (row, col)

    def cycle_color(self):
        self.color_index += 1
        if self.color_index == len(c.COLORS):
            self.color_index = 0
        self.fillcolor(c.COLORS[self.color_index])


def create_bricks(style):
    # Store the bricks in a dictionary, using (row, col) as the key
    bricks = {}
    for row in range(c.ROWS):
        for column in range(c.COLUMNS):
            brick = Brick(
                color_index=150,
                location=(25 - c.EDGE_LR + column * 20 * c.STRETCH, c.EDGE_TB - row * 20),
                row=row,
                col=column,
            )
            brick.style = style[row][column]
            if brick.style == 0:
                brick.hideturtle()
            bricks[brick.id] = brick
    return bricks


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    import numpy as np

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=c.WIDTH, height=c.HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    brick_types = np.ones((c.ROWS, c.COLUMNS))
    brick_array = create_bricks(brick_types)
    screen.update()

    # Remove some random bricks
    for n in range(30):
        brick_array[randint(0, c.ROWS - 1), randint(0, c.COLUMNS - 1)].hideturtle()
        screen.update()
        sleep(1)

    # print(bricks)
    """{(0, 0): <__main__.Brick object at 0x000001FD847DBF70>, ...}"""
    
    screen.exitonclick()
