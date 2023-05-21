from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import db

app = FastAPI()

database = r"bdd.db"