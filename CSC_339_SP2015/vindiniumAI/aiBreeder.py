#A program to find ideal AI using a genetic algorithm

#Create all possible scenarios


###Amounts may be too large or too small to matter. May create unnecessary wasted minions.
##Maybe have area of affect?
##Number of enemies within a _____ distance.


lifeAmounts = [10, 20, "heroes within 1 space", "heroes within 2 spaces", "heroes within 3 spaces"]

distances = [5, 4, 3, 2, 1]

numHeroes = [0, 1, 2, 3]

conditionals = {
    "own gold": [["is greater than x num heroes"] + numHeroes, ["is less than x num heros"] + numHeroes],
    "own life": [["is greater than"] + lifeAmounts, ["is less than"] + lifeAmounts],
    "own mines": [["is greater than x num heroes"] + numHeroes, ["is less than x num heroes"] + numHeroes],
    "opponent gold": [["is greater than x num heroes"] + numHeroes, ["is less than x num heros"] + numHeroes],
    "opponent life": [["is greater than"] + lifeAmounts, ["is less than"]+ lifeAmounts],
    "opponent mines": [["is greater than x num heroes"] + numHeroes, ["is less than x num heroes"] + numHeroes],
    "opponent with highest gold": [["is closer than"] + distances],
    "opponent with lowest health": [["is closer than"] + distances],
    "opponent with most mines": [["is closer than"] + distances],
    "closest opponent": [["is closer than"] + distances],
    "tavern": [["is closer than"] + distances],
    "number of heros 1 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],
    "number of heroes 2 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],
    "number of heroes 3 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],
    "opponent is at tavern" : [True, False]
    }

idConditionals = {
    "opponent with highest gold": [["is closer than"] + distances],
    "opponent with lowest health": [["is closer than"] + distances],
    "opponent with most mines": [["is closer than"] + distances],
    "closest opponent": [["is closer than"] + distances],
    "tavern": [["is closer than"] + distances]
    }

conjunctions = [
    "and",
    "or"
    ]

actions = [
    "go to",
    "run away"
    ]


def OneConditionGenerator(largestNumOfCondition):
    cNum = largestNumOfConditional
    
    
    pass
def interpreter():
    pass
class Breeder:
    pass
class Fighter:
    pass


class randomizer:
    pass

