# backend/preprocessing/preprocess_text.py

import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_text(text):
    """
    Preprocess text while preserving:
    - Capital letters
    - Emojis
    - Punctuation
    - Numbers
    - Tamil + English letters

    Removes only:
    - URLs
    - Mentions (@user)
    - Hashtags (#tag)
    - Extra spaces
    """
    if pd.isna(text):
        return ""

    text = str(text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove mentions & hashtags
    text = re.sub(r"@\w+|#\w+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def encode_labels(labels):
    """
    Encode labels into numeric IDs.
    Returns encoded labels and LabelEncoder object
    """
    encoder = LabelEncoder()
    encoded = encoder.fit_transform(labels)
    return encoded, encoder
