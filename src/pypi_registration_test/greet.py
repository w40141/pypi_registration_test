class Greet(object):

    def __init__(self, number):
        self.number = number

    def say(self):
        print(f'My number is {self.number}.')

    def gprint(self):
        print(self.number)
