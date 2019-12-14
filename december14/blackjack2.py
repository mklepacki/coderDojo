# Moze byc dowolna ilosc graczy 
# Musi byc 1 krupier ktory rozdaje karty
# krupier dobiera karty ostatni
# Kazdy dostaje 2 karty 
# Potem decyduje Hit albo Pass
# Hit - dobiera karte
# Pass - zostajesz z ze swoimi kartami
# Celem jest zebranie 21 pkt
# jesli przekroczysz 21 autoamtycznie przegrywasz
# jesli masz mniej niz krupier to przegrywasz
# AS tp jest 11 lub 1 pkt

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return self.value + ' of ' + self.color

class Deck:
    full_deck = []
    potential_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    potential_colors = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks

    def fill_deck(self):
        pass

    def shuffle_deck(self):
        pass

    def get_deck(self):
        pass

class Player:
    my_cards = []

    def __init__(self, name)
        self.name = name

    def __str__(self):
        return 'My name is ' + self.name + ' and my score is ' + str(self.count_score)

    def hit(self):
        pass

    def pass_turn(self):
        pass

    def count_score(self):
        return 0

class Dealer(Player):
    my_deck =[]

    def deal_cards(self):
        pass


class BlackJackGame:
    pass
