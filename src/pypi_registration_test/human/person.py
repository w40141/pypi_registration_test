from .genger import Gender


class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = Gender(gender)

    def say(self):
        print(f'Hello! I am {self.name}.')
