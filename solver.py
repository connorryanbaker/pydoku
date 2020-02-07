from board import Board

class Solver():
    def __init__(self, filepath):
        self.board = Board.from_file(filepath)
        self.solved_stack = []
        self.unsolved_stack = self.build_unsolved_stack()
    
    def solve(self):
        while len(self.unsolved_stack):
            current = self.unsolved_stack.pop()
            current.val += 1
            while current.val < 10:
                self.board.render()
                if self.possible_val(current):
                    self.solved_stack.append(current) 
                    break
                else:
                    current.val += 1
            if current.val == 10:
                current.val = 0
                self.unsolved_stack.append(current)
                self.unsolved_stack.append(self.solved_stack.pop())
        print('solved!')
    
    def possible_val(self, tile):
        row, col, sq = self.row_of(tile), self.col_of(tile), self.square_of(tile)
        val = tile.val
        return val not in row  and val not in col and val not in sq
    
    def row_of(self, tile):
        row = self.board.rows()[tile.row]
        return row[0:tile.col] + row[tile.col + 1:]

    def col_of(self, tile):
        col = self.board.columns()[tile.col]
        return col[0:tile.row] + col[tile.row + 1:]
    
    def square_of(self, tile):
        squares_idx = self.board.parse_square(tile.row, tile.col)
        sq = self.board.squares(False)[squares_idx]
        return self.filter_square(sq, tile)
    
    def filter_square(self, sq, tile):
        res = []
        for t in sq:
            if t.row == tile.row and t.col == tile.col:
                pass
            else:
                res.append(t.val)
        return res
    
    def build_unsolved_stack(self):
        stack = []
        for row in self.board.grid:
            for tile in row:
                if not tile.static:
                    stack.append(tile)
        return stack

Solver('./s01a.txt').solve()
