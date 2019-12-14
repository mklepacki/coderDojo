import random
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

    def score(self):
        return 0

class Deck:
    full_deck = []
    potential_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    potential_colors = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.fill_deck()
        self.shuffle_deck(100)
    
    def __str__(self):
        return str(self.full_deck)

    def fill_deck(self):
        for _ in range(self.number_of_decks):
            for v in self.potential_values:
                for c in self.potential_colors:
                    card = Card(v, c)
                    self.full_deck.append(card)

    def shuffle_deck(self, num):
        for _ in range(num):
            random.shuffle(self.full_deck)

    def get_deck(self):
        return self.full_deck

class Player:
    my_cards = []

    def __init__(self, name, money=1000):
        self.name = name
        self.money = money

    def __str__(self):
        return 'My name is ' + self.name + ' and my score is ' + str(self.count_score()) + ' and i have ' + str(self.money) + '$' + ' This are my cards ' + str(self.my_cards)

    def hit(self, deck):
        card = deck.pop()
        print(card)
        self.my_cards.append(card)

    def pass_turn(self):
        pass

    def count_score(self):
        return 0

class Dealer(Player):
    my_deck =[]

    def deal_cards(self):
        pass


class BlackJackGame:
    player_list = []
    
    def __init__(self):
        self.create_players()
        self.dealer = Dealer('Dealer')
        self.deck = Deck(1)
        self.deal()

    def __str__(self):
        game_description = 'This is our BlackJack game.\n'
        game_description += 'This is list of players:\n'
        for player in self.player_list:
            game_description += str(player) + '\n'
        game_description += 'This is our deck:\n'
        for card in self.deck.get_deck():
            game_description += str(card) + '\n'
        return game_description

    def create_players(self, num=4):
        for x in range(num):
            player = Player('Player_'+ str(x+1), random.randint(500, 10000))
            self.player_list.append(player)

    def deal(self):
        for player in self.player_list:
            print(len(self.deck.get_deck()))
            player.hit(self.deck.get_deck())

game = BlackJackGame()
# print(game)

# for player in game.player_list:
#     print(player.name)
#     for card in player.my_cards:
#         print(card)
