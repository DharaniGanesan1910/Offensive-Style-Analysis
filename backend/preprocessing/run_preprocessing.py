from .load_csv_data import train_df, test_df, dev_df, full_df
from .preprocess_text import preprocess_text, encode_labels
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def process_split(df, name):
    df["clean_text"] = df["text"].apply(preprocess_text)
    df["label_id"], encoder = encode_labels(df["label"])

    out_path = PROCESSED_DIR / f"{name}.csv"
    df[["clean_text", "label_id"]].to_csv(out_path, index=False)

    print(f"✅ Saved {name} → {out_path}")


process_split(train_df, "train")
process_split(test_df, "test")
process_split(dev_df, "dev")
process_split(full_df, "full")
