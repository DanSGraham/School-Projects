#!/usr/bin/python
# Michael K. Bradshaw
#
# PhaseOneTestingStarter.py
# Spring 2015

import game
import ai
import json
import random

##   GAME STATES
##
##The bot starter code has the ability to store the states of a game for playback.
##To generate new game files I stored a game and copied the line for a particular game state.
##The save file prints out the state dictionary.  a simple eval statement will read it back in.
##
##You will NEED multiple game states to fully test the code.


#Map Files

ENDING_FILE = """{u'viewUrl': u'http://vindinium.org/wplwwnxg', u'game': {u'turn': 40, u'finished': True, u'board': {u'tiles': u'          ##############                          ##  $-  $-  ##                          ##  $-  $-  ##                          ##  $-  $-  ##                          ##  $-  $-  ##                                                                                                                                                    []              []          ##########  ##################          $-                    $-                ##########  ####  ############      @3                                            @1@2      ################          @4$-  $-                            $-  $-                                                                                                                                                                                                        ', u'size': 20}, u'heroes': [{u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 6, u'x': 1}, u'crashed': False, u'mineCount': 0, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 2, u'x': 13}, u'spawnPos': {u'y': 0, u'x': 7}, u'crashed': False, u'mineCount': 10, u'lastDir': u'South', u'id': 2}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 18, u'x': 11}, u'spawnPos': {u'y': 19, u'x': 7}, u'crashed': False, u'mineCount': 15, u'lastDir': u'North', u'id': 3}, {u'life': 98, u'name': u'random', u'gold': 0, u'pos': {u'y': 19, u'x': 13}, u'spawnPos': {u'y': 19, u'x': 12}, u'crashed': False, u'mineCount': 8, u'lastDir': u'South', u'id': 4}], u'id': u'wplwwnxg', u'maxTurns': 40}, u'hero': {u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 6, u'x': 1}, u'crashed': False, u'mineCount': 0, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, u'token': u'24n9', u'playUrl': u'http://vindinium.org/api/wplwwnxg/24n9/play'}"""

CUSTOM_TEST_SURROUNDED = """{u'viewUrl': u'http://vindinium.org/wplwwnxg', u'game': {u'turn': 40, u'finished': True, u'board': {u'tiles': u'          ##############                          ##  $-  $-  ##                          ##  $-  $-  ##                          ##  $-  $-  ##                          ##  $-  $-  ##                                                                                                                                                    []              []          ##########  ##################          $-                    $-                ##########  ####  ############      @3  $-##                                    @1@2        ################          @4$-[]$-                            $-  $-                                                                                                                                                                                                        ', u'size': 20}, u'heroes': [{u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 0, u'x': 13}, u'spawnPos': {u'y': 7, u'x': 1}, u'crashed': False, u'mineCount': 0, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 0, u'x': 7}, u'crashed': False, u'mineCount': 10, u'lastDir': u'South', u'id': 2}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 18, u'x': 11}, u'spawnPos': {u'y': 19, u'x': 7}, u'crashed': False, u'mineCount': 15, u'lastDir': u'North', u'id': 3}, {u'life': 98, u'name': u'random', u'gold': 0, u'pos': {u'y': 19, u'x': 13}, u'spawnPos': {u'y': 19, u'x': 12}, u'crashed': False, u'mineCount': 8, u'lastDir': u'South', u'id': 4}], u'id': u'wplwwnxg', u'maxTurns': 40}, u'hero': {u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 0, u'x': 13}, u'spawnPos': {u'y': 7, u'x': 1}, u'crashed': False, u'mineCount': 0, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, u'token': u'24n9', u'playUrl': u'http://vindinium.org/api/wplwwnxg/24n9/play'}"""

