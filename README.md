# Django Workout Planner Project

## Project Overview

The Django Workout Planner is a robust RESTful API designed to assist users in creating, managing, and tracking personalized workout plans. This project emphasizes secure user authentication, a rich database of predefined exercises, customizable workout plans, progress tracking, and comprehensive API documentation. Developed with Django and Django REST Framework, it features containerized deployment using Docker.

## Key Features

- **User Authentication**: Securely handles user registration, login, and logout with JWT for session management.
- **Predefined Exercises Database**: Features an extensive list of exercises each with detailed descriptions, execution instructions, and target muscles.
- **Personalized Workout Plans**: Enables users to create and manage customized workout plans, specifying workout frequency, goals, exercise selection, and session durations.
- **Tracking and Goals**: Allows users to track their fitness progress over time, including weight and personal fitness achievements.
- **API Documentation**: Implemented with Swagger for straightforward endpoint testing and interaction.

## Tech Stack

- **Backend Framework**: Django / Django REST Framework
- **Database**: SQLite
- **Authentication**: JWT
- **Documentation**: Swagger
- **Containerization**: Docker

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/workout-planner.git
   cd workout-planner
   ```

2. **Environment Configuration:**
   Create a `.env` file in the project root directory and fill in your environment variables:

   ```env
   SECRET_KEY=your_secret_key
   ```

3. **Build and Run with Docker:**
   Use Docker Compose to build and run your application:

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker image for the project and starts the containers defined in your `docker-compose.yml` file.

4. **Create a superuser account (optional):**
   After your containers are up and running, you can create a superuser account to access the Django admin:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Accessing the Application:**
   The API will be available at `http://localhost:8000/api/`, and you can access the Django admin interface at `http://localhost:8000/admin/`.

### API Documentation

The API documentation, powered by Swagger, is accessible at `http://localhost:8000/docs/`. This documentation provides a detailed overview of available endpoints, request formats, and response data.

## Usage Examples

Include examples of how to interact with the API, such as registering a new user, logging in, creating workout plans, adding exercises to a plan, and tracking progress.

## Deployment

Instructions for deploying the application in a production environment, including setting `DEBUG` to `False`, configuring secure environment variables, and scaling with Docker Compose or deploying to cloud services.
