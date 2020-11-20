from Interface import Interface
import PySimpleGUI as sg
import random

class GamePlay(Interface):
    def __init__(self, rows=5, columns=5):
        super().__init__()
        self.rows, self.columns = rows, columns
        self.possibleMoves = []

        #Player classes
        # player = Human()
        # computer = Computer()
        self.currentPlayer = None


        #Places cookies on to the game board
        for i in range(self.rows): # rows or bard
            print()
            matrixCols = []
            for j in range(self.columns): #columns of board
                #print("# ", end="")
                matrixCols.append((i + 1, j + 1))
            self.possibleMoves.append(matrixCols)

    #Gets the cookies that have not been removed from the board by a player action (Clickable cookies)
    def getPlay(self, choice):
        removeIds = [] #Cookies that will be removed from the board
        for row in self.possibleMoves:
            for pair in row:
                if pair[0] >= choice[0] and pair[1] >= choice[1]: #Checking if cookie is to the right and below clicked cookie
                    removeIds.append(pair)

        for tup in removeIds:
            for i in range(len(self.possibleMoves)):
                if tup in self.possibleMoves[i]:
                    self.possibleMoves[i].remove(tup) #remove cookie from board

    #Update the changes made to the board
    def updateBoard(self):
        self.layout = [[sg.Text("Player score: 10"), sg.Text("Computer Score: 39")],
                       [sg.Text("Game Number: 5")]]
        for i in range(len(self.possibleMoves)):
            matrixCols = []
            for j in range(len(self.possibleMoves[i])):
                #draw cookies to the screen
                matrixCols.append(sg.Button("", image_filename=self.image_cookie, key=str((i+1, j+1)), image_size=(50, 50)))
            self.layout.append(matrixCols)
        return self.layout

    #Determines which player plays first using a coin flip
    def playFirst(self):
        toss_layout = [[sg.Text("CHOOSE A EITHER OF THE TWO BELOW TO MAKE A TOSS", text_color="Yellow")],
                       [sg.Button('HEAD', size=(20, 10), key='1'),
                        sg.Text(' ' * 2),
                        sg.Button('TAIL', size=(20, 10), key='0')]]
        win = sg.Window("MAKE A TOSS", toss_layout)
        e, v = win.read()
        win.close()

        toss = random.choice([1, 0]) #flip coin
        print(toss)
        #If the flip matches user select, user goes first else computer
        if eval(e) == toss:
            self.loading()
            # self.currentPlayer = player
            sg.popup_no_titlebar("YOU WON THE TOSS, YOU PLAY FIRST")

        else:
            self.loading()
            # self.currentPlayer = computer
            sg.popup_no_titlebar("YOU LOST THE TOSS, COMPUTER PLAYS FIRST")
