import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Get model pricing for a Gemini model.', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--gemini_model', type=str, default='gemini-1.5-flash',
                    help='''The gemini model to get pricing for (default: gemini-1.5-flash)
Available choices: gemini-1.5-flash, gemini-1.5-pro or gemini-1.0-pro
                    ''')

args = parser.parse_args()
gemini_model = args.gemini_model

# https://ai.google.dev/pricing
model_pricing = {
    "gemini-1.5-flash": {
        "INPUT_PRICING_LOW": 0.075 / 1000000,
        "OUTPUT_PRICING_LOW": 0.30 / 1000000,
        "INPUT_PRICING_HIGH": 0.15 / 1000000,
        "OUTPUT_PRICING_HIGH": 0.60 / 1000000
    },
    "gemini-1.5-pro": {
        "INPUT_PRICING_LOW": 1.25 / 1000000,
        "OUTPUT_PRICING_LOW": 5 / 1000000,
        "INPUT_PRICING_HIGH": 2.5 / 1000000,
        "OUTPUT_PRICING_HIGH": 10 / 1000000
    },
    "gemini-1.0-pro": {
        "INPUT_PRICING_LOW": 0.5 / 1000000,
        "OUTPUT_PRICING_LOW": 1.5 / 1000000,
        "INPUT_PRICING_HIGH": 0.5 / 1000000,
        "OUTPUT_PRICING_HIGH": 1.5 / 1000000
    }
}

if gemini_model not in model_pricing:
    print("ERROR: Invalid model choice.\n")
    parser.print_help()
    sys.exit(1)

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

if not sys.stdin.isatty():
    prompt = sys.stdin.read().strip()
else:
    prompt = input("Enter your prompt: ").strip()

# print('Available base models:', [m.name for m in genai.list_models()])

model = genai.GenerativeModel(f"models/{gemini_model}")

response = model.generate_content(prompt)

response_metadata = response.usage_metadata
input_tokens = int(response_metadata.prompt_token_count)
output_tokens = int(response_metadata.candidates_token_count)

print(response.text)
print(f'{input_tokens=}')
print(f'{output_tokens=}')

if input_tokens <= 128000:
    input_token_cost = input_tokens * model_pricing[gemini_model]["INPUT_PRICING_LOW"]
    output_token_cost = output_tokens * model_pricing[gemini_model]["OUTPUT_PRICING_LOW"]
else:
    input_token_cost = input_tokens * model_pricing[gemini_model]["INPUT_PRICING_HIGH"]
    output_token_cost = output_tokens * model_pricing[gemini_model]["OUTPUT_PRICING_HIGH"]

print(f'Costs using {model_pricing} model:')
print(f'Input costs: ${input_token_cost:.8f}')
print(f'Output costs: ${output_token_cost:.8f}')
print(f'Total cost: ${input_token_cost + output_token_cost:.8f}')
