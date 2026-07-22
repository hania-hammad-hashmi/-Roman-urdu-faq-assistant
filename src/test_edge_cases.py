"""
test_edge_cases.py
Stress-tests both v1 and v2 with messy, unexpected, and out-of-scope input.
Goal: find real weaknesses and document them honestly, not hide them.
"""

from load_data import load_faq_data
from matcher_v1 import find_best_match
from model_v2 import train_classifier, predict_category, get_answer_by_category


if __name__ == "__main__":
    data = load_faq_data("data/sample_data.csv")
    vectorizer, model = train_classifier(data)

    stress_questions = [
        "pni kb mile ga ya ni",
        "agar gatar ka pani bhar jaye toh kya karna chahiay",
        "",  # empty input - tests whether the code crashes or handles it gracefully
    ]

    for q in stress_questions:
        print(f"Input: '{q}'")

        if q.strip() == "":
            matched_q, answer_v1, score = find_best_match(q, data)
            print(f"v1: {answer_v1}")
            print("v2: [not tested on empty input - v2 has no empty-string check yet]")
            print("---")
            continue

        matched_q, answer_v1, score = find_best_match(q, data)
        print(f"v1 match: {matched_q} (score: {score}) -> {answer_v1}")

        category = predict_category(q, vectorizer, model)
        answer_v2 = get_answer_by_category(category, data)
        print(f"v2 predicted category: {category} -> {answer_v2}")
        print("---")
