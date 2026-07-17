from google.genai import types

from config import client
from tools import calculator, web_search

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        tools=[calculator, web_search]
    )
)

print("CLI Research Agent")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = chat.send_message(user_input)
    print(f"Agent: {response.text}\n")