
from Node import *

from aStar import *
#from TEST_LIB import *


def firstTest():


    b = readBoard("map.txt")
    a = AStar(b,(0,0),[(2,3)])
    p = a.calcPath()
    print p.drawPath()
    

def secondTest():
    #Testing calcHeuristicMethod

    b = readBoard("map.txt")
    a1 = AStar(b, (1,0), [(2,3)])
    a2 = AStar(b, (1,0), [(2,3), (1,1)])
    print a1.calcHeuristic((1,1))
    print a2.calcHeuristic((1,0))
    print a2.calcHeuristic((1,1))


def exploreOnlyToGoalTest():

    #Testing that only the known nodes will be added to the list.
    
    b = readBoard("map3.txt")
    a1 = AStar(b, (1,0), [(1,3)])
    knownNodesToBeExpanded = [(1,0), (0,0), (2,0), (1,1), (0,1), (0,2), (2,1), (1,2), (2,2), (1,3)]
    path = a1.calcPath()
    exploredNodes = a1.getExplored()
    for node in exploredNodes:
        assert node.getPos() in knownNodesToBeExpanded


def expandOnceTest():
    #A test to determine that nodes are only expanded once.

    b = readBoard("map3.txt")
    a = AStar(b, (2,0), [(2,5)])
    path = a.calcPath()
    expandedNodesOnce = []
    expandedNodes = a.getExplored()
    for node in expandedNodes:
        for otherNode in expandedNodesOnce:
            if node.getPos() == otherNode.getPos():
                assert False
        expandedNodesOnce.append(node)
        if node.getPos() == (2,5):
            endExpandedNodes = a.expandNode(node)
            endNodePositionList = []
            for endNodeExpandNode in endExpandedNodes:
                endNodePositionList.append(endNodeExpandNode.getPos())
            assert (len(endNodePositionList) == 2 and (1,5) in endNodePositionList and (3,5) in endNodePositionList)


def expandOnceTestTwo():
    b = readBoard("map2.txt")
    a = AStar(b, (2,0), [(2,5)])
    path = a.calcPath()
    expandedNodesOnce = []
    expandedNodes = a.getExplored()
    print "Path \n"
    print path.drawPath()
    print "ExploredNodes \n"
    
    for node in expandedNodes:
        print node.getPos()
        if node.getPos() == (2,5):
            endExpandedNodes = a.expandNode(node)
            endNodePositionList = []
            #for endNodeExpandNode in endExpandedNodes:
                #print endNodeExpandNode.getPos()
                #endNodePositionList.append(endNodeExpandNode.getPos())
            #assert (len(endNodePositionList) == 1 and (3,5) in endNodePositionList)


def expandOnlyToOneGoal():
    b = readBoard("map3.txt")
    a = AStar(b, (2,0), [(2,5), (3,5)])
    path = a.calcPath()
    expandedNodesOnce = []
    expandedNodes = a.getExplored()
    for node in expandedNodes:
        for otherNode in expandedNodesOnce:
            if node.getPos() == otherNode.getPos():
                assert False
        expandedNodesOnce.append(node)
        if node.getPos() == (3,5):
            assert False
        
def main():
    firstTest()
    secondTest()
    exploreOnlyToGoalTest()
    expandOnceTest()
    expandOnceTestTwo()
    expandOnlyToOneGoal()
main()
