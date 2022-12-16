
import random
from uuid import UUID, uuid4
import uvicorn
import requests
from fastapi import FastAPI, HTTPException
from models import  User , Gender
from database import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Chek and add data to user 

def user_chek (user):
    if not user.id: 
        user.id =uuid4() 
    if not user.gender:
        user.gender =  random.choice(list(Gender)) 
    if not user.first_name or not user.last_name: 
        r = requests.get(url = 'http://app:8080/api/names').json()
        if not user.first_name:
            user.first_name = r["first_name"]
        if not user.last_name:
            user.last_name = r["last_name"]
    return user





@app.get("/")
def root():
    return {"Hello"" Please use /api/v1/users" +
            " GET  to see list of user" +
            " POST to add new user" +
            " POST /api/v1/randomusers to add new number of random user"
            " DELETE to remove  user by id"
    }

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.get("/api/v1/users/number")
async def fetch_users():
    return len(db) 

@app.post("/api/v1/users/random")
async def random_users(num:int):
    ids = []
    for x in range(num):
        us = User()
        us = (user_chek(us))
        db.append(us)
        ids.append(us.id)   
    return  ids 
    


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user_chek(user))
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not exists"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)