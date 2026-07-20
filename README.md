# Roman Urdu FAQ Assistant
## Dataset
This dataset was written by me for demonstration purposes. It is NOT real data
collected from students — it was self-authored to protect the privacy of the
community I work with. It represents the kinds of questions students commonly ask.
## How to Run
1. Upload sample_data.csv to a `data/` folder in your Colab session.
2. Upload the .py files from `src/` to your Colab session.
3. Run: !python load_data.py
## v1: Rule-Based Matching (NOT machine learning)
`src/matcher_v1.py` uses Python's built-in `difflib` library to compare a user's
question against every question in the dataset and return the answer for the
closest text match. This is fuzzy string matching, not AI/ML — it has no learning
component and doesn't generalize beyond comparing text similarity.

It also includes a minimum confidence threshold (0.5) — if the best match's
similarity score falls below this, the tool says it doesn't know rather than
guessing. This isn't perfect: testing showed a borderline question can still
score just above the threshold and return a topically related but incorrect answer.

## v2: Machine Learning Classifier
`src/model_v2.py` uses TF-IDF to convert questions into numeric vectors, then
trains a Logistic Regression classifier to predict the category of a new question.
This is genuine, if small-scale, machine learning.

**Known limitation:** unlike v1, this classifier has no confidence threshold —
it always predicts the closest known category, even for questions completely
unrelated to the dataset (e.g. a question about classroom seating returned a
"fees" answer). v1's `min_confidence` check has no equivalent here yet.

