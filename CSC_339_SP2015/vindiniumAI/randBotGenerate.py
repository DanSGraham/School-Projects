#A program to generate a random, encoded, finite state bot. These will be used to save space
#In a text document with about 10000000 of them

from random import *

class botGenerator:

    lifeAmounts = [10, 20, "heroes within 1 space", "heroes within 2 spaces", "heroes within 3 spaces"]

    distances = [5, 4, 3, 2, 1]

    numHeroes = [0, 1, 2, 3]
    
    conditionals = {
        "own gold": [["gt"] + numHeroes, ["lt"] + numHeroes],    #"own gold": ["is greater than x num heroes"]["is less than x num heros"]
        "own life": [["is greater than"] + lifeAmounts, ["is less than"] + lifeAmounts],    #"own life": [["is greater than"] + lifeAmounts, ["is less than"] + lifeAmounts],
        "own mines": [["is greater than x num heroes"] + numHeroes, ["is less than x num heroes"] + numHeroes],    #"own mines": [["is greater than x num heroes"] + numHeroes, ["is less than x num heroes"] + numHeroes],         
        "number of heros 1 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],    #"number of heros 1 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],
        "number of heroes 2 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],    #"number of heroes 2 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],
        "number of heroes 3 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],    #"number of heroes 3 distance away": [["is greater than"] + numHeroes,["is less than"] + numHeroes],
        
    }

    idConditionals = {
        """These conditionals identify a specific enemy"""
        
        "opponent with highest gold": [["is closer than"] + distances],    #"opponent with highest gold": [["is closer than"] + distances]
        "opponent with lowest health": [["is closer than"] + distances],    #"opponent with lowest health": [["is closer than"] + distances],
        "opponent with most mines": [["is closer than"] + distances],   #"opponent with most mines": [["is closer than"] + distances],
        "closest opponent": [["is closer than"] + distances],    #"closest opponent": [["is closer than"] + distances],
        "tavern": [["is closer than"] + distances],    #tavern": [["is closer than"] + distances],
    }

    specificConditionals = {
        """These conditionals target a specific enemy. They may specify a conditional or any hero come after an id conditional"""
        
        "opponent gold": [["is greater than x num heroes"] + numHeroes, ["is less than x num heros"] + numHeroes],    #"opponent gold": [["is greater than x num heroes"] + numHeroes, ["is less than x num heros"] + numHeroes],
        "opponent life": [["is greater than"] + lifeAmounts, ["is less than"]+ lifeAmounts],    #"opponent life": [["is greater than"] + lifeAmounts, ["is less than"]+ lifeAmounts],
        "opponent mines": [["is greater than x num heroes"] + numHeroes, ["is less than x num heroes"] + numHeroes],    #"opponent mines": [["is greater than x num heroes"] + numHeroes, ["is less than x num heroes"] + numHeroes],
        "opponent is at tavern" : [True, False]    #"opponent is at tavern" : [True, False]
    }
    conjunctions = [
        "and",
        "or"
    ]

    actions = [
        "go to",
        "run away"
    ]

    def __init__(self, maxNumStatements, maxStatementSize, numTrials):
        
        self.maxStatements = maxNumStatements
        self.maxStatementSize = maxStatementSize
        self.numTrials = numTrials

    def generateBot(self):
        botString = ""
        numStatements = randint(0, self.maxStatements)
        for i in range(numStatements):
            possibleStatements = conditionals.keys() + idConditionals.keys() + specificConditionals.keys()
            statementSize = randint(0, self.maxStatementSize)
            for j in range(statementSize):
                
        
