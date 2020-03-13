"""
Product descriptions from Acme Corporation
"""
from random import randint


class Product:
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 10000000)

    def stealability(self):
        """Divide the price by the weight to get ratio for stealability"""
        ratio = self.price / self.weight
        if ratio > 0.5:
            print('Not so stealable...')
        elif .05 < ratio < 1:
            print('Kinda stealable')
        else:
            print('Very stealable!')

    def explode(self):
        """Flammability times weight to get explode"""
        bomb = self.flammability * self.weight
        if bomb > 10:
            print('...fizzle')
        elif 10 <= bomb < 50:
            print('...boom!')
        else:
            print('...BABOOM!!')

class BoxingGlove(Product):
    """Subclass of Product"""

    def __init__(self, name, weight = 10):
        super().__init__(name, weight)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        w = self.weight
        if w < 5:
            print('That tickles.')
        elif 5 < w < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')

        