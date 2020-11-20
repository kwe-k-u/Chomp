import PySimpleGUI as sg
import Gameplay as gp

g = gp.GamePlay()
g.loading()
board = g.gameSetup()
g.playFirst()
chp = gp.GamePlay(int(board[0]), int(board[1]))
setupWin = sg.Window("CHOMP", chp.gameBoard(int(board[0]), int(board[1])))
event, values = setupWin.read()
setupWin.close()

while eval(event) != (1, 1):
    chp.loading()
    chp.getPlay(eval(event))
    setupWin = sg.Window("CHOMP", chp.updateBoard())
    event, value = setupWin.read()
    setupWin.close()

d = chp.playAgain()

while d:
    g = gp.GamePlay()
    g.loading()
    board = g.gameSetup()
    g.playFirst()
    chp = gp.GamePlay(int(board[0]), int(board[1]))
    # setupWin = sg.Window("CHOMP " + g.currentPlayer.getName(), chp.gameBoard(int(board[0]), int(board[1])))
    setupWin = sg.Window("CHOMP", chp.gameBoard(int(board[0]), int(board[1])))
    event, values = setupWin.read()
    setupWin.close()

    while eval(event) != (1, 1):
        chp.loading()
        chp.getPlay(eval(event))
        setupWin = sg.Window("CHOMP", chp.updateBoard())
        event, value = setupWin.read()
        setupWin.close()

    d = chp.playAgain()