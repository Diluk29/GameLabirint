# Разработай свою игру в этом файле!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
       GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
       self.x_speed = player_x_speed
       self.y_speed = player_y_speed
    def update(self):
        if packman.rect.x <= width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if packman.rect.y <= height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update (self):
        if self.rect.x <= 540:
            self.side = 'right'
        if self.rect.x >= width - 75:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


barriers = sprite.Group()

width = 700
height = 500
packman = Player('Kot.png', 5, height - 80, 60, 60, 0, 0)
monster = Enemy('monster.png', width - 90,155 , 90, 90, 6)

wal = GameSprite('aa.png' , 80, 380, 200, 50)
wall = GameSprite('aa.png', 80, 120, 30, 400)

barriers.add(wal)
barriers.add(wall)

window = display.set_mode((width, height))
picture = transform.scale(image.load('Rock.png'), (width, height))
display.set_caption('лаберинт')
run = True
back = (255, 255, 255)
finish = False
while run:
    time.delay(50)
    
  
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0 
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0

    if not finish:
        window.fill(back)
        window.blit(picture,(0,0))
        packman.reset()
        packman.update()
        monster.reset()
        monster.update()
        barriers.draw(window)
        if sprite.collide_rect(packman, monster):
            finish = True
            img = image.load('game.png')
            window.blit(transform.scale(img,(width, height)),(0, 0))
    display.update()


