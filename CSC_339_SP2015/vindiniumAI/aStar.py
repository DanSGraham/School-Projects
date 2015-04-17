import math
import Queue
from vinNode import *
import sys



class AStar(object):
    
    #TODO

    #board -  a list of lists to represent the costs of each tile in y,x format
    #start - (y,x) coordinates for the starting position
    #dest   - a list of (y,x) coordinates that can be the destination-find the closest

    def __init__(self,board,start,dest):
        "stores the information and sets up any initial data, see calcPath to actually calcualte the path.  Note that start is not in the list dest"
        self.board = board
        for i in self.board:
            print i
            
        print dest
        self.start = start
        self.destList = dest
        self.startNode = Node(self.start, None, 0, self.calcHeuristic(self.start))
        self.expandedNodes = []
        self.expandedNodes.append(self.startNode)
        self.frontierNodes = Queue.PriorityQueue()
        self.frontierNodes.put(self.startNode)


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


    def expandNode(self, node):
        #expand node may have an issue. Is a node expanded when it is calculated or when it generates children?
        #Only node should be added to expanded nodes list
        #Still giving issues.
        """generates the unvisited children of node.  If a child node has been generated (expanded) previously,
        it will not be generated again.  Returns all children nodes in an unordered list"""
        possibleDirections = node.getCardinalCoordinates()
        nodeList = []
        alreadyPresent = False
        for expanded in self.expandedNodes:
            if node.getPos() == expanded.getPos():
                alreadyPresent = True
        if not alreadyPresent:
            self.expandedNodes.append(node)
            
       
        for direction in possibleDirections:
            if self.canPassThrough(direction):
                alreadyExpanded = False
                for alreadyExpandedNode in self.expandedNodes:
                    if alreadyExpandedNode.getPos() == direction:
                        alreadyExpanded = True
                if not alreadyExpanded:
                    newPNode = Node(direction, node, self.board[direction[0]][direction[1]], self.calcHeuristic(direction))
                    nodeList.append(newPNode)
                    self.expandedNodes.append(newPNode)
                    self.frontierNodes.put(newPNode)
        print "Expansion of Node: ", node
        for i in nodeList:
            print i
        return nodeList
        

    def canPassThrough(self, position):
        """Is it possible to pass through this the (y,x) position stored in position?
           Returns False if there is anything in that position (mountain, mine, tavern, other heroes
            Returns True if there is nothing there.  Note a hero can pass through themself.

            Also Note: Any position that is not on the board should be deemed as impassible as well

            Further Note: The end position can be anything as long as it is in the map.
        """
        if position[0] >= 0 and position[1] >= 0 and position[0] < len(self.board) and (position[1]) < len(self.board[0]):
            return True
        else:              
            return False


    def calcPath(self):
        """calculates the path needed to reach the destination 
           returns the lowest cost path as linked list of Nodes (parent is the link)"""
        currNode = self.frontierNodes.get()
        while not (currNode.getPos() in self.destList):
            self.expandNode(currNode)
            currNode = self.frontierNodes.get()
            print currNode.getPos(), currNode.getParent()
        return currNode



    def getExplored(self):
        "returns an unordered list of all explored(actually expanded) nodes during the calcPath calcuation"
        return self.expandedNodes




        
        
