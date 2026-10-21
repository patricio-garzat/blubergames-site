# DESIGN.md — BluBer Games · "Hielo claro" (prototipo)

> Una mañana en el hielo: todo blanco y azul claro, los juegos flotan como tarjetas de vidrio y todo se mueve despacio.

Prototipo hecho con la skill `web-design` (fase B). Versión clara de "Noche polar" (el usuario prefirió un diseño blanco, no nocturno). No está publicado: solo `index.html` local para comparar con la landing actual.
Las reglas del estudio (`../../CLAUDE.md`, `blubergames-site/BRAND.md`) mandan sobre esta guía: logo oficial intacto, azules de la marca, Montserrat + Figtree, sin emojis, sin rebotes, inglés y español.

## 1. Visual Theme & Atmosphere

**Style**: Hielo y vidrio, minimalista, con tema claro (por defecto) y oscuro, y una textura de grano muy fina
**Keywords**: blanco, hielo, vidrio, grano fino, luz suave, aire, calma, premium, iOS
**Tone**: tranquilo, cuidado y llamativo — NOT neón, NOT "gamer" ruidoso, NOT caricatura
**Feel**: como abrir una app de iOS bien hecha en una mañana de invierno: limpia, luminosa y tranquila.

**Interaction Tier**: L3 Sumergido (escenas fijas que cambian al bajar, 3D real, cursor)
**Dependencies**: GSAP 3.12.5 + ScrollTrigger (cdnjs) · Three.js 0.160.0 (jsDelivr, un solo canvas WebGL)

## 2. Color Palette & Roles

```css
:root {
  /* Fondos: blanco y hielo de la marca */
  --bg: #FFFFFF;              /* página */
  --bg-deep: #F2F9FF;         /* Frost: secciones suaves */
  --surface: rgba(255, 255, 255, 0.78);        /* tarjetas de vidrio claro */
  --surface-alt: #F2F9FF;     /* secciones alternas */
  --surface-hover: #FFFFFF;
  --mist: #E7F3FD;            /* hielo un poco más marcado */
  --paper: #FFFFFF;

  /* Bordes */
  --border: #DCEBF6;
  --border-hover: rgba(80, 175, 234, 0.45);

  /* Texto */
  --text: #00385B;            /* Navy */
  --text-secondary: #3E5F78;
  --text-tertiary: #6A8296;

  /* Acentos de la marca */
  --navy: #00385B;
  --accent: #50AFEA;          /* Sea */
  --sea-deep: #2F8FD0;        /* Sea más profundo, para degradados legibles sobre blanco */
  --ice: #82CAFD;
  --snow: #B6E3FF;

  /* RGB para rgba() */
  --bg-rgb: 255, 255, 255;
  --navy-rgb: 0, 56, 91;
  --accent-rgb: 80, 175, 234;
  --ice-rgb: 130, 202, 253;

  /* Semánticos */
  --success: #6BD6A4;
  --error: #FF8A80;
  --warning: #F1C27A;         /* también es el "Beta" */

  /* Color propio de cada juego (solo dentro de su escena o tarjeta) */
  --g-cs: 111, 142, 247;
  --g-sm: 77, 179, 255;
  --g-fw: 241, 194, 122;
  --g-rl: 253, 28, 34;        /* RaceLine: rojo de su línea de carrera */
}
```

**Tema oscuro** (`html[data-theme="dark"]`; por defecto sigue al sistema, y el botón sol/luna lo cambia y lo recuerda):

