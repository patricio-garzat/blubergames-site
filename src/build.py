"""Genera index.html a partir de src/index.template.html (diseño "Hielo claro", 21 oct 2026).

Inserta, sin modificarlos: el ícono SVG de Cube Swipe (src/parts/app-icon.svg) y su animación de giro (src/parts/cs-turn.css),
y el logo claro de SMUSH! (assets/smush/logo-dark.svg; solo se le agrega una clase para mecer a sus marcianitos con CSS).
El oso y el logo de BluBer se cargan desde brand/ (bluber-bear.svg, bluber-logo.svg y bluber-logo-dark.svg para fondo oscuro).
Uso: python3 src/build.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(*p):
    return open(os.path.join(ROOT, *p), encoding="utf-8").read()


html = read("src", "index.template.html")
smush = re.sub(r"^<svg ", '<svg class="sm-logo" aria-hidden="true" focusable="false" ', read("assets", "smush", "logo-dark.svg").strip(), count=1)
for key, val in {
    "CS_TURN": read("src", "parts", "cs-turn.css"),
    "CS_ICON": read("src", "parts", "app-icon.svg").strip().replace('class="app-icon"', 'class="cs-svg"', 1),
    "SMUSH_LOGO": smush,
}.items():
    html = html.replace("{{" + key + "}}", val)
assert "{{" not in html, re.findall(r"\{\{\w+\}\}", html)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
print("index.html", len(html) // 1024, "KB")
