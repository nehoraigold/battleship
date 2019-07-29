from settings import Settings
from player import Player
from board import Board
import utils

class Game():
    def __init__(self):
        self.introduce()
        self.settings = Settings()
        self.board = Board(self.settings.board_size)
        self.opponent = Player(self.settings.opponent_is_computer)
        self.player = Player()
        self.turn_number = 1
        self.setup()
        self.play()

    def introduce(self):
        print("Welcome to Battleship! Like in the classic game, both you and I will hide a single battleship somewhere on the board, and each of us will take turns guessing the row and column of the other's battleship. If we guess right, we sink the opponent's battleship and win the game.\n\nBefore we do anything else, you'll need to choose how large you want the board to be. We recommend a number between 3 and 9. Remember: the larger the board, the longer the game will likely take!\n")
    
    def setup(self):
        print("Great. So, on a {0}-by-{0} board, each of us will hide our battleship. We'll then take turns guessing where the other's battleship lies. If we guess right, we win! Where will you hide your battleship? Don't worry, I swear I won't peek.".format(self.board.size))
        self.board.print()
        self.player.place_battleship(self.board.size)
        self.opponent.place_battleship(self.board.size)
    
    def play(self):
        while True: 
            print("Turn {}".format(str(self.turn_number)))
            self.board.print()
            guess = self.player.get_guess(self.board.size)
            if self.opponent.is_battleship_location(guess):
                print("Congratulations! You sunk my battleship!") #TODO: Move these responses into the player class
                return
            else:
                print("Aha! You missed my battleship!")
                self.board.mark_as_guessed(guess)
            guess = self.opponent.get_guess(self.board.size)
            if self.player.is_battleship_location(guess):
                print("I guessed {}, and sank your battleship! Game over.".format(utils.convert_coordinate_to_string(guess)))
                return
            else:
                print("{0}! I guessed {1} and missed.\n".format(self.opponent.get_reaction(), utils.convert_coordinate_to_string(guess)))
            self.turn_number += 1
    
    def play_again(self):
        keep_playing = input("Would you like to play again? ")
        while keep_playing not in utils.YES_RESPONSES and keep_playing not in utils.NO_RESPONSES:
            keep_playing = input("Didn't quite catch that. Would you like to play again? ")
        return keep_playing in utils.YES_RESPONSES
        
