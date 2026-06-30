# 🎬 Cine Tracker - Odoo 18 Module

![Cine Tracker Banner](static/description/cine_tracker_banner.png)

**Cine Tracker** is a custom module for **Odoo 18** designed for movie and TV series enthusiasts. It allows you to manage a personal multimedia catalog, classify works, rate them, and track what you've watched.

It features a **smart integration with the TMDB API (The Movie Database)** that automatically autocompletes genres (adding them as color tags), synopsis, release year, and downloads the official cover art with just the title.

---

## 🌐 Live Demo

> **Try it now on Oracle Cloud!**

👉 **[Access the Live Demo](http://51.170.44.49:8069)**

**Demo Credentials:**
- **Email:** `demo@demo.com`
- **Password:** `demo123`

> **ℹ️ Note:** The first time you search for a movie, you'll need to configure your free TMDB API Key. Follow the [TMDB API Configuration](#-tmdb-api-configuration) section below.

*This demo is hosted on an **Oracle Cloud Always Free** server.*

---

## ✨ Key Features

- **Unified Multimedia Catalog:** Manage Movies and TV Series in one place.
- **Advanced Views:**
  - **Kanban View:** Organized by type (Movie/Series) with visual cards, dynamic status badges, and hover zoom effects on posters.
  - **List View:** Quick overview with fast watch toggles and dynamic status badges.
- **Smart Search (TMDB API):** One-click "Search & Autocomplete" button that connects in real-time to the TMDB database.
- **Clean & Intuitive UI:** The API Key configuration box appears dynamically at the top when no key is saved and **disappears completely** once configured.

---

## 🛠️ Module Structure

The module follows a clean architecture adapted to Odoo 18 standards:

```text
movie_series_tracker/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── movie.py                 # Main model (movie.media and movie.genre)
│   └── res_config_settings.py   # Auxiliary variables for API Key
├── security/
│   └── ir.model.access.csv      # System access permissions
├── static/
│   └── description/
│       ├── banner.png           # Module banner image
│       └── icon.png             # Module icon
└── views/
    └── movie_views.xml          # Views (Kanban, List, Form, Search) & Menus
📦 Installation

    Copy the module folder into your Odoo addons directory.

    Go to Apps → Update Apps List.

    Search for "Cine Tracker".

    Click Install.

🔑 TMDB API Configuration

    Create a free account at: https://www.themoviedb.org/

    Go to your profile → Settings → API

    Request an API Key (it's instant and free)

    In Odoo, go to Settings → Cine Tracker Configuration (or Technical → System Parameters → tmdb_api_key)

    Paste your API Key and click Save

The configuration panel will automatically disappear once the API Key is set.
🚀 Deployment on Oracle Cloud

This module is currently running on an Oracle Cloud Always Free instance:

    Server: Oracle Cloud (Ampere A1 instance)

    OS: Ubuntu 22.04 LTS

    Odoo Version: 18.0 (Docker container)

    Database: PostgreSQL 15

    Access: http://51.170.44.49:8069

Deployment Commands (for reference):
bash

# Clone the repository
git clone https://github.com/mateogoranDev/movie_series_tracker.git

# Copy to Odoo addons
cp -r movie_series_tracker /home/ubuntu/odoo18_project/custom_addons/

# Update and install module
docker exec -it odoo18-web odoo -u movie_series_tracker -d movie_tracker --stop-after-init

💡 Perfect For

    Movie collectors

    TV series enthusiasts

    Home cinema lovers

    Personal media management

❤️ Why Cine Tracker?

Unlike generic catalog applications, Cine Tracker is fully integrated into Odoo and follows its native interface.

It combines:

    ✅ Beautiful UI

    ✅ Automatic metadata from TMDB

    ✅ Fast management

    ✅ Odoo ORM architecture

    ✅ Native Odoo experience

👨‍💻 Author

Mateogoran

    GitHub: github.com/mateogoranDev

    Email: mateogoran7bc@gmail.com

⭐ Support the Project

If you enjoy this module:

    ⭐ Rate it on Odoo Apps

    ⭐ Follow future releases

    ⭐ Report issues and suggestions

📄 License

LGPL-3
Enjoy managing your personal movie collection! 🎬