#!/usr/bin/env python3
"""Prepara una foto para el blog: la reduce y le borra TODOS los metadatos (GPS, cámara, fecha).

Uso:
    python3 herramientas/preparar_foto.py RUTA_FOTO CARPETA_DESTINO [NOMBRE]

Ejemplo:
    python3 herramientas/preparar_foto.py ~/Downloads/IMG_1234.jpg assets/img/lisboa portada

Deja la foto en assets/img/lisboa/portada.jpg (1600 px de ancho máximo).
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit(__doc__)

origen = Path(sys.argv[1]).expanduser()
destino = Path(sys.argv[2])
nombre = sys.argv[3] if len(sys.argv) > 3 else origen.stem.lower()

destino.mkdir(parents=True, exist_ok=True)
im = ImageOps.exif_transpose(Image.open(origen)).convert("RGB")
im.thumbnail((1600, 1600))
limpia = Image.new("RGB", im.size)
limpia.paste(im)  # copia solo los píxeles: sin EXIF ni GPS
salida = destino / f"{nombre}.jpg"
limpia.save(salida, quality=84, optimize=True, progressive=True)

chequeo = Image.open(salida)
print(f"Listo: {salida}  ({chequeo.size[0]}x{chequeo.size[1]}, {salida.stat().st_size // 1024} KB, metadatos: {len(chequeo.getexif())})")
print(f'Úsala en un post con: {{% include figure.html src="/{salida.as_posix()}" alt="Describe la foto" caption="Pie de foto" %}}')
