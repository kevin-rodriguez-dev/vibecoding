# 🧱 Breakout

Mini-juego estilo **pixel art** inspirado en los clásicos Breakout.

Proyecto desarrollado con **vibecoding**: la IA se usó como copiloto de programación mediante prompts progresivos, y cada versión se probó, validó y ajustó.

## 💡 Idea original

Este juego es una recreación educativa del género *Breakout*:

- **Breakout** (Atari, 1976), concebido por Nolan Bushnell y Steve Bristow, es el juego que originó el género: una paleta, una pelota y un muro de ladrillos.
- **Brick Breaker** (1999), desarrollado por Ali Asaria, venía preinstalado en teléfonos BlackBerry, y Nokia incluyó versiones similares en muchos celulares de teclas a inicios de los 2000. De esos juegos se tomó la inspiración visual: gráficos pixelados, vidas con corazones y la pelota que reaparece parpadeando sobre la barra.

Todo el código y los gráficos de este proyecto son originales (dibujados con código); no se usan imágenes ni recursos de los juegos originales.

---

## 🎮 Cómo se juega

| Acción | Control |
|---|---|
| Mover la barra | Mouse o deslizar el dedo |
| Lanzar la pelota | Tocar / clic (después del parpadeo) |
| Reiniciar tras ganar o perder | Tocar / clic |
| Salir | Cerrar la ventana o `Ctrl + C` en la terminal |

- Cada bloque vale **10 puntos**.
- Cada 10 bloques la pelota **acelera**.
- El ángulo de rebote depende de **dónde pega la pelota en la barra** (orillas = más inclinado).
- Al perder una vida, la barra y la pelota **parpadean** y la pelota vuelve a salir desde la barra.

---

## ⚙️ Requisitos y cómo ejecutarlo

### Opción A: GitHub Codespaces (como se desarrolló, desde una tablet)

Codespaces no tiene pantalla propia, por eso el repositorio incluye `.devcontainer/devcontainer.json`, que instala:
- Python 3.12
- Pygame
- Un escritorio virtual (`desktop-lite`) que se ve desde el navegador

Pasos:
1. En el repositorio: **Code → Codespaces → Create codespace on main**.
2. Esperar a que termine de configurarse (instala Pygame automáticamente).
3. Ir a la pestaña **Ports**, abrir el puerto **6080 (Escritorio)** en el navegador, tocar **Connect** y usar la contraseña `vscode`.
4. En la terminal ejecutar:
   ```bash
   python main.py
   ```
5. El juego aparece en la pestaña del escritorio virtual.

### Opción B: Computadora local

- Python 3.10 o superior
- Instalar dependencias y ejecutar:
  ```bash
  pip install -r requirements.txt
  python main.py
  ```

---

El `.gitignore` es la **plantilla estándar de Python** que ofrece GitHub al crear el repositorio; evita subir archivos generados como `__pycache__/` o entornos virtuales.

**Técnica de pixel art:** todo se dibuja en una superficie pequeña de 200×150 y luego se agranda 4 veces sin suavizado (`pygame.transform.scale`), así cada pixel se ve como un cuadro.

---

## 🤖 Evidencia de vibecoding (prompts)

> Nota: los prompts 1 a 3 los redacté con ayuda de la IA a partir de mi idea (me sugirió una estructura de prompt claro: lenguaje, tamaño, controles y pedir poco a la vez). Los prompts 4 a 6 son mis propias peticiones, escritas con mis palabras después de probar el juego.

### Prompt 1 – Base del juego
> Crea un juego tipo Breakout en Python con Pygame. Ventana de 800x600. Una barra abajo sigue el mouse/toque, una pelota rebota en las paredes y en la barra, y destruye bloques arriba al tocarlos. Por ahora sin puntaje ni vidas. Comentarios en español.

- **Qué se pidió:** la mecánica mínima jugable.
- **Por qué así:** pedir algo pequeño primero permite verificar que lo básico funciona antes de agregar más. Se especificó control con mouse/toque porque las flechas del teclado fallaban desde la tablet en el escritorio virtual.

