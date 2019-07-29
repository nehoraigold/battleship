class Board():
    def __init__(self, size):
        self.size = size
        self.board = self.create(size)

    def create(self, size):
        board = [ ]
        board.append([" "])

        # Creates header for columns
        for i in range(size):
            board[0].extend([chr(i + 97).upper()])

        # Creates board and row numbers
        for x in range(size):
            board.append([str(x + 1)]) # Board numbers
            board[x + 1].extend(["O"] * size) # Empty board
        return board

    def mark_as_guessed(self, coordinate):
        self.board[coordinate[0]][coordinate[1]] = "X"

    def print(self):
        result = ""
        for row in self.board:
            result += " ".join(row)
            result += "\n"
        print(result)