from bricks import create_bricks, create_bricks_below_paddle
from ball import Ball
from paddle import Paddle
from messenger import Messenger
from scoring import ScoreBoard
from drop_objects import DropObject, get_icons
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
    :return: total_bricks: Number of bricks displayed
    """
    layout = level_layout.levels[level]["layout"]
    brick_layout, bricks_created = create_bricks(layout)
    screen.bgpic(f"images/backgrounds/{level_layout.levels[level]['background']}.gif")
    ball.reset_state()
    paddle.reset_state()
    scoreboard.display_score()
    scoreboard.display_lives()
    if not instructions:
        pause_game()
    screen.update()
    return brick_layout, bricks_created


def level_winner(current_level):
    win_message.message(f"You beat\nLevel {current_level}")
    sleep(3)
    win_message.clear()


def game_winner():
    win_message.message(
        "You have beaten the game!\nWell done!\n"
        "CLICK THE SCREEN TO EXIT.",
    )


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
    def brick_hit(hit_brick):
        """
        The ball has hit this brick.
        Increment the score.
        Remove it from the array if the brick has been hit sufficient times.

        :param hit_brick: brick which has been hit.
        """
        global total_bricks
        hit_brick.hits += 1
        scoreboard.adjust_score(amount=1, instructions=instructions)
        if hit_brick.hits >= hit_brick.hits_required:
            brick_drop_item(hit_brick)
            hit_brick.destroy()
            current_bricks.pop(hit_brick.id)  # Remove the brick from the array
            total_bricks -= 1

    def check_neighbour(brick_id):
        """
        Check brick with the given ID to see if it is visible.
        If so, then this is a simultaneous hit - remove the brick from the array.

        :param brick_id: location of brick in array
        :return: boolean - brick visible
        """
        try:
            neighbouring_brick = brick_array[brick_id]
            if neighbouring_brick.isvisible():
                brick_hit(neighbouring_brick)
                return True
            else:
                return False
        except KeyError:
            return False

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


def get_drop_object():
    """
    Check the list of drop items to see if one is not in use.
    If found, return the list index for that item.

    :return: index: List index of the allocated drop item
    :rtype: int
    """
    for index in range(len(drop_list)):
        if not drop_list[index].in_use:
            drop_list[index].in_use = True
            return index
    print("Error - all drop objects in use")
    return None


def brick_drop_item(brick):
    """
    Drop an item when the brick is destroyed.

    :param brick: The brick being destroyed
    :type brick:
    """
    if brick.style in c.SPECIAL_BRICKS:
        index = get_drop_object()
        if index is not None:
            drop_list[index].style = brick.drop_item
            file = level_layout.brick_types[brick.style]["sprite"]
            drop_list[index].shape(f"images/icons/{file}.gif")
            drop_list[index].setheading(-90)
            drop_list[index].goto(brick.location)
            drop_list[index].showturtle()


def ball_drop_item_collision(item):
    """
    If the drop item is hit by the ball, then add a bonus of 50 points to the score.
    Perform the item's special operation, and make the item in the list available again.

    :param item: item from drop_list
    :type item: DropObject
    """
    if ball.distance(item) < 20:
        location = (ball.xcor(), ball.ycor() - 30)
        ball_message.message("+50\nbonus", location, count=70)
        scoreboard.adjust_score(amount=50, instructions=instructions)
        do_special_item_operation(item)
        item.destroy()


def paddle_drop_item_collision(item):
    """
    If the drop item is hit by the paddle, then increment the score.
    Perform the item's special operation, and make the item in the list available again.

    :param item: item from drop_list
    :type item: DropObject
    """
    for segment in paddle.segments:
        if segment.distance(item) < 20:
            scoreboard.adjust_score(amount=1, instructions=instructions)
            do_special_item_operation(item)
            item.destroy()


def do_special_item_operation(item):
    """
    Perform the item's special operation.

    :param item: item from drop_list
    :type item: DropObject
    """
    global total_bricks
    drop_message.message(item.style, item.position(), count=70)
    match item.style:
        case "+10\npoints":
            # Increase score by 10 points
            scoreboard.adjust_score(amount=10, instructions=instructions)
        case "-10\npoints":
            # Decrease score by 10 points
            scoreboard.adjust_score(amount=-10, instructions=instructions)
        case "+1\nlife":
            # Gain a life
            scoreboard.adjust_lives(1)
        case "-1\nlife":
            # Lose a life
            scoreboard.adjust_lives(-1)
        case "wall":
            # Create a wall below the paddle
            for brick in brick_array.values():
                if brick.id[0] == 18:
                    brick.hideturtle()
            new_bricks, bricks_created = create_bricks_below_paddle()
            total_bricks += bricks_created
            brick_array.update(new_bricks)


def display_instructions():
    """
    Display instruction message on screen
    """
    notify_normal.message(
        message="Use the A Key or the Left cursor key\nto move the paddle to the left.\n"
                "Use the D key or the Right cursor key\nto move the paddle to the right.\n"
                "You will lose a life\nif the ball goes past the paddle.\n\n"
                "Press P, S or Down cursor key to pause the game.\n\n"
                "PRESS SPACE TO START",
        position=(0, -120),
    )


def start_game():
    """
    Start the game.
    Turn off instructions. Set to Level 1 and clear the screen.
    Display the new brick layout.
    """
    global instructions, level, brick_array, total_bricks
    if instructions:
        instructions = False
        level = 1
        clear_screen()
        scoreboard.reset_state()
        brick_array, total_bricks = new_level()


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
    notify_normal.reset_state()


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
        pause_loop()
    else:
        pause = False
        notify_normal.message(message="3")
        sleep(0.5)
        notify_normal.message(message="2")
        sleep(0.5)
        notify_normal.message(message="1")
        sleep(0.5)
        notify_normal.reset_state()
        if instructions:
            display_instructions()


def pause_loop():
    """
    Do nothing while in pause.
    """
    while pause:
        sleep(0.1)
        screen.update()


def check_lives():
    """
    Check if number of lives remaining is zero.
    Display a message - LOSER.

    :return: True if all lives have been used, else False.
    :rtype: boolean
    """
    if scoreboard.current_lives <= 0:
        notify_normal.message(
            message="!! LOSER !!\n"
                    "All of your lives have been used.\n"
                    "Better luck next time...\n"
                    "CLICK THE SCREEN TO EXIT.",
            position=(0, -50),
        )

        return True
    return False


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
level = 0  # Demo level
game_speed = 300000  # Used to control the Game Loop Time
pause = False

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
    fonttype="bold italic"
)
drop_message = Messenger(
    fontcolor="white",
    fontsize=10,
    fonttype="bold"
)
ball_message = Messenger(
    fontcolor="white",
    fontsize=10,
    fonttype="bold"
)
icon_names = get_icons(folder="images/icons/")
drop_list = [DropObject() for _ in range(5)]

# Start with the Instructions screen
instructions = True
brick_array, total_bricks = new_level()
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
screen.onkeyrelease(pause_game, "s")
screen.onkeyrelease(pause_game, "Down")

screen.listen()

"""
    ##############################
    #         Game Loop          # 
    ##############################
