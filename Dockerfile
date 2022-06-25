# Main docker image
FROM python:3.8

# Enviroment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /get_docs
WORKDIR /get_docs

COPY . .

# Installing dependencies
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:80

# Django service port
EXPOSE 80