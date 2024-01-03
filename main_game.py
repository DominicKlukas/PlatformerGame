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
    if playerData.playerDead():
        screen.blit('black_mask75', (0, 0))
        screen.draw.text("Game Over", fontsize=72, color=(255, 0, 0), center=(C.WIDTH/2, C.HEIGHT/2))
   
def update():
    playerData.readKeyboard(keyboard)
    playerData.update()
    playerData.floor = getGround(playerData.x, playerData.y)
    playerActor.midbottom = (playerData.x, playerData.y)

pgzrun.go()
