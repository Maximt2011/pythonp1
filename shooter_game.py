from pygame import *
from random import *
 

 
 
 
window = display.set_mode((700,500))
display.set_caption('Shooter')
 
clock = time.Clock()

init()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
 
 
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Rocket(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
 
class Ufo(GameSprite):
    def update(self):
        global lose, finish, bb
        speed = randint(1, 2)
        self.rect.y += speed
        if self.rect.y >= 450:
            lose += 1
            self.rect.y = randint(0, 50)
            self.rect.x = randint(50,650)
            if lose >= 3:
                finish = True
                
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill
def remove():
    global lose, finish, kills, win
    key_pressed = key.get_pressed()
    if key_pressed[K_e] and finish == True:
        finish = False
        lose = 0  
        win = 0


 
background = transform.scale(image.load('galaxy.jpg'), (700,500))
rocket = Rocket('rocket.png', 300, 350, 75, 100, 5)
ufo1 = Ufo('ufo.png', randint(10, 630), 50, 75, 50, 0)
ufo2 = Ufo('ufo.png', randint(10, 630), 50, 75, 50, 0)
ufo3 = Ufo('ufo.png', randint(10, 630), 50, 75, 50, 0)
ufo4 = Ufo('ufo.png', randint(10, 630), 50, 75, 50, 0)
ufo5 = Ufo('ufo.png', randint(10, 630), 50, 75, 50, 0)




kills = 0
font = font.SysFont('Arial', 30)
los = font.render('YOU LOSE!', True, (255, 215, 0))
lo = font.render('PRESS "E" TO RESTART', True, (255, 215, 0))
win = font.render('YOU WIN!', True, (255, 215, 0))
ufos = sprite.Group()
ufos.add(ufo1)
ufos.add(ufo2)
ufos.add(ufo3)
ufos.add(ufo4)
ufos.add(ufo5)

lose = 0
finish = False
bullets = sprite.Group()
game = True
while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullets.add(Bullet('bullet.png', rocket.rect.centerx-7, rocket.rect.top, 30, 15, 30)) 
    if sprite.groupcollide(bullets, ufos, True, True):
        kills += 1
        fire = mixer.Sound('fire.ogg')
    if len(ufos) <= 3:
        ufos.add(Ufo('ufo.png', randint(10, 630), 50, 75, 50, 0))
    
    if finish == True and lose >= 3:
      
        window.blit(los, (170, 200))
        window.blit(lo, (100, 250))
        remove()
    if finish == False:
        window.blit(background, (0,0))
        
        am = font.render('Счет:' + str(kills), True, (255, 255, 255))
        window.blit(am, (20, 10))
        m = font.render('Пропущенно:' + str(lose), True, (255, 255, 255))
        window.blit(m, (20, 50))
        rocket.paint()
        
        ufos.draw(window)
        bullets.draw(window)
        if kills >= 20:
            finish = True
            window.blit(win, (170, 200))
            window.blit(lo, (100, 250))
            remove()
        #moves
        rocket.move()
        
        ufos.update()
        bullets.update()


    display.update()
    clock.tick(60)