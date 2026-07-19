"""
test_matcher_v1.py
Deliberately tricky/edge-case questions to find where v1 (fuzzy matching) breaks.
This file is meant to expose weaknesses honestly, not to prove the tool is perfect.
"""

from load_data import load_faq_data
from matcher_v1 import find_best_match


if __name__ == "__main__":
    data = load_faq_data("data/sample_data.csv")

    edge_case_questions = [
        "meri wotar botlle gum gai hai, pani kahan sey milay ga ",
        "aaj school hai",
        "mein washroom jaon toh kya hoga",
    ]

    for q in edge_case_questions:
        matched_q, answer, score = find_best_match(q, data)
        print(f"Input: {q}")
        print(f"Closest match: {matched_q} (similarity: {score})")
        print(f"Answer: {answer}")
        print("---")
