from src.ocr_layout import extract_layout, group_into_lines, structure_lines
from src.embeddings import get_embeddings, model
from src.retrieval import create_index, search
from src.llm import generate_answer
from src.utils import prepare_texts, build_context

# Step 1: OCR Layout
blocks = extract_layout("sample_scan.png")
lines = group_into_lines(blocks)
structured_data = structure_lines(lines)

# Step 2: Prepare text
texts = prepare_texts(structured_data)

# Step 3: Embeddings
embeddings = get_embeddings(texts)

# Step 4: FAISS
index = create_index(embeddings)

# Step 5: Query
query = "What is the total amount?"
query_embedding = model.encode([query])

results = search(index, query_embedding, texts, k=3)
context = build_context(results)

# Step 6: LLM
answer = generate_answer(query, context)

print("Answer:", answer)
