from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/rentals/rental_bond_lodgements_2025.xlsx")


def extract_rental_data():
    """
    Extract rental bond lodgement data from Excel.
    """

    df = pd.read_excel(
        RAW_DATA_PATH,
        sheet_name="Year 2025 Rental Bond Lodgments",
        header=2
    )

    return df