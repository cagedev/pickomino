from .tile import Tile


class Board:
    '''Class for keeping track of the gameboard.'''

    tiles = []

    def __init__(self):
        self.initiate_board()

    def initiate_board(self):
        for val in range(21, 36, 1):
            self.tiles.append(Tile(val, (val - 17) // 4, 'OPEN'))
