from app.solver import solve_problem
from app.history import log_question, get_user_history
from app.clarification import ClarificationManager
from langchain_ollama import OllamaLLM

def main_menu():
    clarification_manager = ClarificationManager()
    llama = OllamaLLM(model="llama3.2")

    print("Welcome to ThinkTank!")
    print("-------------------------------------")

    while True:
        print("\nHow may I assist you?")
        print("1. Solve a Problem")
        print("2. Ask for Clarification")
        print("3. View History")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_id = input("Enter your user ID: ").strip()
            question = input("Enter the problem you want to solve: ").strip()
            solution = solve_problem(question)
            print("\nSolution:")
            print(solution)
            log_question(user_id, question, solution)
            clarification_manager.add_to_context(user_id, question, solution)

        elif choice == "2":
            user_id = input("Enter your user ID: ").strip()
            clarification = input("Enter your clarification request: ").strip()

            if user_id in clarification_manager.conversation_context:
                response = clarification_manager.clarify_question(user_id, clarification, llama)
                print("\nClarification Response:")
                print(response)
            else:
                print("\nNo prior questions found for clarification.")

        elif choice == "3":
            user_id = input("Enter your user ID: ").strip()
            history = get_user_history(user_id)
            if history:
                print(f"\nHistory for user {user_id}:")
                for entry in history:
                    print(f"- Question: {entry['question']}")
                    print(f"  Solution: {entry['solution']}")
            else:
                print("\nNo history found for this user ID.")

        elif choice == "4":
            print("\nHope to see you soon! Have a good day!")
            break

        else:
            print("\nInvalid input. Please enter a number from the menu.")

if __name__ == "__main__":
    main_menu()