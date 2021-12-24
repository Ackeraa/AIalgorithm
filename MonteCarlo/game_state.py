class Board():
    def __init__(self, arrays, l, r, summ):
        self.arrays = arrays
        self.l = l
        self.r = r
        self.sum = summ

class GameState():
    def __init__(self, next_to_move, board):
        self.next_to_move = next_to_move
        self.board = board

    @property
    def game_result(self):
        if self.board.sum > 0:
            return 1
        else:
            return -1

    def is_game_over(self):
        return self.board.l > self.board.r

    def move(self, action):
        l = self.board.l
        r = self.board.r
        summ = self.board.sum
        val = 0
        if action[0] == 0:
            val = self.board.arrays[l]
            l += 1
        else:
            val = self.board.arrays[r]
            r -= 1
        
        if self.next_to_move == 1:
            summ += val
        else:
            summ -= val

        new_board = Board(self.board.arrays, l, r, summ)
        new_next_to_move = -self.next_to_move
        new_state = GameState(new_next_to_move, new_board)

        return new_state

    def get_legal_actions(self):
        return [(0, self.board.l), (1, self.board.r)] 


