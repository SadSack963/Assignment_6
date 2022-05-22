from turtle import Turtle
from time import sleep


class Messenger(Turtle):
    def __init__(self, fontcolor, fontsize, fonttype):
        """
        Turtle Class to enable writing messages to the screen
        """
        super(Messenger, self).__init__()
        self.pu()
        self.hideturtle()
        self.pencolor(fontcolor)
        self.font = ("Comic Sans", fontsize, fonttype)

    def message(self, message, position: tuple = None):
        """
        Displays message for the given time.
        """
        self.clear()
        if position:
            self.setposition(position)
        self.write(arg=message, move=False, align="center", font=self.font)

    def message_clear(self):
        """
        Clear all previous messages
        """
        self.clear()
