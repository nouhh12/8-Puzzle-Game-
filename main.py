from searchAlgorithms import *
from functions import isSolvable

firstBoard=randomState()
while(not isSolvable(firstBoard)):
    firstBoard=randomState()
print("FirstBoard:\n",firstBoard)
BFS(firstBoard)
DFS(firstBoard)
print("Manhattan Heuristic:\n")
aStarSearch(firstBoard,calculateManhattanHeuristic)
print("Euclidean Heuristic\n")
aStarSearch(firstBoard,calculateEuclideanHeuristic)