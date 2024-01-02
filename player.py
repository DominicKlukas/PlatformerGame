from constants import C

#This class contains all variables, images, and statistics related to the player

class Player:
    def __init__(self):
        self.image = 'idle__000'
        self.x = C.WIDTH/2
        self.y = C.HEIGHT/2
        self.moveSpeed = 5
        self.isAttacking = False
        self.facingLeft = False
        self.isJumping = False
        
    def getImage(self):#This method returns the current image of the 
        return self.image
    
    def readKeyboard(self, keyboard):
        if keyboard.D:
            self.x += self.moveSpeed
            self.facingLeft = False
        if keyboard.A:#
            self.x -= self.moveSpeed
            self.facingLeft = True
        if keyboard.V:
            self.isAttacking = True
        else:
            self.isAttacking = False

        
    
    def update(self):#
        self.image = 'idle__000'
        if self.isAttacking:
            self.image = 'attack__005'
        if self.facingLeft and self.image[-1:]!='l':#
            self.image += '_l'
