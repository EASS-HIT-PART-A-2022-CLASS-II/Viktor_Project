FROM python:3.9-slim


WORKDIR /Main
COPY . .



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

