# blubergames.com

Esta es la landing page de **BluBer Games**, un estudio que crea juegos para iOS.

La página publicada es `index.html`. **No se edita a mano:** se genera con `python3 src/build.py` a partir de `src/index.template.html`. El script le inserta los logos oficiales de `brand/`, el favicon y las piezas del gameplay de `src/parts/`. Solo carga las fuentes de Google Fonts y las capturas de `assets/`.

## Contenido del repositorio

| Ruta | Qué es |
|---|---|
| `index.html` | La página publicada (generada con `src/build.py`) |
| `src/` | Plantilla de la página, piezas del gameplay y el script que arma `index.html` |
| `assets/cube-swipe/` | Capturas del juego que se ven en la página |
| `privacy/`, `support/` | Política de privacidad y página de soporte (con formulario de Netlify) |
| `social/instagram/` | Foto de perfil, publicaciones, bio y textos de Instagram |
| `BRAND.md` | Guía de marca: colores, tipografía, logo, tono y cómo se sienten los juegos |
| `brand/` | Logos en SVG (fondo blanco, fondo oscuro y solo el oso), el archivo original de Illustrator y la intro animada |

## Secciones de la página

1. **Portada:** "We make games for iOS." / "Creamos juegos para iOS.".
2. **Games we've made:** una tarjeta por juego, con un gameplay animado de una partida real.
3. **About us:** quiénes son y tres valores.
4. **Pie de página.**

La página está en inglés y español. El idioma se elige según el navegador y se puede cambiar con el botón ES/EN. Los textos en español están en el objeto `ES` del `<script>` final, y los de inglés son los que están escritos en el HTML (cada uno con `data-i`).

## Cómo agregar un juego nuevo

1. Copia el bloque `<article class="game">` de Cube Swipe y pégalo debajo.
2. Cambia el nombre, el ícono, la descripción, las características (`.features`), los datos (`.facts`) y el link de "Play now".
3. Agrega las traducciones al español en el objeto `ES`.
4. Actualiza o quita la tarjeta "Game #2 is in the works" (`.next`).

Si el juego no tiene gameplay animado, puede llevar un tablero quieto o una captura dentro del `.phone`.

## Publicación

- La página está en **Netlify**, conectada a este repositorio: cada vez que se sube un cambio a `main`, Netlify la publica sola.
- Dirección de Netlify: <https://blubergames.netlify.app>
- Dominio: **blubergames.com**. Está registrado en GoDaddy y apunta a Netlify:

  | Tipo | Nombre | Valor |
  |---|---|---|
  | A | @ | `75.2.60.5` |
  | CNAME | www | `blubergames.netlify.app` |

## Juegos

| Juego | Estado | Links |
|---|---|---|
| Cube Swipe | [App Store](https://apps.apple.com/app/id6822390183) y web | [Jugar](https://cubeswipe.blubergames.com/) · [Código](https://github.com/patricio-garzat/Puzzle-Propp-Lozenge) |
