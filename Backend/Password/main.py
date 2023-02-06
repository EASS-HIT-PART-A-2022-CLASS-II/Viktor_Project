
import uvicorn
import string
import random
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
origins = [
    "http://react:3000",
    "http://servicemain:80",
    "http://localhost:80",
    "http://localhost:3000"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#returns Random name and Last Name
@app.get("/api/v1/passwords")
async def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    password = list(password)
    password[random.randint(0, len(password) - 1)] = random.choice(string.ascii_uppercase)
    password[random.randint(0, len(password) - 1)] = random.choice(string.digits)
    password[random.randint(0, len(password) - 1)] = random.choice(string.punctuation)
    random.shuffle(password)
    password = ''.join(password[:8 + random.randint(0, 8)])
    return {"password": password}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=50)    