CUSTOM_TEST_CLOSEST_HERO_DIAGONAL = """{u'viewUrl': u'http://vindinium.org/wplwwnxg', u'game': {u'turn': 40, u'finished': True, u'board': {u'tiles': u'          ##############                          ##  $1  $1  ##                          ##  $1  $2  ##                          ##  $2  $2  ##                          ##  $-  $-  ##                                                                                                                                          @3        []              []          ##########  ##################          $-    @4              $-                ##########  ####  ############                                                    @1        @2      ################    $-  $-                            $-  $-                                                                                                                                                                                                        ', u'size': 20}, u'heroes': [{u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 6, u'x': 1}, u'crashed': False, u'mineCount': 10, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 6, u'x': 13}, u'spawnPos': {u'y': 0, u'x': 7}, u'crashed': False, u'mineCount': 10, u'lastDir': u'South', u'id': 2}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 1, u'x': 8}, u'spawnPos': {u'y': 19, u'x': 7}, u'crashed': False, u'mineCount': 5, u'lastDir': u'North', u'id': 3}, {u'life': 98, u'name': u'random', u'gold': 0, u'pos': {u'y': 3, u'x': 10}, u'spawnPos': {u'y': 19, u'x': 12}, u'crashed': False, u'mineCount': 8, u'lastDir': u'South', u'id': 4}], u'id': u'wplwwnxg', u'maxTurns': 40}, u'hero': {u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 6, u'x': 1}, u'crashed': False, u'mineCount': 10, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, u'token': u'24n9', u'playUrl': u'http://vindinium.org/api/wplwwnxg/24n9/play'}"""

CUSTOM_TEST_CLOSEST_HERO_MULTIPLE_SAME = """{u'viewUrl': u'http://vindinium.org/wplwwnxg', u'game': {u'turn': 40, u'finished': True, u'board': {u'tiles': u'          ##############                          ##  $1  $1  ##                          ##  $1  $2  ##                          ##  $2  $3  ##                          ##  $-  $-  ##                                                                                                                                                    []              []          ##########  ##################          $-    @4              $-                ##########  ####  ############            @3                                      @1@2              ################    $-  $-                            $-  $-                                                                                                                                                                                                        ', u'size': 20}, u'heroes': [{u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 6, u'x': 1}, u'crashed': False, u'mineCount': 0, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 2, u'x': 13}, u'spawnPos': {u'y': 0, u'x': 7}, u'crashed': False, u'mineCount': 10, u'lastDir': u'South', u'id': 2}, {u'life': 30, u'name': u'random', u'gold': 0, u'pos': {u'y': 1, u'x': 12}, u'spawnPos': {u'y': 19, u'x': 7}, u'crashed': False, u'mineCount': 15, u'lastDir': u'North', u'id': 3}, {u'life': 98, u'name': u'random', u'gold': 0, u'pos': {u'y': 3, u'x': 10}, u'spawnPos': {u'y': 19, u'x': 12}, u'crashed': False, u'mineCount': 8, u'lastDir': u'South', u'id': 4}], u'id': u'wplwwnxg', u'maxTurns': 40}, u'hero': {u'life': 10, u'elo': 1200, u'gold': 0, u'userId': u'p3iturcp', u'pos': {u'y': 1, u'x': 13}, u'spawnPos': {u'y': 6, u'x': 1}, u'crashed': False, u'mineCount': 0, u'lastDir': u'Stay', u'id': 1, u'name': u'DoctorB'}, u'token': u'24n9', u'playUrl': u'http://vindinium.org/api/wplwwnxg/24n9/play'}"""

CUSTOM_TEST_CLOSEST_HERO_MULTIPLE_SAME_DIAGONAL = "HELLO"
def loadBrain(data):
    #read in as python description!!
    state = eval(data)#json.loads(data)

    #pretty printing for debug
    #print json.dumps(state,sort_keys=True, indent=4,separators=(',',': ')) 

    #create game object
    g = game.Game(state)
    #feed it to AI
    brain = ai.AI()
    brain.process(g)

    return brain


# ####calcAction--note they are y,x coordinates?####
def testCalcAction():
    brain = loadBrain(ENDING_FILE)
    print brain.game.board_map
    print brain.pathTo((13,1), [(2,6)])
    print brain.pathDistanceTo((13,1), [(2,6)])
    
    #Test Main Cases
    assert brain.calcAction((3,4),(3,5)) == "East"
    assert brain.calcAction((3,4), (3,3)) == "West"
    assert brain.calcAction((3,4), (2,4)) == "North"
    assert brain.calcAction((3,4), (4,4)) == "South"
    assert brain.calcAction((3,4), (3,4)) == "Stay"

    #Test Edge Cases
    #When location is in a negative direction
    assert brain.calcAction((0,0), (0,-1)) == "West"
    assert brain.calcAction((0,-1), (0,0)) == "East"
    assert brain.calcAction((0,0), (-1,0)) == "North"
    assert brain.calcAction((-1,0), (0,0)) == "South"

    #When the directions are not cardinal
    assert brain.calcAction((3,4), (3,6)) == "Stay"
    assert brain.calcAction((3,4), (1,4)) == "Stay"
    assert brain.calcAction((3,4), (4,5)) == "Stay"

    

    #Assumptions: Inputs make sense (e.g. tuples of coordinates). This method does not account for movement off of the map or into obstacles. Only tests integers.
    print "testCalcAction Passed"

