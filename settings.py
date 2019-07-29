class Settings():
    def __init__(self):
        self.board_size = self.set_board_size()
        self.opponent_is_computer = True

    def set_board_size(self):
        board_size = input("So, what'll it be? ")
        while len(board_size) != 1 or board_size.isalpha() or 4 > int(board_size) > 9:
            print("\nNah, I don't think so. Try again, buckeroo. ")
            board_size = input("So, what'll it be?")
        board_size = int(board_size)
        return board_size