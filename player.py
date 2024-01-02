from constants import C

#This class contains all variables, images, and statistics related to the player

class Player:
    moveSpeed = 5
    def __init__(self):
        self.image = 'idle__000'
        self.x = C.WIDTH/2
        self.y = C.HEIGHT/2
        
    def getImage(self):#This method returns the current image of the 
        return self.image
    
    def readKeyboard(self, keyboard):
        if keyboard.D:
            self.x += 1