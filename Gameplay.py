from Interface import Interface
import PySimpleGUI as sg
import random
from Human import Human
from Computer import Computer

class GamePlay(Interface):
    def __init__(self):

        name = sg.popup_get_text("Enter your player name: ")

        super(GamePlay, self).__init__(Computer(), Human(name))
        self.reset()

        if self.currentPlayer is None:
            self.playFirst()




    #Asks user for information about the size of the board
    def gameSetup(self):
        self.reset()
        r = sg.popup_get_text("How many rows of cookies do you want?")
        c = sg.popup_get_text("How many columns of cookies do you want?")
        self.columns = c
        self.rows = r
        self.gameNumber += 1

        #Places cookies on to the game board
        for i in range(eval(self.rows)): # rows or bard
            matrixCols = []
            for j in range(eval(self.columns)): #columns of board
                matrixCols.append((i + 1, j + 1))
            self.possibleMoves.append(matrixCols)


    #Gets the cookies that have not been removed from the board by a player action (Clickable cookies)
    def getPlay(self, choice):
        if type(choice) == str:
            choice = eval(choice)
        self.removeIds = [] #Cookies that will be removed from the board
        for row in self.possibleMoves:
            for pair in row:
                if (int(pair[0]) >= int(choice[0]) and int(pair[1]) >= int(choice[1])): #Checking if cookie is to the right and below clicked cookie
                    self.removeIds.append(pair)

        for tup in self.removeIds: #Reoving that users cut off
            for i in range(len(self.possibleMoves)):
                if tup in self.possibleMoves[i]:
                    self.possibleMoves[i].remove(tup) #remove cookie from board

        self.switchPlayer()

    #Determines who begins the game
    def playFirst(self):
        toss_layout = [[sg.Text("CHOOSE A EITHER OF THE TWO BELOW TO MAKE A TOSS", text_color="Yellow")],
                       [sg.Button('HEAD', size=(20, 10), key='1'),
                        sg.Text(' ' * 2),
                        sg.Button('TAIL', size=(20, 10), key='0')]]
        win = sg.Window("MAKE A TOSS", toss_layout)
        e, v = win.read()
        win.close()

        toss = random.choice([1, 0]) #flip coin
        #If the flip matches user select, user goes first else computer
        if eval(e) == toss:
            self.loading()
            self.switchPlayer("player")
            sg.popup_no_titlebar("YOU WON THE TOSS, YOU PLAY FIRST")

        else:
            self.loading()
            self.switchPlayer("computer")
            sg.popup_no_titlebar("YOU LOST THE TOSS, COMPUTER PLAYS FIRST")


    #Resets the value of all class attributes to their defaults
    def reset(self):
        self.possibleMoves = []
        self.columns, self.columns = 5,5
        self.removeIds = []


