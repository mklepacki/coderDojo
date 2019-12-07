class Figure:
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def attack(self):
        raise NotImplementedError

    def move(self):
        pass

class Queen(Figure):
    
    def attack(self):
        print('Im attacking...')

class Knight(Figure):
    pass

class Bishop(Figure):
    pass

class King(Figure):
    pass

class Tower(Figure):
    pass

class Pawn(Figure):
    pass

class ChessBoard:
    size = 8
    def __init__(self):
        pass

    