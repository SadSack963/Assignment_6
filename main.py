import time

from bricks import create_bricks, special_bricks
from ball import Ball
from paddle import Paddle
import constants as c
import level_layout
from background import draw_gradient

from turtle import Screen
from time import sleep


def new_level(current_level):
    print(f"You beat Level {current_level}")
    next_level = current_level + 1
    layout = level_layout.levels[next_level]["layout"]
    brick_layout = create_bricks(layout)
    # print(brick_array)  # {(0, 0): <bricks.Brick object at 0x00000271BB356E00>, ...}

    # GRADIENT REALLY SLOWS DOWN ANIMATION
    # ====================================
    # start_color = level_layout.levels[next_level]["start_color"]
    # target_color = level_layout.levels[next_level]["target_color"]
    # draw_gradient(start_color, target_color)
    return next_level, brick_layout


def winner():
    print("You have beaten the game!")


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

level = 0
level, brick_array = new_level(level)

ball = Ball()
count = 0

go = True
while go:
    ball.move()

    # ToDo: Consider running this in a different thread
    if count % 50 == 0:
        special_bricks(brick_array)
    count += 1

    # Detect collision with paddle
    # ToDo: Maybe use different segments to change the bounce angle
    if ball.ycor() < (40 - c.HEIGHT / 2) and (ball.heading() < 0 or ball.heading() > 180):
        for segment in paddle.segments:
            if ball.distance(segment) <= 25:
                ball.bounce_y(segment.id)
                break

    # This loop runs in about 500us
    # Detect collision with bricks
    win = True
    current_bricks = brick_array.copy()
    for brick in brick_array.values():
        if brick.isvisible():
            # Beat Level
            win = False
            if ball.distance(brick) <= 25:
                brick.destroy()
                current_bricks.pop(brick.id)
                ball.bounce_y()
    brick_array = current_bricks.copy()

    # Beat Level - start new level
    if win:
        if level == len(level_layout.levels):
            winner()
            go = False
        else:
            ball.hideturtle()
            level, brick_array = new_level(level)
            ball = Ball()

    screen.update()
    # sleep(0.005)
    for _ in range(300000):
        pass

screen.update()

screen.exitonclick()
