import turtle

import constants as c

from turtle import Turtle, Screen
from time import sleep


class Paddle:
    def __init__(self):
        self.repeat = False  # Fast Key Repeat
        self.repeat_rate = 20  # milliseconds
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for index in range(-2, 2):
            segment = Turtle()
            segment.color("green")
            segment.shape("square")
            segment.penup()
            segment.goto(index * 20, 10 - c.HEIGHT / 2)
            segment.setheading(0)
            segment.velocity = 10
            segment.id = index
            self.segments.append(segment)

    def start_repeat(self, func):
        """

        The lambda function is passed from onkeypress() in main.py
        :param func:
        :type func:
        :return:
        :rtype:
        """
        # Smooth fast key repeat
        # https://stackoverflow.com/questions/44863600/turtle-graphics-keypress-event-not-repeating
        if not self.repeat:
            self.repeat = True
            func()

    def stop_repeat(self):
        self.repeat = False

    def move_left(self):
        if self.segments[0].xcor() > 7 - c.EDGE_LR:
            self.move(180)
        if self.repeat:
            Screen().ontimer(self.move_left, self.repeat_rate)

    def move_right(self):
        if self.segments[-1].xcor() < c.EDGE_LR - 8:
            self.move(0)
        if self.repeat:
            Screen().ontimer(self.move_right, self.repeat_rate)

    def move(self, heading):
        for segment in self.segments:
            segment.setheading(heading)
            segment.forward(segment.velocity)


if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=c.WIDTH, height=c.HEIGHT)
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
