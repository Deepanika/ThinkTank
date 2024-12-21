import json

history_file = "problem_history.json"

def log_question(user_id: str, question: str, solution: str):
    history = load_history()
    history.append({"user_id": user_id, "question": question, "solution": solution})
    save_history(history)

def load_history():
    try:
        with open(history_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []
    except json.JSONDecodeError:
        # If the file is empty or contains invalid JSON, return an empty list
        print(f"Warning: {history_file} contains invalid JSON. Initializing empty history.")
        return []

def save_history(history):
    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

def get_user_history(user_id: str):
    history = load_history()
    return [entry for entry in history if entry["user_id"] == user_id]
