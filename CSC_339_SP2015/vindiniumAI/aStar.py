import math
import Queue
from Node import *
import sys



class AStar(object):
    
    #TODO
    #Change the board read
    #Make sure the search will stop if it runs out of nodes

    #board -  a list of lists to represent the costs of each tile in y,x format
    #start - (y,x) coordinates for the starting position
    #dest   - a list of (y,x) coordinates that can be the destination-find the closest

    def __init__(self,board,start,dest):
        "stores the information and sets up any initial data, see calcPath to actually calcualte the path.  Note that start is not in the list dest"
        self.board = board
        self.start = start
        self.destList = dest
        self.startNode = Node(self.start, None, 0, self.calcHeuristic(self.start))
        self.expandedNodes = []


    def calcHeuristic(self, pos):
        """calculates the manhatan distance from pos (y,x) to the closest destination"""
        lowestCost = None
        if len(self.destList) > 0:
            lowestCost = (abs(pos[0] - self.destList[0][0])) + abs(pos[1] - self.destList[0][1])
            for i in range(1, len(self.destList)):
                testCost = (abs(pos[0] - self.destList[i][0])) + abs(pos[1] - self.destList[i][1])
                if testCost < lowestCost:
                    lowestCost = testCost
        return lowestCost


    def expandNode(self,node):
        """generates the unvisited children of node.  If a child node has been generated (expanded) previously,
        it will not be generated again.  Returns all children nodes in an unordered list"""
        possibleDirections = node.getCardinalCoordinates()
        nodeList = []
        for direction in possibleDirections:
            if direction[0] >= 0 and direction[0] < len(self.board) and direction[1] >= 0 and direction[1] < len(self.board[0]):
                newPNode = Node(direction, node, self.board[direction[0]][direction[1]], self.calcHeuristic(direction))
                alreadyExpanded = False
                for alreadyExpandedNode in self.expandedNodes:
                    if alreadyExpandedNode.getPos() == direction:
                        alreadyExpanded = True
                if not alreadyExpanded:
                    nodeList.append(newPNode)
                    self.expandedNodes.append(newPNode)

        return nodeList
        
        pass



    def calcPath(self):
        """calculates the path needed to reach the destination 
           returns the lowest cost path as linked list of Nodes (parent is the link)"""
        pathQueue = Queue.PriorityQueue(-1)
        currNode = self.startNode
        self.expandedNodes.append(currNode)
        while not (currNode.getPos() in self.destList):
            possibleNodes = self.expandNode(currNode)
            for pNode in possibleNodes:
                pathQueue.put((pNode.calcF(), pNode))
            currNode = pathQueue.get()[1]
            
        return currNode


    def getExplored(self):
        "returns an unordered list of all explored(actually expanded) nodes during the calcPath calcuation"

        return self.expandedNodes




        
        
