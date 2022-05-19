import constants as c

from turtle import Turtle
from random import randint


class Brick(Turtle):
    def __init__(self, color_index, location, row, col):
        super(Brick, self).__init__()
        self.color_index = color_index
        self.fillcolor(c.COLORS[self.color_index])
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=c.STRETCH)
        self.penup()
        self.goto(location)
        self.style = 2
        self.id = (row, col)

    def cycle_color(self):
        self.color_index += 1
        if self.color_index == len(c.COLORS):
            self.color_index = 0
        self.fillcolor(c.COLORS[self.color_index])


def create_bricks(layout):
    rows = len(layout)

    # Store the bricks in a dictionary, using (row, col) as the key
    bricks = {}
    for row in range(rows):
        for column in range(c.COLUMNS):
            brick = Brick(
                color_index=150,
                location=(25 - c.EDGE_LR + column * 20 * c.STRETCH, c.EDGE_TB - row * 20),
                row=row,
                col=column,
            )
            brick.style = layout[row][column]
            if brick.style == 0:
                brick.hideturtle()
            bricks[brick.id] = brick
    return bricks


def special_bricks(bricks):
    pass
    # ToDo: Consider running this in a different thread
    for brick in bricks.values():
        if brick.isvisible():
            match brick.style:
                case 2:
                    brick.cycle_color()
                case 3:
                    brick.fillcolor("red")


if __name__ == "__main__":
    from turtle import Screen
    from time import sleep
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

    rows = len(layout)
    # Remove some random bricks
    for n in range(30):
        brick_array[randint(0, rows - 1), randint(0, c.COLUMNS - 1)].hideturtle()
        screen.update()
        sleep(1)

    # print(bricks)
    """{(0, 0): <__main__.Brick object at 0x000001FD847DBF70>, ...}"""
    
    screen.exitonclick()
