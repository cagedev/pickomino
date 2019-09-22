from .board import Board
from .turn import Turn


class Game:

    turns = []
    players = []
    board = Board()

    def __init__(self, players):
        self.players = players

    def take_turn(self, playername):
        # check if playername is correct
        other_players = []
        for player in self.players:
            if playername == player.name:
                active_player = player
            else:
                other_players.append(player)

        self.turns.append(Turn(active_player, other_players, self.board))
        # return Turn(active_player, other_players, self.board)

    def print_debug(self):
        for player in self.players:
            print(player.name)
