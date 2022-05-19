from turtle import Turtle
from time import sleep


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for id in range(-2, 2):
            segment = Turtle()
            segment.color("green")
            segment.shape("square")
            segment.penup()
            segment.goto(id * 20, -190)
            segment.setheading(0)
            segment.velocity = 10
            segment.id = id
            self.segments.append(segment)

    def move_left(self):
        if self.segments[0].xcor() > -285:
            self.move(180)

    def move_right(self):
        if self.segments[-1].xcor() < 285:
            self.move(0)

    def move(self, heading):
        for segment in self.segments:
            segment.setheading(heading)
            segment.forward(segment.velocity)


if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=620, height=405)
    screen.bgcolor("black")
    screen.tracer(0)

    paddle = Paddle()

    screen.onkeypress(paddle.move_left, "a")
    screen.onkeypress(paddle.move_left, "Left")
    screen.onkeypress(paddle.move_right, "d")
    screen.onkeypress(paddle.move_right, "Right")
    screen.listen()

    while True:
        screen.update()
        sleep(0.01)

    screen.exitonclick()
