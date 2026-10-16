"""Genera index.html a partir de src/index.template.html.

Inserta los logos oficiales (brand/bluber-bear.svg y brand/bluber-logo.svg, sin modificarlos),
el favicon (el oso) y las piezas del gameplay guardadas en src/parts/.
Uso: python3 src/build.py
"""
import os
import re
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(*p):
    return open(os.path.join(ROOT, *p), encoding="utf-8").read()


def svg_inner(name):
    s = read("brand", name)
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    body = re.sub(r"^<svg[^>]*>", "", s.strip())
    body = body[: body.rindex("</svg>")]
    body = re.sub(r"<title>.*?</title>", "", body)
    return vb, re.sub(r">\s+<", "><", body).strip()


bear_vb, bear = svg_inner("bluber-bear.svg")
logo_vb, logo = svg_inner("bluber-logo.svg")
favicon = "data:image/svg+xml," + urllib.parse.quote(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{bear_vb}">{bear}</svg>', safe="")

head = read("src", "parts", "head.html").replace("{{FAVICON}}", favicon)
html = read("src", "index.template.html")
for key, val in {
    "HEAD_TOP": head,
    "BEAR_VB": bear_vb, "BEAR": bear,
    "LOGO_VB": logo_vb, "LOGO": logo,
    "APP_ICON": read("src", "parts", "app-icon.svg").strip(),
    "GP_SVG": read("src", "parts", "gameplay.svg").strip(),
    "GP_SCRIPT": read("src", "parts", "gameplay.js").strip(),
    "ARROW": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6 14 14 6M8 6h6v6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "APPLE": read("src", "parts", "apple.svg").strip(),
    "PLAY": '<svg class="i-play" viewBox="0 0 20 20" aria-hidden="true"><path d="M6.5 4.6v10.8a1 1 0 0 0 1.5.86l8.6-5.4a1 1 0 0 0 0-1.72L8 3.74a1 1 0 0 0-1.5.86z" fill="currentColor"/></svg>',
}.items():
    html = html.replace("{{" + key + "}}", val)
assert "{{" not in html, re.findall(r"\{\{\w+\}\}", html)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
print("index.html", len(html) // 1024, "KB")
