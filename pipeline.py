import http.client
import os 
import json
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

def extract_gasprices(): 
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = { 
    'content-type': "application/json", 
    'authorization': f"apikey {os.getenv('GASPRICES_API_KEY')}" 
}

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()

    gas_data = json.loads(data.decode("utf-8"))

    print(json.dumps(gas_data, indent=4))
    gasprices = [gas_data['result']]
    return gas_data


def transform_gasprices(gas_data):
    city_data = gas_data['result']['cities']
    cities_df = pd.DataFrame(city_data)
    cities_df.head()
    cities_df = cities_df.drop(columns=['lowername'])
    cities_df = cities_df.rename(columns={'name': 'cities'})
    return cities_df


def load_gasprices(cities_df):

    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    cities_df.to_sql('gasprices_pipeline', con=engine, if_exists='replace', index=False)


def main():
    gas_data = extract_gasprices()
    cities_df = transform_gasprices(gas_data)
    load_gasprices(cities_df)
    print('ETL process completed successfully.')

if __name__ == "__main__":
    main()




