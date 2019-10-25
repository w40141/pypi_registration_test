import pandas as pd


class Hello(object):

    def __init__(self, number):
        self.number = number

    def nprint(self):
        print(self.number)

    def say(self):
        print(f'Hello! My number is {self.number}.')

    def series(self):
        return pd.Series([self.number])
