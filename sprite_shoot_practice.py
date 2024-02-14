import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("laser_shot.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path,pos_x,pos_y, scale_factor):
        super().__init__()
        original_target = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(original_target,(int(original_target.get_width() * scale_factor),int(original_target.get_height() * scale_factor)))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]


#PyGame Setup
pygame.init()
clock = pygame.time.Clock()

#Window Setup
logo = pygame.image.load("gatoironico.jpeg")
pygame.display.set_icon(logo)
pygame.display.set_caption("test")

#Game Screen
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("night_city.png")
pygame.mouse.set_visible(False)

#Scaling bg
originalbg_widht, originalbg_height = background.get_size()
scaledbg = pygame.transform.scale(background, (screen_width,screen_height))

#Crosshair
crosshair = Crosshair("erina_sprite.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("apple.png",random.randrange(0,screen_width),random.randrange(0,screen_height),0.2)
    target_group.add(new_target)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(scaledbg,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)

