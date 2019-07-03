from Problem import Problem
from Algorithms import Algorithms
board = [[1,2,3],
         [4,5,6],
         [7,8,0]]
p = Problem(None,board,None)
alg = Algorithms(p)
simple_board = [[1,2,3],
                [0,4,6],
                [7,5,8]]
print("BFS answer :")
alg.BFS(simple_board,simple_board)
print("max node expored : ",alg.maxNodeExplored," max node expanded : ",alg.maxNodeExpanded," answer depth : ",alg.answerDepth)
alg.resetfactors()

print("DFS growing depth answer :")
alg.DFS_Growing_Depth(simple_board,simple_board,100,0)
print("max node expored : ",alg.maxNodeExplored," max node expanded : ",alg.maxNodeExpanded," answer depth : ",alg.answerDepth)
alg.resetfactors()

print("DFS unlimited :")
alg.DFS_Unlimited(simple_board,simple_board)
print("max node expored : ",alg.maxNodeExplored," max node expanded : ",alg.maxNodeExpanded," answer depth : ",alg.answerDepth)
alg.resetfactors()

print("bidirectional answer :")
alg.bidirectional([simple_board],[p.final_state],[],[],0)
print("max node expored : ",alg.maxNodeExplored," max node expanded : ",alg.maxNodeExpanded," answer depth : ",alg.answerDepth)
alg.resetfactors()

print("A* answer :")
alg.Astar(simple_board,simple_board)
print("max node expored : ",alg.maxNodeExplored," max node expanded : ",alg.maxNodeExpanded," answer depth : ",alg.answerDepth)
alg.resetfactors()