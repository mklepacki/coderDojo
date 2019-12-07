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
    return []

def queen_diagonal_attack_2(x1, y1):
    """
    This goes left and down
    """
    return []

def queen_diagonal_attack_3(x1, y1):
    """
    This goes right and up
    """
    return []

def queen_diagonal_attack_4(x1, y1):
    """
    This goes left and up
    """
    return []

def queen_attack(x1, y1):
    return queen_horizontal_attack(x1, y1) + queen_vertical_attack(x1, y1) + queen_diagonal_attack_1(x1, y1) + queen_diagonal_attack_2(x1,y1) + queen_diagonal_attack_3(x1, y1) + queen_diagonal_attack_4(x1,y1)

def is_queen_attacked(x1, y1, x2, y2):
    """This is main function, that will provide answer to the question """
    attacked_fields = queen_attack(x1, y1)
    second_queen_position = [x2, y2]
    if second_queen_position in attacked_fields:
        return True
    return False

print(is_queen_attacked(0,0,1,1))