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
For creating a Google API KEY, take a look [here](https://ai.google.dev/gemini-api/docs/oauth)

```shell
echo "GOOGLE_API_KEY='<API_KEY>' > .env"
```

4. Run the tool

```shell
python ./gemini_calculator.py
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

2. Run interactively

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

### Pricing model

The prices are taken from [here](https://ai.google.dev/pricing) and are placed in the code as constants: `INPUT_PRICING_LOW`, `OUTPUT_PRICING_LOW`, `INPUT_PRICING_HIGH`, `OUTPUT_PRICING_HIGH`.