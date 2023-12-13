import pygame
from time import sleep
from random import randint

pygame.init()
#VARIÁVEIS
x_bola = randint(450, 650)
y_bola = randint(200, 450)
y_barrad = 300
y_barrae = 300
vel_barras = 5
vel_bola = 5
a = randint(0, 1)                #movimentação no eixo y
b = randint(0, 1)                #movimentação no eixo x
c = 0
timer = 0
vivo = 0
morte_e = 0
morte_d = 0
bateu_esquerda = 0
bateu_direita = 0

#DOWNLOAD DAS IMAGENS
bola = pygame.image.load('bola.png')
barra = pygame.image.load('barra.png')             #30x130
canto = pygame.image.load('canto.png')
barra_lateral = pygame.image.load('barra_lateral.png')
fonte = pygame.font.SysFont('arial black', 80)
fonte2 = pygame.font.SysFont('arial black', 120)
fonte3 = pygame.font.SysFont('arial black', 40)
game_over = fonte2.render('GAME OVER', True, (255, 0, 0), (0, 0, 0))
vencedor_esquerda = fonte3.render('O jogador da esquerda ganhou!', True, (255, 0, 0), (0, 0, 0))
vencedor_direita = fonte3.render('O jogador da direita ganhou!', True, (255, 0, 0), (0, 0, 0))
pos_vencedor = vencedor_direita.get_rect()
pos_vencedor.center = (600, 400)
tempo = fonte.render('Tempo: ', True, (255, 255, 255), (0, 0, 0))
pos_texto = tempo.get_rect()
pos_texto.center = (580, 300)
pos_placar = tempo.get_rect()
pos_placar.center = (685, 100)
pos_go = game_over.get_rect()
pos_go.center = (600, 150)
modos_de_jogo = pygame.image.load('modos_de_jogo.png')
mdj1 = pygame.image.load('1.png')
mdj2 = pygame.image.load('2.png')
mdj3 = pygame.image.load('3.png')

janela = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Jogo')
janela_aberta = True
mdj = fundo = 0
while janela_aberta:                                         #tela para escolher o modo de jogo e a cor das barras
    pygame.time.delay(10)
    for event in pygame.event.get():
        comandos = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            janela_aberta = False
    if mdj != 0 and fundo != 0:
        sleep(1)
        janela_aberta = False
    janela.blit(modos_de_jogo, (0, 0))
    if comandos[pygame.K_1]:
        janela.blit(mdj1, (0, 0))
        mdj = 1
    if comandos[pygame.K_2]:
        janela.blit(mdj2, (0, 0))
        mdj = 2
    if comandos[pygame.K_3]:
        janela.blit(mdj3, (0, 0))
        mdj = 3
    if comandos[pygame.K_4]:
        fundo = pygame.image.load('fundo.png')
    if comandos[pygame.K_5]:
        fundo = pygame.image.load('campo.png')
    if comandos[pygame.K_6]:
        fundo = pygame.image.load('quadra.png')
    pygame.display.update()

