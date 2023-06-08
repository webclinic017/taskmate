FROM python:3.8.16-slim-bullseye

# Set the working directory
WORKDIR /run

RUN apt-get update && apt-get install -y netcat

# Copy requirements.txt and install dependencies
RUN python -m venv venv
COPY requirements.txt ./requirements.txt
RUN venv/bin/pip3 install -r requirements.txt

# Copy required code
COPY web ./web
COPY migrations ./migrations
COPY boot.sh gunicorn.conf.py ./

# Pass db environment variable
ARG DATABASE_HOST
ENV DATABASE_HOST=${DATABASE_HOST}

ARG DATABASE_PORT
ENV DATABASE_PORT=${DATABASE_PORT}

# Run the application
EXPOSE 5001
RUN chmod a+x boot.sh
ENTRYPOINT ["./boot.sh"]