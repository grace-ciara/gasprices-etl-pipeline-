import pandas as pd

def transform_gasprices(gas_data):
    city_data = gas_data['result']['cities']
    cities_df = pd.DataFrame(city_data)
    cities_df.head()
    cities_df = cities_df.drop(columns=['lowername'])
    cities_df = cities_df.rename(columns={'name': 'cities'})
    return cities_df