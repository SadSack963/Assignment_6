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
        self.active = False
        self.count = 0

    def message(self, message, position: tuple = None, count=0):
        """
        Displays message at given position.
        Set the message active, and set the count (used externally to clear the message, e.g. after a delay).
        """
        self.reset_state()
        self.count = count
        if position:
            self.setposition(position)
        self.write(arg=message, move=False, align="center", font=self.font)
        self.active = True

    def reset_state(self):
        """
        Clear all messages
        """
        self.clear()
        self.active = False
        self.count = 0
