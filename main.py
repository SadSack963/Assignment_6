from bricks import create_bricks
from ball import Ball
from paddle import Paddle
from messenger import Messenger
from scoring import ScoreBoard
from drop_objects import DropObject
import constants as c
import level_layout

from turtle import Screen
from time import sleep


def new_level():
    """
    Get the new brick layout and display on the screen.
    Reset flash counters.
    Display the background.
    Reset the ball and paddle.

    :return: brick_layout: New brick array
    """
    global count_1, count_2
    count_1, count_2 = 0, 0
    layout = level_layout.levels[level]["layout"]
    brick_layout = create_bricks(layout)
    screen.bgpic(f"images/background/{level_layout.levels[level]['background']}.gif")
    ball.reset_state()
    paddle.reset_state()
    scoreboard.display_score()
    scoreboard.display_lives()
    screen.update()
    return brick_layout


def level_winner(current_level):
    win_message.message(f"You beat\nLevel {current_level}")
    sleep(3)
    win_message.clear()


def game_winner():
    win_message.message("You have beaten the game!\nWell done!")


def get_drop_object():
    for index in range(len(drop_list)):
        if not drop_list[index].in_use:
            drop_list[index].in_use = True
            return index
    print("Error - all drop objects in use")
    return None


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
    def brick_hit(brick):
        """
        The ball has hit this brick.
        Increment the score.
        Remove it from the array if the brick has been hit sufficient times.

        :param brick: brick which has been hit.
        """
        brick.hits += 1
        scoreboard.increase_score(amount=1, instructions=instructions)
        if brick.hits >= brick.hits_required:
            drop(brick)
            brick.destroy()
            current_bricks.pop(brick.id)  # Remove the brick from the array

    def check_neighbour(id):
        """
        Check brick with the given ID to see if it is visible.
        If so, then this is a simultaneous hit - remove the brick from the array.

        :param id: location of brick in array
        :return: boolean - brick visible
        """
        try:
            neighbouring_brick = brick_array[id]
            if neighbouring_brick.isvisible():
                brick_hit(neighbouring_brick)
                return True
            else:
                return False
        except KeyError:
            return False

    def drop(brick):
        match brick.drop:
            case "+10 points":
                index = get_drop_object()
                if index is not None:
                    drop_list[index].type = brick.drop
                    drop_list[index].shape("turtle")
                    drop_list[index].setheading(-90)
                    drop_list[index].goto(brick.location)
                    drop_list[index].showturtle()

    # Check each brick in the array to see if the ball has hit it.
    level_win = True
    current_bricks = brick_array.copy()  # Copy the array so that we can alter it without breaking the for loop
    for brick in brick_array.values():
        if brick.isvisible():
            level_win = False  # Bricks are still visible -> Level is still active

            # Hit brick on left side
            if ball.distance(brick.left) <= 15:
                brick_hit(brick)
                # Decide which way to bounce
                if ball.heading() < 90 or ball.heading() > 270:  # Travelling
                    # Check for simultaneous hit with neighbouring brick
                    if check_neighbour((brick.id[0], brick.id[1] - 1)):
                        ball.bounce_y()
                    else:
                        ball.bounce_x()
                else:
                    ball.bounce_y()
                break  # Prevent hits on multiple bricks

            # Hit brick on right side
            if ball.distance(brick.right) <= 15:
                brick_hit(brick)
                # Decide which way to bounce
                if 90 < ball.heading() < 270:  # Travelling left
                    # Check for simultaneous hit with neighbouring brick
                    if check_neighbour((brick.id[0], brick.id[1] + 1)):
                        ball.bounce_y()
                    else:
                        ball.bounce_x()
                else:
                    ball.bounce_y()
                break  # Prevent hits on multiple bricks

            # Hit brick in middle
            if ball.distance(brick) <= 25:
                brick_hit(brick)
                ball.bounce_y()
                break  # Prevent hits on multiple bricks
    return current_bricks, level_win


def display_instructions():
    """
    Display instruction message on screen
    """
    notify_normal.message(
        message="Use the A Key or the Left cursor key\nto move the paddle to the left.\n"
                "Use the D key or the Right cursor key\nto move the paddle to the right.\n"
                "You will lose a life\nif the ball goes past the paddle.\n\n"
                "Press P to pause the game.\n\n"
                "PRESS SPACE TO START",
        position=(0, -120),
    )


def start_game():
    """
    Start the game.
    Turn off instructions. Set to Level 1 and clear the screen.
    Display the new brick layout.
    """
    global instructions, level, brick_array, count_1, count_2
    if instructions:
        instructions = False
        level = 1
        clear_screen()
        brick_array = new_level()
        scoreboard.reset()


def clear_screen():
    """
    Remove all bricks.
    Reset the ball and paddle positions.
    Clear any existing messages.
    """
    for brick in brick_array.values():
        brick.hideturtle()
    ball.reset_state()
    paddle.reset_state()
    notify_normal.message_clear()


def pause_game():
    """
    Toggle the pause state.
    If in pause, display message and call the infinite loop.
    If coming out of pause, remove the message.
    If instructions is True then display the instructions.
    """
    global pause
    if not pause:
        pause = True
        notify_normal.message(message="PAUSED")
        loop()
    else:
        pause = False
        if instructions:
            display_instructions()


def loop():
    """
    Do nothing while in pause.
    """
    while pause:
        sleep(0.1)
        screen.update()


"""
    ##############################
    #     Start of game code     # 
    ##############################
"""

screen = Screen()
screen.colormode(255)
screen.setup(width=c.WIDTH, height=c.HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Variables
level = 0
count_1, count_2 = 0, 0
game_speed = 300000
pause = False
instructions = True

# Define objects
notify_normal = Messenger(
    fontcolor="white",
    fontsize=16,
    fonttype="normal"
)
paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()
win_message = Messenger(
    fontcolor="red",
    fontsize=20,
    fonttype="italic"
)
drop_list = [DropObject() for _ in range(5)]

brick_array = new_level()
display_instructions()

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

"""
    ##############################
    #         Game Loop          # 
    ##############################
"""
go = True
while go:
    ball.move()

    # Detect ball collision with paddle
    ball_paddle_collision()

    # Detect collision with bricks
    brick_array, win = ball_brick_collision()

    for item in drop_list:
        if item.in_use:
            item.move()

    # Beat Level - start new level
    if win:
        if level == len(level_layout.levels) - 1:
            ball.hideturtle()
            game_winner()
            go = False
        else:
            ball.hideturtle()
            level_winner(level)
            if not instructions:
                level += 1
            brick_array = new_level()

    screen.update()

    # Loop to control game speed
    for _ in range(game_speed):
        pass

screen.update()

screen.exitonclick()
