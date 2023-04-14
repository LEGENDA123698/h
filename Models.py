from pygame import*

WZ=(700,500)
FPS = 60
pl_size = (80,80)
BZ = (50,50)
window = display.set_mode(WZ)
class Gamesprite(sprite.Sprite):
    def __init__(self, image_name, speed, size, pos_x, pos_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(Gamesprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WZ[1] - pl_size[1]:
            self.rect.y += self.speed
 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WZ[1] - pl_size[1]:
            self.rect.y += self.speed