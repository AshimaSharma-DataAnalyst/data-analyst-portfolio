from app.services.research_service import ResearchService

research = ResearchService()

sample = {

    "name": "Satya Nadella",

    "company": "Microsoft",

    "designation": "CEO",

    "education": "Manipal Institute of Technology",

    "city": "Hyderabad"

}

profile = research.build_profile(sample)

print("=" * 70)

for key, value in profile.items():

    print(f"{key}: {value}")