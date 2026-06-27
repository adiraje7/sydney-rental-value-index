from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw/rentals/rental_bond_lodgements_2025.xlsx")

df = pd.read_excel(
    DATA_PATH,
    sheet_name="Year 2025 Rental Bond Lodgments",
    header=2
)

print("=" * 60)
print("Dataset Summary")
print("=" * 60)

print(f"\nRows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Dwelling Types:")
print(df["Dwelling Type"].value_counts(dropna=False))