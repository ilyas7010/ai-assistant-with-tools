from langchain_openai import ChatOpenAI
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    return f"Hi {name}, I hope you are well"

def main():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    print("Welcome King Ilyas! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        lowered = user_input.lower()

        if lowered.startswith("greet "):
            name = user_input[6:].strip().title()
            result = say_hello.invoke({"name": name})
            print(f"\nAssistant: {result}")
            continue

        if "+" in user_input:
            parts = user_input.split("+")
            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())
                    result = calculator.invoke({"a": a, "b": b})
                    print(f"\nAssistant: {result}")
                    continue
                except ValueError:
                    pass

        response = model.invoke(user_input)
        print(f"\nAssistant: {response.content}")

if __name__ == "__main__":
    main()