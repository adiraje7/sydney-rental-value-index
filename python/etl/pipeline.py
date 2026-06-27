from extract import extract_rental_data
from validate import validate
from transform import transform
from load import save_processed


def main():

    df = extract_rental_data()

    validate(df)

    df = transform(df)
    save_processed(df)

    print("\nAfter Transformation")
    print("=" * 50)

    print(df.dtypes)

    print(df.head())


if __name__ == "__main__":
    main()