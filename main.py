from fastapi import FastAPI
from policy_engine import get_policy_answer
from llm_explainer import explain_policy

app = FastAPI()

@app.post("/ask")
def ask(data: dict):
    question = data.get("question")

    policy_key, policy_data = get_policy_answer(question)

    if not policy_data:
        return {
            "answer": "This question is outside the scope of company policies."
        }

    final_answer = explain_policy(question, policy_data)
    return {"answer": final_answer}
