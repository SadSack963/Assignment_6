import turtle

import constants as c

from turtle import Turtle, Screen
from time import sleep

VELOCITY = 12


class Paddle:
    def __init__(self):
        self.repeat = False  # Fast Key Repeat
        self.repeat_rate = 20  # milliseconds
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        """
        Create a paddle consisting of several turtles. This helps with accurate collision detection.
        The segment ID is used to alter the ball angle when a collision occurs.
        """
        for index in range(-2, 3):
            segment = Turtle()
            segment.color("black")
            segment.shape("square")
            segment.penup()
            segment.goto(index * 20, 60 - c.HEIGHT // 2)
            segment.setheading(0)
            segment.velocity = VELOCITY
            segment.id = index
            self.segments.append(segment)

    def start_repeat(self, func):
        """
        Turns Key Repeat ON.
        Calls the function passed to it -  move_left() or move_right().

        :param func: The lambda function is passed from onkeypress() in main.py
        """
        # Smooth fast key repeat
        # https://stackoverflow.com/questions/44863600/turtle-graphics-keypress-event-not-repeating
        if not self.repeat:
            self.repeat = True
            func()

    def stop_repeat(self):
        """
        Turn Key Repeat OFF
        """
        self.repeat = False

    def move_left(self):
        """
        Move the paddle left (heading 180), until it hits the edge of the screen.
        If Key Repeat is ON, set an event timer to run this function again.
        """
        if self.segments[0].xcor() > 7 - c.EDGE_LR:
            self.move(180)
        if self.repeat:
            Screen().ontimer(self.move_left, self.repeat_rate)

    def move_right(self):
        """
        Move the paddle right (heading 0), until it hits the edge of the screen.
        If Key Repeat is ON, set an event timer to run this function again.
        """
        if self.segments[-1].xcor() < c.EDGE_LR - 8:
            self.move(0)
        if self.repeat:
            Screen().ontimer(self.move_right, self.repeat_rate)

    def move(self, heading):
        """
        Move the paddle the desired distance at the requested heading.

        :param heading: turtle heading
        :type heading: float
        """
        for segment in self.segments:
            segment.setheading(heading)
            segment.forward(segment.velocity)

    def reset_state(self):
        for segment in self.segments:
            segment.goto(segment.id * 20, 50 - c.HEIGHT // 2)
            segment.setheading(0)
            segment.velocity = VELOCITY


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
