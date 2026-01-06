from src.llm import call_llm

def extract_claims(backstory_text):
    prompt = f"""
    Extract factual claims about the character's:
    - upbringing
    - beliefs
    - fears
    - values
    - moral limits

    Return bullet points only.

    Backstory:
    {backstory_text}
    """
    response = call_llm(prompt)
    claims = [
        line.strip("- ").strip()
        for line in response.split("\n")
        if line.strip()
    ]
    return claims

