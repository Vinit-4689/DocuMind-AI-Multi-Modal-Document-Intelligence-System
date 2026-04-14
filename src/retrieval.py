import faiss
import numpy as np


def create_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index


def search(index, query_embedding, texts, k=3):
    D, I = index.search(query_embedding, k)
    return [texts[i] for i in I[0]]