```css
html[data-theme="dark"] {
  --bg: #021626; --bg-deep: #010D18; --surface: rgba(255, 255, 255, 0.05); --surface-alt: #04223A; --surface-hover: rgba(255, 255, 255, 0.09);
  --mist: #06345A; --solid: #0A2A44;
  --border: rgba(182, 227, 255, 0.14); --border-hover: rgba(182, 227, 255, 0.34);
  --text: #F2F9FF; --text-secondary: rgba(226, 242, 255, 0.74); --text-tertiary: rgba(226, 242, 255, 0.52);
  --label: #82CAFD; --btn-bg: #F2F9FF; --btn-ink: #00385B;
  --grad-1: #B6E3FF; --grad-2: #82CAFD; --grad-3: #50AFEA;
  --card-bg: linear-gradient(170deg, rgba(255, 255, 255, .09) 30%, rgba(255, 255, 255, .04));
  --shadow-rgb: 0, 0, 0; --bg-rgb: 2, 22, 38;
  --studio-glow: rgba(80, 175, 234, .16); --final-glow: rgba(80, 175, 234, .2);
  --grain: url(…ruido blanco…); --grain-opacity: .06;
}
```
En claro, los mismos tokens valen: `--solid #FFF`, `--label #2F8FD0`, `--btn-bg #00385B`, `--btn-ink #FFF`, `--grad-*` Sea → Sea profundo, `--shadow-rgb 0,56,91` (navy), grano negro al 4.5 %.

**Color Rules:**
- Todos los colores salen de estas variables; nada de hex sueltos en los componentes.
- El estudio usa blanco y los azules de la marca. Cada juego conserva su mundo de color dentro de su escena (la noche de Cube Swipe, el cielo de SMUSH!, la medianoche de Fireworks): son sus portadas, sobre el blanco.
- Los rombos amarillo, rojo y azul son solo de Cube Swipe.
- Sombras con `rgba(var(--shadow-rgb), …)`: navy transparente en claro, negro en oscuro.
- En oscuro (decisión del usuario, 21 oct 2026): el oso oficial tal cual, sin tarjeta ni contorno. El logo completo usa `assets/bluber-logo-dark.svg`: el mismo logo con solo las letras "BluBer" (navy) en blanco; el ojo y la nariz siguen navy.

## 3. Typography Rules

**Font Stack:**
```css
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Figtree:wght@400;500;600;700&display=swap');
--f-display: "Montserrat", "Helvetica Neue", Arial, sans-serif;
--f-body: "Figtree", "Helvetica Neue", Arial, sans-serif;
```

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Hero H1 | Montserrat | clamp(44px, 6.2vw, 92px) | 800 | 1.02 | -0.038em |
| Section H2 | Montserrat | clamp(34px, 4.4vw, 60px) (estudio: hasta 52px) | 800 | 1.06 | -0.032em |
| H3 | Montserrat | clamp(30px, 3.1vw, 46px) | 800 | 1.04 | -0.032em |
| Lead | Figtree | clamp(17px, 1.35vw, 20px) | 400 | 1.6 | — |
| Body | Figtree | 17px (16.5 en celular) | 400 | 1.65 | — |
| Label | Montserrat | 12px | 700 | 1 | 0.18em (mayúsculas) |
| Mono/Code | — (no se usa) | — | — | — | — |

**Typography Rules:**
- Títulos siempre en Montserrat 800; texto en Figtree.
- **NEVER use**: Inter, Space Grotesk, serifas decorativas, fuentes del sistema como fuente principal.

**Text Decoration** (según `text-decoration-rules.md`, estilo oscuro):
- Hero h1: navy sólido; solo la palabra clave ("play") en degradado Sea → Sea profundo con un brillo que se mueve. Sin sombra de texto (las palabras se recortan para entrar y la sombra se veía en cuadros).
- Section h2: palabra clave en degradado Sea → Sea profundo (en cada letra, porque el título se parte en letras), sin sombra.
- Párrafos: sin decoración.

## 4. Component Stylings

### Buttons
```css
.btn { display: inline-flex; align-items: center; gap: 10px; min-height: 48px; padding: 14px 26px; border-radius: 999px; border: 0;
  font: 700 16px var(--f-display); text-decoration: none; cursor: pointer; transition: transform .4s var(--ease), box-shadow .4s var(--ease), background .3s; }
.btn-primary { color: var(--paper); background: var(--navy); box-shadow: 0 10px 26px rgba(var(--navy-rgb), .22); }
.btn-primary:hover { box-shadow: 0 14px 34px rgba(var(--navy-rgb), .3), 0 0 0 4px rgba(var(--accent-rgb), .15); }
.btn-primary:active { transform: scale(.97); }
.btn:focus-visible { outline: 2px solid var(--ice); outline-offset: 4px; }
.btn[disabled] { opacity: .45; cursor: not-allowed; box-shadow: none; }
.btn-ghost { color: var(--text); background: var(--surface); border: 1px solid var(--border); }
.btn-ghost:hover { background: var(--surface-hover); border-color: var(--border-hover); }
```

