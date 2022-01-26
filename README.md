# UUID Generator

A guide to starting up the project on your pc - requires python

Setting up Django on your pc

#### First, create a .env file from .env.example
#### The .env.example file has been filled to make it easy for you to run as this is a test project.

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# Visit localhost:8000/api/
```