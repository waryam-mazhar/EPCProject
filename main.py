# backend/main.py
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from models import EPCData
from schemas import EPCDataSchema
import crud

app = FastAPI()

origins = [
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "test-api-key"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

Base.metadata.create_all(bind=engine)

@app.get("/properties", dependencies=[Depends(verify_api_key)])
def get_properties(db: Session = Depends(get_db)):
    return crud.get_all_properties(db)

@app.get("/properties/{uprn}", dependencies=[Depends(verify_api_key)])
def get_property(uprn: str, db: Session = Depends(get_db)):
    return crud.get_property(db, uprn)

@app.get("/properties/search", dependencies=[Depends(verify_api_key)])
def search_by_postcode(q: str, db: Session = Depends(get_db)):
    return crud.search_by_postcode(db, q)

@app.get("/properties/filter", dependencies=[Depends(verify_api_key)])
def filter_by_rating(rating: str, db: Session = Depends(get_db)):
    return crud.filter_by_rating(db, rating)

@app.get("/stats/average-rating", dependencies=[Depends(verify_api_key)])
def average_rating(db: Session = Depends(get_db)):
    return crud.get_average_rating(db)

@app.get("/stats/top-improvements", dependencies=[Depends(verify_api_key)])
def top_improvements(db: Session = Depends(get_db)):
    return crud.get_top_improvements(db)
