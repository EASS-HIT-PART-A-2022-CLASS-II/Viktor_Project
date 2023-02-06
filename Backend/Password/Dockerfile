FROM python:3.9-slim

WORKDIR /Password
COPY . .


RUN pip install fastapi
RUN pip install "uvicorn[standard]"

EXPOSE 50
# 


# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50"]