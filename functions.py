import numpy as np
from math import sqrt

#Checks if instance of Board is Solvable
def isSolvable(boardState):
    inversionsCount=0
    tempBoardState=np.copy(boardState)
    tempBoardState=boardState.flatten() #Board is flattened to 1d array to iterate over it easier
    for i in range(0,9):
        for j in range(i+1,9):
            if tempBoardState[i]!=0 and tempBoardState[j]!=0 and tempBoardState[i]>tempBoardState[j]:
                inversionsCount+=1
    #If number of Inversions is odd then the instance is not solvable
    if inversionsCount%2==0:
        return True
    else:
        return False

#Used to turn Board(2d array) to a single number stored as a string 
#Makes comparisons in (dict) and (set) data structured do-able, unlike 2d arrays which can't be used as index 
#in such data structures 
def matrixToNum(boardState):
    tempBoardState=np.copy(boardState)
    tempBoardState=tempBoardState.flatten()
    arr=[]
    for x in tempBoardState:
        arr.append(str(x))
    tempBoardState=''.join(arr)
    return tempBoardState

#Used to reverse the effect of turning the board into a single number stored as string
#Returns the board in original form (2d array)
def numToMatrix(matrixAsNumber):
    arr=[int(digit) for digit in str(matrixAsNumber)]
    arr=np.array(arr)
    arr=np.reshape(arr,(-1,3))
    return arr

#Checks if board has reached goal state
def isGoalState(boardState):
    arr=[[0,1,2],[3,4,5],[6,7,8]]
    for i in range(3):
        for j in range(3):
            if boardState[i][j]!=arr[i][j]:
                return False
    return True

#Generate random instances of board for initial use of program
def randomState():
    arr=[0,1,2,3,4,5,6,7,8]
    arr=np.array(arr)
    np.random.shuffle(arr)
    return np.reshape(arr,(-1,3))

#Used to swap the empty(0) tile with adjacent tile
def swap(boardState,row1,column1,row2,column2):
    tempBoardState=np.copy(boardState)
    tempBoardState[row1][column1],tempBoardState[row2][column2]=tempBoardState[row2][column2],tempBoardState[row1][column1]
    return tempBoardState

#Used to find index of empty tile 
#Used in nextStates() function
def findTileIndex(boardState):
    finalI,finalJ=0,0
    for i in range(3):
        for j in range(3):
            if boardState[i][j]==0:
                finalI,finalJ= i, j
                return finalI,finalJ

#Used to get path of final state of board 
#Starting from goal state and moving upwards from it till reaching the initial state
def getPath(parentMap):
    child = '012345678' #Initial child is final state of board which is the goal state
    parent = parentMap[child] #Get the parent of that final state
    path = [child] #Store final state in stack
    while child != parent:
        child = parent
        parent = parentMap[child]
        path.append(child) #Adding each parent to the path stack until reaching initial state

    cost = len(path) - 1    #Cost is the depth of the path
    for i in range(len(path)):
        print(numToMatrix(path.pop()))  #Popping from stack(initial state->final state)
    print(f'\nCost= {cost}')

#Used to calculate the Manhattan Heuristic according to equation given in pdf
def calculateManhattanHeuristic(boardState):
    h = 0
    for i in range(3):
        for j in range(3):
            if boardState[i][j] != 0:
                h += abs(boardState[i][j] // 3 - i) + abs(boardState[i][j] % 3 - j) 
    return h

#Used to calculate the Euclidean Heuristic according to equation given in pdf
def calculateEuclideanHeuristic(boardState):
    h = 0
    for i in range(3):
        for j in range(3):
            if boardState[i][j] != 0:
                h += sqrt(abs(boardState[i][j] // 3 - i) ** 2 + abs(boardState[i][j] % 3 - j) ** 2)
    return h

#Finding the possible next states of current Board (up to 4 possible next states)
def nextStates(boardState):
    i,j=findTileIndex(boardState)
    states=[]
    if i>0: #move tile upwards
        states.append(swap(boardState,i,j,i-1,j))
    if j>0: #move tile left
        states.append(swap(boardState,i,j,i,j-1))
    if i<2: #move tile down
        states.append(swap(boardState,i,j,i+1,j))
    if j<2: #move tile roght
        states.append(swap(boardState,i,j,i,j+1))
    return states