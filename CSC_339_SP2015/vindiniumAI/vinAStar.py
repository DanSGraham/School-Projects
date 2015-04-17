import math
import Queue
from vinNode import *
import sys



class AStar(object):
    

    #board -  a list of lists to represent the costs of each tile in y,x format
    #start - (y,x) coordinates for the starting position
    #dest   - a list of (y,x) coordinates that can be the destination-find the closest


    def __init__(self,board,start,dest):
        "stores the information and sets up any initial data, see calcPath to actually calcualte the path.  Note that start is not in the list dest"
        self.board = board
        self.start = start
        self.destList = dest
        self.expandedNodes = []
        self.frontier = Queue.PriorityQueue()


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
        #One nice feature is that because the costs of nodes are uniform, 1, the first destination reached will be the top of the queue.
        
        """generates the unvisited children of node.  If a child node has been generated (expanded) previously,
        it will not be generated again.  Returns all children nodes in an unordered list"""

        alreadyPresent = False
        for expanded in self.expandedNodes:
            if node.getPos() == expanded.getPos():
                alreadyPresent = True
        if not alreadyPresent:
            self.expandedNodes.append(node)


        possibleDirections = node.getCardinalCoordinates()
        for direction in possibleDirections:
            if self.canPassThrough(direction):
                alreadyExpanded = False
                for alreadyExpandedNode in self.expandedNodes:
                    if alreadyExpandedNode.getPos() == direction:
                        alreadyExpanded = True
                if not alreadyExpanded:
                    newPNode = Node(direction, node, 1, self.calcHeuristic(direction))
                    self.frontier.put(newPNode)
                    self.expandedNodes.append(newPNode)
        

    #Copied from ai. Seems more fitting here.
    def canPassThrough(self, position):
        """Is it possible to pass through this the (y,x) position stored in position?
           Returns False if there is anything in that position (mountain, mine, tavern, other heroes
            Returns True if there is nothing there.  Note a hero can pass through themself.

            Also Note: Any position that is not on the board should be deemed as impassible as well

            Further Note: The end position can be anything as long as it is in the map.
        """
        #The only time the hero can move to a place is when the place is within the board, and either a blank space (" ") or herself (indicated by self.pos)
        if position[0] >= 0 and position[1] >= 0 and position[0] < len(self.board) and (position[1]) < len(self.board[0]) and \
           (self.board[position[0]][position[1]] == " " or self.board[position[0]][position[1]] == "X" or position == self.start or position in self.destList or self.board[position[0]][position[1]] == "H"):
            return True
        else:              
            return False

    def calcPath(self):
        """calculates the path needed to reach the destination 
           returns the lowest cost path as linked list of Nodes (parent is the link)"""
        startNode = Node(self.start, None, 0, self.calcHeuristic(self.start))
        currNode = startNode
        while not (currNode.getPos() in self.destList):
            self.expandNode(currNode)
            if self.frontier.empty():
                return None
            #print "Current Expanded Nodes are: "
            #for i in range(len(self.getExplored())):
                #print self.expandedNodes[i]
            currNode = self.frontier.get()
            
            
        return currNode



    def getExplored(self):
        "returns an unordered list of all explored(actually expanded) nodes during the calcPath calcuation"
        return self.expandedNodes




        
        
