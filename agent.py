from google.genai import types

from config import client
from tools import calculator, web_search


def main():
    print("🤖 CLI Research Agent (type 'exit' to quit)\n")

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            tools=[calculator, web_search],
            tool_config=types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(
                    mode="ANY"
                )
            )
        )
    )

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = chat.send_message(user_input)
            print(f"Agent: {response.text}\n")

        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()