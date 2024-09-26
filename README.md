# GeminiAI price calculator

GeminiAI price calculator written in Python.

You can read [here](https://ai.google.dev/gemini-api/docs/tokens?lang=python) about tokens.



### How to run it

1. Git clone this repo

2. Install the requirements
```shell
pip install -r requirements.txt
```

3. Configure the Google API KEY

For creating a Google API KEY, take a look [here](https://ai.google.dev/gemini-api/docs/oauth) or [here](https://aistudio.google.com/app/plan_information)

```shell
echo "GOOGLE_API_KEY='<API_KEY>' > .env"
```

4. Run the tool

```shell
python ./gemini_calculator.py
```

5. CLI ARGS

```shell
python ./gemini_calculator.py --help
usage: gemini_calculator.py [-h] [--gemini_model GEMINI_MODEL]

Get model pricing for a Gemini model.

options:
  -h, --help            show this help message and exit
  --gemini_model GEMINI_MODEL
                        The gemini model to get pricing for (default: gemini-1.5-flash)
                        Available choices: gemini-1.5-flash, gemini-1.5-pro or gemini-1.0-pro
```

### Example Usage

1. Run with standard input

```shell
echo "What is the capital of France?" | python ./gemini_calculator.py
The capital of France is **Paris**. 

input_tokens=8
output_tokens=8
Input costs: $0.00000060
Output costs: $0.00000240
Total cost: $0.00000300
```

2. Run interactively (with the default flash model)

```shell
python ./gemini_calculator.py
Enter your prompt: What is the capital of France?
The capital of France is **Paris**. 

input_tokens=8
output_tokens=8
Input costs: $0.00000060
Output costs: $0.00000240
Total cost: $0.00000300
```

3. Run with `gemini-1.5-pro` model

```shell
python ./gemini_calculator.py --gemini_model gemini-1.5-pro
Enter your prompt: what is the capital of france?
The capital of France is **Paris**. 🇫🇷 

input_tokens=8
output_tokens=11
Input costs: $0.00001000
Output costs: $0.00005500
Total cost: $0.00006500
```

4. Run with `gemini-1.0-pro` model

```shell
Enter your prompt: what is the capital of france?
Paris
input_tokens=8
output_tokens=1
Input costs: $0.00000400
Output costs: $0.00000150
Total cost: $0.00000550
```

### Pricing model

The prices are taken from [here](https://ai.google.dev/pricing) and are placed in the code as constants: `INPUT_PRICING_LOW`, `OUTPUT_PRICING_LOW`, `INPUT_PRICING_HIGH`, `OUTPUT_PRICING_HIGH`.