def prepare_texts(structured_data):
    return [item['text'] for item in structured_data if item['text'].strip()]


def build_context(results):
    return "\n".join(results)
