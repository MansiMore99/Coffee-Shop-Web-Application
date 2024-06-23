## Django Coffee Shop Web Application

This repository contains a beginner-friendly Django project demonstrating the creation of a Coffee Shop web application. Learn how to use Django framework to build a simple yet functional web application where users can explore various coffee, tea, and milkshake options along with their prices. The application also includes a search feature for easy navigation.

## Getting Started:

Follow the steps below to set up and run the project locally:

## Installation

1. Clone the repository:

```
git clone https://github.com/your_username/django-coffee-shop.git
cd django-coffee-shop
```

2. Create a virtual environment:

```
python -m venv env
```

3. Activate the virtual environment:

On Windows:
```
.\env\Scripts\activate
```
On macOS and Linux:
```
source env/bin/activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```


## Usage:

1. Navigate to the project directory where manage.py is located.

2. Apply migrations:

```
python manage.py migrate
```

3. Create a superuser (admin):

```
python manage.py createsuperuser
```

4. Start the development server:

```
python manage.py runserver
```

5. Open your web browser and go to http://127.0.0.1:8000/ to view the application.

## Project Structure:


manage.py: Django project management script.
coffee_shop/: Main project folder.
settings.py: Project settings including database configuration, static files, etc.
urls.py: URL/path mapper for the project.
coffee_app/: Django application folder.
models.py: Database models for coffee shop items.
views.py: Views handling HTTP requests and rendering templates.
templates/: HTML templates for rendering pages.
static/: Static files (CSS, JavaScript, images).
