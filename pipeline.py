from src.chunking import chunk_novel
from src.claim_extraction import extract_claims
from src.retrieval import retrieve_chunks
from src.consistency_check import check_claim
from src.decision import aggregate

def run(novel_text, backstory_text):
    chunks = chunk_novel(novel_text)
    claims = extract_claims(backstory_text)

    results = []
    for claim in claims:
        evidence = retrieve_chunks(claim, chunks)
        verdict = check_claim(claim, evidence)
        results.append(verdict)

    return aggregate(results)
