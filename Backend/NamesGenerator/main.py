import random
import uvicorn
from fastapi import FastAPI

from names import DataNames

app = FastAPI()

@app.get("/api/names")
async def fetch_users():
    return(DataNames[random.randint(0,len(DataNames)-1)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)    