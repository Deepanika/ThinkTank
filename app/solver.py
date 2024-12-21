from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llama = OllamaLLM(model="llama3.2")

def solve_problem(question: str) -> str:
    template = (
        "You are a knowledgeable tutor skilled in solving problems step by step.\n\n"
        "Here is the question: {question}\n\n"
        "Please provide a detailed step-by-step solution explaining each step clearly."
    )
    prompt = PromptTemplate(input_variables=["question"], template=template)
    chain = prompt | llama
    return chain.invoke({"question": question})
