from extract import extract_gasprices
from transform import transform_gasprices
from load import load_gasprices


def main():
    gas_data = extract_gasprices()
    cities_df = transform_gasprices(gas_data)
    load_gasprices(cities_df)
    print('ETL process completed successfully.')

if __name__ == "__main__":
    main()
