import constants as c
from level_layout import brick_types

from turtle import Turtle, Screen
from random import randint


class Brick(Turtle):
    def __init__(self, style: int, row: int, col: int):
        # Main brick
        super(Brick, self).__init__()
        self.location = (25 - c.EDGE_LR + col * 20 * c.STRETCH, c.EDGE_TB - row * 20)
        self.style = style
        self.id = (row, col)
        self.type = brick_types[self.style]["title"]
        self.hits_required = brick_types[self.style]["hits"]
        self.hits = 0
        self.color_index = 0
        self.fillcolor(brick_types[self.style]["color"][self.color_index])
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=c.STRETCH)
        self.penup()
        self.goto(self.location)
        self.drop_item = brick_types[self.style]["drop"]
        self.start_cycle = False
        self.count = 0
        self.cycle_delay = randint(200, 400)
        self.repeat_rate = 50  # milliseconds

        # Create left and Right edges of brick for collision detection and x bounce
        # Left (invisible)
        self.left = Turtle()
        self.left.color("yellow")
        self.left.shape("square")
        self.left.shapesize(stretch_len=c.STRETCH / 12)  # 5 pixels wide
        self.left.penup()
        self.left.goto(self.location[0] - 28 + c.STRETCH / 12, self.location[1])
        self.left.hideturtle()

        # Right (invisible)
        self.right = Turtle()
        self.right.color("blue")
        self.right.shape("square")
        self.right.shapesize(stretch_len=c.STRETCH / 12)  # 5 pixels wide
        self.right.penup()
        self.right.goto(self.location[0] + 28 - c.STRETCH / 12, self.location[1])
        self.right.hideturtle()

        if self.style in [2, 7, 8]:
            self.start_cycle = True
            self.cycle_color()

    def cycle_color(self):
        if self.start_cycle:
            self.color_index += 1
            if self.color_index == len(brick_types[self.style]["color"]):
                self.color_index = 0
                self.start_cycle = False
            self.fillcolor(brick_types[self.style]["color"][self.color_index])
        Screen().ontimer(self.cycle_color, self.repeat_rate)
        self.count += 1
        if self.count == self.cycle_delay:
            self.start_cycle = True
            self.count = 0

    def destroy(self):
        self.hideturtle()


def create_bricks(layout_array: list):
    rows = len(layout_array)

    # Store the bricks in a dictionary, using (row, col) as the key
    bricks = {}
    for row in range(rows):
        for column in range(c.COLUMNS):
            if layout_array[row][column] > 0:
                brick = Brick(
                    style=layout_array[row][column],
                    row=row,
                    col=column,
                )
                bricks[brick.id] = brick
    return bricks


def create_bricks_below_paddle():
    bricks = {}
    for column in range(c.COLUMNS):
        brick = Brick(
            style=1,
            row=18,
            col=column,
        )
        bricks[brick.id] = brick
    return bricks


if __name__ == "__main__":
    from turtle import Screen
    import level_layout

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=c.WIDTH, height=c.HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    level = 1
    layout = level_layout.levels[level]["layout"]
    brick_array = create_bricks(layout)
    screen.update()

    # print(bricks)
    """{(0, 0): <__main__.Brick object at 0x000001FD847DBF70>, ...}"""
    
    screen.exitonclick()
