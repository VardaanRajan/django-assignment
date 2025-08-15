# Django Chai Project

A Django web application for managing and showcasing different varieties of Indian chai (tea). Users can view various types of chai, their details, and add new varieties through the admin interface.

## Features

- 🫖 Display different types of chai (Masala, Elaichi, Green Tea, etc.)
- 📸 Image upload support for each chai variety
- 🔍 Detailed view for individual chai types
- 📱 Responsive design
- 👩‍💼 Admin interface for content management

## Tech Stack

- Django 4.x
- Python 3.x
- SQLite Database
- HTML/CSS
- Bootstrap classes

## Installation

1. Clone the repository:
```bash
git clone https://github.com/atharvabarve08/django-chai-project.git
cd django-chai-project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Usage

- Access the main application: `http://127.0.0.1:8000/chai/`
- Admin interface: `http://127.0.0.1:8000/admin/`
- View chai details: `http://127.0.0.1:8000/chai/<id>/`

## Project Structure

```
DjangoProject/
├── chai/                   # Main app directory
│   ├── templates/         # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── forms.py          # Forms
│   └── urls.py           # URL configurations
├── media/                 # Uploaded images
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Atharva Barve
