from turtle import Turtle
from random import randint

ROWS = 5
COLUMNS = 10
STRETCH = 3


class Brick(Turtle):
    def __init__(self, color, location, row, col):
        super(Brick, self).__init__()
        self.fillcolor(color)
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=STRETCH)
        self.penup()
        self.goto(location)
        self.style = 0
        self.id = (row, col)


def create_bricks(style):
    # Store the bricks in a dictionary, using (row, col) as the key
    bricks = {}
    for row in range(ROWS):
        for column in range(COLUMNS):
            brick = Brick(
                color=(randint(0, 255), randint(0, 255), randint(0, 255)),
                location=(-274 + column * 20 * STRETCH, 190 - row * 20),
                row=row,
                col=column,
            )
            brick.style = style[row, column]
            bricks[brick.id] = brick
    return bricks


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
    import numpy as np

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=620, height=405)
    screen.bgcolor("black")
    screen.tracer(0)

    brick_types = np.ones((ROWS, COLUMNS))
    brick_array = create_bricks(brick_types)
    screen.update()

    # Remove some random bricks
    for n in range(30):
        brick_array[randint(0, 4), randint(0, 9)].hideturtle()
        screen.update()
        sleep(1)

    # print(bricks)
    """{(0, 0): <__main__.Brick object at 0x000001FD847DBF70>, ...}"""
    
    screen.exitonclick()
