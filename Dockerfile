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
RUN chmod +x run_dev.sh
CMD ./run_dev.sh

# Django service port
EXPOSE 80