###simpleDistanceTo###
def testSimpleDistanceTo():
    brain = loadBrain(ENDING_FILE)


    #Test Main Cases
    assert brain.simpleDistanceTo((3,6), (3,6)) == 0.0
    assert brain.simpleDistanceTo((3,6), (3,7)) == 1.0
    assert brain.simpleDistanceTo((3,6), (3,5)) == 1.0
    assert brain.simpleDistanceTo((3,6), (2,6)) == 1.0
    #The following test may cause issues due to inaccuracies in the square root of two being irrational.
    assert brain.simpleDistanceTo((3,6), (4,7)) == (2**.5)

    #Edge Cases
    #Going into negative terroritory
    assert brain.simpleDistanceTo((3,6), (3,-1)) == 7.0
    assert brain.simpleDistanceTo((3,6), (-1,6)) == 4.0
    assert brain.simpleDistanceTo((-1,-1), (-1,0)) == 1.0

                                  

    print "testSimpleDistanceTo Passes"


###canPassThrough###
def testCanPassThrough():
    brain = loadBrain(ENDING_FILE)
    #Test Main Cases
    assert brain.canPassThrough((-50,-50)) == False
    assert brain.canPassThrough((8,6)) == False
    assert brain.canPassThrough((9,6)) == False
    assert brain.canPassThrough((10,0)) == False
    assert brain.canPassThrough((13,2)) == False
    assert brain.canPassThrough((-1, 0)) == False
    assert brain.canPassThrough((0,-1)) == False
    assert brain.canPassThrough((20,0)) == False
    assert brain.canPassThrough((0,20)) == False
    
    assert brain.canPassThrough((13,1)) == True
    assert brain.canPassThrough((0,0)) == True
    assert brain.canPassThrough((11,5)) == True

    brain = loadBrain(CUSTOM_TEST_SURROUNDED)
    #Load custom map where player is surrounded on all sides and one side is off the map
    assert brain.canPassThrough((13,0)) == True
    assert brain.canPassThrough((14,0)) == False
    assert brain.canPassThrough((12,0)) == False
    assert brain.canPassThrough((13, -1)) == False
    assert brain.canPassThrough((13,1)) == False

    print "testCanPassThrough Passes"

###findClosestEnemy###

def testFindClosestEnemy():
    brain = loadBrain(ENDING_FILE)
    #Test Main Cases
    assert brain.findClosestEnemy().pos == (13,2) 

    #Test diagonal closer than cardinal
    brain = loadBrain(CUSTOM_TEST_CLOSEST_HERO_DIAGONAL)
    assert brain.findClosestEnemy().pos == (10,3)

    #Test Multiple heros same distance
    brain = loadBrain(CUSTOM_TEST_CLOSEST_HERO_MULTIPLE_SAME)
    assert brain.findClosestEnemy().pos == (12, 1) or brain.findClosestEnemy().pos == (13, 2)
    print "testFindClosestEnemy Passes"
    
###findMaxEarningHeroPosition###

def testFindMaxEarningHeroPosition():

    #Player 3 Has most Mines owned
    brain = loadBrain(ENDING_FILE)
    assert brain.findMaxEarningHero().pos == (11,18)

    #Tie between player 1 and 2 for most mines
    brain = loadBrain(CUSTOM_TEST_CLOSEST_HERO_DIAGONAL)
    assert brain.findMaxEarningHero().pos == (13, 1)
    print "testFindMaxEarningHeroPosition Passes"

###heroDistanceToSpawnPoint###

def testHeroDistanceToSpawnPoint():
    #main Case
    brain = loadBrain(ENDING_FILE)
    assert brain.heroDistanceToSpawnPoint() == 13
    

    brain = loadBrain(CUSTOM_TEST_SURROUNDED)
    assert brain.heroDistanceToSpawnPoint() == (193**.5)

    print "testHeroDistanceToSpawnPoint Passes"


def testPathCreation():
    brain = loadBrain(ENDING_FILE)
    print brain.game.board_map
    print brain.pathTo(brain.game.hero.pos, [(1,0),(0,0)])
    
def main():
    testCalcAction()
    testSimpleDistanceTo()
    testCanPassThrough()
    testFindClosestEnemy()
    testFindMaxEarningHeroPosition()
    testHeroDistanceToSpawnPoint()
    testPathCreation()
    
main()
