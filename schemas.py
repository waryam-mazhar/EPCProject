# backend/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class EPCDataSchema(BaseModel):
    uprn: str
    address: str
    postcode: str
    rating: str
    potential_rating: str
    property_type: str
    built_form: str
    energy_consumption: int
    co2_emissions: float
    recommendations: Optional[List[str]]

    class Config:
        orm_mode = True