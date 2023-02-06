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
    "http://react:3000",
    "http://localhost:3000",
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
    if user.roles == []:
        user.reles.append('user')
    if not user.first_name or not user.last_name: 
        r = requests.get(url = 'http://servicegenerator:8080/api/names').json()
        if not user.first_name:
            user.first_name = r["first_name"]
        if not user.last_name:
            user.last_name = r["last_name"]
    if not user.password or not passwordCheck(user.password):
        password_response = requests.get(url = 'http://passwordgenerator:50/api/v1/passwords').json()
        user.password = password_response['password']        
    return user

def passwordCheck(password):
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(not char.isalnum() for char in password):
        return False
    if len(password) < 8 or len(password) > 16:
        return False
    return True 


@app.get("/")
def root():
    return {"Hello"" Please use /api/v1/users" +
            " GET  to see list of user" +
            " POST to add new user" +
            " POST /api/v1/randomusers to add new number of random user"
            " DELETE to remove  user by id"
    }

#fetch_users: Returns the list of users stored in the db variable.
@app.get("/api/v1/users")
async def fetch_users():
    return db

#fetch_users: Returns the number of users stored in the db.
@app.get("/api/v1/users/number")
async def fetch_users():
    return len(db) 

#random_users: Adds a specified number of random users to the db variable.
@app.post("/api/v1/users/random")
async def random_users(num:int):
    ids = []
    for x in range(num):
        us = User()
        us = (user_chek(us))
        db.append(us)
        ids.append(us.id)   
    return  ids 
    

#register_user: Adds a new user to the db variable.
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user_chek(user))
    return {"id": user.id}

#delete_user: Deletes a user with a specified ID from the db variable.
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