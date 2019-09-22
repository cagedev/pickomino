from random import randint


class Turn:
    '''Class for executing a turn.
    TODO: A turn uses the player's type for interaction.

    Arguments:
    player -- player taking the turn
    other_players -- list of other players
    board -- the game board
    '''

    available_tiles = []
    available_dice = 8
    chosen_dice = []
    current_roll = []

    def __init__(self, player, other_players, board):
        for opponent in other_players:
            try:
                self.available_tiles.append(opponent.stack[-1])
            except IndexError:
                pass
        for tile in board.tiles:
            if tile.state == 'OPEN':
                self.available_tiles.append(tile)
        # self.print_debug()

    def roll_dice(self):
        for dice in range(self.available_dice):
            self.current_roll.append(randint(1, 6))
        self.current_roll.sort()
        print(self.current_roll)

    def ask_end_turn(self):
        pass

    def ask_pick_dice(self):
        user_input = input('current_roll: ' + str(self.current_roll))
        try:
            choice = int(user_input)
            if choice not in self.current_roll:
                print(user_input + ' in unavailable. Pick a different number.')
                self.pick()
            else:
                count = self.current_roll.count(choice)  # always ok
                self.available_dice -= count
                self.chosen_dice.extend([choice] * count)

        except ValueError:
            print(user_input + ' is not a valid number. Try again.')
            self.pick()

    def print_debug_tiles(self):
        for tile in self.available_tiles:
            print(tile)

    def print_debug(self):
        print('available_dice:' + str(self.available_dice))
        print('chosen_dice:' + str(self.chosen_dice))
        print('current_roll:' + str(self.current_roll))
