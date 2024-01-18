# Importando librería de Pygame.
import pygame
import random
import math
from pygame import mixer

pygame.init()

# Resolución de la ventana del videojuego.
screen_width = 800
screen_height = 600

size = (screen_width, screen_height)

# Definir el tamaño de la ventana con Pygame.
screen = pygame.display.set_mode(size)

# Agregando el fondo de pantalla.
background = pygame.image.load("galaxy-bg-3.png")

# Música de fondo.
mixer.music.load("SITB-Theme.wav")
mixer.music.play(-1)

bullet_sound = mixer.Sound("shoot-ship.wav")
bullet_sound.set_volume(0.5)

explosion_sound = mixer.Sound("hit-enemy.wav")
explosion_sound.set_volume(0.2)

# Definir el título de la ventana.
pygame.display.set_caption("Space Invaders: The Basics")

# Ícono de la ventana.
icon = pygame.image.load("ufo.png")

pygame.display.set_icon(icon)

# Balas.
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 2
bullet_state = "ready"

score = 0
score_text = pygame.font.Font("score_text.ttf", 32)
score_x = 10
score_y = 10

# Función del puntaje.
def show_score(x, y):
    text_score = score_text.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text_score, (x, y))

# Coordenadas del jugador.
player_x = 365
player_y = 480
player_img = pygame.image.load("space-ship.png")
player_x_change = 0

# Fuente para la pantalla de Game Over.
go_font = pygame.font.Font("score_text.ttf", 80)
go_x = 215
go_y = 250

# Lista de parámetros para múltiples enemigos.
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

number_enemies = 12

# Agregando al enemigo.
for item in range(number_enemies):
    enemy_img.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0, 730))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(1)
    enemy_y_change.append(30)

# Función para llamar al personaje en el Game Loop.
def player(x, y):
    screen.blit(player_img, (x, y))

# Función del enemigo.
def enemy(x, y):
    screen.blit(enemy_img[item], (x, y))

# Función de disparo de la nave.
def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Función de la colisión al disparar. 
def is_collision (enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)

    if distance < 27:
        return True
    else:
        return False

# Función de Game Over.
def game_over():
    go_text = go_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(go_text, (go_x, go_y))

# Game loop: para correr y retener el videojuego.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Movimiento al presionar la tecla izquierda.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.8
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("shoot-ship.wav")
                    bullet_sound.set_volume(0.15)
                    bullet_sound.play()
                    bullet_x = player_x
                fire (bullet_x, bullet_y)

# Movimiento al dejar de presionar la tecla izquierda.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

# Color del fondo de pantala.
    rgb = (41, 60, 94)
    screen.fill(rgb)

    screen.blit(background, (0, 0))

    player_x += player_x_change

# Límites de la nave en pantalla.
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

# Límites/generación del enemigo.
    for item in range(number_enemies):
        if enemy_y[item] > 445:
            for j in range(number_enemies):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[item] += enemy_x_change[item]

        if enemy_x[item] <= 0:
            enemy_x_change[item] = 0.65
            enemy_y[item] += enemy_y_change[item]
        
        elif enemy_x[item] >= 742:
            enemy_x_change[item] = -1
            enemy_y[item] += enemy_y_change[item]

# Colisiones de disparo hacia el enemigo.
        collision = is_collision(enemy_x[item], enemy_y[item], bullet_x, bullet_y)

        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            enemy_x[item] = random.randint(0, 735)
            enemy_y[item] = random.randint(50, 150)
            explosion_sound.play()
            explosion_sound.set_volume(0.25)
        
        enemy(enemy_x[item], enemy_y[item])

# Balas/disparo posicionamiento y llamado al Game Loop.
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    show_score(score_x, score_y)

    player(player_x, player_y)
    
    pygame.display.update()