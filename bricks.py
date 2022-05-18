from turtle import Turtle
from random import randint


STRETCH = 3


class Brick(Turtle):
    def __init__(self, color, position):
        super(Brick, self).__init__()
        self.fillcolor(color)
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=STRETCH)
        self.penup()
        self.goto(position)


if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=620, height=405)
    screen.bgcolor("black")

    for row in range(5):
        for column in range(10):
            brick = Brick(
                color=(randint(0, 255), randint(0, 255), randint(0, 255)),
                position=(-274 + column * 20 * STRETCH, 190 - row * 20)
            )

    screen.exitonclick()
