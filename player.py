from random import randint, choice
from coordinate import Coordinate

class Player():
    def __init__(self, is_computer=False):
        self.is_computer = is_computer
        self.battleship_coord = None
        self.guessed_coordinates = {}
        self.computer_reactions = ["Rats", "Dang it", "Aw, phooey", "Curses", "Alas", "Blast", "Shoot", "Drat", "Ugh"]

    def place_battleship(self, board_size):
        if self.is_computer:
            self.battleship_coord = self.get_random_battleship_coord(board_size)
            print("Okay, I've placed my battleship.\n")
        else:
            battleship_coord = Coordinate.from_str(input("Where will you place your battleship? Enter the column letter and number (e.g., \"B3\") "))
            while not battleship_coord or not battleship_coord.is_valid_for(board_size):
                battleship_coord = Coordinate.from_str(input("That is not a valid choide. Where will you place your battleship? "))
            self.battleship_coord = battleship_coord
    
    def get_guess(self, board_size):
        guess = self.get_computer_guess(board_size) if self.is_computer else self.get_player_guess(board_size)
        self.guessed_coordinates[str(guess)] = True
        return guess

    def get_player_guess(self, board_size):
        guess = Coordinate.from_str(input("Which space will you guess? "))
        while not guess or not guess.is_valid_for(board_size) or self.guessed_coordinates.get(str(guess), False):
            if self.guessed_coordinates.get(str(guess), False):
                print("You guessed that one already.\n")
            elif not guess:
                print("Uh... not quite sure what that was. Let's try that again, shall we?\n")
            else:
                print("Oops, that's not even in the ocean.\n")
            guess = Coordinate.from_str(input("Which space will you guess? "))
        return guess

    def get_computer_guess(self, board_size):
        guess = self.get_random_battleship_coord(board_size)
        while self.guessed_coordinates.get(str(guess), False):
            guess = self.get_random_battleship_coord(board_size)
        return guess
    
    def get_random_battleship_coord(self, board_size):
        return Coordinate.from_values(randint(1, board_size), randint(1, board_size))

    def is_battleship_location(self, coordinate):
        return coordinate == self.battleship_coord

    def get_reaction(self):
        return choice(self.computer_reactions)