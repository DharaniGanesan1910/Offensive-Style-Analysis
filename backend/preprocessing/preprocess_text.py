# backend/preprocessing/preprocess_text.py
import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_text(text):
    """
    Clean text but preserve emojis, punctuation, capital letters, and numbers.
    Removes URLs, mentions, hashtags, and extra spaces only.
    """
    if pd.isna(text):
        return ""
    text = str(text).strip()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove mentions and hashtags
    text = re.sub(r"@\w+|#\w+", "", text)
    # Normalize multiple spaces
    text = re.sub(r"\s+", " ", text)
    return text
def encode_labels(labels):
    """
    Convert string labels to numeric IDs using pandas factorize.
    Returns encoded labels and the mapping encoder.
    """
    encoded, uniques = pd.factorize(labels)
    encoder = {label: idx for idx, label in enumerate(uniques)}
    return encoded, encoder