from pathlib import Path


def save_processed(df):

    output_path = Path("data/processed/rental_lodgements_2025_clean.csv")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        output_path,
        index=False
    )

    print("\nSaved cleaned dataset")

    print(output_path)