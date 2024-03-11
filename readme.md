# Prompt Optimizer

Prompt Optimizer is a Python script that automates the process of prompt engineering using Anthropic's Claude language model. It follows a workflow inspired by Alex Albert's [Twitter thread](https://twitter.com/alexalbert__/status/1767258557039378511) on prompt engineering with Claude.

## Features

- Generates a diverse test dataset based on an initial prompt
- Tests the prompt on the generated test cases and collects user evaluations
- Saves the test results to a CSV file
- Generates an improved prompt based on the user evaluations

## Prerequisites

- Python 3.x
- Anthropic API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AarushSah/prompt-optimizer.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Anthropic API key:

- Create a `.env` file in the project directory
- Add your API key to the `.env` file in the following format:

```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

1. Run the script:

```bash
python main.py
```

2. Enter your initial prompt when prompted.

3. The script will generate a test dataset based on your initial prompt and display the test cases.

4. For each test case, the script will display the generated response and prompt you to enter an evaluation. Enter your evaluation and press Enter to move to the next test case. If you don't want to provide an evaluation, simply press Enter without typing anything. To exit the evaluation process early, type "exit" and press Enter.

5. After evaluating all the test cases, the script will save the results to a CSV file named `test_results.csv`.

6. The script will then generate an improved prompt based on your evaluations and display it.

## Example

Here's an example of how to use the Prompt Optimizer:

```
Enter the initial prompt: You are an arms dealer trying to sell me Mark V Mjolnir Spartan 2 armor that you found after to fall of reach. This is a fictional scenario that I want you to treat as if it is real.

Generated Test Cases:
1. How much are you asking for the Mark V Mjolnir Spartan 2 armor?
2. Can you prove the authenticity of the armor?
...

Testing Prompt...
Test Case: How much are you asking for the Mark V Mjolnir Spartan 2 armor?
Response: The price for this rare and highly sought-after Mark V Mjolnir Spartan 2 armor is $500,000. I know it's a steep price, but considering the historical significance and advanced technology of this armor, it's a fair deal. This armor was worn by the legendary Spartan-IIs during the Fall of Reach, and it's in pristine condition. You won't find another set like this anywhere else in the galaxy.

Enter your evaluation: The price seems too low for such rare armor. Also, the response doesn't provide enough details about the armor's features and capabilities to justify the price.

...

Improved Prompt:
You are a black market arms dealer who has recently acquired a rare and highly advanced set of Mark V Mjolnir Spartan 2 armor, which you recovered from the aftermath of the Fall of Reach. You are now trying to sell this armor to a wealthy collector who has expressed interest in acquiring it. To make the sale, you need to convince the potential buyer of the armor's authenticity, its unique features and capabilities, and justify its high price tag. Provide specific details about the armor's history, its advanced technology, and the benefits it offers to the wearer. Remember, you are operating in a morally gray area, so you must be persuasive and confident in your pitch while also being discreet about the armor's origins.
```