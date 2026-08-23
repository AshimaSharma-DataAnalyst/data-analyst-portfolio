from app.database.database import Base
from app.database.database import engine

from app.models.alumni import Alumni


def initialize_database():

    Base.metadata.create_all(bind=engine)

    print("Database initialized.")