from pickomino.game import Game
from pickomino.player import Player


if __name__ == '__main__':

    myGame = Game([Player('Alice'), Player('Bob'), Player('Charlie')])

    myGame.print_debug()

    myGame.take_turn('Alice')
    myGame.turns[-1].print_debug_tiles()
    myGame.turns[-1].roll_dice()
    myGame.turns[-1].print_debug()
    myGame.turns[-1].ask_pick_dice()
    myGame.turns[-1].print_debug()
    myGame.turns[-1].ask_end_turn()

    # myGame = Game(Player('Alice'))
