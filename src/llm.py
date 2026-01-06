def call_llm(prompt: str) -> str:
    # TEMPORARY STUB (replace with real LLM later)
    if "Extract factual claims" in prompt:
        return (
            "- Character distrusts authority\n"
            "- Character has strong political beliefs\n"
            "- Character values justice over family"
        )

    if "Does the evidence contradict" in prompt:
        return "unclear"

    return "unclear"
