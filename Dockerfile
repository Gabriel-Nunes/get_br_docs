# # Main docker image
# FROM python:3.8

# # Enviroment variables
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# RUN mkdir /get_docs
# WORKDIR /get_docs

# COPY . .

# # Installing dependencies
# RUN apt-get update -y
# # RUN apt-get install software-properties-common -y
# # RUN apt-get install sudo ufw build-essential libpq-dev python3.8-dev libpython3.8-dev -y
# RUN pip install --upgrade pip setuptools
# RUN pip install -r requirements.txt
# # RUN chmod +x run_dev.sh
# # CMD ./run_dev.sh

# ENTRYPOINT [ "sh", "/get_docs/entrypoint.sh" ]

# # Django service port
# EXPOSE 8000

# # VOLUME /home/gabriel/workspace/get_br_docs/media /get_docs/media

# ================================================================
# # Use the official Python image
# FROM python:3.8

# # Set the working directory to /app
# WORKDIR /get_br_docs

# # Copy the requirements file to the container
# COPY requirements.txt .

# # Install the required packages
# RUN apt update && apt upgrade -y
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the source code to the container
# COPY . .

# # Run migrations to create the database
# RUN python manage.py migrate

# # Expose port 8000 for gunicorn
# EXPOSE 8000

# # Start gunicorn
# CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "get_br_docs.wsgi:application"]

# FROM ubuntu:20.04
# ADD . /get_docs
# WORKDIR /get_docs
# RUN apt-get update -y
# RUN apt-get install software-properties-common -y
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt-get install python3.8 -y
# RUN apt-get install python3-pip -y
# RUN python3.8 -m pip install --upgrade setuptools
# RUN apt-get install sudo ufw build-essential libpq-dev python3.8-dev libpython3.8-dev -y
# RUN python3.8 -m pip install -r requirements.txt
# RUN python3.8 -m pip install psycopg2-binary
# RUN sudo ufw allow 8000
# EXPOSE 8000


# ====================================================
FROM python:3.8
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "entrypoint.sh"]