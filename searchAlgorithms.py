import time
import heapdict as hp
from functions import *

def BFS(boardState):
    startTime=time.time()
    frontier=[] #Frontier here is used as a queue
    optFrontier=set() #Used to make searching for previously retrieved states in frontier faster O(1)
    frontier.append(boardState) #Enqueue
    board_As_Number=matrixToNum(boardState) #Convert board into a single number to be stored in set 
    optFrontier.add(board_As_Number)        #as sets can't take 2d arrays (unhashable)
    explored=set()
    parentMap={board_As_Number:board_As_Number} #Storing Initial State of Board as a single str(number) in dictionary 
    while len(frontier)>0:
        currentState=frontier.pop(0) #Dequeue from first index in queue (FIFO)
        explored.add(matrixToNum(currentState))  #Adding board state as a number to explored set
        if isGoalState(currentState):
            break
        else:
            children=nextStates(currentState)
            for child in children: #Iterate over possible next states of current board state
                child_As_Number=matrixToNum(child)
                if child_As_Number not in optFrontier and child_As_Number not in explored: #Searching through previously 
                    frontier.append(child)                                                 #retrieved states in O(1)
                    optFrontier.add(child_As_Number)
                    parentMap[child_As_Number]=matrixToNum(currentState) #Adding current state as parent in path
        
    totalTime=time.time()-startTime
    print(currentState)
    print("\nBFS Path:\n")
    getPath(parentMap)
    print("Number of nodes expanded=",len(explored))
    print(f"Total runtime of BFS={totalTime} seconds\n\n")

def DFS(boardState):
    startTime=time.time()
    frontier=[] #Frontier here is used as stack
    optFrontier=set() #Used to make searching for previously retrieved states in frontier faster O(1)
    frontier.append(boardState)
    board_As_Number=matrixToNum(boardState) #Convert board into a single number to be stored in set 
    optFrontier.add(board_As_Number)        #as sets can't take 2d arrays (unhashable)
    explored=set()
    parentMap={board_As_Number:board_As_Number} #Storing Initial State of Board as a single str(number) in dictionary 
    while len(frontier)>0:
        currentState=frontier.pop() #Pop last index in stack (LIFO)
        explored.add(matrixToNum(currentState)) #Adding board state as a number to explored set
        if isGoalState(currentState):
            break
        else:
            children=nextStates(currentState)
            for child in children: #Iterate over possible next states of current board state
                child_As_Number=matrixToNum(child)
                if child_As_Number not in optFrontier and child_As_Number not in explored: #Searching through previously 
                    frontier.append(child)                                                 #retrieved states in O(1)
                    optFrontier.add(child_As_Number)
                    parentMap[child_As_Number]=matrixToNum(currentState) #Adding current state as parent in path
        
    totalTime=time.time()-startTime
    print("\nDFS Path:\n")
    getPath(parentMap)
    print("Number of nodes expanded=",len(explored))
    print(f"Total runtime of DFS={totalTime} seconds\n\n")

def aStarSearch(initialState, heuristic):
    startTime = time.time()
    frontier = hp.heapdict() #Using heapdict as priority queue
    board_As_Number=matrixToNum(initialState)
    frontier[board_As_Number] = heuristic(initialState)
    explored = set()
    parentMap = {board_As_Number: board_As_Number} #Storing Initial State of Board as a single str(number) in dictionary
    gScore = {board_As_Number: int}
    hscore = {board_As_Number: int}
    gScore[board_As_Number] = 0 #Initial state has gScore of 0
    hscore[board_As_Number] = heuristic(initialState) #Calculate hScore of initial state
    expanded = 0
    while len(frontier):
        expanded += 1 #Counter for number of nodes expanded
        currentState = frontier.popitem()[0] #Pop the state with highest priority (lowest gScore+hScore)
        current_Board_As_Number=matrixToNum(currentState)
        explored.add(current_Board_As_Number)
        if isGoalState(currentState):
            break
        else:
            children = nextStates(numToMatrix(currentState))
            for child in children: #Iterate over possible next states of current board state
                child_As_Number=matrixToNum(child)
                if child_As_Number not in explored and child_As_Number not in frontier:
                    gScore[child_As_Number] = gScore[current_Board_As_Number] + 1 #gScore of child=gscore of parent + 1
                    hscore[child_As_Number] = heuristic(child) #Calculate hscore of child
                    frontier[child_As_Number] = gScore[child_As_Number] + hscore[child_As_Number] #Add score to frontier priority queue
                    parentMap[child_As_Number] = current_Board_As_Number #Adding current state as parent in path
                
    totalTime = time.time() - startTime
    print('A* PATH:\n')
    getPath(parentMap)
    print(f'\nNumber of nodes expanded A*: {expanded}')
    print(f'\nA* completed in {totalTime} seconds\n')

        
