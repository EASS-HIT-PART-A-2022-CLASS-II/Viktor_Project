
import random
import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from names import DataNames


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
@app.get("/api/names")
async def fetch_users():
    return(DataNames[random.randint(0,len(DataNames)-1)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)    