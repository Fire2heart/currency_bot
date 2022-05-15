import requests
from config import API_KEY, currencies_list
from database import insert


def format_data(data):
    result = {}
    for item in data:
        result[item['asset_id_quote']] = item['rate']
    return {key: value for key, value in sorted(result.items())}


def pull_in_base(currencies: list) -> dict:
    # base currency USD!!!

    currencies_ = currencies.copy()
    currencies_str = ','.join(currencies_)

    url = f'http://rest.coinapi.io/v1/exchangerate/USD?invert=false&filter_asset_id={currencies_str}&apikey={API_KEY}'
    data = requests.get(url).json()['rates']
    data = format_data(data)

    return data


if __name__ == "__main__":
    currencies = currencies_list.copy()
    currencies.remove('USD')
    info = pull_in_base(currencies)
    insert(info)
