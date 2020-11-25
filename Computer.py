from Human import Human
import random
# from Gameplay import GamePlay

class Computer(Human):

    # gamePlay = GamePlay

    def __init__(self):
        self.name = "AI"

    def checkMoves(self, gamePlay):
        #Select a random row from possible moves. Then select a random cookie from that row
        #removing the null arrays
        if (gamePlay.possibleMoves.count([]) != 0):
            moves = gamePlay.possibleMoves[: -gamePlay.possibleMoves.count([])]
        else:
            moves = gamePlay.possibleMoves
        choice = random.choice(random.choice(moves))
        return (choice[0],choice[1])
