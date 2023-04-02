import openai
import time

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="curie",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

def print_human_like(message):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

if __name__ == "__main__":
    print("Welcome to the simple chatbot!")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        response = generate_response(prompt)
        print("Chatbot: ", end="")
        print_human_like(response)