### Cards (vidrio, con luz que sigue al cursor)
```css
.glass { position: relative; border-radius: 28px; background: var(--surface); border: 1px solid var(--border); overflow: hidden;
  backdrop-filter: blur(12px); transition: border-color .4s var(--ease), transform .5s var(--ease), background .4s; }
.glass::before { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: 0; transition: opacity .4s;
  background: radial-gradient(360px circle at var(--mx, 50%) var(--my, 50%), rgba(var(--snow-rgb), .14), transparent 45%); }
.glass:hover { border-color: var(--border-hover); background: var(--surface-hover); }
.glass:hover::before { opacity: 1; }
.glass:focus-within { border-color: var(--ice); }
```

### Navigation
```css
.nav { position: fixed; inset: 0 0 auto; z-index: 50; transition: background .4s, border-color .4s; border-bottom: 1px solid transparent; }
.nav.scrolled { background: rgba(var(--bg-rgb), .72); backdrop-filter: blur(12px); border-bottom-color: var(--border); }
/* Sobre blanco, el oso oficial va directo, sin tarjeta */
.nav .brand img { width: 54px; }
```

### Links
```css
.link { color: var(--text-secondary); text-decoration: none; background: linear-gradient(var(--ice), var(--ice)) 0 100% / 0 1.5px no-repeat; transition: color .3s, background-size .4s var(--ease); }
.link:hover, .link:focus-visible { color: var(--text); background-size: 100% 1.5px; }
```

### Tags / Badges
```css
.tag { font: 700 11px var(--f-display); letter-spacing: .14em; text-transform: uppercase; padding: 5px 10px; border-radius: 999px; }
.tag-live { color: var(--navy); background: var(--snow); }
.tag-beta { color: #3D2A00; background: var(--warning); }
```
El badge "Download on the App Store" es el oficial de Apple, sin modificar.

## 5. Layout Principles

**Container:** max 1200px · padding 32px (escritorio) / 20px (celular) · variante angosta 760px para texto.
**Spacing Scale:** secciones 140px (escritorio) / 88px (celular) · gap de componentes 24px · relleno de tarjeta 28px.
**Grid:**
```css
.wrap { width: min(1200px, 100%); margin-inline: auto; padding-inline: 32px; }
.split { display: grid; grid-template-columns: 1fr 1.15fr; gap: 64px; align-items: center; }
.values { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
```

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | sin sombra, borde `--border` | etiquetas, textos |
| Glass | vidrio + borde | tarjetas de valores |
| Elevated | `0 30px 80px rgba(0,0,0,.45)` | tarjetas de juegos flotando |
| Glow | `0 0 80px rgba(var(--g-*), .45)` | luz de color de cada juego |
| Grano | capa fija encima de todo, ruido SVG (`feTurbulence`) en mosaico de 160 px, 4.5 % (claro) / 6 % (oscuro), se mueve a saltos (`steps`) para que se sienta vivo | toda la página |
| Glass | blanco translúcido + borde `--border` + sombra navy suave | tarjetas de juegos y valores |

La profundidad de la portada se da con escala y opacidad (no con `filter: blur` en elementos que se mueven).

## 7. Animation & Interaction

**Motion Philosophy**: todo se mueve lento y suave, como la aurora; solo `transform` y `opacity`; nada de rebotes.
**Tier**: L3

**Escena del estudio (21 oct 2026):** el cristal 3D no se entendía; ahora es el oso oficial sobre su témpano en un mar en calma (como en la landing), con capas que se mueven con el mouse y al bajar, nieve, sol de día y luna con estrellas de noche. La página ya no usa WebGL.

