import _thread
from slidingPuzzle_values import slidingPuzzle_value


class Algorithms:
    solved = False
    maxNodeExplored = 0
    maxNodeExpanded = 0
    answerDepth = 0

    def find(self, board, x):
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == x):
                    return i, j

    def state_cost(self, state):
        cost = 0
        for r in range(1, 9):
            i, j = self.find(state, r)
            cost += abs(slidingPuzzle_value[r - 1]['i'] - i) + abs(slidingPuzzle_value[r - 1]['j'] - j)
        return cost

    def resetfactors(self):
        self.maxNodeExpanded = 0
        self.maxNodeExplored = 0
        self.answerDepth = 0
        self.solved = False

    def __init__(self, problem):
        self.problem = problem

    def copy_array(self, original_board):
        board_update = []
        for item in original_board:
            board_update.append(item)
        return board_update

    def DFS_Unlimited(self, state, states_array):
        try:
            if not self.solved:
                self.answerDepth += 1
                if (self.problem.is_final_state(state)):
                    print(states_array)
                    self.solved = True
                    self.answerDepth = len(states_array)
                    return state, states_array
                states_generated = self.problem.allowed_actions(state)
                self.maxNodeExplored += 1
                self.maxNodeExpanded += 1
                for section_state in states_generated:
                    if section_state not in states_array:
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_state)
                        self.DFS_Unlimited(section_state, new_copy)
        except:
            print('DFS unlimited exceed its max recursion')

    def DFS_Limited(self, state, states_array, counter):
        try:
            if not self.solved:
                # limit = 500
                self.answerDepth += 1
                if (self.problem.is_final_state(state)):
                    print(states_array)
                    self.solved = True
                    self.answerDepth = len(states_array)
                    return state, states_array
                if counter == 500:
                    return -1
                states_generated = self.problem.allowed_actions(state)
                self.maxNodeExpanded += 1
                self.maxNodeExplored += 1
                for section_state in states_generated:
                    if section_state not in states_array:
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_state)
                        self.DFS_Limited(section_state, new_copy, counter + 1)
        except:
            print('DFS limited exceed its max recursion')

    def DFS_Growing_Depth(self, state, states_array, maxDepth, counter):
        try:
            if not self.solved:
                # limit = 500
                self.answerDepth += 1
                if (self.problem.is_final_state(state)):
                    print(states_array)
                    self.solved = True
                    self.answerDepth = len(states_array)
                    return state, states_array
                if counter > maxDepth:
                    return -1
                if counter % 100 == 0:
                    maxDepth *= 2
                states_generated = self.problem.allowed_actions(state)
                self.maxNodeExpanded += 1
                self.maxNodeExplored += 1
                for section_state in states_generated:
                    if section_state not in states_array:
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_state)
                        self.DFS_Growing_Depth(section_state, new_copy, maxDepth, counter + 1)
        except:
            print('DFS_growing_depth exceed its max recursion')
    count = 0
    def BFS(self, state, states_array):
        try:
            if not self.solved:
                states_generated = self.problem.allowed_actions(state)
                for section_state in states_generated:
                    self.maxNodeExplored += 1
                    if (self.problem.is_final_state(section_state)):
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_state)
                        print(new_copy)
                        self.solved = True
                        self.answerDepth = len(states_array)
                        return state, states_array
                for section_state in states_generated:
                    self.maxNodeExpanded += 1
                    new_copy = self.copy_array(states_array)
                    new_copy.append(section_state)
                    self.BFS(section_state, new_copy)
        except:
            print('BFS exceed its max recursion')

    def bidirectional(self, states_start, states_end, cl_list_start, cl_list_end, counter):
        try:
            new_copy_end = states_end
            new_copy_start = states_start
            if not self.solved:
                if counter == 0:
                    states_generated_start = self.problem.allowed_actions(cl_list_start.pop() if len(cl_list_start) != 0 else states_start[0])
                    for section_state in states_generated_start:
                        self.maxNodeExpanded += 1
                        cl_list_start.append(section_state)
                        new_copy_start = self.copy_array(states_start)
                        new_copy_start.append(section_state)
                if counter == 1:
                    states_generated_end = self.problem.allowed_actions(cl_list_end.pop() if len(cl_list_end) != 0 else states_end[0])
                    for section_state in states_generated_end:
                        self.maxNodeExpanded += 1
                        cl_list_end.append(section_state)
                        new_copy_end = self.copy_array(states_end)
                        new_copy_end.append(section_state)
                self.maxNodeExplored += 1
                for state in states_start :
                    if state in states_end :
                        self.solved = True
                        print(states_start,states_end)
                        self.answerDepth = len(states_start) + len(states_end) + 1
                self.bidirectional(new_copy_start,new_copy_end,cl_list_start,cl_list_end,1 if counter == 0 else 0)
        except:
            print('bidirectional exceed its max recursion')


    def Astar(self, state, states_array):
        try:
            if not self.solved:
                states_generated = self.problem.allowed_actions(state)
                states_cost = []
                for section_state in states_generated:
                    states_cost.append({'state': section_state, 'cost': self.state_cost(section_state)})
                sorted_states = sorted(states_cost, key=lambda kv: kv['cost'])
                for section_rating in sorted_states:
                    self.maxNodeExplored += 1
                    if (self.problem.is_final_state(section_rating['state'])):
                        self.solved = True
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_rating['state'])
                        print(new_copy)
                        self.answerDepth = len(states_array) + 1
                        return state, states_array
                for section_rating in sorted_states:
                    new_copy = self.copy_array(states_array)
                    new_copy.append(section_rating['state'])
                    self.maxNodeExpanded += 1
                    self.Astar(section_rating['state'], new_copy)
        except:
            print('A* exceed its max recursion')
