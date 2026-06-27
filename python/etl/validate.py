def validate(df):

    print("\nValidation Report")
    print("-" * 40)

    print(f"Rows: {len(df):,}")

    print(f"Columns: {len(df.columns)}")

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nDuplicate Rows")

    print(df.duplicated().sum())