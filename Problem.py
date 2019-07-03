import numpy as np


class Problem:
    def __init__(self, states, final_state, actions):
        ## index number of state is equal to indexOf state element in states array
        ## actions is a 2D array which shows states you can go from a state
        self.states = states
        self.final_state = final_state
        self.actions = actions

    ##just for sliding puzzles
    def find_blank(self, board):
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == 0):
                    return i, j

    def assign_movement(self, original_board, direction):
        board_update = []
        for i in range(0, 3):
            board_update.append([1, 2, 3])
        for i in range(0, 3):
            for j in range(0, 3):
                board_update[i][j] = original_board[i][j]
        x, y = self.find_blank(board_update)
        if direction == 'u':
            board_update[x][y] = board_update[x - 1][y]
            board_update[x - 1][y] = 0
        if direction == 'd':
            board_update[x][y] = board_update[x + 1][y]
            board_update[x + 1][y] = 0
        if direction == 'r':
            board_update[x][y] = board_update[x][y + 1]
            board_update[x][y + 1] = 0
        if direction == 'l':
            board_update[x][y] = board_update[x][y - 1]
            board_update[x][y - 1] = 0
        return board_update

    def state_generator(self, state):
        x, y = self.find_blank(state)
        allowed_moves = ['d', 'u', 'r', 'l']
        if x == 0:
            allowed_moves.remove('u')
        if x == 2:
            allowed_moves.remove('d')
        if y == 0:
            allowed_moves.remove('l')
        if y == 2:
            allowed_moves.remove('r')
        new_boards = []
        for move in allowed_moves:
            new_boards.append(self.assign_movement(state, move))
        return new_boards

    ##/just for sliding puzzle
    def allowed_actions(self, state):
        if (self.actions != None):
            return self.actions[state]
        else:
            return self.state_generator(state)

    def is_final_state(self, state):
        return np.array_equal(state, self.final_state)
