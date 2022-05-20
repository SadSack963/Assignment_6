import constants as c

from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color("silver")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.setheading(-45)
        self.velocity = 5

    def move(self):
        self.forward(self.velocity)
        # Bounce at screen edges
        if self.xcor() >= c.EDGE_LR or self.xcor() <= -c.EDGE_LR:
            self.bounce_x()
        if self.ycor() >= c.EDGE_TB or self.ycor() <= -c.EDGE_TB:
            self.bounce_y()

    def bounce_x(self):
        self.setheading(180 - self.heading())

    def bounce_y(self, modifier=0):
        new_angle = - (modifier * 5 + self.heading())
        self.setheading(new_angle)


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
