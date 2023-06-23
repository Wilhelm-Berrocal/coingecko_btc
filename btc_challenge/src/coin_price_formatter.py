import logging
import pandas as pd

def coin_price_formatter(coin_historic_prices_json):
    """Converts a json historic price to a dataframe and returns daily data"""

    coin_price_df = pd.DataFrame(coin_historic_prices_json['prices'], columns =['utc_epoch', 'usd_price'])

    coin_price_df['utc_epoch'] = pd.to_numeric(coin_price_df['utc_epoch'], errors='coerce')
    coin_price_df['usd_price'] = pd.to_numeric(coin_price_df['usd_price'], errors='coerce')
    coin_price_df.dropna(how='any', inplace=True)

    coin_price_df['utc_datetime'] = pd.to_datetime(coin_price_df['utc_epoch'], unit='ms').dt.date
    coin_price_df.drop(['utc_epoch'], axis = 1, inplace = True)

    coin_price_df = coin_price_df.groupby(['utc_datetime']).mean().reset_index()
    coin_price_df['usd_price'] = coin_price_df['usd_price'].round(2)

    logging.info(f"coin_price_formatter processed {len(coin_price_df)} records")
    coin_price_df.to_csv('./data/price_of_coins/coin_price.csv', index=False)

    return coin_price_df
