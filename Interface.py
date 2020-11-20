import PySimpleGUI as sg

class Interface:
    def __init__(self):
        self.layout = []
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

    @staticmethod
    #Asks user for information about the size of the board
    def gameSetup():
        r = sg.popup_get_text("How many rows of cookies do you want?")
        c = sg.popup_get_text("How many columns of cookies do you want?")
        return [r, c]

    def gameBoard(self, rows, col):
        #Draws game board with initial cookies
        for i in range(rows):
            matrixCols = []
            for j in range(col):
                matrixCols.append(sg.Button("", image_filename=self.image_cookie, key=str((i+1, j+1)), image_size=(50, 50)))
            self.layout.append(matrixCols)
        return self.layout