### Prompt 2 – Reglas del juego
> Agrega al juego: puntaje (10 puntos por bloque), 3 vidas que se pierden cuando la pelota cae, mensaje de GAME OVER al perder todas, mensaje de GANASTE al romper todos los bloques, y que al tocar la pantalla se reinicie.

- **Por qué se refinó:** la versión 1 no tenía objetivo ni forma de perder, así que no era realmente un juego.

### Prompt 3 – Mejora de jugabilidad
> Mejora el juego: que el ángulo de rebote dependa de dónde pega la pelota en la barra (orillas = más inclinado), que cada fila de bloques tenga un color diferente y que la pelota acelere cada 10 bloques rotos.

- **Por qué se refinó:** al probar, la pelota siempre rebotaba igual y el juego se volvía repetitivo; no había forma de apuntar.

### Prompt 4 – Estilo del juego original
> Haz el juego más parecido al Brick Breaker de los celulares de teclas: pelota cuadrada, estilo pixelado, vidas con corazones de pixeles, y que al perder una vida la barra y la pelota parpadeen y la pelota salga desde la barra al tocar la pantalla.

- **Por qué se refinó:** quería que se sintiera como el juego que recordaba; se le pidió a la IA buscar el juego original como referencia.

### Prompt 5 – Pixel art real y código limpio
> Haz que todo el juego sea pixel art como el original, separa el código en varios archivos para que quede ordenado, evita tener que ejecutar export cada vez y que no salga error al cerrar con Ctrl+C.

- **Por qué se refinó:** solo algunos elementos se veían pixelados, todo el código estaba en un solo archivo difícil de leer, y al probar aparecieron dos molestias (el `export` y el error de `Ctrl+C`).

### Prompt 6 – Ajustes visuales finales
> Los bloques de colores no me gustan, deberían ser pixeles también y verdes. La letra casi no se distingue, dale más estilo.

- **Por qué se refinó:** la fuente del sistema escalada se veía borrosa e ilegible, y los bloques planos no combinaban con el estilo retro.

## Validación del resultado

### Cómo se probó
Pruebas manuales después de cada prompt, ejecutando `python main.py` y jugando en el escritorio virtual:
- Mover la barra de orilla a orilla (no debe salirse de la pantalla).
- Pegarle a la pelota con la orilla izquierda, el centro y la orilla derecha para comprobar el ángulo.
- Dejar caer la pelota 3 veces para verificar la pérdida de corazones, el parpadeo y el GAME OVER.
- Tocar la pantalla para reiniciar y confirmar que todo vuelve al inicio.
- Romper 10 bloques para comprobar que la pelota acelera.

### Errores, limitaciones y ajustes realizados

| Problema encontrado | Ajuste |
|---|---|
| La pelota rebotaba siempre en el mismo ángulo | Ángulo calculado según el punto de impacto en la barra |
| El texto se veía borroso y casi ilegible | Fuente pixel 3x5 propia con sombra |

**Limitaciones conocidas:** al chocar con un bloque solo se invierte la dirección vertical, así que si la pelota pega de lado el rebote no es del todo realista. El juego tiene un solo nivel y no tiene sonido.

---

## 🧠 Reflexión final

> ✏️ *Completar con mis propias palabras.*

**¿Qué aprendí usando IA para programar?**
_(Ej.: cómo dividir un problema en pasos pequeños, cómo describir con precisión lo que quiero, qué pasó cuando un prompt fue vago…)_

**Ventajas del vibecoding:**
_(Ej.: velocidad, poder probar ideas rápido, aprender viendo código comentado…)_


**Partes del código que comprendo:**
_(Ej.: el ciclo principal, los estados del juego, cómo se detectan los choques con `colliderect`…)_

**Partes que necesito reforzar:**
_(Ej.: las clases y `@property`, el cálculo del ángulo de rebote, el escalado de superficies…)_

---

## 📄 Licencia

MIT. Ver archivo `LICENSE`.
