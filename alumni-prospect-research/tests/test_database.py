from app.models.schemas import AlumniCreate


def test_schema():

    alumni = AlumniCreate(
        name="Ashima",
        company="Microsoft",
        designation="Data Analyst",
        city="Toronto",
        linkedin_url="https://linkedin.com/in/test",
        source="Manual",
        summary="Testing"
    )

    assert alumni.name == "Ashima"

    print("✅ Schema Test Passed")


if __name__ == "__main__":
    test_schema()