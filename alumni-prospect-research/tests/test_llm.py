import requests

response = requests.get("https://openrouter.ai/api/v1/models")

models = response.json()["data"]

for model in models:
    model_id = model["id"]

    if ":free" in model_id:
        print(model_id)