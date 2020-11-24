from Human import Human
import random
# from Gameplay import GamePlay

class Computer(Human):

    # gamePlay = GamePlay

    def __init__(self):
        self.name = "AI"

    def checkMoves(self, gamePlay):
        #Select a random row from possible moves. Then select a random cookie from that row
        try:
            choice = random.choice(random.choice(gamePlay.possibleMoves))
        except: #Repeat process if an error occurs. (repetition of error is unlikely
            choice = random.choice(random.choice(gamePlay.possibleMoves))
        return (choice[0],choice[1])

