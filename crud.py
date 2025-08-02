# backend/crud.py
from sqlalchemy.orm import Session
from models import EPCData


def get_all_properties(db: Session):
    return db.query(EPCData).all()


def get_property(db: Session, uprn: str):
    return db.query(EPCData).filter(EPCData.uprn == uprn).first()


def search_by_postcode(db: Session, q: str):
    return db.query(EPCData).filter(EPCData.postcode.ilike(f"%{q}%")).all()


def filter_by_rating(db: Session, rating: str):
    return db.query(EPCData).filter(EPCData.rating == rating.upper()).all()


def get_average_rating(db: Session):
    from sqlalchemy import func
    ratings = db.query(EPCData.rating).all()
    rating_map = {"A": 7, "B": 6, "C": 5, "D": 4, "E": 3, "F": 2, "G": 1}
    nums = [rating_map.get(r[0].upper(), 0) for r in ratings if r[0]]
    return {"average_numeric_rating": round(sum(nums) / len(nums), 2)} if nums else {}


def get_top_improvements(db: Session):
    from collections import Counter
    all_recs = db.query(EPCData.recommendations).all()
    flat_list = [item for sublist in all_recs if sublist[0] for item in sublist[0]]
    most_common = Counter(flat_list).most_common(5)
    return [{"recommendation": rec, "count": cnt} for rec, cnt in most_common]
