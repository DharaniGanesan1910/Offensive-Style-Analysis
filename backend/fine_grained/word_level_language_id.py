import os
import pandas as pd
import re
from collections import Counter
import enchant  # pip install pyenchant

# -------------------------------
# Paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed", "train.csv")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
ENGLISH_PATH = os.path.join(RESOURCES_DIR, "english_words.txt")
TAMIL_PATH = os.path.join(RESOURCES_DIR, "tamil_words.txt")
OUTPUT_PATH = os.path.join(BASE_DIR, "train_word_level_lang.csv")
AUTO_TAMIL_PATH = os.path.join(RESOURCES_DIR, "tamil_words_auto.txt")

# -------------------------------
# Load CSV
# -------------------------------
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ File not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)
print("✅ File loaded:", DATA_PATH)
print("Columns:", df.columns)

TEXT_COL = df.columns[0]  # change if needed

# -------------------------------
# Load word lists
# -------------------------------
def load_words(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Word list not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return set(w.strip().lower() for w in f if w.strip())

english_words = load_words(ENGLISH_PATH)
tamil_words = load_words(TAMIL_PATH)
print(f"✅ English words: {len(english_words)}, Tamil words: {len(tamil_words)}")

english_dict = enchant.Dict("en_US")

# -------------------------------
# Clean text
# -------------------------------
def clean_text(text):
    text = str(text).lower()
    # Keep English a-zA-Z and Tamil unicode \u0B80-\u0BFF
    text = re.sub(r"[^a-zA-Z\u0B80-\u0BFF\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -------------------------------
# Build list of unknown words for Tamil expansion
# -------------------------------
all_words = []
for text in df[TEXT_COL]:
    all_words.extend(clean_text(text).split())

unknown_words = []
for word in all_words:
    # if word has Tamil letters OR in Tamil list → skip
    if any("\u0B80" <= c <= "\u0BFF" for c in word) or word in tamil_words:
        continue
    # if word is English → skip
    if word in english_words or english_dict.check(word):
        continue
    unknown_words.append(word)

# Count frequency
unknown_counter = Counter(unknown_words)
TOP_N = 500
most_common_unknown = [w for w, _ in unknown_counter.most_common(TOP_N)]
tamil_words.update(most_common_unknown)

# Save updated Tamil list
with open(AUTO_TAMIL_PATH, "w", encoding="utf-8") as f:
    for w in sorted(tamil_words):
        f.write(w + "\n")
print(f"✅ Updated Tamil word list saved: {AUTO_TAMIL_PATH}")

# -------------------------------
# Word-level language tagging
# -------------------------------
def word_level_lang_id(text):
    words = clean_text(text).split()
    labeled = []

    for word in words:
        if any("\u0B80" <= c <= "\u0BFF" for c in word):  # contains Tamil letters
            lang = "TA"
        elif word in tamil_words:                            # Romanized Tamil
            lang = "TA"
        elif word in english_words or english_dict.check(word):
            lang = "EN"
        else:
            lang = "UNK"
        labeled.append(f"{word}/{lang}")

    return " ".join(labeled)

# -------------------------------
# Apply tagging
# -------------------------------
df["word_lang"] = df[TEXT_COL].apply(word_level_lang_id)

# -------------------------------
# Save output
# -------------------------------
df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Word-level language tagging complete. Saved to {OUTPUT_PATH}")
