import PySimpleGUI as sg
import Gameplay as gp

g = gp.GamePlay()
g.loading()
g.gameSetup()
setupWin = sg.Window("CHOMP", g.updateBoard())
if g.currentPlayer.getName() != "AI":
    event, values = setupWin.read()
else:
    event = g.currentPlayer.checkMoves(g)
setupWin.close()
print
while event != (1, 1):
# while eval(event) != (1, 1):
    g.loading()
    g.getPlay(event)
    setupWin = sg.Window("CHOMP", g.updateBoard())
    if g.currentPlayer.getName() != "AI":
        event, values = setupWin.read()
    else:
        event = g.currentPlayer.checkMoves(g)
    setupWin.close()

d = g.playAgain()

while d:
    g.loading()
    g.gameSetup()
    setupWin = sg.Window("CHOMP", g.updateBoard())
    if g.currentPlayer.getName() != "AI":
        event, values = setupWin.read()
    else:
        event = g.currentPlayer.checkMoves(g)
    setupWin.close()

    while event != (1, 1):
        g.loading()
        g.getPlay(event)
        setupWin = sg.Window("CHOMP", g.updateBoard())

        if g.currentPlayer.getName() != "AI":
            event, values = setupWin.read()
        else:
            event = g.currentPlayer.checkMoves(g)
        setupWin.close()

    d = g.playAgain()