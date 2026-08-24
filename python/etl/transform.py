import pandas as pd


VALID_DWELLING_TYPES = {
    "F",  # Flat/unit
    "H",  # House
    "T",  # Terrace/townhouse/semi-detached
    "O",  # Other
    "U",  # Unknown
}


def transform(df):

    df = df.copy()

    # --------------------------------------------------
    # 1. Standardise column names
    # --------------------------------------------------

    df.columns = [
        "lodgement_date",
        "postcode",
        "dwelling_type",
        "bedrooms",
        "weekly_rent"
    ]

    # --------------------------------------------------
    # 2. Convert data types
    # --------------------------------------------------

    df["lodgement_date"] = pd.to_datetime(
        df["lodgement_date"],
        errors="coerce"
    )

    df["postcode"] = pd.to_numeric(
        df["postcode"],
        errors="coerce"
    ).astype("Int64")

    df["bedrooms"] = pd.to_numeric(
        df["bedrooms"],
        errors="coerce"
    )

    df["weekly_rent"] = pd.to_numeric(
        df["weekly_rent"],
        errors="coerce"
    )

    # --------------------------------------------------
    # 3. Standardise dwelling type
    # --------------------------------------------------

    df["dwelling_type"] = (
        df["dwelling_type"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    # Flag recognised dwelling types
    df["dwelling_type_valid"] = (
        df["dwelling_type"].isin(VALID_DWELLING_TYPES)
    )

    # --------------------------------------------------
    # 4. Remove exact duplicate records
    # --------------------------------------------------

    df = df.drop_duplicates()

    # --------------------------------------------------
    # 5. Remove records without usable rental price
    # --------------------------------------------------

    df = df.dropna(
        subset=[
            "lodgement_date",
            "postcode",
            "weekly_rent"
        ]
    )

    # --------------------------------------------------
    # 6. Remove zero/negative rents
    # --------------------------------------------------

    df = df[df["weekly_rent"] > 0]

    # --------------------------------------------------
    # 7. Sort records
    # --------------------------------------------------

    df = df.sort_values(
        by="lodgement_date"
    ).reset_index(drop=True)

    return df