from Interface import Interface
import PySimpleGUI as sg
import random

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

    def playFirst(self):
        toss_layout = [[sg.ReadFormButton('HEAD', button_color=sg.TRANSPARENT_BUTTON,
                            image_filename=self.image_head, auto_size_button=True, border_width=0),
                        sg.Text(' ' * 2),
                        sg.ReadFormButton('TAIL', button_color=sg.TRANSPARENT_BUTTON,
                            image_filename=self.image_tail, auto_size_button=True, image_subsample=2, border_width=0)]]
        win = sg.Window("MAKE A TOSS", toss_layout, background_color="White")
        e, v = win.read()
        win.close()
        toss = random.choice([1, 0])
        print(toss)
        if eval(e) == toss:
            self.loading()
            sg.popup_no_titlebar("YOU WON THE TOSS, YOU PLAY FIRST")
        else:
            self.loading()
            sg.popup_no_titlebar("YOU LOST THE TOSS, COMPUTER PLAYS FIRST")
