from src.llm import call_llm

def check_claim(claim, evidence_chunks):
    context = "\n\n".join(evidence_chunks)

    prompt = f"""
    Claim:
    {claim}

    Evidence from the novel:
    {context}

    Question:
    Does the evidence contradict the claim?

    Answer with one word:
    - supported
    - contradicted
    - unclear
    """

    response = call_llm(prompt).lower()

    if "contradicted" in response:
        return "contradicted"
    if "supported" in response:
        return "supported"
    return "unclear"
