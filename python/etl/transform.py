import pandas as pd


def transform(df):
    """
    Clean and standardize the rental dataset.
    """

    # Standardise column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Weekly rent -> numeric
    df["weekly_rent"] = pd.to_numeric(
        df["weekly_rent"],
        errors="coerce"
    )

    # Bedrooms -> numeric
    df["bedrooms"] = pd.to_numeric(
        df["bedrooms"],
        errors="coerce"
    )

    return df