import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animación de Movimiento en 4 Direcciones")

# Cargar el fondo
background = pygame.image.load("fondo.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajustar el fondo al tamaño de la pantalla

# Cargar los sprites en una lista
sprite_images = [
    pygame.image.load("Walk1.png"),
    pygame.image.load("Walk2.png"),
    pygame.image.load("Walk3.png"),
    pygame.image.load("Walk4.png"),
    pygame.image.load("Walk5.png"),
    pygame.image.load("Walk6.png"),
    pygame.image.load("Walk7.png"),
    pygame.image.load("Walk8.png")
]

# Configuración inicial
x, y = 50, 310  # Posición inicial del personaje
velocidad_x, velocidad_y = 0, 0  # Velocidad de movimiento inicial (detenido)
current_sprite = 0  # Índice de sprite actual
sprite_cambio_velocidad = 0.2  # Velocidad de cambio de sprite
direccion_derecha = True  # Dirección inicial (mirando a la derecha)

# Bucle principal del juego
clock = pygame.time.Clock()  # Reloj para controlar FPS

while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Detectar teclas presionadas
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:  # Flecha derecha
        velocidad_x = 3
        velocidad_y = 0
        direccion_derecha = True  # Mirar hacia la derecha
    elif keys[pygame.K_LEFT]:  # Flecha izquierda
        velocidad_x = -3
        velocidad_y = 0
        direccion_derecha = False  # Mirar hacia la izquierda
    elif keys[pygame.K_UP]:  # Flecha arriba
        velocidad_y = -3
        velocidad_x = 0
    elif keys[pygame.K_DOWN]:  # Flecha abajo
        velocidad_y = 3
        velocidad_x = 0
    else:
        velocidad_x = 0  # Detenerse si no se presiona ninguna tecla
        velocidad_y = 0

    # Actualizar posición del personaje
    x += velocidad_x
    y += velocidad_y

    # Mantener al personaje dentro de los bordes de la pantalla
    if x > WIDTH - 50:
        x = WIDTH - 50
    elif x < 0:
        x = 0
    if y > HEIGHT - 50:
        y = HEIGHT - 50
    elif y < 0:
        y = 0

    # Actualizar el sprite actual para la animación
    if velocidad_x != 0 or velocidad_y != 0:  # Cambiar el sprite solo si el personaje se está moviendo
        current_sprite += sprite_cambio_velocidad
        if current_sprite >= len(sprite_images):
            current_sprite = 0  # Volver al primer sprite al final de la secuencia

    # Dibujar el fondo
    screen.blit(background, (0, 0))  # Dibujar el fondo en la pantalla

    # Seleccionar el sprite actual y voltearlo si es necesario
    sprite = sprite_images[int(current_sprite)]
    if not direccion_derecha:
        sprite = pygame.transform.flip(sprite, True, False)  # Voltear horizontalmente si va hacia la izquierda

    # Dibujar el sprite del personaje en la pantalla
    screen.blit(sprite, (x, y))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)  # Controlar los FPS (60 FPS)
