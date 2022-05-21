from bricks import create_bricks, special_bricks
from ball import Ball
from paddle import Paddle
from messenger import Messenger
import constants as c
import level_layout

from turtle import Screen
from time import sleep


def new_level():
    global count_1, count_2
    count_1, count_2 = 0, 0
    layout = level_layout.levels[level]["layout"]
    brick_layout = create_bricks(layout)
    screen.bgpic(f"images/background/{level_layout.levels[level]['background']}.gif")
    screen.update()
    return brick_layout


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
    """
    Check for a collision between the ball and the paddle.
    Only checks when the ball is at the approximate height of the paddle and travelling downwards.
    """
    if ball.ycor() < (80 - c.HEIGHT / 2) and (ball.heading() < 0 or ball.heading() > 180):
        for segment in paddle.segments:
            if ball.distance(segment) <= 20:
                ball.bounce_y(segment.id)
                break


def ball_brick_collision():
    """
    Check for a collision between the ball and a brick. Only one collision is allowed.
    Make sure the ball is travelling in the right direction when detecting collision with the sides of the brick.
    Hit bricks are removed from the array, to speed up the loop.

    :return: Array with brick removed, level complete flag

    """
    # -- This loop runs in about 500us regardless of number of bricks --
    win = True
    current_bricks = brick_array.copy()
    for brick in brick_array.values():
        if brick.isvisible():
            # Beat Level
            win = False
            if ball.distance(brick.left) <= 15:
                brick.destroy()
                current_bricks.pop(brick.id)  # Remove the brick from the array
                if ball.heading() < 90 or ball.heading() > 270:  # Travelling right
                    ball.bounce_x()
                else:
                    ball.bounce_y()
                break  # Prevent hits on multiple bricks
            if ball.distance(brick.right) <= 15:
                brick.destroy()
                current_bricks.pop(brick.id)  # Remove the brick from the array
                if 90 < ball.heading() < 270:  # Travelling left
                    ball.bounce_x()
                else:
                    ball.bounce_y()
                break  # Prevent hits on multiple bricks
            if ball.distance(brick) <= 25:
                brick.destroy()
                current_bricks.pop(brick.id)  # Remove the brick from the array
                ball.bounce_y()
                break  # Prevent hits on multiple bricks
    return current_bricks, win


def display_instructions():
    notify_normal.message_time(
        message="Use the A Key or the Left cursor key\nto move the paddle to the left.\n\n"
                "Use the D key or the Right cursor key\nto move the paddle to the right.\n\n"
                "You will lose a life\nif the ball goes past the paddle.\n\n"
                "PRESS SPACE TO START",
        time=0,
    )


def start_game():
    global instructions, level, brick_array, count_1, count_2
    if instructions:
        instructions = False
        level = 1
        clear_screen()
        brick_array = new_level()


def clear_screen():
    for brick in brick_array.values():
        brick.hideturtle()
    ball.reset_state()
    paddle.reset_state()
    notify_normal.message_clear()


def pause_game():
    global pause
    if not pause:
        pause = True
        notify_normal.message_time(message="PAUSED")
        loop()
    else:
        pause = False
        notify_normal.message_clear()
        if instructions:
            display_instructions()


def loop():
    while pause:
        sleep(0.1)
        screen.update()


screen = Screen()
screen.colormode(255)
screen.setup(width=c.WIDTH, height=c.HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

notify_normal = Messenger(
    fontcolor="white",
    fontsize=16,
    fonttype="normal"
)
paddle = Paddle()
ball = Ball()

# Fast Key Repeat bindings
screen.onkeypress(lambda: paddle.start_repeat(paddle.move_left) if not pause else None, "a")
screen.onkeyrelease(paddle.stop_repeat, "a")
screen.onkeypress(lambda: paddle.start_repeat(paddle.move_left) if not pause else None, "Left")
screen.onkeyrelease(paddle.stop_repeat, "Left")

screen.onkeypress(lambda: paddle.start_repeat(paddle.move_right) if not pause else None, "d")
screen.onkeyrelease(paddle.stop_repeat, "d")
screen.onkeypress(lambda: paddle.start_repeat(paddle.move_right) if not pause else None, "Right")
screen.onkeyrelease(paddle.stop_repeat, "Right")

screen.onkeyrelease(start_game, "space")
screen.onkeyrelease(pause_game, "p")

screen.listen()

level = 0
brick_array = new_level()
count_1, count_2 = 0, 0

game_speed = 300000

pause = False
instructions = True
display_instructions()

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
            if not instructions:
                level += 1
            brick_array = new_level()
            ball.reset_state()

    screen.update()

    # Loop to control game speed
    for _ in range(game_speed):
        pass

screen.update()

screen.exitonclick()
