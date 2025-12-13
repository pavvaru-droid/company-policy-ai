from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_policy(question, policy_data):
    prompt = f"""
You are a company HR assistant.
Answer strictly based on the policy data below.
Do not assume anything extra.

Policy Data:
{policy_data}

User Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You explain company policies clearly."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

