import openai
import random

# Set up your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Function to generate a space-related fact
def generate_space_fact():
    prompts = [
        "Generate a random space fact:",
        "Tell me something interesting about space:",
        "I want to learn a new space fact:",
        "Space is fascinating. Give me a fact about it:",
        "What's something cool about space?",
        "Tell me a space-related fact:",
    ]
    
    prompt = random.choice(prompts)
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    return response.choices[0].text.strip()

# Generate and print a space-related fact
print(generate_space_fact())
