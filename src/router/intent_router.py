import numpy as np
from embeddings import get_embeddings
from router.domain_embeddings import DOMAIN_VECTORS

embed = get_embeddings()

def cosine(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def classify_intent(query: str) -> str:
    q_vec = embed.embed_query(query)

    scores = {}

    for domain, vectors in DOMAIN_VECTORS.items():
        similarities = [cosine(q_vec, v) for v in vectors]
        scores[domain] = max(similarities)

    return max(scores, key=scores.get)
