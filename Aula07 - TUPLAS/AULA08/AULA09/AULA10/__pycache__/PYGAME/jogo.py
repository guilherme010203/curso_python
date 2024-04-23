import pygame
from pygame.locals import*
from sys import exit
from random import*

pygame.init()

altura = 480
largura = 640

#definindo posição de tamanho do objeto
pox_y_retangulo= altura/2
pox_x= largura/2
largura_retangulo = 30
altura_retangulo = 40

#definindo posição e tamanho do circulo
pos_y_circulo = 40
pos_x_circulo = 40
raio_circulo = 10

#definindo fontes
fonte = pygame.font.SysFont("arial",20, True,False)
pontos = 0

#criando janela
tela = pygame.display.set_mode((largura, altura))
#deifinir titulo da janela
pygame.display.set_caption("CRIANDO JOGOS")


#modificar a taxa de atualização de pixel por segundo
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0)) 
    mensagem = f"pontos:{pontos}"  
    textoFormatado = fonte.render(mensagem,True,(255,255,255))     
    #colocando eventos no pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       # if event.type == KEYDOWN:
       #     if event.key == K_UP:
        #        pox_y_retangulo -= 10
         #   if event.key == K_DOWN:
          #      pox_y_retangulo += 10             
           # if event.key ==K_LEFT:
            #    pox_x -= 10
         #   if event.key == K_RIGHT:
          #      pox_x += 10
          
    if pygame.key.get_pressed()[K_w]:
       pox_y_retangulo -= 10
    elif pygame.key.get_pressed()[K_a]:
         pox_x -= 10   
    elif pygame.key.get_pressed()[K_d]:
         pox_x += 10
    elif pygame.key.get_pressed()[K_s]:
         pox_y_retangulo += 10                 
                    
    retangulo = pygame.draw.rect(tela, (0,0,255), (pox_x, pox_y_retangulo,largura_retangulo, altura_retangulo))
    
    circulo = pygame.draw.circle(tela,(255,0,255), (pos_x_circulo, pos_y_circulo), raio_circulo )
    
    if retangulo.colliderect(circulo):
        pos_x_circulo = randint(40,600)
        pos_y_circulo = randint(50,430)
        pontos += 1
        
    tela.blit(textoFormatado, (400,40))    
        
    
    #atualizar o jogo a cada atualização
    pygame.display.update()        