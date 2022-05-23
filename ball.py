import constants as c

from turtle import Turtle
from random import choice
from time import sleep

VELOCITY = 5


class Ball(Turtle):
    initial_angles = [angle for angle in range(30, 151, 5) if angle < 80 or angle > 100]

    def __init__(self):
        super(Ball, self).__init__()
        self.color("grey90", "grey20")
        self.shape("circle")
        self.penup()
        self.goto(0, 70 - c.HEIGHT / 2)
        self.setheading(choice(self.initial_angles))
        self.velocity = VELOCITY

    def reset_state(self):
        self.showturtle()
        self.goto(0, 50 - c.HEIGHT / 2)
        self.setheading(choice(self.initial_angles))
        self.velocity = VELOCITY

    def move(self, instructions=False):
        self.forward(self.velocity)
        # Bounce at screen edges
        if self.xcor() >= c.EDGE_LR and (self.heading() < 90 or self.heading() > 270):  # Travelling right
            self.bounce_x()
        elif self.xcor() <= -c.EDGE_LR and 90 < self.heading() < 270:  # Travelling left
            self.bounce_x()
        if self.ycor() >= c.EDGE_TB and 0 < self.heading() < 180:  # Travelling up
            self.bounce_y()
        elif self.ycor() <= -c.EDGE_TB and 180 < self.heading() <= 359 and instructions:  # Travelling down
            self.bounce_y()

    def bounce_x(self, instructions=False):
        self.setheading(180 - self.heading())
        self.move(instructions)

    def bounce_y(self, modifier=0, instructions=False):
        # Don't allow the ball angle to become too shallow
        if 180 < self.heading() < 220 and modifier < 0 or \
                340 < self.heading() < 359 and modifier > 0:
            modifier = 0
        new_angle = - (modifier * 5 + self.heading())
        self.setheading(new_angle)
        self.move(instructions)


if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=c.WIDTH, height=c.HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    ball = Ball()

    go = True
    while go:
        ball.move()
        screen.update()
        sleep(0.01)

    screen.exitonclick()
