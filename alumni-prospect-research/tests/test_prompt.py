from app.services.prompt_service import PromptService

prompt_service = PromptService()

profile = {

    "name": "Satya Nadella",

    "company": "Microsoft",

    "designation": "CEO",

    "education": "Manipal Institute of Technology",

    "city": "Hyderabad"

}

prompt = prompt_service.build_prompt(profile)

print("=" * 70)

print(prompt)

print("=" * 70)
