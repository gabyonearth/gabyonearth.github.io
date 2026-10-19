# Gaby on Earth

Blog bilingüe (ES/EN) hecho con Jekyll y publicado gratis en GitHub Pages: https://gabyonearth.github.io
Repositorio: https://github.com/gabyonearth/gabyonearth.github.io

## 1. Cómo cambiar algo y publicarlo

Cada vez que algo llega a la rama `main`, GitHub reconstruye el sitio solo (1–2 minutos). Hay dos formas:

**A. Directo en GitHub (cambios chicos de texto).** Abre el archivo en el repo → lápiz (Edit) → *Commit changes*. Tecla `.` abre un editor tipo VS Code en el navegador.

**B. En tu computador (cambios grandes, fotos, probar antes).** Dentro de esta carpeta:

```bash
git pull                      # trae lo que editaste en GitHub (hazlo SIEMPRE antes de empezar)
./serve.sh                    # ver el sitio en http://127.0.0.1:4000 (opcional)
git add .
git commit -m "Describe el cambio"
git push
```

Si `git push` da error de conflicto, casi siempre es que olvidaste el `git pull`.
Trabaja solo dentro de `github_gabyonearth`: la carpeta de arriba (`Claudito`) tiene otros proyectos que NO deben subirse.

## 2. Dónde está cada cosa

| Qué | Archivo |
|---|---|
| Sobre mí (ES / EN) | `sobre-mi.md` / `en/about.md` |
| Columnas, prensa y entrevistas | `_data/columnas.yml` |
| Frase de portada, menú y textos fijos | `_data/i18n.yml` |
| Nombre y colores de cada tema | `_data/categories.yml` |
| Redes sociales | `_config.yml` (sección `social`) |
| Entradas del blog | `_posts/` |
| Colores y estilo | `assets/css/style.css` (variables arriba, en `:root`) |
| Ilustración del inicio (Andes) | `_includes/hero.svg` |
| Logo (geoide con satélite) | `_includes/geoid.svg` |

## 3. Escribir una entrada nueva

Crea `_posts/AAAA-MM-DD-titulo.md` (en GitHub: *Add file → Create new file*). Haz una por idioma:

```markdown
---
title: "Título"
date: 2026-11-02
lang: es                # es o en
ref: mi-viaje           # IGUAL en la versión traducida: enlaza ES <-> EN
category: viajes        # viajes, ciencia, phd, comida, mujeres, reflexiones, entrevistas
thumb: /assets/img/lisboa/portada.jpg   # foto de la tarjeta del inicio (opcional)
location: Lisboa        # opcional
excerpt: "Resumen corto que aparece en la tarjeta."
---

Texto en Markdown.

{% include figure.html src="/assets/img/lisboa/foto1.jpg" alt="Descripción" caption="Pie de foto" %}
```

Notas:
- `thumb:` es la foto de la miniatura en el inicio y en Temas. Sin `thumb:` se usa la ilustración de montañas.
- `image:` (distinto de `thumb`) pone una portada grande arriba del texto del post. Si usas la misma foto en `thumb` y dentro del texto, no uses `image` para no repetirla.
- Si una entrada no tiene traducción, el botón de idioma lleva al inicio del otro idioma.
- Galería: envuelve varias `figure.html` en `<div class="gallery"> ... </div>`.
- Para borrar una entrada, borra su archivo en `_posts/`.

## 4. Fotos (importante: privacidad)

Las fotos del celular traen la ubicación exacta (GPS), el modelo de cámara y la fecha. Antes de subirlas, pásalas por el script, que las reduce a 1600 px y borra todos los metadatos:

```bash
python3 herramientas/preparar_foto.py ~/Downloads/IMG_1234.jpg assets/img/lisboa portada
```

Deja `assets/img/lisboa/portada.jpg` y te imprime la línea lista para pegar en el post. Requiere la librería Pillow (`pip install pillow`; ya viene en conda). El repo conviene mantenerlo bajo ~1 GB en total.

## 5. Columnas, prensa y entrevistas

Edita `_data/columnas.yml`. Cada entrada lleva `tipo` (`columna`, `prensa` o `entrevista`), `title`, `medio`, y `date` (AAAA-MM-DD) o `when` (texto libre, como "Julio 2026"). `url`, `nota` y `nota_en` son opcionales. Sin `url`, el título se muestra sin link.

## 6. Ver el sitio en tu computador

Ruby ya está instalado (Homebrew) con las gems del proyecto:

```bash
./serve.sh
```

Abre http://127.0.0.1:4000. `serve.sh`, `.local/` y `.bundle/` son solo para tu Mac; GitHub Pages no los usa.

## 7. Paleta (teoría del color)

Verde `#2F6B4A` (147°) + malva `#9A5FA5` (291°) son los principales. Rosa-coral `#E0485A` (353°) es el tercero: con el verde y el malva forma una tríada dividida complementaria. Teal `#2A8C9E` (189°) es el cuarto: complementario del rosa, cierra una tétrada doble complementaria. Uso: verde y malva dominan; rosa para destacar (hover, casa, flores); teal para detalles (río, LinkedIn, "Sígueme").

## 8. Privacidad: lo que conviene recordar

- Los commits usan el correo noreply de GitHub (`343177197+gabyonearth@users.noreply.github.com`), configurado solo en este repo. No cambies el correo por uno personal.
- Borra siempre los metadatos de las fotos (sección 4).
- Instagram y LinkedIn enlazados están en `_config.yml`; si creas un Instagram para el blog, cámbialo ahí.
