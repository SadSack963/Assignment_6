from turtle import Turtle
from random import randint


STRETCH = 3


class Brick(Turtle):
    def __init__(self, color, position, row, col):
        super(Brick, self).__init__()
        self.fillcolor(color)
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=STRETCH)
        self.penup()
        self.goto(position)
        self.id = (row, col)


if __name__ == "__main__":
    from turtle import Screen
    ROWS = 5
    COLUMNS = 10

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=620, height=405)
    screen.bgcolor("black")
    screen.tracer(0)

    # Store the bricks in a dictionary, using (row, col) as the key
    bricks = {}
    for row in range(ROWS):
        for column in range(COLUMNS):
            brick = Brick(
                color=(randint(0, 255), randint(0, 255), randint(0, 255)),
                position=(-274 + column * 20 * STRETCH, 190 - row * 20),
                row=row,
                col=column,
            )
            bricks[brick.id] = brick

    screen.update()
    # print(bricks)
    """{(0, 0): <__main__.Brick object at 0x000001FD847DBF70>, ...}"""
    
    screen.exitonclick()
