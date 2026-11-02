"""Funciones de dibujo estilo pixel art."""
import pygame
import config as c
from pixel_font import LETRAS, ANCHO_LETRA, ALTO_LETRA


def texto(sup, mensaje, x, y, color=c.BLANCO, grande=False, centrado=False):
    """Escribe con la fuente pixel propia y una sombra para que resalte."""
    tam = 3 if grande else 1  # tamaño de cada pixel de la letra
    mensaje = mensaje.upper()
    paso = (ANCHO_LETRA + 1) * tam  # ancho de letra + espacio
    ancho = len(mensaje) * paso - tam
    if centrado:
        x, y = x - ancho // 2, y - (ALTO_LETRA * tam) // 2
    # Primero la sombra desplazada, luego la letra encima
    for desfase, col in ((tam, c.SOMBRA), (0, color)):
        for i, letra in enumerate(mensaje):
            patron = LETRAS.get(letra, LETRAS[" "])
            for fila, linea in enumerate(patron):
                for columna, p in enumerate(linea):
                    if p == "#":
                        px = x + i * paso + columna * tam + desfase
                        py = y + fila * tam + desfase
                        pygame.draw.rect(sup, col, (px, py, tam, tam))


def dibujar_corazon(sup, x, y):
    for fila, linea in enumerate(c.CORAZON):
        for col, letra in enumerate(linea):
            if letra == "X":
                sup.set_at((x + col, y + fila), c.ROJO)


def dibujar_marcador(sup, puntos, vidas):
    texto(sup, f"PUNTOS {puntos}", 3, 3)
    for i in range(vidas):
        dibujar_corazon(sup, c.BASE_ANCHO - 10 - i * 9, 3)
    pygame.draw.line(sup, c.BLANCO, (0, c.ALTO_MARCADOR), (c.BASE_ANCHO, c.ALTO_MARCADOR))


def dibujar_bloque(sup, rect, color):
    """Bloque pixel art: bisel claro/oscuro y textura de puntos."""
    claro = tuple(min(255, v + 60) for v in color)
    oscuro = tuple(v // 2 for v in color)
    textura = tuple(int(v * 0.8) for v in color)
    l, t, r, b = rect.left, rect.top, rect.right - 1, rect.bottom - 1
    pygame.draw.rect(sup, color, rect)
    for x in range(l + 2, r - 1, 4):  # puntitos alternados
        sup.set_at((x, t + 2), textura)
        sup.set_at((x + 2, t + 3), textura)
    pygame.draw.line(sup, claro, (l, t), (r, t))    # brillo arriba
    pygame.draw.line(sup, claro, (l, t), (l, b))    # brillo izquierda
    pygame.draw.line(sup, oscuro, (l, b), (r, b))   # sombra abajo
    pygame.draw.line(sup, oscuro, (r, t), (r, b))   # sombra derecha


def dibujar_barra(sup, barra):
    r = barra.rect
    pygame.draw.rect(sup, c.BLANCO, r)
    for esquina in [(r.left, r.top), (r.right - 1, r.top),
                    (r.left, r.bottom - 1), (r.right - 1, r.bottom - 1)]:
        sup.set_at(esquina, c.FONDO)


def dibujar_pelota(sup, pelota):
    pygame.draw.rect(sup, c.BLANCO, pelota.rect)


def escalar(base, pantalla):
    """Agranda la imagen pequeña a la ventana sin suavizar los pixeles."""
    pygame.transform.scale(base, pantalla.get_size(), pantalla)