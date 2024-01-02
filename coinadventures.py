from random import randint
import pgzrun
import pygame
import os
WIDTH = 900
HEIGHT = 360
TITLE = "Coin Adventures"

os.environ['SDL_VIDEO_CENTERED'] = '1'

background = Actor("background_grass")



#Variables to do with the player
player = Actor("idle__000")
run_images = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
player.x = WIDTH/2
player.y = HEIGHT/2
player.score = 0
playerSpeed = 5
facing_left = False


#Variables to do with the Dino
Dino = Actor('idle1')
Dinorun = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'run7', 'run8']
DinoSpawns = 3
DinoSpeed = 5
Dino.x =  randint(0, WIDTH)
Dino.y =  randint(0, HEIGHT)
DinoMovingLeft = False

#Variables to do with the coin
coin=Actor("coin")
coin.x = randint(0, WIDTH)
coin.y = randint(0, HEIGHT)


def startGame():
    #Variables to do with the player
    player.image = "idle__000"
    player.x = WIDTH/2
    player.y = HEIGHT/2
    player.score = 0
    playerSpeed = 5


    #Variables to do with the Dino
    Dino.image = 'idle1'
    DinoSpeed = 5
    Dino.x = randint(0, WIDTH)
    Dino.y = randint(0, HEIGHT)

    #Variables to do with the coin
    coin.x = randint(0, WIDTH)
    coin.y = randint(0, HEIGHT)

def draw():
    screen.clear()
    background.draw()
    player.draw()
    coin.draw()
    screen.draw.text(f"Punkte: {player.score}", (10, 10))
    if player.score >= DinoSpawns:
        Dino.draw()
    if player.image == 'dead__009':
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2),fontsize=69, color=(255, 0, 0))
        screen.draw.text("Press R to play again", fontsize=32, center=(WIDTH/2, HEIGHT/2 + 32))
    
def update ():
    #player.next_image()
    global facing_left
    if player.image == 'dead__009':
        if keyboard.R:
            startGame()
        return
    DinoMovingLeft = checkIfMovingLeft(Dino)
    player_moved = False
    if keyboard.D:
        player.x += playerSpeed
        player_moved = True
        facing_left = False
    if keyboard.A:
        player.x -= playerSpeed
        player_moved = True
        facing_left = True
    if keyboard.W:
        player.y -= playerSpeed
        player_moved = True
    if keyboard.S:
        player.y += playerSpeed
        player_moved = True
    if keyboard.up:
        player.y -= playerSpeed
        player_moved = True
    if keyboard.down:
        player.y += playerSpeed
        player_moved = True
    if keyboard.right:
        player.x += playerSpeed
        player_moved = True
        facing_left = False
    if keyboard.left:
        player.x -= playerSpeed
        player_moved = True
        facing_left = True
    
    runAnimation(player, player_moved, run_images, facing_left)
    
    if DinoSpawns <= player.score:
        epsilon = 2
        if player.x < Dino.x - epsilon:
            Dino.x -= DinoSpeed
            DinoMovingLeft = True
        elif player.x > Dino.x + epsilon:
            Dino.x += DinoSpeed
            DinoMovingLeft = False
        if player.y < Dino.y:
            Dino.y -= DinoSpeed
        elif player.y > Dino.y:
            Dino.y += DinoSpeed
        runAnimation(Dino, True, Dinorun, DinoMovingLeft)
        
    offScreen(player)
    offScreen(Dino)
        
    if player.score >= DinoSpawns:
        if player.colliderect(Dino):
            player.image = 'dead__009'
        
    if player.colliderect(coin):
        coin.x = randint(0, WIDTH)
        coin.y = randint(0, HEIGHT)
        player.score += 1

def runAnimation(thing, thingMoved, images, directionLeft):
    if thing.image[-1:] == 'l':
        thing.image = thing.image[:-2]
    if thingMoved:
        if thing.image == images[len(images)-1]:
            thing.image = images[0]
        elif thing.image[:4] == 'idle':
            thing.image = images[0]
        else:
            current_image = thing.image
            image_name_length = len(current_image)
            thing.image = current_image[:-1] + str((int(current_image[-1:])+1))
    else:
        thing.image = "idle__000"
    if directionLeft:
        thing.image = thing.image + '_l'
        
def offScreen(thing):
    if thing.x < 0:
        thing.x = WIDTH
    if thing.x > WIDTH:
        thing.x = 0
    if thing.y < 0:
        thing.y = HEIGHT
    if thing.y > HEIGHT:
        thing.y = 0

def checkIfMovingLeft(thing):
    if thing.image[:4] != 'idle' and thing.image[-1:] == 'l':
        return True
    return False

pgzrun.go()