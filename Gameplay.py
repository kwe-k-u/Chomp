from Interface import Interface
import PySimpleGUI as sg
class GamePlay(Interface):
    def __init__(self, rows=5, columns=5):
        super().__init__()
        self.rows, self.columns = rows, columns
        self.possibleMoves = []
        #Gameboard
        for i in range(self.rows):
            print()
            matrixCols = []
            for j in range(self.columns):
                #print("# ", end="")
                matrixCols.append((i + 1, j + 1))
            self.possibleMoves.append(matrixCols)

    def getPlay(self, choice):
        removeIds = []
        for row in self.possibleMoves:
            for pair in row:
                if pair[0] >= choice[0] and pair[1] >= choice[1]:
                    removeIds.append(pair)

        for tup in removeIds:
            for i in range(len(self.possibleMoves)):
                if tup in self.possibleMoves[i]:
                    self.possibleMoves[i].remove(tup)

    def updateMatrix(self):
        for i in self.possibleMoves:
            print()
            for j in range(len(i)):
                print("# ", end="")

    def updateBoard(self):
        self.layout = []
        for i in range(len(self.possibleMoves)):
            matrixCols = []
            for j in range(len(self.possibleMoves[i])):
                matrixCols.append(sg.Button(str((i + 1, j + 1))))
            self.layout.append(matrixCols)
        return self.layout

