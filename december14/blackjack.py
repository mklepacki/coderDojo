class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    
    def __str__(self):
        return '{} of {}'.format(self.value, self.color)

class Deck:
    pass

class Game:
    pass
