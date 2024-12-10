### Requirements

- Python 3.10+
- Django 4.2+
- Ninja 0.1.0+

### Create a Django Project

```bash
django-admin startproject projectname .
```

### Local Environment

```bash
python -m venv .env
source .env/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run

In src directory run:
```bash
python manage.py runserver
```

### Open API
When you run the server, you can access the API documentation at:
```bash
http://127.0.0.1:8000/api/docs
```
