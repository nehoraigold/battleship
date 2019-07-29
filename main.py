from game import Game

if __name__ == "__main__":
    keep_playing = True
    while keep_playing:
        game = Game()
        keep_playing = game.play_again()


#TODO: Multiple ships
#TODO: Single ship with multiple spaces
#TODO: Adjust spacing of text