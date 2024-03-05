import pygame
import random
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cat_img = pygame.image.load("cat.png")
cat_rect = cat_img.get_rect()
cat_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
score = 0
f = pygame.font.Font("f.otf",32)
score_text = f.render(f"score:{score}", True, (0,255,0))
score_rect = score_text.get_rect()
score_rect.topleft = (0,0)

fish_image = pygame.image.load("fish.png")
fish_rect = fish_image.get_rect()
fish_rect.bottom = SCREEN_HEIGHT
fish_rect.centerx = SCREEN_WIDTH/2
FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.load("bg.wav")
pygame.mixer.music.play(-1)


catch_sound = pygame.mixer.Sound("catch.wav")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_UP]:
        cat_rect.y -= 5
    if keys[pygame.K_DOWN]    :
        cat_rect.y += 5
        
    if keys[pygame.K_LEFT]:
        cat_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        cat_rect.x += 5
     
    if cat_rect.colliderect(fish_rect):
        catch_sound.play()
        fish_rect.bottom = SCREEN_HEIGHT
        fish_rect.centerx = random.randint(0,SCREEN_WIDTH)
        
        
    fish_rect.y -= 5
    
    if fish_rect.top <= 0:
        fish_rect.bottom = SCREEN_HEIGHT
        fish_rect.centerx = random.randint(0,SCREEN_WIDTH)
        
    
    screen.fill((255,0,255))
    screen.blit(cat_img, cat_rect)
    screen.blit(fish_image, fish_rect)
    screen.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)