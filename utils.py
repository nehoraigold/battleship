YES_RESPONSES = ["y", "Y", "yes", "YES", "Yes"]
NO_RESPONSES = ["n", "N", "no", "NO", "No"]

def convert_input_to_coordinate(string):
    try:
        row = int(string[1:])
        col = int(ord(string[0])) - 64
        return (row, col)
    except:
        return False

def convert_coordinate_to_string(coordinate):
    try:
        row, col = coordinate
        return chr(col + 96).upper() + str(row)
    except:
        return False

def validate_coord(coordinate, board_size):
    if not coordinate or not board_size:
        return False
    try:
        (x, y) = coordinate
        return x > 0 and x <= board_size and y > 0 and y <= board_size
    except:
        return False