janela_aberta = True
if mdj == 1:                                                   #1º modo de jogo
    while janela_aberta:
        pygame.time.delay(10)
        for event in pygame.event.get():
            comandos = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            janela_aberta = False
        if comandos[pygame.K_w] and 30 <= y_barrae:
            y_barrae -= vel_barras
        if comandos[pygame.K_s] and y_barrae <= 530:
            y_barrae += vel_barras
        if comandos[pygame.K_UP] and 30 <= y_barrad:
            y_barrad -= vel_barras
        if comandos[pygame.K_DOWN] and y_barrad <= 530:
            y_barrad += vel_barras

        # LÓGICA DO JOGO
        if x_bola <= 10:
            vel_bola = 0
            vivo = 1  # vivo = 1 significa que o jogador da esquerda perdeu
        if x_bola >= 1140:
            vel_bola = 0
            vivo = 2  # vivo = 2 significa que o jogador da direita perdeu

        # TIMER
        if vivo == 0:
            timer += 1
            tempo_segundo = timer / 50
            tempo = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 255, 255), (0, 0, 0))
            tempo2 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (0, 0, 255), (0, 0, 0))
            tempo3 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (0, 255, 0), (0, 0, 0))
            tempo4 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 0, 0), (0, 0, 0))

        # MOVIMENTAÇÃO DA BOLA E COLISÃO
        # eixo y
        if y_bola <= 20:
            a = 1
        if y_bola >= 620:
            a = 0
        if a == 0:
            y_bola -= vel_bola
        if a == 1:
            y_bola += vel_bola
        # eixo x
        if x_bola <= 10 or (x_bola <= 52 and y_barrae - 25 <= y_bola <= y_barrae + 120):  # 30x130
            b = 0
        if x_bola >= 1140 or (x_bola >= 1100 and y_barrad - 25 <= y_bola <= y_barrad + 120):
            b = 1
        if b == 0:
            x_bola += vel_bola
        if b == 1:
            x_bola -= vel_bola
        if tempo_segundo == 10:
            vel_bola += 3
            vel_barras += 2
        if tempo_segundo == 20:
            vel_bola += 2
            vel_barras += 1
        if tempo_segundo == 30:
            vel_bola += 5
            vel_barras += 3

        # FAZER AS COISAS APARECEREM NA TELA
        janela.blit(fundo, (0, 0))
        janela.blit(barra, (20, y_barrae))
        janela.blit(barra, (1150, y_barrad))
        janela.blit(barra_lateral, (-10, 0))
        janela.blit(barra_lateral, (1190, 0))
        janela.blit(canto, (0, -15))
        janela.blit(canto, (0, 680))
        if vivo == 0:
            if tempo_segundo < 10:
                janela.blit(tempo, pos_texto)
            if 10 <= tempo_segundo <= 20:
                janela.blit(tempo2, pos_texto)
            if 20 < tempo_segundo <= 30:
                janela.blit(tempo3, pos_texto)
            if tempo_segundo > 30:
                janela.blit(tempo4, pos_texto)
        janela.blit(bola, (x_bola, y_bola))

        if vivo == 1 or vivo == 2:  # Mostrar que o jogador perdeu
            janela.blit(game_over, pos_go)
            tempo_final = fonte3.render(f'Tempo final: {tempo_segundo:.1f} segundos', True, (255, 0, 0), (0, 0, 0))
            janela.blit(tempo_final, (300, 250))
            if vivo == 1:
                janela.blit(vencedor_direita, pos_vencedor)
            if vivo == 2:
                janela.blit(vencedor_esquerda, pos_vencedor)

        pygame.display.update()

    pygame.quit()

if mdj == 2:                        #2º modo de jogo
    vel_bola = 7
    while janela_aberta:
        pygame.time.delay(10)
        for event in pygame.event.get():
            comandos = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            janela_aberta = False
        if comandos[pygame.K_w] and 30 <= y_barrae:
            y_barrae -= vel_barras
        if comandos[pygame.K_s] and y_barrae <= 530:
            y_barrae += vel_barras
        if comandos[pygame.K_UP] and 30 <= y_barrad:
            y_barrad -= vel_barras
        if comandos[pygame.K_DOWN] and y_barrad <= 530:
            y_barrad += vel_barras

        # LÓGICA DO JOGO
        if x_bola <= 10 and morte_e < 5:
            morte_e += 1  # O jogador da esquerda perdeu
        if x_bola >= 1140 and morte_d < 5:
            morte_d += 1  #O jogador da direita perdeu
        placar = fonte.render(f'{morte_d}X{morte_e}', True, (255, 255, 255), (0, 0, 0))
        if morte_e == 5 or morte_d == 5:
            vel_bola = 0

        # TIMER
        if morte_d < 5 and morte_e < 5:
            timer += 1
            tempo_segundo = timer / 50
            tempo = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 255, 255), (0, 0, 0))
            tempo2 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (0, 0, 255), (0, 0, 0))
            tempo3 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (0, 255, 0), (0, 0, 0))
            tempo4 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 0, 0), (0, 0, 0))

        # MOVIMENTAÇÃO DA BOLA E COLISÃO
        # eixo y
        if y_bola <= 20:
            a = 1
        if y_bola >= 620:
            a = 0
        if a == 0:
            y_bola -= vel_bola
        if a == 1:
            y_bola += vel_bola
        # eixo x
        if x_bola <= 10 or (x_bola <= 52 and y_barrae - 25 <= y_bola <= y_barrae + 120):  # 30x130
            b = 0
        if x_bola >= 1140 or (x_bola >= 1100 and y_barrad - 25 <= y_bola <= y_barrad + 120):
            b = 1
        if b == 0:
            x_bola += vel_bola
        if b == 1:
            x_bola -= vel_bola
        if tempo_segundo == 10:
            vel_bola += 3
            vel_barras += 2
        if tempo_segundo == 20:
            vel_bola += 2
            vel_barras += 1
        if tempo_segundo == 30:
            vel_bola += 5
            vel_barras += 3

        # FAZER AS COISAS APARECEREM NA TELA
        janela.blit(fundo, (0, 0))
        janela.blit(barra, (20, y_barrae))
        janela.blit(barra, (1150, y_barrad))
        janela.blit(barra_lateral, (-10, 0))
        janela.blit(barra_lateral, (1190, 0))
        janela.blit(canto, (0, -15))
        janela.blit(canto, (0, 680))
        if morte_e < 5 and morte_d < 5:
            if tempo_segundo < 10:
                janela.blit(tempo, pos_texto)
            if 10 <= tempo_segundo <= 20:
                janela.blit(tempo2, pos_texto)
            if 20 < tempo_segundo <= 30:
                janela.blit(tempo3, pos_texto)
            if tempo_segundo > 30:
                janela.blit(tempo4, pos_texto)
        janela.blit(placar, pos_placar)
        janela.blit(bola, (x_bola, y_bola))

        if morte_e == 5 or morte_d == 5:  # Mostrar que o jogador perdeu
            janela.blit(fonte2.render('FIM DE JOGO', True, (255, 0, 0), (0, 0, 0)), pos_go)
            tempo_final = fonte3.render(f'Tempo final: {tempo_segundo:.1f} segundos', True, (255, 0, 0), (0, 0, 0))
            janela.blit(tempo_final, (300, 250))
            if morte_e == 5:
                janela.blit(vencedor_direita, pos_vencedor)
            if morte_d == 5:
                janela.blit(vencedor_esquerda, pos_vencedor)

        pygame.display.update()

    pygame.quit()

