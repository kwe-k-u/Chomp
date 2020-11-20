import PySimpleGUI as sg
import Gameplay as gp

g = gp.GamePlay()
g.loading()
g.gameSetup()
setupWin = sg.Window("CHOMP", g.updateBoard())
event, values = setupWin.read()
setupWin.close()

while eval(event) != (1, 1):
    g.loading()
    g.getPlay(eval(event))
    setupWin = sg.Window("CHOMP", g.updateBoard())
    event, value = setupWin.read()
    setupWin.close()

d = g.playAgain()

while d:
    g.loading()
    g.gameSetup()
    setupWin = sg.Window("CHOMP", g.updateBoard())
    event, values = setupWin.read()
    setupWin.close()

    while eval(event) != (1, 1):
        g.loading()
        g.getPlay(eval(event))
        setupWin = sg.Window("CHOMP", g.updateBoard())
        event, value = setupWin.read()
        setupWin.close()

    d = g.playAgain()