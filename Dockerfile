FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=workout_planner.settings

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
