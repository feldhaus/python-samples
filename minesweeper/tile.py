class Tile:
    
    def __init__(self, col, row):
        """Create a new tile."""
        self.col = col
        self.row = row
        self.mine = False
        self.flag = False
        self.show = False
        self.adjacents = -1
        self.neighbors = (
            (col-1, row-1), (col-1, row), (col-1, row+1),
            (col+1, row-1), (col+1, row), (col+1, row+1),
            (col,   row-1), (col,   row+1)
        )
        
    def __str__(self):
        if self.mine and self.show:
            return ' # '
        elif self.flag:
            return ' ? '
        elif self.adjacents > 0:
            return '[{}]'.format(self.adjacents)
        elif self.adjacents == 0:
            return '   '
        else:
            return '[ ]'
