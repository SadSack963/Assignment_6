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
    start_color = level_layout.levels[next_level]["start_color"]
    target_color = level_layout.levels[next_level]["target_color"]
    draw_gradient(start_color, target_color)
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

go = True
while go:
    ball.move()
    # ToDo: Consider running this in a different thread
    # special_bricks(brick_array)

    # Detect collision with paddle
    # ToDo: Maybe use different segments to change the bounce angle
    if ball.ycor() < (40 - c.HEIGHT / 2) and (ball.heading() < 0 or ball.heading() > 180):
        for segment in paddle.segments:
            if ball.distance(segment) <= 25:
                ball.bounce_y()

    # ToDo: Consider running this in a different thread
    # Detect collision with bricks
    win = True
    for brick in brick_array.values():
        if brick.isvisible():
            # Beat Level
            win = False
            if ball.distance(brick) <= 25:
                brick.destroy()

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
    for _ in range(100):
        pass

screen.update()

screen.exitonclick()
