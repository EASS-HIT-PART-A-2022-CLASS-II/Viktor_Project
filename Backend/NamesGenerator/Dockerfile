FROM python:3.9-slim

WORKDIR /NamesGenerator
COPY . .


RUN pip install fastapi
RUN pip install "uvicorn[standard]"

EXPOSE 8080
# 


# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]