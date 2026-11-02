"""Objetos del juego: barra, pelota y bloques."""
import pygame
import config as c


class Barra:
    def __init__(self):
        self.rect = pygame.Rect(0, c.BASE_ALTO - 8, c.BARRA_ANCHO, c.BARRA_ALTO)
        self.rect.centerx = c.BASE_ANCHO // 2

    def seguir(self, x):
        """Centra la barra en x sin salirse de la pantalla."""
        self.rect.centerx = x
        self.rect.clamp_ip(pygame.Rect(0, 0, c.BASE_ANCHO, c.BASE_ALTO))


class Pelota:
    def __init__(self):
        # Posición y velocidad con decimales para que se mueva suave
        self.x = self.y = 0.0
        self.vx = self.vy = 0.0

    @property
    def rect(self):
        """Rectángulo actual de la pelota (para detectar choques)."""
        return pygame.Rect(round(self.x), round(self.y), c.PELOTA_TAM, c.PELOTA_TAM)

    def pegar_a(self, barra):
        """Deja la pelota quieta encima del centro de la barra."""
        self.x = barra.rect.centerx - c.PELOTA_TAM / 2
        self.y = barra.rect.top - c.PELOTA_TAM
        self.vx = self.vy = 0.0

    def lanzar(self):
        self.vx, self.vy = c.VEL_INICIAL

    def mover(self):
        """Mueve la pelota y la hace rebotar en las paredes."""
        self.x += self.vx
        self.y += self.vy
        if self.x <= 0:
            self.x, self.vx = 0, abs(self.vx)
        if self.x + c.PELOTA_TAM >= c.BASE_ANCHO:
            self.x, self.vx = c.BASE_ANCHO - c.PELOTA_TAM, -abs(self.vx)
        if self.y <= c.ALTO_MARCADOR + 1:
            self.y, self.vy = c.ALTO_MARCADOR + 1, abs(self.vy)

    def rebotar_en_barra(self, barra):
        """Rebota con un ángulo que depende de dónde pega en la barra."""
        if self.vy > 0 and self.rect.colliderect(barra.rect):
            self.vy = -abs(self.vy)
            desplazamiento = (self.rect.centerx - barra.rect.centerx) / (barra.rect.width / 2)
            self.vx = desplazamiento * c.VEL_MAX_X
            if abs(self.vx) < 0.3:  # evita que suba totalmente recta
                self.vx = 0.3 if self.vx >= 0 else -0.3

    def acelerar(self):
        self.vy += c.AUMENTO_VELOCIDAD if self.vy > 0 else -c.AUMENTO_VELOCIDAD

    def se_cayo(self):
        return self.y > c.BASE_ALTO


def crear_bloques():
    """Devuelve una lista de (rectángulo, color) para cada bloque."""
    bloques = []
    for fila in range(c.FILAS):
        for col in range(c.COLUMNAS):
            rect = pygame.Rect(col * c.BLOQUE_SEP_X + 1, c.BLOQUES_Y + fila * c.BLOQUE_SEP_Y,
                               c.BLOQUE_ANCHO, c.BLOQUE_ALTO)
            bloques.append((rect, c.COLORES_FILAS[fila]))
    return bloques