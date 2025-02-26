import os
import sys
import time
from openai import OpenAI
from dotenv import load_dotenv  # Import dotenv to load .env variables

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),  # Read GITHUB_TOKEN from .env
)
print(f"API Key Loaded: {os.getenv('GITHUB_TOKEN')}")

# Guide the user on how to use the chatbot
print("\n🤖 Welcome to the AI Chatbot!")
print("👉 Type your message to start the conversation.")
print("❌ Type 'exit', 'quit' or 'bye' to close the chat.\n")


def typing_effect(text, delay=0.05):
    sys.stdout.write("Typing")
    sys.stdout.flush()
    for _ in range(3):  # Three dots blinking
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    time.sleep(0.5)
    print("\n")  # New line before response

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()  # Move to the next line after typing is done


while True:
    # Get user input
    user_input = input("🤠: ")

    # Check for exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("\🤖 Chatbot: Goodbye! Have a great day!\n")
        break

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a a very high intelligent AI assistant, designed to assist with logical and reasoning tasks especially in coding and mathematical topics. Please provide a well-detailed answer as a result of a well structured thought-process.",
                },
                {
                    "role": "user",
                    "content": user_input,  # Use user's input
                },
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1,
        )

        # Ensure chatbot responds properly
        if hasattr(response, "choices") and response.choices:
            chatbot_response = response.choices[0].message.content
        else:
            chatbot_response = "⚠️ No response received."

        # Print chatbot response with typing effect
        print("🤖 You: ", end="")
        typing_effect(chatbot_response)

    except Exception as e:
        print(f"⚠️ Error: {e}")
        chatbot_response = f"⚠️ Error: {str(e)}"
