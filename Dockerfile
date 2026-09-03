FROM python:3.12.8-slim-bookworm
WORKDIR /app
COPY . /app
CMD ["python3", "app.py"]
