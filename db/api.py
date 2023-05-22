from fastapi import FastAPI, Path, Query, HTTPException, status
import bdd

app = FastAPI()

database = r"bdd.db"

