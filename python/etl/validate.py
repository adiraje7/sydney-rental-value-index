def validate(df):

    print("\nValidation Report")
    print("-" * 40)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    print("\nMissing Values")
    print(df.isna().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nPotential Quality Issues")
    print("-" * 40)

    # Missing bedrooms
    print(
        f"Missing bedrooms: "
        f"{df['bedrooms'].isna().sum():,}"
    )

    # Bedrooms greater than 9
    print(
        f"Bedrooms > 9: "
        f"{(df['bedrooms'] > 9).sum():,}"
    )

    # Invalid rent
    print(
        f"Rent <= $0: "
        f"{(df['weekly_rent'] <= 0).sum():,}"
    )

    # Unrecognised dwelling types
    invalid_dwelling_types = (
        df.loc[
            ~df["dwelling_type_valid"],
            "dwelling_type"
        ]
        .value_counts()
    )

    print("\nUnrecognised Dwelling Types")
    print(invalid_dwelling_types)

    print("\nRecognised Dwelling Types")
    print(
        df.loc[
            df["dwelling_type_valid"],
            "dwelling_type"
        ].value_counts()
    )

    return df