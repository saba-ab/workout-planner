# Use an official Python runtime as a base image
FROM python:3.10-slim

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=workout_planner.settings

# Run migrate and then run the command to start uWSGI
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
