from tile import Tile
from random import randint

class Minefield:
    
    def __init__(self, width, height, mines):
        """Create a new minefield."""
        self.height = height
        self.width = width
        self.mines = mines
        self.exploded = False
        
        # builds an array, each item being a tile object
        self.tiles = [[Tile(col, row) for row in range(self.height)] for col in range(self.width)]
                        
        # sort the mines
        for _ in range(0, self.mines):
            col = randint(0, self.width-1)
            row = randint(0, self.height-1)
            while self.tiles[col][row].mine:
                col = randint(0, self.width-1)
                row = randint(0, self.height-1)
            self.tiles[col][row].mine = True
            
    @property            
    def uncleared_tiles(self):
        """int: Amount of uncleared tiles."""
        total = 0
        for row in range(self.height):
            for col in range(self.width):
                total += self.tiles[col][row].adjacents == -1 and 1 or 0
        return total
        
    def blow_up(self):
        """Reveals everything."""
        for row in range(self.height):
            for col in range(self.width):
                self.tiles[col][row].show = True

    def display(self):
        """Show the minefield."""
        print('   {}'.format('  '.join(str(x) for x in range(self.width))))
        for row in range(self.height):
            line = []
            line.append('{} '.format(str(row)))
            for col in range(self.width):
                line.append(str(self.tiles[col][row]))
            print(''.join(line))
            
    def in_bounds(self, col, row):
        """True if column and row are inside of minefield bounds."""
        return row >= 0 and row < self.width and col >=0 and col < self.height
    
    def mines_around(self, col, row):
        """Look the adjacent tiles and returns the amount of mines around."""
        total = 0
        tile = self.tiles[col][row]
        for n in tile.neighbors:
            if self.in_bounds(n[0], n[1]) and self.tiles[n[0]][n[1]].mine:
                total += 1
                
        return total
            
    def take_turn(self, col, row, action='g'):
        """Take some action in a tile."""
        if not self.in_bounds(col, row):
            return
        
        # get the tile
        tile = self.tiles[col][row]
        
        # if action is flag, set tile as flagged
        if action == 'f':
            tile.flag = True
            return
        
        # if the tile has a mine, explode
        if tile.mine:
            self.exploded = True
            return
        
        # if the tile already has a flag, get out
        if tile.flag:
            return
        
        # first time in this tile, see tiles around
        if tile.adjacents == -1:
            tile.adjacents = self.mines_around(col, row)
            
            if self.tiles[col][row].adjacents == 0:
                for n in tile.neighbors:
                    self.take_turn(n[0], n[1])
