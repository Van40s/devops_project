FROM python:3.12-slim-bookworm

WORKDIR app

COPY requirements.txt .

RUN pip install -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app

# Define env APP_SCRIPT_PATH when running the container
CMD ["sh", "-c", "python $APP_SCRIPT_PATH"]