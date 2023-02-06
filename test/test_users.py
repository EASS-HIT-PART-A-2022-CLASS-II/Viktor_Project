from codecs import register_error
import random
from uuid import UUID, uuid4
import uvicorn
import requests
from fastapi import FastAPI, HTTPException
from Backend.Main.main import delete_user, random_users, register_user, user_chek
from Backend.Main.models import  User , Gender
from Backend.Main.database import db
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from typing import Optional ,List
from pydantic import BaseModel
from Backend.Main.main import fetch_users



def test_user_chek():
    user = User()
    user = user_chek(user)
    assert user.id is not None
    assert user.gender in list(Gender)
    assert user.roles == ['user']
    assert user.first_name is not None
    assert user.last_name is not None

def test_fetch_users():

    db = [User(), User()]
    assert len(fetch_users()) == 2

def test_random_users():
    ids = random_users(3)
    assert len(ids) == 3
    assert all(isinstance(i, UUID) for i in ids)
    assert len(db) == 3

def test_register_user():
    user = User()
    register_error(user)
    assert user in db

def test_delete_user():
    user = User()
    user_id = user.id
    register_user(user)
    delete_user(user_id)
    assert user not in db;





def test_random_users():
    ids = random_users(3)
    assert len(ids) == 3
    assert all(isinstance(i, UUID) for i in ids)
    assert len(db) == 3

def test_register_user_invalid_input():
    user = User(first_name=None, last_name=None)
    response = register_user(user)
    assert response.status_code == 400
    assert response.json() == {"detail": "first_name and last_name are required"}    


def test_delete_user_not_found():
    user_id = uuid4()
    response = delete_user(user_id)
    assert response.status_code == 404
    assert response.json() == {"detail": f"user with id: {user_id} does not exists"}    



def test_user_chek_valid_input():
    user = User(first_name='John', last_name='Doe')
    user = user_chek(user)
    assert user.id is not None
    assert user.gender in list(Gender)
    assert user.roles == ['user']
    assert user.first_name is 'John'
    assert user.last_name is 'Doe'