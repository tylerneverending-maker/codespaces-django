# Copilot Instructions for codespaces-django

## Project Overview
- This is a Django web application scaffolded for use in GitHub Codespaces.
- The main Django app is `hello_world`, with core logic in `hello_world/core/`.
- Static files are in `hello_world/static/` and templates in `hello_world/templates/`.
- The project uses SQLite by default (`db.sqlite3`).

## Key Workflows
- **Install dependencies:**
  ```sh
  pip install -r requirements.txt
  ```
- **Run the development server:**
  ```sh
  python manage.py runserver
  ```
- **Collect static files:**
  ```sh
  python manage.py collectstatic
  ```

## Project Structure & Conventions
- All Django settings are in `hello_world/settings.py`.
- Views are implemented in `hello_world/core/views.py`.
- The main URL configuration is in `hello_world/urls.py`.
- Static assets (e.g., CSS) go in `hello_world/static/`.
- HTML templates are in `hello_world/templates/`.
- No custom management commands or apps beyond `core` are present by default.

## Patterns & Integration
- Use Django's standard class/function-based views and template rendering.
- No REST API or external service integration is scaffolded by default.
- The project is designed for rapid prototyping and experimentation in Codespaces.

## Examples
- To add a new view, edit `hello_world/core/views.py` and register it in `hello_world/urls.py`.
- To add a new template, place it in `hello_world/templates/` and reference it from your view.
- To add static files, place them in `hello_world/static/` and use `{% static 'main.css' %}` in templates.

## Additional Notes
- There are no project-specific linting, testing, or CI/CD workflows defined yet.
- See `README.md` for the latest developer instructions.
