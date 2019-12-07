board_values = [0,1,2,3,4,5,6,7]

def is_in_board(x, y):
    if 7 >= x >= 0 and 7 >= y >= 0:
        return True
    return False

def queen_horizontal_attack(x1, y1):
    attacked_fields = []
    for i in board_values:
        if i != x1:
            attacked_fields.append([i, y1])
    return attacked_fields

def queen_vertical_attack(x1, y1):
    attacked_fields = []
    for i in board_values:
        if y1 != i:
            attacked_fields.append([x1, i])
    return attacked_fields

def queen_diagonal_attack_1(x1, y1):
    """
    This goes right and down
    """
    pass
def queen_diagonal_attack_2(x1, y1):
    """
    This goes left and down
    """
    pass
def queen_diagonal_attack_3(x1, y1):
    """
    This goes right and up
    """
    pass
def queen_diagonal_attack_4(x1, y1):
    """
    This goes left and up
    """
    pass


def is_queen_attacked(x1, y1, x2, y2):
    pass


    