"""Rompe bloques retro: archivo principal."""
import os
os.environ.setdefault("DISPLAY", ":1")  # usa el escritorio virtual sin hacer export

import pygame
import config as c
import graphics as g
from entities import Barra, Pelota, crear_bloques


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((c.ANCHO, c.ALTO))
    pygame.display.set_caption("Rompe bloques retro")
    base = pygame.Surface((c.BASE_ANCHO, c.BASE_ALTO))  # aquí se dibuja en pequeño
    reloj = pygame.time.Clock()

    barra = Barra()
    pelota = Pelota()
    bloques = crear_bloques()
    puntos = 0
    vidas = c.VIDAS_INICIALES
    estado = "esperando"  # "esperando", "jugando", "perdiste" o "ganaste"
    inicio_espera = pygame.time.get_ticks()

    while True:
        ahora = pygame.time.get_ticks()

        # 1. Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == "esperando" and ahora - inicio_espera > c.TIEMPO_PARPADEO:
                    pelota.lanzar()
                    estado = "jugando"
                elif estado in ("perdiste", "ganaste"):
                    bloques = crear_bloques()
                    puntos, vidas = 0, c.VIDAS_INICIALES
                    estado, inicio_espera = "esperando", ahora

        # 2. La barra sigue el mouse (se divide entre la escala)
        barra.seguir(pygame.mouse.get_pos()[0] // c.ESCALA)

        # 3. Lógica según el estado
        if estado == "esperando":
            pelota.pegar_a(barra)
        elif estado == "jugando":
            pelota.mover()
            pelota.rebotar_en_barra(barra)

            indice = pelota.rect.collidelist([rect for rect, _ in bloques])
            if indice != -1:
                bloques.pop(indice)
                pelota.vy = -pelota.vy
                puntos += 10
                if puntos % 100 == 0:
                    pelota.acelerar()

            if pelota.se_cayo():
                vidas -= 1
                if vidas == 0:
                    estado = "perdiste"
                else:
                    estado, inicio_espera = "esperando", ahora

            if not bloques:
                estado = "ganaste"

        # 4. Dibujar en la superficie pequeña
        base.fill(c.FONDO)
        g.dibujar_marcador(base, puntos, vidas)
        for rect, color in bloques:
            g.dibujar_bloque(base, rect, color)

        parpadeando = estado == "esperando" and ahora - inicio_espera < c.TIEMPO_PARPADEO
        visible = not parpadeando or (ahora // 120) % 2 == 0
        if visible:
            g.dibujar_barra(base, barra)
            if estado in ("esperando", "jugando"):
                g.dibujar_pelota(base, pelota)

        if estado == "esperando" and not parpadeando:
            g.texto(base, "TOCA PARA LANZAR", c.BASE_ANCHO // 2, 95, centrado=True)

        if estado in ("perdiste", "ganaste") and (ahora // 400) % 2 == 0:
            mensaje = "GANASTE" if estado == "ganaste" else "GAME OVER"
            g.texto(base, mensaje, c.BASE_ANCHO // 2, 80, c.AMARILLO, grande=True, centrado=True)
            g.texto(base, "TOCA PARA REINICIAR", c.BASE_ANCHO // 2, 98, centrado=True)

        # 5. Agrandar a la ventana y mostrar
        g.escalar(base, pantalla)
        pygame.display.flip()
        reloj.tick(c.FPS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nJuego cerrado con Ctrl+C")
    finally:
        pygame.quit()