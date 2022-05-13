from dotenv import load_dotenv
from os import environ, path
import re

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

API_KEY = environ.get('API_KEY')
TOKEN = environ.get('TOKEN')
DATABASE = 'currency_bot/currencies.db'
TABLE = 'currencies'


currencies_list = ['USD', 'EUR', 'RUB', 'UAH', 'PLN', 'AUD', 'JPY',
                   'CHF', 'CAD', 'GBP', 'BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'LTC', 'CZK', 'XLM']
currencies_list.sort()

rule = '^\d+\s[A-Z, a-z]{3}$'
test = '1 usd'

if re.search(rule, test):
    amount, cur = test.split()

