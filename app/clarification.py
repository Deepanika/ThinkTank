class ClarificationManager:
    def __init__(self):
        self.conversation_context = {}

    def add_to_context(self, user_id: str, question: str, solution: str):
        if user_id not in self.conversation_context:
            self.conversation_context[user_id] = []
        self.conversation_context[user_id].append({"question": question, "solution": solution})

    def clarify_question(self, user_id: str, clarification: str, llama):
        context = self.conversation_context.get(user_id, [])
        if not context:
            return "No previous question found for this user. Please solve a problem first."
        
        last_question = context[-1]["question"]
        prompt = (
            f"Based on the earlier solution to '{last_question}', the user asked for clarification: "
            f"'{clarification}'. Please provide additional details."
        )
        # Ensure the prompt is passed as a list
        response = llama.generate([prompt])

        # Access the first generation and its text attribute
        if response and response.generations and len(response.generations) > 0:
            return response.generations[0][0].text
        else:
            return "Unable to generate clarification."
