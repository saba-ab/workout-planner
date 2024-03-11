# Django Workout Planner Project

## Project Ovrrview

The Django Workout Planner is a dope RESTful API designed to help users make, manage, and keep track of their personalized workout plans. This project's got secure user login stuff, a bunch of predefined exercises, customizable workout plans, prgress tracking, and API docs. Made with Django and Django REST Framework, and it's all set up to run in Docker cuz it's cooler that way.

## Key Features

- **User Authentication**: Takes care of user sign up, login, and logout with JWT to keep sessions secure.
- **Predefined Exercises Database**: Got abig ol' list of exercises with all the deets like what they are, how to do 'em, and which muscles they work.
- **Personalized Workout Plans**: Lets users make their own workout plans with how often they wanna work out, their goals, picking exercises, and how long they wanna go for.
- **Tracking and Goals**: Users can track how they're doing over time, like how much they weigh and if they're hitting their fitness targets.
- **API Documentation**: We use Swagger so you can easily see and try out what the API can do.

## Tech Stack

- **Backend Framework**: Django / Django REST Framework
- **Database**: SQLite (simple and good for starting out)
- **Authentication**: JWT (for keeping things secure)
- **Documentation**: Swagger (makes understanding the API a breeze)
- **Containerization**: Docker (because containers are awesome)

## Getting Started

### You Gotta Have

- Docker
- Docker Compose

### Setup and Installation

1. **Grab the code:**

   ```bash
   git clone https://github.com/yourusername/workout-planner.git
   cd workout-planner
   docker-compose up --build
   ```

The API's at http://localhost:8000/api/,
and the Django admin panel's over at http://localhost:8000/admin/.

Use http://localhost:8000/docs/ to test with Swagger ui
