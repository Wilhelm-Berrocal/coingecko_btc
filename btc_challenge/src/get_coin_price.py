import logging
import pandas as pd
import requests
from datetime import date, datetime


log_format = "%(asctime)s::%(levelname)s::%(name)s::""%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='./logs/get_coin_price.log', level='DEBUG', format=log_format)


def get_coin_price(ini = '01-01-2022', end = '31-03-2022'):
    """Takes two utc dates in the format dd-mm-yyyy and gets historic prices from the coingecko api, and returns them in a dataframe, grouped by date, requires pandas as pd, requests and datetime"""
    
    btc_start_date = int(datetime.strptime('28-04-2013', "%d-%m-%Y").timestamp())
    current_timestamp = int(datetime.now().timestamp())
    
    ini_timestamp = int(datetime.strptime(ini, "%d-%m-%Y").timestamp())
    end_timestamp = int(datetime.strptime(end, "%d-%m-%Y").timestamp())
    
    status = None
    
    if ini_timestamp < btc_start_date:
        ini_timestamp = btc_start_date
    
    if end_timestamp > current_timestamp:
        end_timestamp = current_timestamp

    try:
        coin_url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={ini_timestamp}&to={end_timestamp}&precision=2'
        request = requests.get(coin_url)
        coin_historic_prices_json = request.json()
    
    except requests.exceptions.RequestException as e:
        logging.info(f"Exception - {e} occured")
    
    finally:
        if request.status_code != 200:
            status = "FAIL"
            logging.info(f"get_coin_price : {status}")
        else:
            status = "PASS"
            logging.info(f"get_coin_price : {status}")
    
    return coin_historic_prices_json
