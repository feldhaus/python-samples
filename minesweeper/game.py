from minefield import Minefield
import os

class Game:
    
    def __init__(self):
        """Create a new game."""
        self.minefield = Minefield(10, 10, 10)
    
    def start(self):
        """Start the game."""
        while not self.gameOver:
            self.clear()
            self.minefield.display()
            print('')
            col = int(raw_input("Col:"))
            row = int(raw_input("Row:"))
            action = raw_input("Do you want to flag or guess a point? (f/g)").lower()
            self.minefield.take_turn(col, row, action)
        
        # show result
        self.minefield.blow_up()
        self.clear()
        self.minefield.display()
        if self.won:
            print("\nYou won! (:")
        else:
            print("\nYou lost! ):")

    def clear(self):
        """Clear screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
            
    @property
    def won(self):
        """bool: True if won, False otherwise."""
        return self.minefield.uncleared_tiles == self.minefield.mines
        
    @property
    def lost(self):
        """bool: True if lost, False otherwise."""
        return self.minefield.exploded
        
    @property
    def gameOver(self):
        """bool: True if game over, False otherwise."""
        return self.won or self.lost

if __name__ == '__main__':
    game = Game()
    game.start()
