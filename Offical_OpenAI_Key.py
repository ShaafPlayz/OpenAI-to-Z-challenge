import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("OPEN_AI_KEY")


client = OpenAI(
    api_key=token
)

response = client.chat.completions.create(
  model="gpt-4.1",
  messages=[],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.output_text)