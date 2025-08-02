# backend/seed_data.py
import csv
from sqlalchemy.orm import Session
from backend.models import EPCData
from backend.database import SessionLocal, engine, Base

csv_file = "Sample_EPC_Data.csv"

Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if db.query(EPCData).filter_by(uprn=row['uprn']).first():
            continue
        epc = EPCData(
            uprn=row['uprn'],
            address=row['address'],
            postcode=row['postcode'],
            rating=row['rating'],
            potential_rating=row['potential_rating'],
            property_type=row['property_type'],
            built_form=row['built_form'],
            energy_consumption=int(row['energy_consumption']),
            co2_emissions=float(row['co2_emissions']),
            recommendations=row['recommendations'].strip('{}').split('|') if row['recommendations'] else []
        )
        db.add(epc)
    db.commit()

db.close()
print("✅ Seeding complete.")
