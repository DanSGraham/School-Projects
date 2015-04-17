#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################
#
# HAL10000
#
########################################################################

import random
from math import *
from vinAStar import *

"""Information the AI needs:
    distance to all things can be calculated for each.
    Path to all can be calculated from position"""

class AI:
    """Pure AWESOME A.I, you may DEFINITELY use it to win ;-)"""
    def __init__(self):
        pass

    def process(self, game):
        """Do whatever you need with the Game object game"""
        self.game = game


    
    def printMap(self):
        """Prints out an easier to read map of the game state"""
        for line in self.game.board_map:
            print line

    def simpleDistanceTo(self,startingPos,endingPos):
        """calculates the euclidian distance from the y,x tuples, startingPos to endingPos"""
        
        distance = float(((endingPos[0] - startingPos[0])**2 + (endingPos[1] - startingPos[1])**2)**.5)
        
        return distance

    def manDistanceTo(self, startingPos, endingPos):
        """calculates the Manhattan distance from y,x tuples, startingPos to endingPos"""

        distance = abs(startingPos[0] - endingPos[0]) + abs(startingPos[1] - endingPos[1])

        return distance

    def pathDistanceTo(self, startingPos, endingPos):
        """calulates the distance the hero must travel to reach the ending pos using pathTo"""

        return len(self.pathTo(startingPos, endingPos))
        

    def calcAction(self,startingPos,endingPos):
        #This method seems unnecessary......
        """calculate the direction needed to go from (y,x) tuples startingPos to endingPos.
           if the positions are the same, you should issue the Stay command
           if they positions are not cardinal neighbors it is an error and you should return the Stay command
           Otherwise, return North,South,East,West as appropriate
        """
        
        if endingPos[0] == startingPos[0]:
            if endingPos[1] == (startingPos[1] + 1):
                return "East"
            elif endingPos[1] == (startingPos[1] - 1):
                return "West"
        elif endingPos[1] == startingPos[1]:
            if endingPos[0] == (startingPos[0] - 1):
                return "North"
            elif endingPos[0] == (startingPos[0] + 1):
                return "South"
            
        return "Stay"

    
    def canPassThrough(self,position):
        #This method is copied in vinAStar and slightly modified to allow the ending node to be pass throughable.
        
        """Is it possible to pass through this the (y,x) position stored in position?
           Returns False if there is anything in that position (mountain, mine, tavern, other heroes
            Returns True if there is nothing there.  Note a hero can pass through themself.

            Also Note: Any position that is not on the board should be deemed as impassible as well
        """
        #The only time the hero can move to a place is when the place is within the board, and either a blank space (" ") or herself (indicated by self.pos).
        if position[0] >= 0 and position[1] >= 0 and position[0] < self.game.board_size and (position[1]) < self.game.board_size and \
           (self.game.board_map[position[0]][position[1]] == " " or position == self.game.hero.pos):
            return True
        else:
            return False


    def findClosestEnemy(self):
        """Need someone to kill?  return the closest enemy hero (using Euclidian distance)"""
        
        currEnemyHero = None
        for poHero in self.game.heroes:
            if poHero.pos != self.game.hero.pos:
                if currEnemyHero == None:
                    currEnemyHero = poHero
                else:
                    testDistance = self.simpleDistanceTo(self.game.hero.pos, poHero.pos)
                    if testDistance < self.simpleDistanceTo(self.game.hero.pos, currEnemyHero.pos):
                        currEnemyHero = poHero
                        
        return currEnemyHero

    def findClosestPathEnemy(self):
        """Finds the closest enemy hero based on path length"""
        

    def findClosestEnemyNotAtTavern(self):
        """Returns the closest hero not currently at a tavern"""

        currEnemyHero = None       
        for poHero in self.game.heroes:
            if poHero.pos != self.game.heroes and not self.heroAtTavern(hero):
                if currEnemyHero == None:
                    currEnemyHero = poHero
                else:
                    testDistance = self.simpleDistanceTo(self.game.hero.pos, poHero.pos)
                    if testDistance < self.simpleDistanceTo(self.game.hero.pos, currEnemyHero.pos):
                        currEnemyHero = poHero
                        
        return currEnemyHero   

    def findMaxEarningHero(self):
        """who ever is earning the most is a worthwhile target to kill.
           This function returns the person with the most mines.
           Note, you can return your own hero
        """
        
        currMaxEarningHero = None
        for poHero in self.game.heroes:
            if currMaxEarningHero == None:
                currMaxEarningHero = poHero
            else:
                if poHero.mine_count > currMaxEarningHero.mine_count:
                    currMaxEarningHero = poHero
                    
        return currMaxEarningHero

    def findLowestHealthHero(self):
        """Returns the hero with the lowest health.
            Note: May return self."""

        lowestHealthHero = self.game.hero
        
        for poHero in self.game.heroes:
            if poHero.life < lowestHealthHero.life:
                lowestHealthHero = poHero
                
        return lowestHealthHero

    def findEnemyWithMostGold(self):
        """Returns the hero with the most gold. May be own hero"""

        highestGoldHero = self.game.hero

        for poHero in self.game.heroes:
            if poHero.gold > highestGoldHero:
                highestGoldHero = poHero
                
        return highestGoldHero

    def findClosestTavern(self):
        """the only brew for the brave and true comes from the Green Dragon! Use this function to find a brew!"""
        
        closestTavern = None
        for tavernLocation in self.game.taverns_locs:
            if closestTavern == None:
                closestTavern = tavernLocation
            else:
                if simpleDistanceTo(self.game.hero.pos, tavernLocation) < simpleDistanceTo(self.game.hero.pos, tavernLocation):
                    closestTavern = tavernLocation
                    
        return closestTavern

            
    def findClosestMine(self):
        """returns the position of the closest mine (using euclidian distance)
        Note: Can return a mine owned by your hero"""

        currClosestMine = self.game.mines_locs[0]

        for poMine in self.game.mine_locs:
            if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestMine):
                currClosestMine = poMine
                
        return currClosestMine


    def findClosestOwnMine(self):
        """Returns the position of the your closest mine"""

        currClosestOwnMine = None
        if self.game.hero.mine_count > 0:
            currClosestOwnMine = self.game.hero.mines[0]
            for poMine in self.game.hero.mines:
                if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestOwnMine):
                    currClosestMine = poMine
                    
        return currClosestOwnMine

    def findClosestEnemyMine(self):
        """Returns the position of the closest enemy Mine"""
        
        currClosestEnemyMine = None
        for poMine in self.game.mines_locs:
            if not poMine in self.game.hero.mines:
                if currClosestEnemyMine == None:
                    currClosestEnemyMine = poMine
                else:
                    if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestEnemyMine):
                        currClosestEnemyMine = poMine
                        
        return currClosesetEnemyMine
            
    def findClosestSpecificEnemyMine(self, specificHero):
        """Returns the position of the closest mine to a specific hero"""
        
        currClosestHeroMine = None
        if specificHero.mine_count > 0:
            currClosestHeroMine = specificHero.mines[0]
            for poMine in specificHero.mines:
                if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestHeroMine):
                    currClosestHeroMine = poMine
                    
        return currClosestHeroMine
        
    def heroDistanceToSpawnPoint(self):
        """Returns the distance of your hero to the spawn Point"""
        return self.simpleDistanceTo(self.game.hero.pos,self.game.hero.spawn_pos)

    def getCardinalCoordinates(self, startingCoord):
        """Returns a list of the cardinal coordinates of the startingCoord in the order [North, East, South, West]"""
        north = (startingCoord[0] - 1, startingCoord[1])
        east = (startingCoord[0], startingCoord[1] + 1)
        south = (startingCoord[0] + 1, startingCoord[1])
        west = (startingCoord[0], startingCoord[1] - 1)
        return [north, east, south, west]
    
    def pathTo(self, startingCoordinates, endCoordinates):
        """Returns the shortest path to the end coordinates using A* search. Hueristic is the euclidian distance."""
        #Unsure if the path must start with the startingCoordinate or if it can start with the first move.
        pathArray = []
        aStarSearch = AStar(self.game.board_map, startingCoordinates, endCoordinates)
        pathEnd = aStarSearch.calcPath()
        
        return pathEnd.getRPath([])[::-1]
                    
        
    def noDamagePathTo(self, startingCoordinates, endingCoordinates):
        """Returns a path that does not go near opponents"""
        pass            
        
        
    def attackHero(self, heroToAttack):
        """Returns a path to attack a hero in it's current state."""
        return pathTo(self.game.hero.pos, [heroToAttack.pos])

    def goToNearestTavern(self):
        """Returns a path to the nearest available tavern"""
        return pathTo(self.game.hero.pos, self.game.taverns_locs)
        
    def nearestUninterruptedTavern(self):
        """Returns the closest tavern the hero can reach without other players reaching them first."""

    def goToClosestMine(self):
        """Returns the closest available mine. May be useful to lure a hero towards a mine which may then deplete their health for me to then attack"""
        return pathTo(self.game.hero.pos, self.game.mines_locs)

    def goToNearestEnemyMine(self):
        """returns the nearest enemy controlled mine"""
        enemyMines = []
        for poMine in self.game.mines:
            if not poMine in self.game.hero.mines:
                enemyMines.append(poMine)
        pathTo(self.game.hero.pos, enemyMines)
    
    def goToNearestSpecificEnemyMine(self, hero):
        """returns the nearest mine of a specific hero"""
        pathTo(self.game.hero.pos, hero.mines)

    def heroWithLowestScore(self):
        """returns the position of the hero with the lowest score"""
        lowestHero = self.game.hero
        for poHero in self.game.heroes:
            if poHero.gold < lowestHero.gold:
                lowestHero = poHero
        return lowestHero.pos
    
    def heroAtTavern(self, hero):
        """determines if a hero is at a tavern currently"""

        tavernPatronPositions = []
        for tavernLoc in self.game.taverns_locs:
            tavernEarners = self.getCardinalCoordinates(tavernLoc)
            tavernPatronPositions += tavernEarners

        return hero.pos in tavernPatronPositions
        

    def runFromHeroes(self):
        """Moves away from adjacent heroes. Not smart, but it works."""
        possibleMoves = self.getCardinalCoordinates(self.game.hero.pos)
        for poMove in possibleMoves:
            if self.canPassThrough(poMove):
                return [self.game.hero.pos] + [poMove]
            
        return [self.game.hero.pos]

    def getHeroHealth(self, heroWantHealth):
        """Returns the health of the desired hero"""
        return heroWantHealth.life


    def orderHerosByDistance(self):
        heroList = []
        ownPosition = self.game.hero.getPos()
        for pHero in self.game.heroes:
            if pHero.getPos() != ownPosition:
                if len(heroList) == 0:
                    heroList.append(pHero)
                else:
                    for i in range(len(heroList)):
                        if self.pathToDistance(ownPosition, pHero.getPos()) < self.pathToDistance(ownPosiiton, heroList[i]):
                            heroList.insert(i, pHero)
                    if not pHero in heroList:
                        heroList.append(pHero)
        return heroList

    def orderTavernsByDistance(self):
        tavernList = []
        ownPosition = self.game.hero.getPos()
        for pTav in self.game.taverns_locs:
            if len(tavernList) == 0:
                tavernList.append(pTav)
            else:
                for i in range(len(tavernList)):
                    if self.pathToDistance(ownPosition, pTav) < self.pathToDistance(ownPosiiton, tavernList[i]):
                        tavernList.insert(i, pTav)
                if not pTav in tavern:
                    tavernList.append(pTav)
        return tavernList

    def orderUnownedMinesByDistance(self):
        mineList = []
        ownPosition = self.game.hero.getPos()
        for pMine in self.game.mines_locs:
            if not pMine in self.game.hero.mines:
                if len(mineList) == 0:
                    mineList.append(pMine)
                else:
                    for i in range(len(mineList)):
                        if self.pathToDistance(ownPosition, pMine) < self.pathToDistance(ownPosiiton, mineList[i]):
                            mineList.insert(i, pMine)
                    if not pMine in mineList:
                        mineList.append(pMine)
        return mineList
            

    def createInputs(self, numInputs):
        #Unsure why numInputs is a parameter...
        """returns a list of numbers to represent the inputs to each of the neurons in the Neural Network"""
        """List of inputs:
            Distance to closest hero
            difference in mines
            difference in gold
            difference in life
            repeat for next closest hero and so on
            distance to closest mine
            distance to closest mine owned by enemy with most mines
            distance to closest mine owned by enemy with most gold
            distance to closest tavern
            """
        inputList = []
        ownHero = self.game.hero
        orderHeros = self.orderHerosByDistance()
        orderTaverns = self.orderTavernsByDistance()
        orderMines = self.orderUnownedMinesByDistance()
        inputList.append(ownHero.life)
        inputList.append(ownHero.gold)
        if ownHero.getPos() == ownHero.spawn_pos:
            inputList.append(1)
        else:
            inputList.append(0)

        inputList.append(ownHero.mineCount)
        
        if self.heroAtTavern(ownHero):
            inputList.append(1)
        else:
            inputList.append(0)

        for pHero in orderHeros:
            inputList.append(self.pathToDistance(ownHero.getPos(), pHero.getPos()))
            inputList.append(pHero.life)
            inputList.append(pHero.gold)
            if pHero.getPos() == pHero.spawn_pos:
                inputList.append(1)
            else:
                inputList.append(0)

            inputList.append(pHero.mineCount)
        
            if self.heroAtTavern(pHero):
                inputList.append(1)
            else:
                inputList.append(0)
        for pTavern in orderTaverns:
            inputList.append(self.pathToDistance(ownHero.getPos(), pTavern))

        for pMine in orderMines:
            inputList.append(self.pathToDistance(ownHero.getPos(), pMine))

        for i in range(31 - len(inputList)):
            inputList.append(0)
            
        return inputList
        

    def determineClass(self, destPoint):
        """returns the class the destPoint belongs to. The return value will be a number from 0 up to classes."""
        classVal = 0
        ownPosition = self.game.hero.getPos()
        distOfPoint = self.pathToDistance(ownPosition, destPoint)

        """all ordered by location"""
        orderHeros = self.orderHerosByDistance()
        orderTaverns = self.orderTavernsByDistance()
        orderMines = self.orderUnownedMinesByDistance()

        for pHero in orderHeros:
            if destPoint == pHero.getPos():
                return classVal
            else:
                classVal += 1

        for tavernPos in orderTaverns:
            if destPoint == tavernPos:
                return classVal
            else:
                classVal += 1

        classVal = 7
        for minePos in orderMines:
            if destPoint == minePos:
                return classVal
            else:
                classVal += 1

        return """CLASS VAL ERROR"""


        

    def decide(self):
        """Must return a tuple containing in that order:
          1 - path_to_goal :
                  A list of coordinates representing the path to your
                 bot's goal for this turn:
                 - i.e: [(y, x) , (y, x), (y, x)]
                 where y is the vertical position from top and x the
                 horizontal position from left.

          2 - action:
                 A string that will be displayed in the 'Action' place.
                 - i.e: "Go to mine"

          3 - decision:
                 A list of tuples containing what would be useful to understand
                 the choice you're bot has made and that will be printed
                 at the 'Decision' place.

          4- hero_move:
                 A string in one of the following: West, East, North,
                 South, Stay

          5 - nearest_enemy_pos:
                 A tuple containing the nearest enemy position (see above)

          6 - nearest_mine_pos:
                 A tuple containing the nearest mine position (see above)

          7 - nearest_tavern_pos:
                 A tuple containing the nearest tavern position (see above)"""

        actions = ['mine', 'tavern', 'fight']

        decisions = {'mine': [("Mine", 30), ('Fight', 10), ('Tavern', 5)],
                    'tavern': [("Mine", 10), ('Fight', 10), ('Tavern', 50)],
                    'fight': [("Mine", 15), ('Fight', 30), ('Tavern', 10)]}

        walkable = []
        path_to_goal = []
        dirs = ["North", "East", "South", "West", "Stay"]

        for y in range(self.game.board_size):
            for x in range(self.game.board_size):
                if (y, x) not in self.game.walls_locs or \
                        (y, x) not in self.game.taverns_locs or \
                        (y, x) not in self.game.mines_locs:

                    walkable.append((y, x))

        # With such a random path, path highlighting would
        # display a random continuous line of red bullets over the map.
        first_cell = self.game.hero.pos
        path_to_goal.append(first_cell)

        for i in range(int(round(random.random()*self.game.board_size))):
            for i in range(len(walkable)):
                random.shuffle(walkable)
                if (walkable[i][0] - first_cell[0] == 1 and
                        walkable[i][1] - first_cell[1] == 0) or \
                        (walkable[i][1] - first_cell[1] == 1 and
                        walkable[i][0] - first_cell[0] == 0):
                    path_to_goal.append(walkable[i])
                    first_cell = walkable[i]
                    break

        hero_move = random.choice(dirs)
        action = random.choice(actions)
        decision = decisions[action]
        nearest_enemy_pos = random.choice(self.game.heroes).pos
        nearest_mine_pos = random.choice(self.game.mines_locs)
        nearest_tavern_pos = random.choice(self.game.mines_locs)

        return (path_to_goal,
                action,
                decision,
                hero_move,
                nearest_enemy_pos,
                nearest_mine_pos,
                nearest_tavern_pos)


if __name__ == "__main__":
    
    pass
