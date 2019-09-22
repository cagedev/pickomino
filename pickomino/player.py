class Player:
    '''Class for keeping track of a player.
    TODO: extend this class depending on type of player {ai, console, web
    etc...}.

    Arguments:
    name -- unique player name
    '''

    stack = []
    name = ''

    def __init__(self, name):
        self.name = name
