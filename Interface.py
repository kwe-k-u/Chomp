import PySimpleGUI as sg

class Interface:
    def __init__(self, computer, human):
        self.computer = computer
        self.gameNumber  = 0
        self.player = human
        self.layout = [[sg.Text("Player score: " + str(self.player.getScore())), sg.Text("Computer Score: 0")],
                       [sg.Text("Game Number: " + str(self.gameNumber))]]
        self.image_cookie = './cookieHead.png'
        self.image_coin = './coin.png'
        sg.theme("DarkAmber")



    @staticmethod
    #Displays a loading indicator to the screen
    def loading():
        for i in range(100000):
            sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, background_color="White", time_between_frames=100)
        sg.popup_animated(None)

    @staticmethod
    #Asks user if (s)he wants a rematch
    def playAgain():
        decision = sg.popup_yes_no("Want to play again?", grab_anywhere=True)

        return "Yes" == decision

    def updateBoard(self):

        self.layout = [[sg.Text("Player score: " + str(self.player.getScore())), sg.Text("Computer Score: " + str(self.computer.getScore()))],
                       [sg.Text("Game Number: " + str(self.gameNumber))]]
        # self.gameBoard(self.possibleMoves, self.possibleMoves)
        for i in range(len(self.possibleMoves)):
            matrixCols = []

            for j in range(len(self.possibleMoves[i])):
                #draw cookies to the screen
                matrixCols.append(sg.Button("", image_filename=self.image_cookie, key=str((i+1, j+1)), image_size=(50, 50)))
            self.layout.append(matrixCols)
        return self.layout
