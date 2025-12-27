import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_text(text):
    if pd.isna(text):
        return ""

    text = str(text).lower()

    # remove urls
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove mentions & hashtags
    text = re.sub(r"@\w+|#\w+", "", text)

    # keep Tamil + English only
    text = re.sub(r"[^a-zA-Z\u0B80-\u0BFF\s]", "", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def encode_labels(labels):
    encoder = LabelEncoder()
    encoded = encoder.fit_transform(labels)
    return encoded, encoder
