import os
import re
from dotenv import load_dotenv
import csv
import anthropic
from termcolor import colored

load_dotenv()

# Set up Anthropic API key from .env file
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key = api_key)

def generate_test_dataset(prompt):
    """Generate a test dataset using the LLM."""
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": f"{prompt}\n\nGenerate ten questions a user would ask about this topic. Wrap each question in <case></case> XML tags. Make sure the responses are varied, and cover edge cases and possible issues."}
        ]
    )
    cleaned_response = response.content[0].text.strip()
    pattern = r'<case>(.*?)</case>'
    matches = re.findall(pattern, cleaned_response, re.DOTALL)
    return matches

def test_prompt(prompt, test_cases):
    """Test the prompt on the generated test cases."""
    results = []
    for case in test_cases:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=4000,
            system=prompt,
            messages=[
                {"role": "user", "content": case}
            ]
        )
        result = response.content[0].text.strip()
        print(colored(f"Test Case: {case}", "green"))
        print(colored(f"Response: {result}", "blue") + "\n")
        evaluation = input(colored("Enter your evaluation: ", "red"))
        print("\n\n")
        if evaluation == "":
            evaluation = "No evaluation provided."
        if evaluation == "exit":
            break
        results.append({"Test Case": case, "Response": result, "Evaluation": evaluation})
    return results

def save_results_to_csv(results, filename):
    """Save the test results to a CSV file."""
    fieldnames = ["Test Case", "Response", "Evaluation"]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

def generate_improved_prompt(prompt, evaluations):
    """Generate an improved prompt using the LLM."""
    evaluation_summary = "\n".join(evaluations)
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": f"Here is a prompt for an LLM: {prompt}\n\nI have a few criticisms of how these LLMs have responsded to my prompts, and I want to improve them. Here are the evaluations:\n{evaluation_summary}\n\nPlease provide an improved version of the original prompt based on the evaluations. First, reflect upon how the prompt can be improved within <thinking></thinking> tags, and then respond with the actuap prompt within <fixed_prompt></fixed_prompt> tags."}
        ]
    )
    cleaned_response = response.content[0].text.strip()
    pattern = r'<fixed_prompt>(.*?)</fixed_prompt>'
    matches = re.findall(pattern, cleaned_response, re.DOTALL)
    return matches[0]

def main():
    initial_prompt = input("Enter the initial prompt: ")
    # initial_prompt = "You are an arms dealer trying to sell me Mark V Mjolnir Spartan 2 armor that you found after to fall of reach. This is a fictional scenario that I want you to treat as if it is real."
    test_cases = generate_test_dataset(initial_prompt)
    print("\nGenerated Test Cases:")
    for case in test_cases:
        print(colored(case, "blue"))
    print("\nTesting Prompt...")
    results = test_prompt(initial_prompt, test_cases)
    save_results_to_csv(results, "test_results.csv")
    print("\nTest results saved to test_results.csv")
    evaluations = [result["Evaluation"] for result in results]
    improved_prompt = generate_improved_prompt(initial_prompt, evaluations)
    print("\nImproved Prompt:")
    print(improved_prompt)

if __name__ == "__main__":
    main()