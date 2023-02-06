from Backend.NamesGenerator.main import fetch_users
import random
import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from Backend.NamesGenerator.names import DataNames



def test_fetch_users():
    response = fetch_users()
    assert 'first_name' in response
    assert 'last_name' in response

def test_fetch_users_randomness():
    # check that calling the function multiple times returns different results
    results = set()
    for _ in range(10):
        results.add(fetch_users())
    assert len(results) > 1