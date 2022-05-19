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
        if self.xcor() >= 290 or self.xcor() <= -290:
            self.bounce_x()
        if self.ycor() >= 190 or self.ycor() <= -190:
            self.bounce_y()

    def bounce_x(self):
        self.setheading(180 - self.heading())

    def bounce_y(self):
        self.setheading(-self.heading())


if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=620, height=405)
    screen.bgcolor("black")
    screen.tracer(0)

    ball = Ball()

    go = True
    while go:
        ball.move()
        screen.update()
        sleep(0.01)

    screen.exitonclick()
