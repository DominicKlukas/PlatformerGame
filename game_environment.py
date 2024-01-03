from constants import C

grassblockHeight = 70
grassblockWidth = 71

grassblockY = C.HEIGHT - grassblockHeight

platformY = [100, 200, 300]
platformX = [100, 800, 500]
platformWidth = [3, 3, 3]

def drawEnvironment(screen):
    for x in range(int(C.WIDTH/grassblockWidth)+1):
        screen.blit('grassblock', (x*grassblockWidth, grassblockY))#
    
    for y in range(3):
        for x in range(platformWidth[y]):
            screen.blit('grassblock', (platformX[y] + x*grassblockWidth, platformY[y]))


def getGround(x, y):##
    for i in range(3):
        if y <= platformY[i]+grassblockHeight/2:
            if x > platformX[i] - C.PLAYERWIDTH/4 and x < platformX[i] + platformWidth[i]*grassblockWidth + C.PLAYERWIDTH/4:
                return platformY[i]
    return grassblockY