**Cuarta vuelta, "pantalla de inicio de consola" (21 oct 2026; el usuario la quiere más de videojuegos, sin perder la calma ni el profesionalismo, sin juegos que desaparezcan y sin amontonar):**
- La portada es como la pantalla de inicio de una consola (Apple TV, Switch): un estante con los 4 juegos en tarjetas grandes con su **portada animada** (el cubo girando, el cielo de SMUSH!, los fuegos artificiales en vivo y la carrera de RaceLine). Siempre se ven los cuatro.
- El juego elegido se marca con un anillo del color del juego, se levanta un poco y lo cruza un brillo; abajo, un panel con su información y el botón para jugar. Se elige con el mouse, con las flechas ← → del teclado (Enter para jugar) o deslizando en el celular (el del centro es el elegido).
- En escritorio, si nadie toca nada, el estante avanza solo cada 7 s con una barrita de progreso (como el modo de demostración de una consola); al primer toque, se detiene.
- **Regla:** ninguna animación de scroll toca la opacidad de los juegos. La entrada usa un envoltorio interno (`.tile-in`) y luego se limpia.
- Se quitó la escena fija (pin) y el abanico: el estante ya muestra todo. Quedan la tira de letras, el estudio con el cristal 3D, el final y el pie.
- Detalle escondido: al llegar al final aparece un aviso de logro, como en las consolas ("Achievement unlocked · Explorer"), una vez por visita.

**Cuatro juegos (21 oct 2026):** se agregó RaceLine (Beta), igual que en blubergames.com: cuarta tarjeta del abanico (en celular, cuatro tarjetas chicas), cuarta escena de la sección de juegos (circuito visto desde arriba, la línea roja se traza y el carro la recorre), cuarto ícono del final y el contador dice 4.

**Tercera vuelta (noise, temas y más movimiento, minimalista):**
- Cambio de tema: un círculo que se abre desde el botón sol/luna y revela el otro tema (View Transitions; sin soporte o con "reducir movimiento", cambio directo). El cristal 3D cambia sus colores con el tema.
- Grano fino en toda la página (ver §6).
- Navegación: el link de la sección donde estás se marca solo.
- Etiquetas de sección: su rayita crece al aparecer.
- Botón principal: un brillo cruza al pasar el mouse.
- Escena de juegos: entra con un recorte que se abre (`clip-path`), además de subir.
- Tira de letras: acelera un poco cuando bajas rápido y vuelve sola a su ritmo.
- Menos adornos: se quitaron las bolitas flotantes de la portada.

**Pulido (2ª vuelta):** las animaciones de entrada esperan a que carguen las fuentes (`document.fonts.ready`) para que nada salte; curva `expo.out` para entradas; cada palabra del h1 se recorta con relleno abajo para no cortar las colas de g, y, p; en la escena de juegos, los textos entran escalonados y cada botón del riel muestra el avance; contadores en el estudio (3 juegos · 0 anuncios · 2 idiomas).

