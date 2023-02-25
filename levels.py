import numpy as np
from turtle import Screen, Turtle
import constants as c
from bricks import create_bricks, Brick
from time import sleep


blank = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]


class Level:
    def __init__(self):
        self.background = "0.gif"
        self.layout = blank.copy()  # [[0] * 10] * 19  # np.zeros((10, 10))  #
        self.layout[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def create_brick(self, x, y):
        global new_brick, row, col
        # print(x, y)
        col = int((x + 300) // 60)
        row = - int((y - 200) // 20) - 1
        # print(row, col)
        # location = (25 - c.EDGE_LR + col * 20 * c.STRETCH, c.EDGE_TB - row * 20)
        if self.layout[row][col] == 1:
            self.layout[row][col] = 0
        else:
            self.layout[row][col] = 1
        # print(self.layout)
        new_brick = True


if __name__ == "__main__":
    def display_level():
        """
        Get the new brick layout and display on the screen.
        Reset flash counters.
        Display the background.
        Reset the ball and paddle.

        :return: brick_layout: New brick array
        :return: total_bricks: Number of bricks displayed
        """
        brick_layout, bricks_created = create_bricks(new_level.layout)
        screen.bgpic(f"images/backgrounds/{new_level.background}")
        screen.update()
        return brick_layout, bricks_created


    screen = Screen()
    screen.colormode(255)
    screen.setup(width=c.WIDTH, height=c.HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    new_level = Level()
    screen.onclick(new_level.create_brick)
    screen.listen()

    brick_layout, bricks_created = display_level()
    # print(brick_layout, bricks_created)

    new_brick = False
    row = -1
    col = -1

    while True:
        screen.update()
        sleep(0.5)
        if new_brick:
            # Hide the turtle before it is removed from the dictionary
            try:
                brick_layout[(row, col)].destroy()
                bricks_created -= 1
            except KeyError:
                pass

            if new_level.layout[row][col] > 0:
                # Create a Turtle object that gets displayed on the screen
                brick = Brick(
                    style=1,
                    row=row,
                    col=col,
                )
                brick_layout[brick.id] = brick
                bricks_created += 1

            # brick_layout, bricks_created = create_bricks(new_level.layout)
            # print(brick_layout, bricks_created)
            new_brick = False


    screen.exitonclick()
