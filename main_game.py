from random import randint
import pgzrun
import pygame
import os
#Homemade programs
from player import Player
from constants import C

TITLE = "THE DINOS are TAKING OVER THE WORLD"

os.environ['SDL_VIDEO_CENTERED'] = '1'

background = Actor("background1")



#Variables to do with the player
playerData = Player()
playerActor = Actor(playerData.getImage())


def draw():
    screen.clear()
    background.draw()
    playerActor.draw()
    
def update ():
    playerData.readKeyboard(keyboard)
    playerActor.x = playerData.x
    playerActor.y = playerData.y


pgzrun.go()