### Dependencies
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script type="module">import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js";</script>
```

### Signature moments (6 categorías obligatorias + scroll-story)
| Categoría | Efecto | Dónde |
|---|---|---|
| Background | Aurora: manchas de luz de la marca que se mueven despacio + estrellas | portada y estudio |
| Hero H1 | SplitText: las palabras suben una por una; "play" con brillo que corre | portada |
| Section H2 | ScrollFloat: las letras flotan hacia su lugar al llegar | todos los h2 |
| Body | ScrollReveal: el texto del estudio se ilumina palabra por palabra al bajar | estudio |
| Elemento | Magnet en el botón principal + luz que sigue al cursor en la portada | portada |
| Componente | Estante de juegos estilo consola (portadas animadas, anillo de selección, teclado) + SpotlightCard en los valores | portada, estudio |
| Scroll-story 1 | Constelación (Pattern 1) y convergencia: las tarjetas se juntan al centro al bajar (Pattern 2) | portada → juegos |
| Scroll-story 2 | Escena fija: a la izquierda el texto del juego, a la derecha su mundo, que cambia al bajar (Pattern 3) | juegos |
| Scroll-story 3 | WebGL: un cristal de hielo 3D que gira con el scroll, con nieve (Pattern 4) | estudio |
| Detalle | Al pasar el mouse por el oso del pie cae un poco de nieve | pie |

### Base Setup
```js
gsap.registerPlugin(ScrollTrigger);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const small = matchMedia('(max-width: 760px)').matches;
```

### Entrance Animation
```css
.word { display: inline-block; overflow: hidden; vertical-align: top; }
.word > span { display: inline-block; transform: translateY(105%); }
```
```js
gsap.to('.hero h1 .word > span', { y: 0, duration: 1.2, ease: 'power3.out', stagger: .08, delay: .2 });
```

### Scroll Behavior
- Constelación → centro: `ScrollTrigger` con `scrub: 1` sobre la portada.
- Escena de juegos: sección de 300vh con contenido `position: sticky`; el progreso elige la escena (fundido de 0.6 s).
- Cristal 3D: la rotación sigue al scroll (`scrub: 1`) y gira despacio por sí solo; se pausa fuera de pantalla.
- Barra de progreso arriba y navegación que se vuelve vidrio al bajar.

### Hover & Focus States
Botones, links, tarjetas y escenas tienen hover y `:focus-visible` (anillo Ice de 2px). El cursor solo cambia efectos con `(hover: hover)`.

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .word > span { transform: none !important; }
}
```
Con "reducir movimiento": sin escenas fijas animadas (los juegos se ven como lista), sin WebGL (cristal estático), sin parallax ni cursor.

## 8. Do's and Don'ts

### Do
- Usar el logo y el oso oficiales tal cual, directo sobre el blanco.
- Que cada juego se vea con su propio color e imagen (su ícono real).
- Mover todo despacio, con curvas suaves (`power2/power3`, `sine`), y respetar "reducir movimiento".
- Pausar animaciones y el WebGL cuando no se ven.
- Textos en inglés y español con el botón ES/EN.
- Íconos de línea en SVG con los azules de la marca.

### Don't
- ❌ Redibujar, recolorear o recortar el logo, o escribir "BluBer Games" con la fuente como si fuera el logo.
- ❌ Usar los rombos de colores de Cube Swipe como decoración del estudio.
- ❌ Emojis en cualquier parte.
- ❌ Rebotes de caricatura o animaciones rápidas y nerviosas.
- ❌ `filter: blur()` en elementos que se mueven; más de un canvas WebGL.
- ❌ Neón, glitch, colores saturados fuera de la marca.
- ❌ Texto con contorno (`-webkit-text-stroke`): en Montserrat se ven los trazos encimados por dentro.
- ❌ Sombra de texto en palabras que se recortan para animarse (se ve la caja).
- ❌ Tarjeta blanca o contorno alrededor del logo en oscuro; tampoco el logo con "BluBer" en navy sobre oscuro (ahí va `bluber-logo-dark.svg`).
- ❌ Grano encima del 7 % o con `filter` animado (se ve sucio y pesa).
- ❌ Más de 2 escenas fijas (pin) en la página.
- ❌ Scroll secuestrado (sin Lenis): el scroll nativo manda.
- ❌ Texto gris sobre gris: el contraste del texto principal debe ser alto.

## 9. Responsive Behavior

| Name | Width | Key Changes |
|------|-------|-------------|
| Desktop | > 1024px | constelación completa, escena fija de juegos en dos columnas, cristal WebGL |
| Tablet | 761–1024px | constelación más chica, escena de juegos en una columna |
| Mobile | ≤ 760px | constelación de 3 tarjetas quieta, juegos como lista de tarjetas (sin pin), cristal estático, valores en una columna |

**Touch Targets:** mínimo 44×44px.
**Collapsing Strategy:** la navegación se queda con el oso, ES/EN y "Play"; los links internos se ocultan.

```css
@media (max-width: 760px) {
  .wrap { padding-inline: 20px; }
  .split, .values { grid-template-columns: 1fr; }
  .pin { height: auto; } .pin-inner { position: static; height: auto; }
}
```
