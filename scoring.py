from messenger import Messenger


class ScoreBoard:
    def __init__(self):
        self.current_score = 0
        try:
            with open("max_score.txt", mode="r") as fp:
                self.max_score = int(fp.readline())
        except FileNotFoundError:
            self.max_score = 0
        self.current_lives = 5
        self.score = Messenger(
            fontcolor="white",
            fonttype="italic",
            fontsize=10,
        )
        self.lives = Messenger(
            fontcolor="white",
            fonttype="italic",
            fontsize=10,
        )

    def increase_score(self, amount, instructions=False):
        """
        Increment / Decrement the score.

        :param amount: integer - can be positive or negative
        :param instructions: boolean - update maximum score if False
        """
        self.current_score += amount
        if not instructions:
            self.save_max_score()
        self.display_score()

    def save_max_score(self):
        if self.current_score > self.max_score:
            self.max_score = self.current_score
            with open("max_score.txt", mode="w") as fp:
                fp.write(str(self.max_score))

    def increase_lives(self, amount):
        """
        Increment / Decrement the lives.

        :param amount: integer - can be positive or negative
        """
        self.current_lives += amount
        self.display_lives()

    def display_score(self):
        self.score.message(f"Score\n{self.current_score} / {self.max_score}", position=(-280, -190))

    def display_lives(self):
        self.lives.message(f"Lives\n{self.current_lives}", position=(280, -190))

    def reset(self):
        self.current_score = 0
        self.current_lives = 5
