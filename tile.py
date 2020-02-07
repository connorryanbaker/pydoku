from termcolor import colored


class Tile():
    def __init__(self, val, row, col):
        self.static = True if val else False
        self.val = val
        self.row = row
        self.col = col

    def __str__(self):
        if self.static:
            return colored(str(self.val), 'red')
        else:
            return colored(str(self.val), 'green')

