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
**Known limitation:**
- **v1 (fuzzy matching)** uses a min_confidence threshold (0.5) to avoid guessing
  wrong. Testing across multiple rounds found this only partially works: on Day 6,
  2 of 3 unrelated test questions still passed the threshold with wrong answers.
  On Day 10, a water-related question was incorrectly matched to an unrelated
  "old books" question at a 0.57 score — still above threshold. The confidence
  score does not reliably reflect topical correctness.

- **v2 (ML classifier)** has no confidence threshold at all — it always predicts
  the closest known category. A direct comparison (Day 8) showed v1 correctly
  refusing 3 unrelated questions (scores 0.48/0.37/0.45) while v2 confidently
  answered all 3 wrong. However, v2 is not uniformly worse: on Day 10, v2 correctly
  identified the "water" category for a question v1 had matched incorrectly,
  likely because it learned water-related word patterns during training rather
  than relying on a single closest-question comparison.

- **v2 has no handling for empty input** and was not tested against it.

- **Dataset size** (~[your actual row count — fill in]) rows) is small, which
  limits how well the ML classifier can generalize to phrasing it hasn't seen.

- **Overall:** neither version reliably distinguishes "confident and correct" from
  "confident and wrong." v1 fails by passing a bad match through its threshold;
  v2 fails by having no threshold at all. Fixing this properly would likely
  require a larger dataset and a confidence mechanism for v2, which is out of
  scope for this version.
