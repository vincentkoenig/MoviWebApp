# MoviWebApp 🎬

A multi-user web application for managing personal movie collections. Each user gets their own movie list — add any film by title and the app fetches title, director, year, and poster automatically from the **OMDb API**.

## Features

- 👥 **Multi-user support** — create multiple users, each with their own movie collection
- 🔍 **OMDb API integration** — add movies by title; poster, director, and year are fetched automatically
- ✏️ **Update movies** — edit title, director, and year of any saved movie
- 🗑️ **Delete movies** — remove any movie from a user's collection
- 🖼️ **Movie posters** — poster images fetched and displayed directly from OMDb
- ⚠️ **Custom error pages** — dedicated 404 and 500 error templates
- 💾 **SQLite database** — persistent storage via SQLAlchemy ORM

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

## Data Model

```
User                        Movie
────────────────            ──────────────────────
id (PK)                     id (PK)
name                        name
                            director
                            year
                            poster_url
                            user_id (FK → user.id)
```

Each user can have many movies. Movies are linked to their owner via a foreign key.

## Project Structure

```
MoviWebApp/
├── app.py              # Flask routes & application logic
├── data_manager.py     # DataManager class — database query logic
├── models.py           # SQLAlchemy models (User, Movie)
├── data/
│   └── movies.db       # SQLite database (auto-created on first run)
└── templates/
    ├── index.html      # User list & create user form
    ├── movies.html     # Movie list per user
    ├── 404.html        # Custom 404 error page
    └── 500.html        # Custom 500 error page
```

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | List all users |
| `POST` | `/users` | Create a new user |
| `GET` | `/users/<id>/movies` | Show movies for a user |
| `POST` | `/users/<id>/movies` | Add a movie (fetched from OMDb) |
| `POST` | `/users/<id>/movies/<id>/update` | Update movie details |
| `POST` | `/users/<id>/movies/<id>/delete` | Delete a movie |

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/MoviWebApp.git
cd MoviWebApp
```

**2. Install dependencies**
```bash
pip install flask flask-sqlalchemy python-dotenv requests
```

**3. Create a `.env` file with your OMDb API key**
```
API_KEY=your_api_key_here
```
> Get a free key at [omdbapi.com](http://www.omdbapi.com/)

**4. Run the app**
```bash
python app.py
```

The database is created automatically on first run via `db.create_all()`.

**5. Open in your browser**
```
http://localhost:5000
```

## What I Learned

- Building a multi-user Flask application with user-scoped data
- Integrating a third-party REST API (OMDb) with secure key management via `python-dotenv`
- Separating database logic into a dedicated `DataManager` class
- Designing a SQLAlchemy data model with a foreign key relationship between User and Movie
- Handling API errors gracefully (movie not found, unreachable API) with appropriate HTTP responses
- Creating custom error pages for 404 and 500 errors in Flask
