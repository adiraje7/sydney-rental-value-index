from extract import extract_rental_data
from transform import transform
from validate import validate
from load import save_processed


def main():

    # Extract raw data
    df = extract_rental_data()

    # Transform and clean data
    df = transform(df)

    # Validate transformed data
    validate(df)

    # Save processed data
    save_processed(df)

    print("\nAfter Transformation")
    print("=" * 50)
    print(df.dtypes)
    print("\nFirst five rows:")
    print(df.head())


if __name__ == "__main__":
    main()