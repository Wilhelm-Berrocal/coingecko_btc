import logging
import requests
import pandas as pd
import sqlite3


log_format = "%(asctime)s::%(levelname)s::%(name)s::""%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='./logs/get_coin_list.log', level='DEBUG', format=log_format)


def get_coin_list():
    """Gets a list of coins from the coingecko api, and returns a dataframe with a list of coins, requieres pandas as pd and requests"""
    #We could save the data as a json with
    #list_of_coins.to_json('coin_list.json', orient='records',lines=True)

    coins_url = 'https://api.coingecko.com/api/v3/coins/list'

    try:
        request = requests.get(coins_url)
        coins = request.json()
        list_of_coins = pd.json_normalize(coins)
    except requests.exceptions.RequestException as e:
        logging.info(f"Exception - {e} occured")
        return
    finally:
        status = None
        if request.status_code != 200:
            status = "FAIL"
            logging.info(f"List of coins : {status}")
        else:
            status = "PASS"
            logging.info(f"List of coins : {status}")
    list_of_coins.to_csv('./data/list_of_coins/list_of_coins.csv', index=False)

    return list_of_coins
