from bricks import create_bricks, special_bricks
from ball import Ball
from paddle import Paddle
import constants as c
import level_layout

from turtle import Screen


def new_level(current_level):
    next_level = current_level + 1
    layout = level_layout.levels[next_level]["layout"]
    brick_layout = create_bricks(layout)
    # print(brick_array)  # {(0, 0): <bricks.Brick object at 0x00000271BB356E00>, ...}

    return next_level, brick_layout


def level_winner(current_level):
    print(f"You beat Level {current_level}")


def game_winner():
    print("You have beaten the game!")


def color_cycling(count_1, count_2):
    if count_1 % 300 == 0:
        if count_2 % 3 == 0:
            special_bricks(brick_array)
        count_2 += 1
    if count_2 > 62:
        count_2 = 0
    if count_2 == 0:
        count_1 += 1
    return count_1, count_2


def ball_paddle_collision():
    if ball.ycor() < (40 - c.HEIGHT / 2) and (ball.heading() < 0 or ball.heading() > 180):
        for segment in paddle.segments:
            if ball.distance(segment) <= 25:
                ball.bounce_y(segment.id)
                break


def ball_brick_collision():
    # -- This loop runs in about 500us regardless of number of bricks --
    win = True
    current_bricks = brick_array.copy()
    for brick in brick_array.values():
        if brick.isvisible():
            # Beat Level
            win = False
            if ball.distance(brick) <= 30:
                brick.destroy()
                current_bricks.pop(brick.id)  # Remove the brick from the array
                ball.bounce_y()
    return current_bricks, win


screen = Screen()
screen.colormode(255)
screen.setup(width=c.WIDTH, height=c.HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()

# Fast Key Repeat bindings
screen.onkeypress(lambda: paddle.start_repeat(paddle.move_left), "a")
screen.onkeyrelease(paddle.stop_repeat, "a")
screen.onkeypress(lambda: paddle.start_repeat(paddle.move_left), "Left")
screen.onkeyrelease(paddle.stop_repeat, "Left")

screen.onkeypress(lambda: paddle.start_repeat(paddle.move_right), "d")
screen.onkeyrelease(paddle.stop_repeat, "d")
screen.onkeypress(lambda: paddle.start_repeat(paddle.move_right), "Right")
screen.onkeyrelease(paddle.stop_repeat, "Right")


screen.listen()


level = 0
level, brick_array = new_level(level)

ball = Ball()

repeating = False
count_1 = 0
count_2 = 0
game_speed = 300000

go = True
while go:
    ball.move()

    # Bricks Colour Cycling
    count_1, count_2 = color_cycling(count_1, count_2)

    # Detect ball collision with paddle
    ball_paddle_collision()

    # Detect collision with bricks
    brick_array, win = ball_brick_collision()

    # Beat Level - start new level
    if win:
        if level == len(level_layout.levels):
            ball.hideturtle()
            game_winner()
            go = False
        else:
            ball.hideturtle()
            level_winner(level)
            level, brick_array = new_level(level)
            ball.reset_state()

    screen.update()

    # Loop to control game speed
    for _ in range(game_speed):
        pass

screen.update()

screen.exitonclick()
