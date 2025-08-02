# backend/models.py
from sqlalchemy import Column, String, Text, Integer, Float, ARRAY
from database import Base

class EPCData(Base):
    __tablename__ = "epc_data"

    uprn = Column(String, primary_key=True, index=True)
    address = Column(Text)
    postcode = Column(String)
    rating = Column(String(1))
    potential_rating = Column(String(1))
    property_type = Column(String)
    built_form = Column(String)
    energy_consumption = Column(Integer)
    co2_emissions = Column(Float)
    recommendations = Column(ARRAY(Text))