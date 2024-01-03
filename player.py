from constants import C

#This class contains all variables, images, and statistics related to the player

class Player:
    def __init__(self):
        self.image = 'idle__000'
        self.runningImages = ['run__000', 'run__001', 'run__002', 'run__003', 'run__004', 'run__005', 'run__006', 'run__007', 'run__008', 'run__009']
        self.runningImageIndex = 0
        self.x = C.WIDTH/2
        self.y = C.HEIGHT/2
        self.floor = self.y
        self.moveSpeed = 5
        self.isAttacking = False
        self.facingLeft = False
        self.isJumping = False
        self.isSliding = False
        self.isGliding = False
        self.velocity_y = 0
        self.velocity_x = 0
        self.maxSpeed = 10
        self.accel = 1
        self.jumpPower = 20
        self.glidingSpeed = 2
        self.attackLength = 0
        
    def getImage(self):#This method returns the current image of the 
        return self.image
    
    def readKeyboard(self, keyboard):
        accelerating = False
        if keyboard.D:
            self.velocity_x += self.accel
            if self.velocity_x > self.maxSpeed:
                self.velocity_x = self.maxSpeed
            elif self.velocity_x < 0:
                self.velocity_x += 2*self.accel
            accelerating = True
        if keyboard.A:#
            self.velocity_x -= self.accel
            if self.velocity_x < -self.maxSpeed:
                self.velocity_x = -self.maxSpeed#
            elif self.velocity_x > 0:
                self.velocity_x -= 2*self.accel
            accelerating = True
        if keyboard.S:
            self.isSliding = True
        else:
            self.isSliding = False
        if keyboard.V and self.attackLength < 10:
            self.isAttacking = True
            self.attackLength += 1
        else:
            self.isAttacking = False
        if not keyboard.V:
            self.attackLength = 0
        if keyboard.SPACE and self.isJumping == False:
            self.isJumping = True
            self.velocity_y = -self.jumpPower
        
        if not accelerating:
            if self.velocity_x > 0:
                self.velocity_x -= self.accel
            elif self.velocity_x < 0:
                self.velocity_x += self.accel
        
    
    def update(self):#
        # this condition checks if you are on the ground
        if(self.y >= self.floor and self.velocity_y > 0):
            self.velocity_y = 0
            self.y = self.floor
            self.isJumping = False
        else:
            self.isJumping = True
        
        if self.x < 0 + 72/2:
            self.velocity_x = 0
            self.x = 0 + 72/2
        
        if self.x > C.WIDTH - 72/2:
            self.velocity_x = 0
            self.x = C.WIDTH - 72/2
        
        self.y += self.velocity_y
        self.velocity_y += C.GRAVITY
        
        self.x += self.velocity_x
        
        self.image = 'idle__000'
        
        
        if self.velocity_x != 0:
            self.image = self.runningImages[self.runningImageIndex]
            self.runningImageIndex += 1
            if self.runningImageIndex >= len(self.runningImages):
                self.runningImageIndex = 0
            if self.isSliding and not self.isJumping:
                self.image = 'slide__005'
        #
        if self.isJumping and self.isSliding and self.velocity_y > 0:
            self.image = 'glide__006'
            self.velocity_y = self.glidingSpeed
    
        if self.velocity_x > 0:
            self.facingLeft = False
        elif self.velocity_x < 0:
            self.facingLeft = True
        
        if self.isAttacking:
            self.image = 'attack__005'
        
        if self.facingLeft and self.image[-1:]!='l':#
            self.image += '_l'
