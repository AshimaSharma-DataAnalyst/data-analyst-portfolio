from app.database.database import SessionLocal
from app.services.etl_service import ETLPipeline

db = SessionLocal()

etl = ETLPipeline(db)

df = etl.load_csv("data/alumni.csv")

results = etl.process_dataframe(df)

print()

print("=" * 70)

for alumni in results:

    if alumni:

        print(alumni.id)

        print(alumni.name)

        print(alumni.company)

        print(alumni.designation)

        print("-" * 60)

db.close()
