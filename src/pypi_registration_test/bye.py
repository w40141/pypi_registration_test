from .greet import Greet


class Bye(Greet):

    def __init__(self, number):
        super().__init__(number)
        self.letter = 'Bye'

    def say(self):
        super().say()
        print(self.letter)
