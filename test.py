import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
APIKEY=os.getenv("OpenRouterAPIKey")


while True:
  prompt = input(str("Enter prompt: "))
  if not prompt:
    break
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer {APIKEY}",
      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model": "openrouter/owl-alpha",
      "messages": [
        {
          "role": "user",
          "content": f"{prompt}"
        }
      ]
    })
  )
  data = response.json()
  print(data['choices'][0]['message']['content'])