# Guía de marca de BluBer Games

Esta guía es la referencia para todo lo que lleve la marca BluBer Games: la landing, los juegos nuevos, los íconos y las intros.

Si estás empezando un juego nuevo en otro chat, pídele que lea este archivo primero. Por ejemplo: "usa la guía de marca de `patricio-garzat/blubergames-site`".

## Qué es BluBer Games

- Es un estudio independiente que **crea juegos para iOS** (iPhone y iPad).
- Hace juegos de rompecabezas fáciles de empezar, difíciles de soltar y cuidados hasta el último detalle.
- El primer juego es **Propp Lozenge**.
  - Juego: <https://patricio-garzat.github.io/Puzzle-Propp-Lozenge/>
  - Repositorio: `patricio-garzat/Puzzle-Propp-Lozenge`
- El dominio de la marca es **blubergames.com**.

## Logo

| Archivo | Uso |
|---|---|
| `brand/bluber-logo.svg` | Logo principal: oso más "BluBer GAMES", **sobre fondo blanco**. Es la versión por defecto. |
| `brand/bluber-logo-dark-bg.svg` | Versión para fondo azul marino o fondos oscuros, con el texto en azules claros. |
| `brand/bluber-bear.svg` | Solo el oso. Para íconos pequeños, favicon y encabezados. |
| `brand/source/BluBer Games.svg` | Archivo original de Illustrator, con todas las versiones. |

Reglas:

- **Fondo:** el logo vive sobre blanco. Sobre fondos oscuros, usa la versión `dark-bg`.
- **Forma:** no lo deformes, no lo rotes y no le cambies los colores.
- **Espacio libre:** deja alrededor al menos el alto de la "B" de "BluBer".
- **Tamaño mínimo del logo completo:** 120 px de ancho. Por debajo de eso, usa solo el oso.
- **En la intro de los juegos:** el logo va centrado horizontal y verticalmente, a un tamaño moderado (unos 200 px en celular y 270 px en computadora), nunca gigante.

## Colores

| Nombre | Hex | Uso |
|---|---|---|
| Navy | `#00385B` | "BluBer", títulos, texto principal y botones principales |
| Sea | `#50AFEA` | Sombras del oso y acentos (palabras destacadas, enlaces, foco) |
| Ice | `#82CAFD` | Cuerpo del oso y "GAMES" |
| Snow | `#B6E3FF` | Detalles de hielo y bordes decorativos |
| Frost | `#F2F9FF` | Superficies muy claras (secciones y botones secundarios) |
| Paper | `#FFFFFF` | Fondo de la marca |
| Line | `#DCEBF6` | Bordes suaves |
| Ink 2 | `#3E5F78` | Texto secundario |

Cada juego puede tener su propia paleta. Propp Lozenge, por ejemplo, usa amarillo, rojo y azul en los rombos y un fondo nocturno `#12102A`. Lo que siempre es de BluBer es la intro y la landing.

## Tipografía

- **Títulos y logo:** Montserrat (600 a 800), de Google Fonts. Es la misma familia del logo.
- **Texto:** Figtree (400 a 700), de Google Fonts.
- **Títulos grandes:** con letter-spacing ligeramente negativo (`-0.025em`).
- **Etiquetas en mayúsculas:** con espaciado amplio (`0.18em`).

## Tono de los textos

- **Idioma:** inglés por defecto, con español como opción. Los juegos tienen un ajuste de idioma, y la landing tiene un botón ES/EN.
- **Estilo:** frases cortas, claras y cálidas. Hablarle al jugador de "tú", sin tecnicismos.
- **Terminología de Propp Lozenge en inglés:** tiles, Target, Hint, Shuffle, Free play, Build your own, clockwise / counterclockwise.

## Cómo se sienten los juegos (preferencias aprendidas)

Esto salió de construir Propp Lozenge. Úsalo como punto de partida en cada juego nuevo.

**Animaciones**
- Fluidas, suaves y profesionales.
- **Sin rebotes exagerados.** Un rebote "de caricatura" se ve chafo; mejor desvanecidos y movimientos suaves.
- Respetar "reducir movimiento" del sistema.

**Sonido**
- Relajante, tipo ASMR, y nunca agudo.
- Cada movimiento lleva solo un "thump" suave, sin notas musicales.
- Las melodías se reservan para los momentos de premio (estrellas, victoria, intro) y van en tonos medios o graves.
- Los sonidos van con pequeñas variaciones para no cansar, y deben oírse en las bocinas del celular (nada demasiado grave).

**Celular**
- Sin scroll en la pantalla de juego.
- Pocas cosas en pantalla, solo lo necesario.
- Controles por deslizamiento.
- Estructura de app de iOS: inicio, ajustes, cómo jugar y récords.

**Cero glitches**
- Las barras de arriba y de abajo del iPhone nunca deben salir de otro color que el fondo del tema.
- No debe haber destellos al cargar.
- Lo centrado debe estar centrado de verdad (usar `100dvh`, no `100vh`).
- Ver las notas técnicas abajo.

**Intro**
- Al abrir un juego sale primero la intro de BluBer (unos 4 s), siempre con todo el fondo blanco, también en modo oscuro. La página carga con el fondo del tema y pasa a blanco justo después de cargar. Durante la intro, `<html>` también va en blanco para que no se asome una franja oscura abajo; al terminar regresa al fondo del tema.
- Después viene la intro del juego. Ninguna de las dos se puede saltar.

**Niveles**
- Dificultad progresiva, estrellas, pistas que se pueden guardar y un pequeño secreto al final.

## Intro animada de BluBer

Está en `brand/intro/bluber-intro.html`, con controles para repetirla y verla en cámara lenta. Dura 4 segundos:

| Tiempo | Qué pasa |
|---|---|
| 0.25 s | El oso aparece con un desvanecido suave, sin rebote |
| 1.2 s | "BluBer" sube letra por letra |
| 1.95 s | "GAMES" se abre desde el centro |
| 2.7 s | Un brillo recorre "BluBer" y el oso levanta la cabeza y parpadea |

La versión que usa Propp Lozenge está dentro de su `index.html`, en `#studio` y `playStudio()`.

## Notas técnicas para web apps en iPhone

- **Color de las barras (comprobado en el simulador, Safari de iOS 26):**
  - Safari pinta sus barras de arriba y de abajo con las capas **fijas** (`position: fixed`) que tocan los bordes. Si no hay ninguna, usa el fondo de `<html>`/`<body>`.
  - **Solo vuelve a revisar cuando cambia el fondo de `<html>`/`<body>`.** No lo hace cuando cambia el color de una capa fija, cuando aparece una capa nueva ni cuando se quita una.
  - Ponle a `html` el color de fondo del tema desde el `<head>`.
  - Para que una pantalla (como la intro blanca) pinte las barras: esconde las capas fijas (`visibility: hidden` basta) y cambia el fondo de `<html>` **y** de `<body>` a ese color. Al terminar, regresa todo.
  - No uses capas fijas blancas desde la carga en apps oscuras: la barra se queda blanca.
- **Barra de estado:** en `apple-mobile-web-app-status-bar-style`, usa `black-translucent` en modo oscuro y deja espacio con `env(safe-area-inset-top)`.
- **Alto de pantalla:** usa `100dvh` para lo que deba ocupar exactamente la pantalla visible.
- **Sonido en iPhone:** el audio solo arranca después de un toque. Para que suene aunque el teléfono esté en silencio, reproduce un audio mudo al primer toque.
