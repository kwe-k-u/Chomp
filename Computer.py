from Human import Human


class Computer(Human):

    def __init__(self):
        self.name = "AI"


    def checkMoves(self):
        #TODO work on this
        pass
    #return moves

    def makeMove(self):
        pass
        m = self.checkMoves()
        #TODO work on this
        someIndex = 0
        self.makeMove(m[someIndex])
