FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && poetry install
COPY . /app
CMD ["pytest"]