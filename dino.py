from constants import C


class Dino:
    def __init__(self):
        self.image = "idle1"
        self.velocity_y = 0
        self.velocity_x = 0
        self.y = C.HEIGHT - 70
        self.x = 0
        self.floor = self.y
        self.isJumping = False
        self.jumpPower = 25
        self.accel = 1


    def getImage(self):
        return self.image

    def moveDino(self, targetX, targetY):
        if targetX < self.x:
            self.velocity_x -= self.accel
        elif targetX > self.x:
            self.velocity_x += self.accel
        elif targetY < self.y and not self.isJumping:
            self.velocity_y = -self.jumpPower
            self.isJumping = True


    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_y += C.GRAVITY
        if(self.y >= self.floor and self.velocity_y > 0):
            self.velocity_y = 0
            self.y = self.floor
