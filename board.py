from tile import Tile
import os


class Board():
    COLUMN_IDX_OFFSET = 3

    def __init__(self, grid):
        self.grid = grid

    def render(self):
        os.system('clear')
        for row in self.grid:
            print(' '.join([str(tile) for tile in row]))

    def rows(self):
        return [[tile.val for tile in row] for row in self.grid]

    def columns(self):
        cols = [list() for i in range(9)]
        for row in self.grid:
            for idx, tile in enumerate(row):
                cols[idx].append(tile.val)

        return cols

    def squares(self, val=True):
        sqs = [list() for i in range(9)]
        for row_idx, row in enumerate(self.grid):
            for col_idx, tile in enumerate(row):
                squares_idx = self.parse_square(row_idx, col_idx)
                sqs[squares_idx].append(tile.val if val else tile)

        return sqs

    def parse_square(self, r, c):
        if r < 3:
            return self.parse_col(c)
        elif r < 6:
            return self.parse_col(c) + self.COLUMN_IDX_OFFSET
        else:
            return self.parse_col(c) + self.COLUMN_IDX_OFFSET * 2

    def parse_col(self, c):
        if c < 3:
            return 0
        elif c < 6:
            return 1
        else:
            return 2

    def solved(self):
        solved_row = [i for i in range(1, 10)]
        row_solved = [sorted(row) == solved_row for row in self.rows()]
        col_solved = [sorted(col) == solved_row for col in self.columns()]
        sqs_solved = [sorted(sq) == solved_row for sq in self.squares()]

        return all(row_solved) and all(col_solved) and all(sqs_solved)

    @classmethod
    def from_file(cls, filepath):
        grid = []
        with open(filepath) as f:
            line = f.readline()
            row = 0
            while line:
                chars = line.rstrip().split(' ')
                grid.append([Tile(int(char), row, col) for col, char in enumerate(chars)])
                line = f.readline()
                row += 1
        return cls(grid)

