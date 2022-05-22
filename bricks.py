import constants as c

from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color_index, location, row, col):
        # Main brick
        super(Brick, self).__init__()
        self.color_index = color_index
        self.fillcolor(c.COLORS[self.color_index])
        self.pencolor("white")
        self.shape("square")
        self.shapesize(stretch_len=c.STRETCH)
        self.penup()
        self.goto(location)
        self.style = 1
        self.hits_required = 1
        self.hits = 0
        self.id = (row, col)

        # Create left and Right edges of brick for collision detection and x bounce
        # Left section
        self.left = Turtle()
        self.left.color("yellow")
        self.left.shape("square")
        self.left.shapesize(stretch_len=c.STRETCH / 12)  # 5 pixels wide
        self.left.penup()
        self.left.goto(location[0] - 28 + c.STRETCH / 12, location[1])
        self.left.hideturtle()

        # Right section
        self.right = Turtle()
        self.right.color("blue")
        self.right.shape("square")
        self.right.shapesize(stretch_len=c.STRETCH / 12)  # 5 pixels wide
        self.right.penup()
        self.right.goto(location[0] + 28 - c.STRETCH / 12, location[1])
        self.right.hideturtle()

    def cycle_color(self, colors: list):
        self.color_index += 1
        if self.color_index == len(colors):
            self.color_index = 0
        self.fillcolor(c.COLORS_CYCLE[self.color_index])

    def destroy(self):
        self.hideturtle()


def create_bricks(layout):
    rows = len(layout)

    # Store the bricks in a dictionary, using (row, col) as the key
    bricks = {}
    for row in range(rows):
        for column in range(c.COLUMNS):
            if layout[row][column] > 0:
                brick = Brick(
                    color_index=0,
                    location=(25 - c.EDGE_LR + column * 20 * c.STRETCH, c.EDGE_TB - row * 20),
                    row=row,
                    col=column,
                )
                brick.style = layout[row][column]
                bricks[brick.id] = brick
    return bricks


def special_bricks(bricks: [Brick]):
    # ToDo: Types yet to be defined
    for brick in bricks.values():
        if brick.isvisible():
            match brick.style:
                case 2:
                    brick.cycle_color(c.COLORS_CYCLE)
                case 3:
                    brick.fillcolor("red")
                    brick.hits_required = 2


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

    # print(bricks)
    """{(0, 0): <__main__.Brick object at 0x000001FD847DBF70>, ...}"""
    
    screen.exitonclick()
