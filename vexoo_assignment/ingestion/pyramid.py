def summarize(chunk):
    # take first sentence as summary
    return chunk.split(".")[0]


def categorize(chunk):
    chunk = chunk.lower()
    
    if "ai" in chunk or "intelligence" in chunk:
        return "AI"
    elif "law" in chunk:
        return "Legal"
    else:
        return "General"


def extract_keywords(chunk):
    words = chunk.split()
    return words[:5]  # first 5 words


def build_pyramid(chunks):
    pyramid = []

    for chunk in chunks:
        data = {
            "raw": chunk,
            "summary": summarize(chunk),
            "category": categorize(chunk),
            "keywords": extract_keywords(chunk)
        }
        pyramid.append(data)

    return pyramid