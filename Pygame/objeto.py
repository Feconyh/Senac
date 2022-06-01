import sys, pygame, random
from pygame.locals import *

'''
class Personagem():
    def __init__(self, posicaoX, posicaoY, radio):
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
        self.player =  pygame.draw.circle(screen, (0,0,0), (self.posicaoX,self.posicaoY),15)
'''

class jogo():
    playerpos = 3
    def __init__(self):
        pass
    
    def tela():
        global game
        screen = [1, 1, 1, 1, 1, 1]
        game = screen
        game[jogo.playerpos] = 8

    def move():
        global playerpos
        decision = int(input("1 para esquerda / 2 para direita : "))
        if decision == 1:
            jogo.playerpos -= 1
        else:
            jogo.playerpos += 1

while True:
    jogo.tela()
    print(game)
    jogo.move()
    
# screen = [1,1,1,1,1,1]
# game = screen
# playerpos = 3
# while True:
#     screen = [1, 1, 1, 1, 1, 1]
#     game = screen
#     game[playerpos] = 8
#     print(game)
#     decision = int(input("1 para esquerda / 2 para direita : "))
#     if decision == 1:
#         playerpos -= 1
#     else:
#         playerpos +=1
