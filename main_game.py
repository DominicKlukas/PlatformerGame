from random import randint
import pgzrun
import pygame
import os
#Homemade programs
from player import Player
from constants import C
from game_environment import *

TITLE = "THE DINOS are TAKING OVER THE WORLD. So we have to stop them (With nukes)."

os.environ['SDL_VIDEO_CENTERED'] = '1'

background = Actor("background1")

WIDTH = C.WIDTH
HEIGHT = C.HEIGHT


#Variables to do with the player
playerData = Player()
playerActor = Actor(playerData.getImage())


def draw():
    screen.clear()
    background.draw()
    playerActor.image = playerData.getImage()
    playerActor.draw()
    drawEnvironment(screen)
    
def update():
    playerData.readKeyboard(keyboard)
    playerData.update()
    playerData.floor = getGround(playerData.x, playerData.y)
    playerActor.midbottom = (playerData.x, playerData.y)

pgzrun.go()