if mdj == 3:                                         #3º modo de jogo
    while janela_aberta:
        pygame.time.delay(10)
        for event in pygame.event.get():
            comandos = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            janela_aberta = False
        if comandos[pygame.K_w] and 30 <= y_barrae:
            y_barrae -= vel_barras
        if comandos[pygame.K_s] and y_barrae <= 530:
            y_barrae += vel_barras
        if comandos[pygame.K_UP] and 30 <= y_barrad:
            y_barrad -= vel_barras
        if comandos[pygame.K_DOWN] and y_barrad <= 530:
            y_barrad += vel_barras

        # LÓGICA DO JOGO
        if x_bola <= 10:
            vel_bola = 0
            vivo = 1  # vivo = 1 significa que o jogador perdeu
        if x_bola >= 1140:
            vel_bola = 0
            vivo = 1

        # TIMER
        if vivo == 0:
            timer += 1
            tempo_segundo = timer / 50
            tempo = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 255, 255), (0, 0, 0))
            tempo2 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (0, 0, 255), (0, 0, 0))
            tempo3 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (0, 255, 0), (0, 0, 0))
            tempo4 = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 0, 0), (0, 0, 0))

        # MOVIMENTAÇÃO DA BOLA E COLISÃO
        # eixo y
        if y_bola <= 20:
            a = 1
        if y_bola >= 620:
            a = 0
        if a == 0:
            y_bola -= vel_bola
        if a == 1:
            y_bola += vel_bola
        # eixo x
        if x_bola <= 10 or (x_bola <= 52 and y_barrae - 25 <= y_bola <= y_barrae + 120):  # 30x130
            b = 0
        if x_bola >= 1140 or (x_bola >= 1100 and y_barrad - 25 <= y_bola <= y_barrad + 120):
            b = 1
        if b == 0:
            x_bola += vel_bola
        if b == 1:
            x_bola -= vel_bola
        if tempo_segundo == 10:
            vel_bola += 3
            vel_barras += 2
        if tempo_segundo == 20:
            vel_bola += 2
            vel_barras += 1
        if tempo_segundo == 30:
            vel_bola += 5
            vel_barras += 3

        # FAZER AS COISAS APARECEREM NA TELA
        janela.blit(fundo, (0, 0))
        janela.blit(barra, (20, y_barrae))
        janela.blit(barra, (1150, y_barrad))
        janela.blit(barra_lateral, (-10, 0))
        janela.blit(barra_lateral, (1190, 0))
        janela.blit(canto, (0, -15))
        janela.blit(canto, (0, 680))
        if vivo == 0:
            if tempo_segundo < 10:
                janela.blit(tempo, pos_texto)
            if 10 <= tempo_segundo <= 20:
                janela.blit(tempo2, pos_texto)
            if 20 < tempo_segundo <= 30:
                janela.blit(tempo3, pos_texto)
            if tempo_segundo > 30:
                janela.blit(tempo4, pos_texto)
        janela.blit(bola, (x_bola, y_bola))

        if vivo == 1:
            janela.blit(game_over, pos_go)
            tempo_final = fonte3.render(f'Tempo final: {tempo_segundo:.1f} segundos', True, (255, 0, 0), (0, 0, 0))
            janela.blit(tempo_final, (300, 250))

        pygame.display.update()

    pygame.quit()