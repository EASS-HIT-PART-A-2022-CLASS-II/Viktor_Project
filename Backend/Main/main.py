
import random
from uuid import UUID, uuid4
import uvicorn
import requests
from fastapi import FastAPI, HTTPException
from models import  User , Gender
from database import db

app = FastAPI()

@app.get("/")
def root():
    return {"Hello"" Please use /api/v1/users" +
            " GET  to see list of user" +
            " POST to add new user" +
            " DELETE to remove  user by id" 
    }

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    if not user.id: 
        user.id =uuid4() 
    if not user.gender:
        user.gender =  random.choice(list(Gender)) 
    if not user.first_name or not user.last_name: 
        r = requests.get(url = 'http://localhost:8080/api/names').json()
        if not user.first_name:
            user.first_name = r["first_name"]
        if not user.last_name:
            user.last_name = r["last_name"]
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not found"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)