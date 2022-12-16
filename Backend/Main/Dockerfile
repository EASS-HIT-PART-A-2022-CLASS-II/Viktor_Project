FROM python:3.9-slim


WORKDIR /Main
COPY . .
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install requests


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

