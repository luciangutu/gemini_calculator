import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

if not sys.stdin.isatty():
    prompt = sys.stdin.read().strip()
else:
    prompt = input("Enter your prompt: ").strip()

# https://ai.google.dev/pricing
INPUT_PRICING_LOW = 0.075 / 1000000
OUTPUT_PRICING_LOW = 0.30 / 1000000
INPUT_PRICING_HIGH = 0.15 / 1000000
OUTPUT_PRICING_HIGH = 0.60 / 1000000

# print('Available base models:', [m.name for m in genai.list_models()])

model = genai.GenerativeModel("models/gemini-1.5-flash")

response = model.generate_content(prompt)

response_metadata = response.usage_metadata
input_tokens = int(response_metadata.prompt_token_count)
output_tokens = int(response_metadata.candidates_token_count)

print(response.text)
print(f'{input_tokens=}')
print(f'{output_tokens=}')

if input_tokens <= 128000:
    input_token_cost = input_tokens * INPUT_PRICING_LOW
    output_token_cost = output_tokens * OUTPUT_PRICING_LOW
else:
    input_token_cost = input_tokens * INPUT_PRICING_HIGH
    output_token_cost = output_tokens * OUTPUT_PRICING_HIGH

print(f'Input costs: ${input_token_cost:.8f}')
print(f'Output costs: ${output_token_cost:.8f}')
print(f'Total cost: ${input_token_cost + output_token_cost:.8f}')
