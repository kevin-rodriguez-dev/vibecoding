"""Configuración general del juego: tamaños, colores y tiempos."""

# Resolución interna pequeña que se agranda para verse pixel art
BASE_ANCHO, BASE_ALTO = 200, 150
ESCALA = 4
ANCHO, ALTO = BASE_ANCHO * ESCALA, BASE_ALTO * ESCALA
FPS = 60

# Colores
FONDO = (12, 20, 16)  # fondo oscuro verdoso
SOMBRA = (0, 0, 0)    # sombra del texto
COLORES_FILAS = [(170, 230, 90), (130, 210, 70), (90, 190, 60), (60, 165, 60), (40, 140, 60)]
BLANCO = (255, 255, 255)
ROJO = (230, 40, 60)
AMARILLO = (255, 220, 0)

# Marcador (franja de arriba)
ALTO_MARCADOR = 12

# Bloques
FILAS, COLUMNAS = 5, 10
BLOQUE_ANCHO, BLOQUE_ALTO = 18, 6
BLOQUE_SEP_X, BLOQUE_SEP_Y = 20, 8
BLOQUES_Y = 18  # altura donde empieza la primera fila

# Barra y pelota
BARRA_ANCHO, BARRA_ALTO = 28, 4
PELOTA_TAM = 3
VEL_INICIAL = (1.0, -1.5)
VEL_MAX_X = 2.0
AUMENTO_VELOCIDAD = 0.25

# Reglas
VIDAS_INICIALES = 3
TIEMPO_PARPADEO = 1500  # milisegundos

# Corazón en pixel art: cada "X" es un pixel
CORAZON = [
    " XX XX ",
    "XXXXXXX",
    "XXXXXXX",
    " XXXXX ",
    "  XXX  ",
    "   X   ",
]