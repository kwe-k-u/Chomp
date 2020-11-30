import  PySimpleGUI as sg
import Gameplay as gp
import pygame
from pygame import mixer


def playerTurn():
        if g.currentPlayer.getName() != "AI":
            event, values = setupWin.read()
        else:
            event, values = setupWin.read(timeout =900)
            event = g.currentPlayer.checkMoves(g)
        setupWin.close()
        return event, values

pygame.init()

g = gp.GamePlay()
g.loading()
mixer.music.load("background.wav")
mixer.music.play(-1)

g.gameSetup()
setupWin = sg.Window("CHOMP", g.updateBoard())
event, value = playerTurn()

while event != (1, 1):
    g.loading()
    g.getPlay(event)
    setupWin = sg.Window("CHOMP", g.updateBoard())
    event, value = playerTurn()

d = g.playAgain()

while d and event != (1,1):
    g.loading()
    g.gameSetup()
    setupWin = sg.Window("CHOMP", g.updateBoard())
    event, value = playerTurn()

    while event != (1, 1):
        g.loading()
        g.getPlay(event)
        setupWin = sg.Window("CHOMP", g.updateBoard())

        event, value = playerTurn()

    d = g.playAgain()


