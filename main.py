from bricks import create_bricks
from ball import Ball
from paddle import Paddle
import constants as c
import level_layout
from background import draw_gradient

from turtle import Screen
from time import sleep

screen = Screen()
screen.colormode(255)
screen.setup(width=c.WIDTH, height=c.HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()

screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "d")
screen.onkeypress(paddle.move_right, "Right")
screen.listen()

level = 1
layout = level_layout.levels[level]["layout"]
brick_array = create_bricks(layout)
# print(brick_array)  # {(0, 0): <bricks.Brick object at 0x00000271BB356E00>, ...}
start_color = level_layout.levels[level]["start_color"]
target_color = level_layout.levels[level]["target_color"]
draw_gradient(start_color, target_color)

ball = Ball()

go = True
while go:
    ball.move()
    for brick in brick_array.values():
        match brick.style:
            case 2:
                brick.cycle_color()
            case 3:
                brick.fillcolor("red")
    screen.update()
    sleep(0.01)

screen.update()

screen.exitonclick()
