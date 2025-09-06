from fastapi import FastAPI
from api import *
app = FastAPI()

@app.get("/")
def root():
    return {"message": "SpeechWise Backend Running"}