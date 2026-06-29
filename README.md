# Cine Tracker 🎬 - Odoo 18 Module

![Cine Tracker Banner](static/description/cine_tracker_banner.png)

**Cine Tracker** es un módulo personalizado para **Odoo 18** diseñado para los amantes del cine y las series. Permite gestionar un catálogo personal de contenido multimedia, clasificar las obras, puntuarlas y realizar un seguimiento de lo que has visto. 

Además, cuenta con una **integración inteligente con la API de TMDB (The Movie Database)** que autocompleta automáticamente los géneros (añadiéndolos como etiquetas de colores), la sinopsis, el año de estreno y descarga la carátula oficial con solo escribir el título.

---

## ✨ Características Principales

* **Catálogo Multimedia:** Gestión unificada de Películas y Series en un mismo lugar.
* **Vistas Avanzadas:** * **Vista Kanban:** Organizada por tipo (Película/Serie) con tarjetas visuales, estados dinámicos y un efecto de zoom en las portadas.
    * **Vista de Lista:** Resumen rápido con toggles de visionado rápido y badges dinámicos.
* **Buscador Inteligente (TMDB API):** Botón superior "Buscar y Autocompletar" que conecta en tiempo real con la base de datos de TMDB.
* **UI/UX Limpia e Intuitiva:** El cuadro de configuración de la API Key aparece dinámicamente arriba del todo si el sistema no tiene ninguna clave guardada, y **desaparece por completo** una vez configurada para no molestar.

---

## 🛠️ Estructura del Módulo

El módulo sigue una arquitectura limpia y adaptada a los estándares de desarrollo de Odoo 18:

```text
movie_series_tracker/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── movie.py                 # Modelo principal (movie.media y movie.genre)
│   └── res_config_settings.py   # Variables auxiliares para la API Key
├── security/
│   └── ir.model.access.csv      # Permisos de acceso del sistema
└── views/
    └── movie_views.xml          # Vistas (Kanban, List, Form, Search) y Menús