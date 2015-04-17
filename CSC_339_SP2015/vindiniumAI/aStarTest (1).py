
from vinNode import *

from aStar import *
#from TEST_LIB import *

#"Node:{0} {1}={2}+{3}"
#self.pos, self.calcF, self.g self.h
#pos - 2-tuple for the y,x coordinate
#g   - cost to get to node
#h   - heuristic cost
#parent - preceding node used to get to this node.
def firstTest():


    b = readBoard("map.txt")
    a = AStar(b,(0,0),[(2,3)])
    print a.calcHeuristic((0,0))
    p = a.calcPath()
    n1 = Node((0,0), None, 0, 5)
    n2 = Node((1,0), n1,4,4)
    n3 = Node((1,1),n2,1,3)
    n4 = Node((1,2),n3,9,2)
    n5 = Node((1,3),n4,1,1)
    n6 = Node((2,3),n5,6,0)
    #print n6
    #print n5
    #print n4
    #print n3
    #print n2
    #print n1
    
    s = p
    print "s ",p
    print "n6 ", n6
    assert n6 == s
    s = s.getParent()
    assert n5 == s
    s = s.getParent()
    assert n4 == s
    s = s.getParent()
    assert n3 == s
    s = s.getParent()
    assert n2 == s
    s = s.getParent()
    assert n1 == s
    s = s.getParent()
    assert None is s
    
    print p.drawPath()
    
    
def secondTest():
    
    b = readBoard("map.txt")
    a = AStar(b,(0,0),[(2,3)])
    n1 = Node((0,0), None, 0, 5)

    
    gen2 = Node((1,0), n1,4,4)

    gen3 = Node((0,1), n1,10, 4)


    assert gen2,gen3 in a.expandNode(n1)
    assert n1 not in a.expandNode(n1)

    gen4 = Node((1,1), gen2,1,3)
    gen5 = Node((2,0), gen2,1,3)
    gen6 = Node((0,0), gen2,1,5)
    nodelist = [gen4,gen5]

    
    assert sorted(nodelist) == sorted(a.expandNode(gen2))
    assert gen6 not in a.expandNode(gen2)


    # right
    gen7 = Node((1,2), Node((1,1),gen2,1,3), 9, 2)
    # up

    gen8 = Node((0,1), Node((1,1),gen2,1,3), 10, 4)
    #down
    gen9 = Node((2,1), Node((1,1),gen2,1,3), 8, 2)
    # should be parent node
    gen10 = Node((1,1), Node((1,1),gen2,1,3), 0, 3)
    gen11 = Node((1,0), Node((1,1),gen2,1,3), 4, 5)
   
    assert gen7, gen9 in a.expandNode(Node((1,1),gen2,1,3))
    print "expected"
    print gen8.pos
    print gen8.parent
    print "observed"
    l = a.expandNode((Node((1,1),gen2,1,3)))
    for i in l:
        print i
   
    assert gen8 not in l
    gen12 = Node((1,3), gen7, 1,1)#middle
    gen13 = Node((0,3), gen12, 5, 2)#up
    gen14 = Node((2,3), gen12, 6, 0)#down
    gen15 = Node((1,2), gen12, 9, 2)#left
    gen16 = Node((1,4), gen12, 7, 2)#right
    genlist = [gen13, gen14, gen16]


    assert sorted(genlist) == sorted(a.expandNode(gen12))


    
def thirdTest():
    b = readBoard("map.txt")
    a = AStar(b,(0,0),[(2,3)])
    p = a.calcPath()
    
    #print "path\n",p.drawPath()
    ls = sorted(a.getExplored())
    for i in ls:
        print i

    t = Node((2,4), p, 10, 1)
    assert t not in a.getExplored()  
    t = Node((3,3), p, 1, 1)
    assert t in a.getExplored()  
                  
def main():
    firstTest()
    secondTest()
    thirdTest()
main()
