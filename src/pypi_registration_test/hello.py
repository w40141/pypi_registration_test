import pandas as pd

from .greet import Greet


class Hello(Greet):

    def __init__(self, number):
        super().__init__(number)
        self.letter = 'Hello'

    def say(self):
        print(self.letter)
        super().say()

    def series(self):
        return pd.Series([self.number])
