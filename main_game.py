from random import randint
import pgzrun
import pygame
import os
#Homemade programs
from player import Player
from dino import Dino
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


dinoData = Dino()
dinoActor = Actor(dinoData.getImage())


def draw():
    screen.clear()
    background.draw()
    playerActor.image = playerData.getImage()
    playerActor.draw()

    dinoActor.image = dinoData.getImage()
    dinoActor.draw()
    drawEnvironment(screen)
    if playerData.playerDead():
        screen.blit('black_mask75', (0, 0))
        screen.draw.text("Game Over", fontsize=72, color=(255, 0, 0), center=(C.WIDTH/2, C.HEIGHT/2))

   
def update():
    playerData.readKeyboard(keyboard)
    playerData.update()
    dinoData.update()
    dinoData.moveDino(playerData.x, playerData.y)
    playerData.floor = getGround(playerData.x, playerData.y)
    dinoData.floor = getGround(dinoData.x, dinoData.y)
    dinoActor.midbottom = (dinoData.x, dinoData.y)
    playerActor.midbottom = (playerData.x, playerData.y)

    if playerActor.colliderect(dinoActor):
        playerData.killPlayer()

pgzrun.go()
