def retrieve_chunks(claim, chunks, k=5):
    claim_words = claim.lower().split()
    ranked = sorted(
        chunks,
        key=lambda c: sum(w in c.lower() for w in claim_words),
        reverse=True
    )
    return ranked[:k]
