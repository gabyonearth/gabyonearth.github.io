# Gaby on Earth

Blog bilingüe (ES/EN) en Jekyll, con estilo acuarela. Se publica gratis en GitHub Pages.

## 1. Publicar por primera vez

1. Crea tu cuenta de GitHub (con 2FA activado) y un repositorio **público** llamado exactamente `TUUSUARIO.github.io`.
2. En `_config.yml` cambia `url` por `https://TUUSUARIO.github.io`.
3. Sube esta carpeta:

```bash
git init -b main
git add .
git commit -m "Primer commit"
git remote add origin https://github.com/TUUSUARIO/TUUSUARIO.github.io.git
git push -u origin main
```

4. En GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root)**.
5. En 1–2 minutos el sitio estará en `https://TUUSUARIO.github.io`.

## 2. Escribir una entrada

Crea un archivo en `_posts/` llamado `AAAA-MM-DD-titulo.md`:

```markdown
---
title: "Título"
date: 2026-11-02
lang: es            # es o en
ref: mi-viaje       # el mismo en la versión traducida, para enlazar ES <-> EN
category: viajes    # viajes, ciencia, phd, comida, mujeres, reflexiones, entrevistas
location: Lisboa    # opcional
image: /assets/img/lisboa/portada.jpg   # opcional, portada de la tarjeta
excerpt: "Resumen corto que aparece en la tarjeta."
---

Texto en Markdown.

{% include figure.html src="/assets/img/lisboa/foto1.jpg" caption="Pie de foto" %}
```

Si una entrada no tiene traducción, el botón de idioma lleva al inicio del otro idioma.
Para una galería, envuelve varias figuras: `<div class="gallery"> ... </div>`.

## 3. Columnas de opinión

Agrega líneas en `_data/columnas.yml` (título, medio, fecha, link). Aparecen en `/columnas/` y `/en/columns/`.

## 4. Fotos (importante)

- Redúcelas y **quita los datos de ubicación (GPS/EXIF)** antes de subirlas:

```bash
brew install imagemagick
magick foto.jpg -resize 1600x -strip -quality 82 foto-web.jpg
```

- Guárdalas en `assets/img/<carpeta-del-post>/`. El repo recomienda no pasar de ~1 GB en total.

## 5. Ver el sitio en tu computador (opcional)

Ya está instalado Ruby (Homebrew) y las gems. Desde esta carpeta:

```bash
./serve.sh
```

Abre http://127.0.0.1:4000 (se recarga solo al guardar cambios). `serve.sh` y `.local/` son solo para tu Mac; GitHub Pages no los usa.

## Personalizar colores

Todos están al inicio de `assets/css/style.css` (`:root`). Los colores de cada tema están en `_data/categories.yml`.

## Redes sociales

En `_config.yml`, bajo `social:`, están tus links de Instagram y LinkedIn; cámbialos cuando quieras. Aparecen en el inicio, en "Sobre mí" y en el pie de página.

## Paleta (teoría del color)

Verde `#2F6B4A` (147°) + malva `#9A5FA5` (291°) son los colores principales. Rosa-coral `#E0485A` (353°) es el tercero: junto al verde y al malva forma una tríada dividida complementaria. Teal `#2A8C9E` (189°) es el cuarto: complementario del rosa, cierra una tétrada doble complementaria. Uso sugerido: verde y malva dominan, rosa para destacar (hover, casa, flores), teal para detalles (río, enlaces de LinkedIn).
