def simple_match_score(query, text):
    query_words = query.lower().split()
    text = text.lower()
    
    score = 0
    for word in query_words:
        if word in text:
            score += 1
    return score


def search_pyramid(pyramid, query):
    best_score = 0
    best_result = None

    for item in pyramid:
        score_raw = simple_match_score(query, item["raw"])
        score_summary = simple_match_score(query, item["summary"])
        score_keywords = simple_match_score(query, " ".join(item["keywords"]))
        
        # combine all scores
        score = score_raw + score_summary + score_keywords

        if score > best_score:
            best_score = score
            best_result = item

    return best_result