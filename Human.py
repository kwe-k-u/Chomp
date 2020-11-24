class Human:
    name = ""
    score = 0
    numMoves = 0

    def __init__(self, uName = "Human"):
        self.name = uName

    def getName(self):
        return self.name

    def makeMove(self):
        self.numMoves +=1
        pass

