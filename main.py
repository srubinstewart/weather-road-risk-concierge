# main.py
"""
Entry point for the Daily Weather and Road Risk Concierge Agent.

Run this file to interact with the CoordinatorAgent in a simple
command-line loop.
"""

from agents import CoordinatorAgent
from session import InMemorySessionService


def main():
    session_service = InMemorySessionService()
    coordinator = CoordinatorAgent(session_service=session_service)

    # For this simple demo we just use a fixed user id.
    user_id = "demo_user"

    print("Daily Weather and Road Risk Concierge")
    print("Type 'quit' to exit.")
    print("Examples:")
    print("  Set my default location to 80498")
    print("  What are the weather and road conditions this morning?")
    print("  What about this evening?")

    while True:
        message = input("\nYou: ").strip()
        if message.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        response = coordinator.handle_message(user_id=user_id, message=message)
        print(f"\nAgent:\n{response}")


if __name__ == "__main__":
    main()
