class Coordinate():
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @staticmethod
    def from_str(string):
        try:
            row = int(string[1:])
            col = int(ord(string[0].upper())) - 64
            return Coordinate(row, col)
        except:
            return False
    
    @staticmethod
    def from_values(row, column):
        try:
            return Coordinate(row, column)
        except:
            return False

    def __repr__(self):
        return (self.row, self.column)

    def __str__(self):
        return "{0}{1}".format(chr(self.column + 96).upper(), str(self.row))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
    
    def is_valid_for(self, board_size):
        return self.row > 0 and self.row <= board_size and self.column > 0 and self.column <= board_size
    
