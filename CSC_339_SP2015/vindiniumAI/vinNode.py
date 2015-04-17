
import types




def readBoard(filename):
    "reads a board from a file. could just do this in code if you like"

    f = open(filename)
    lines= f.readlines()
    f.close()
    
    board = []
    for line in lines:
        row = line.strip().split()
        row2 = [int(x) for x in row]
        board.append(row2)
    return board


class Node(object):
    
    #pos - 2-tuple for the y,x coordinate
    #g   - cost to get to node
    #h   - heuristic cost
    #parent - preceding node used to get to this node.
    

    def __init__(self,pos,parent,c,h):
        "As above and c is the cost to go from the parent node to this node"
        self.pos = pos
        self.parent=parent
        if(isinstance(parent,types.NoneType)):   
            self.g = c 
        else: 
            self.g = parent.g + c
        self.h = h

        
    def calcF(self):
        "calculates the f value fo the node"
        return self.g + self.h;

    def __cmp__(self,other):
        """a comparison opperator, returns 1 is the F() is higher, -1 if it is lower,
        and 0 if they have the same F(), This will make the defauilt priority Queues in Python work"""

        #needed this to stop the None time checks from breaking
        if(isinstance(other,types.NoneType)): return -1
            
    
        return cmp(self.calcF(),other.calcF())
        
    #The following method has been added to the Node class. Makes it a ton easier...
    def getCardinalCoordinates(self):
        """Returns a list of the cardinal coordinates of the startingCoord in the order [North, East, South, West]"""
        startingCoord = self.pos
        north = (startingCoord[0] - 1, startingCoord[1])
        east = (startingCoord[0], startingCoord[1] + 1)
        south = (startingCoord[0] + 1, startingCoord[1])
        west = (startingCoord[0], startingCoord[1] - 1)
        return [north, east, south, west] 

    def equalTo(self,other):
        "ignores parent data for purposes of comparision"
        return self.pos==other.pos and self.g==other.g and self.h==other.h

    def __str__(self):
        """returns a string representaiton"""

        s = "Node:{0} {1}={2}+{3}".format(self.pos,self.calcF(),self.g,self.h)
        return s

    def getPos(self):
        "returns the pos of the node"
        return self.pos


    def getParent(self):
        "who is your daddy?"
        return self.parent

    def drawPath(self):
        "debug function prints the current node and all descendants"
        print str(self)
        if(not isinstance(self.parent,types.NoneType)):
            self.parent.drawPath()

    def getRPath(self, pArray):
        """Recursively adds elements to an array to return as a reversed version of the path"""
        pathArray = pArray
        pathArray.append(self.pos)
        if (not isinstance(self.parent, types.NoneType)):
            return self.parent.getRPath(pathArray)
        else:
            return pathArray
    
    def __str__(self):
        return str(self.pos)
