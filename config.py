from dotenv import load_dotenv
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

API_KEY = environ.get('API_KEY')
TOKEN = environ.get('TOKEN')

currencies_list = ['USD', 'EUR', 'RUB', 'UAH', 'PLN', 'AUD', 'JPY',
                   'CHF', 'CAD', 'GBP', 'BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'LTC', 'CZK', 'XLM']
currencies_list.sort()


