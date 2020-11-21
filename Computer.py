from Human import Human
import random
# from Gameplay import GamePlay

class Computer(Human):

    # gamePlay = GamePlay

    def __init__(self):
        self.name = "AI"

    def checkMoves(self, gamePlay):

        valid_move = False
        while not valid_move:
            row_move = random.randint(0, gamePlay.rows - 1)
            column_move = random.randint(0, gamePlay.columns - 1)
            if gamePlay.possibleMoves[row_move][column_move] == " ":
                continue
            else:
                valid_move = True
        return row_move, column_move


