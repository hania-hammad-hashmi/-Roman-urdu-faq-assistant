"""
compare_v1_v2.py
Runs the same set of questions through both v1 (fuzzy matching) and
v2 (TF-IDF + Logistic Regression) so their behavior can be directly compared.
"""

from load_data import load_faq_data
from matcher_v1 import find_best_match
from model_v2 import train_classifier, predict_category, get_answer_by_category


if __name__ == "__main__":
    data = load_faq_data("data/sample_data.csv")
    vectorizer, model = train_classifier(data)

    comparison_questions = [
        "ya larkon ki fees aur akrkion ki fees same hai ",
        "agar koi lakra maray toh theek hai aur koi larki kisi ko maaray toh kya hoga ",
        "aap din mein kitni baar nahatay ho",
    ]

    for q in comparison_questions:
        print(f"Input: {q}")

        matched_q, answer_v1, score = find_best_match(q, data)
        print(f"  v1 (fuzzy match): {answer_v1} (confidence: {score})")

        category = predict_category(q, vectorizer, model)
        answer_v2 = get_answer_by_category(category, data)
        print(f"  v2 (ML classifier): {answer_v2} (predicted category: {category})")
        print("---")
