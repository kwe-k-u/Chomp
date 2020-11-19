import PySimpleGUI as sg

class Interface:
    def __init__(self):
        self.userName = ""
        self.layout = []

    @staticmethod
    def loading():
        for i in range(100000):
            sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, background_color="White", time_between_frames=100)
        sg.popup_animated(None)

    @staticmethod
    def playAgain():
        decision = sg.popup_yes_no("Want to play again?", grab_anywhere=True)
        return "Yes" == decision

    def userDetails(self):
        self.userName = sg.popup_get_text("Hello player, what's your name?", grab_anywhere=True)

    @staticmethod
    def gameSetup():
        r = sg.popup_get_text("How many rows of cookies do you want?")
        c = sg.popup_get_text("How many columns of cookies do you want?")
        return [r, c]

    def gameBoard(self, rows, col):
        for i in range(rows):
            matrixCols = []
            for j in range(col):
                matrixCols.append(sg.Button(str((i+1, j+1))))
            self.layout.append(matrixCols)
        return self.layout

