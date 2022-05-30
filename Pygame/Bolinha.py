import sys, pygame, random
from pygame.locals import *

pygame.init()

px = 300
py = 500

ex = random.randint(45,450)
ey = random.randint(45,300)

ex2 = random.randint(45,450)
ey2 = random.randint(45,300)

SPEED = 0
size = (600,600)
screen = pygame.display.set_mode((size))

pygame.display.set_caption('😃👍')

music = pygame.mixer.music.load('sons/BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

song = pygame.mixer.Sound('sons/smw_coin.wav')
song.set_volume(1)

carangueijo = pygame.image.load('imagens/pixil-frame-0.png')
carangueijo_imagem = carangueijo.get_rect()

font = pygame.font.SysFont('arial', 30, True, True)
score = 0

clock = pygame.time.Clock()
FPS = 60

while True:
    clock.tick(FPS)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    ey += SPEED
    ey2 += SPEED
    
    if pygame.key.get_pressed()[K_a] and px >= 40:
        px += -10
    if pygame.key.get_pressed()[K_d] and px <= 560:
        px += 10
    if pygame.key.get_pressed()[K_w] and py >= 40:
        py -= 10
    if pygame.key.get_pressed()[K_s] and py <= 565:
        py += 10
    if pygame.key.get_pressed()[K_t]:
        pygame.quit()
        exit()

    player = pygame.draw.circle(screen, (0,0,0), (px,py),15)
    inimigo = pygame.draw.circle(screen, (255,255,255), (ex,ey),5)
    inimigo2 = pygame.draw.circle(screen, (255,255,255), (ex2,ey2),5)

    carangueijo_imagem.midtop = px,py-50
    screen.blit(carangueijo,carangueijo_imagem)

    if player.colliderect(inimigo):
        ex = random.randint(45,450)
        ey = random.randint(45,300)
        score += 1
        SPEED += 0.4
        song.play()

    if player.colliderect(inimigo2): 
        ex2 = random.randint(45,450)
        ey2 = random.randint(45,300)
        score += 1
        SPEED += 0.4
        song.play()

    score_font = font.render(f'Pontos: {score}', True, (255,255,255))
    screen.blit(score_font, (10, 10))

    #Top
    pygame.draw.line(screen, (255,255,0), (0,0), (600,0), 5)
    #Left
    pygame.draw.line(screen, (255,255,0), (0,0), (0,600), 5)
    #Right
    pygame.draw.line(screen, (255,255,0), (600,600), (600,0), 5)
    #Down
    pygame.draw.line(screen, (255,255,0), (600,600), (0,600), 5)
    
    pygame.display.update() 

    if ey >= 602.5 and ey2 >= 602.5:
        game_over_screen = font.render('Game Over', True, (255,0,0))
        game_over = game_over_screen.get_rect()
        game_over.midtop = (300,300)
        screen.blit(game_over_screen, game_over)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if pygame.key.get_pressed()[K_t]:
                    pygame.quit()
                    exit()
