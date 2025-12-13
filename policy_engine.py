from policies import POLICIES

def get_policy_answer(question: str):
    q = question.lower()

    if "work from home" in q or "wfh" in q:
        return "wfh", POLICIES["wfh"]

    if "leave" in q:
        return "leave", POLICIES["leave"]

    if "working hours" in q or "office timing" in q:
        return "working_hours", POLICIES["working_hours"]

    return None, None