"""
go = True
while go:
    """
    Total loop time (excluding the time delay at the bottom) 
    varies from 15ms to 3ms depending upon the number of turtles on the screen.
    
    """
    # Move the ball
    ball.move(instructions)
    if not instructions and ball.ycor() <= -c.EDGE_TB:
        scoreboard.adjust_lives(-1)
        no_lives = check_lives()
        # Check if all lives used up
        if no_lives:
            go = False
            break
        paddle.reset_state()
        ball.reset_state()
        pause_game()
        continue

    # Clear the message after a delay
    if ball_message.active:
        ball_message.count -= 1
        if ball_message.count <= 0:
            ball_message.reset_state()

    # Detect ball collision with paddle
    ball_paddle_collision()

    # Detect collision with bricks
    # Collision detection is about 0.5ms regardless of number of bricks
    brick_array, bricks_destroyed = ball_brick_collision()

    # Move the dropped items and check for collisions
    drop_items_in_use = False
    for drop_item in drop_list:
        if drop_item.in_use:
            drop_items_in_use = True
            drop_item.move()
            ball_drop_item_collision(drop_item)
            paddle_drop_item_collision(drop_item)
            # Check if all lives used up
            no_lives = check_lives()
            if no_lives:
                go = False
                break

    # Clear the message after a delay
    if drop_message.active:
        drop_message.count -= 1
        if drop_message.count <= 0:
            drop_message.reset_state()

    # Check to see if the level is complete
    if bricks_destroyed and not drop_items_in_use:
        if level == len(level_layout.levels) - 1:
            # Beat All Levels - end the game
            ball.hideturtle()
            game_winner()
            go = False
        else:
            # Beat Level - start new level
            ball.hideturtle()
            level_winner(level)
            if not instructions:
                level += 1
            brick_array, total_bricks = new_level()

    # Screen update time varies from about 13ms with a lot of bricks
    #   down to about 2ms with very few bricks on screen
    screen.update()

    # Loop to control game speed - much better than time.sleep()!
    # For game_speed = 300000, loop time is about 10ms
    # Use the number of bricks to give a constant game speed.
    # This keeps the game loop time to approximately 15 to 18 milliseconds
    # with game_speed set to 300000.
    loop_delay = int(game_speed * (1 - total_bricks / 100))

    for _ in range(loop_delay):
        pass


screen.update()

screen.exitonclick()
