from .load_csv_data import train_df, test_df, dev_df, full_df
from .preprocess_text import preprocess_text
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def process_labeled_split(df, name, label_map=None, fit=False):
    df["clean_text"] = df["text"].apply(preprocess_text)

    if fit:
        labels = sorted(df["label"].unique())
        label_map = {label: idx for idx, label in enumerate(labels)}

    df["label_id"] = df["label"].map(label_map)

    if df["label_id"].isna().any():
        unseen = df[df["label_id"].isna()]["label"].unique()
        raise ValueError(f"❌ Unseen labels found in {name}: {unseen}")

    out_path = PROCESSED_DIR / f"{name}.csv"
    df[["clean_text", "label_id"]].to_csv(out_path, index=False)

    print(f"✅ Saved {name} → {out_path}")
    return label_map


def process_unlabeled_split(df, name):
    df["clean_text"] = df["text"].apply(preprocess_text)

    out_path = PROCESSED_DIR / f"{name}.csv"
    df[["clean_text"]].to_csv(out_path, index=False)

    print(f"✅ Saved {name} (unlabeled) → {out_path}")


# 1️⃣ Train → fit label mapping
label_map = process_labeled_split(train_df, "train", fit=True)

# 2️⃣ Test & Dev → reuse mapping
process_labeled_split(test_df, "test", label_map=label_map)
process_labeled_split(dev_df, "dev", label_map=label_map)

# 3️⃣ Full → text only (NO labels)
process_unlabeled_split(full_df, "full")
