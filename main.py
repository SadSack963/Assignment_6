from bricks import create_bricks
from ball import Ball
from paddle import Paddle
from turtle import Turtle, Screen
import numpy as np
from random import randint
from time import sleep

ROWS = 5
COLUMNS = 10

screen = Screen()
screen.colormode(255)
screen.setup(width=620, height=405)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()

screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "d")
screen.onkeypress(paddle.move_right, "Right")
screen.listen()

brick_types = np.ones((ROWS, COLUMNS))
brick_array = create_bricks(brick_types)

ball = Ball()
go = True
while go:
    ball.move()
    screen.update()
    sleep(0.01)

screen.update()

screen.exitonclick()
