# Full-Stack Developer Capstone Project

## Project Overview

This is the xrwvm-fullstack_developer_capstone project - a comprehensive full-stack web application for Cars Dealership, a national car retailer in the U.S. The application allows users to view dealership branches, read and submit reviews for dealerships, and interact with a responsive web interface.

## Technology Stack

### Backend
- **Django 5.2.9** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Database (development)
- **MongoDB** - Database (production, optional)

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **Node.js 23.5.0** - JavaScript runtime
- **npm 10.9.2** - Package manager

### Deployment & DevOps
- **Docker** - Containerization
- **Kubernetes** - Orchestration
- **IBM Cloud Code Engine** - Cloud deployment
- **GitHub Actions** - CI/CD pipeline

## Features

### Core Functionality
- **Dealership Management**: View all dealership locations across the U.S.
- **Review System**: Read and submit reviews for dealerships
- **User Authentication**: Registration, login, and logout functionality
- **Car Inventory**: Browse available car makes and models
- **Sentiment Analysis**: Automatic sentiment analysis of reviews

### API Endpoints
- `GET /api/dealers/` - Retrieve all dealers
- `GET /api/dealers/<id>/` - Get specific dealer details
- `GET /api/dealers/state/<state>/` - Get dealers by state
- `GET /api/reviews/dealer/<dealer_id>/` - Get reviews for a dealer
- `POST /api/reviews/post/` - Submit a new review
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/register/` - User registration
- `GET /api/dealers/makes/` - Get all car makes and models
- `POST /api/reviews/analyze/` - Analyze review sentiment

## Project Structure

```
cars-dealership/
├── server/                          # Django backend
│   ├── dealers/                     # Dealers app
│   ├── reviews/                     # Reviews app
│   ├── frontend/                    # React frontend
│   ├── server/                      # Django settings
│   ├── manage.py                    # Django management script
│   └── db.sqlite3                   # SQLite database
├── README.md                        # Project documentation
└── requirements.md                  # Assignment requirements
```

## Installation & Setup

### Backend Setup
```bash
cd server
pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py runserver
```

### Frontend Setup
```bash
cd server/frontend
npm install
npm start
```

## Development Team

This application was developed as part of the Coursera Full-Stack Development Capstone Project, demonstrating skills in:
- Full-stack web development
- RESTful API design
- Database modeling and management
- Frontend-backend integration
- Responsive UI design
- Containerization and deployment
- CI/CD pipeline implementation
- Microservices architecture
- Sentiment analysis

## License

This project is developed for educational purposes as part of the Coursera curriculum.
