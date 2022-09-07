from random import randrange

class State:
    #Game state
    destiny = 0
    potatoes = 0
    orcs = 0
    potatoesPerOrc = 1
    numTurns = 0

    #Experiment state
    numGames = 0
    numDestinyWins = 0
    numPotatoWins = 0
    numOrcWins = 0
    numGamesToRun = 1000000

#An experiment is a group of games
def runExperiment(s):
    while s.numGames < s.numGamesToRun:
        initializeNewGame(s)
        runGame(s)
        s.numGames += 1
    print(f'GamesRan:{s.numGames} DestinyWins:{s.numDestinyWins} PotatoeWins:{s.numPotatoWins} OrcWins:{s.numOrcWins}')

def initializeNewGame(s):
    s.destiny = 0
    s.potatoes = 0
    s.orcs = 0
    s.potatoesPerOrc = 1
    s.numTurns = 0

def runGame(s):
    while not gameOver(s):
        playerLogic(s)       
        takeTurn(s)

def gameOver(s):
    if s.destiny >= 10 or s.potatoes >= 10 or s.orcs >= 10:
        #print(f'GameNum:{s.numGames} Destiny:{s.destiny} Potatoes:{s.potatoes} Orcs:{s.orcs} Turns:{s.numTurns}', end=' ')
        if s.destiny >= 10:
            #print("Winner:Destiny")
            s.numDestinyWins += 1
        if s.potatoes >= 10:
            #print("Winner:Potato")
            s.numPotatoWins += 1
        if s.orcs >= 10:
            #print("Winner:Orc")
            s.numOrcWins += 1
        return True
    else:
        return False

def playerLogic(s):
    if s.orcs >= 8 and s.potatoesPerOrc <= s.potatoes:
        s.orcs -= 1
        s.potatoes -= s.potatoesPerOrc

def takeTurn(s):
    s.numTurns += 1
    firstRoll = randrange(1,7)
    secondRoll = randrange(1,7)
    if firstRoll == 1 or firstRoll == 2:
        if secondRoll == 1:
            s.potatoes += 1
        
        elif secondRoll == 2:
            s.potatoes += 1
            s.destiny += 1
        
        elif secondRoll == 3:
            s.destiny += 1
            s.orcs += 1
        
        elif secondRoll == 4:
            s.orcs += 1
            s.potatoes -= 1
        
        elif secondRoll == 5:
            s.potatoes -= 1
        
        elif secondRoll == 6:
            s.potatoes += 2   

    elif firstRoll == 3 or firstRoll == 4:
        if secondRoll == 1:
            s.orcs += 1
        
        elif secondRoll == 2:
            s.destiny += 1
        
        elif secondRoll == 3:
            s.orcs += 1
            s.destiny += 1
        
        elif secondRoll == 4:
            s.potatoes -= 1
            s.orcs += 2
        
        elif secondRoll == 5:
            s.destiny += 1
        
        elif secondRoll == 6:
            s.potatoes += 2
    
    else:
        s.potatoesPerOrc += 1

if __name__ == '__main__':
    s = State()
    runExperiment(s)