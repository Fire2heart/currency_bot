# def show_currency(base_currency: str, currencies: list, base_num: int = 1) -> str:
#     currencies_ = currencies.copy()
#     if base_currency in currencies_:
#         currencies_.remove(base_currency)
#     currencies_str = ','.join(currencies_)
#
#     data = get_data(
#         f'http://rest.coinapi.io/v1/exchangerate/{base_currency}?invert=false&filter_asset_id={currencies_str}&apikey={API_KEY}')
#
#     res = f'{base_num} {base_currency}:\n'
#     for curr in currencies_:
#         value = round(data[currencies_.index(curr)]['rate'], 2)*base_num
#         res += f'\n{data[currencies_.index(curr)]["asset_id_quote"]} = {value}'
#
#     return res

# test_data = [
#     {
#       "time": "2022-05-05T13:17:31.6000000Z",
#       "asset_id_quote": "AUD",
#       "rate": 1.3941540148510710605325935409
#     },
#     {
#       "time": "2022-05-05T13:17:31.6000000Z",
#       "asset_id_quote": "RUB",
#       "rate": 65.615607639294344313077279239
#     },
#     {
#       "time": "2022-05-05T13:17:31.6000000Z",
#       "asset_id_quote": "UAH",
#       "rate": 32.748810183924745076389666322
#     }
#   ]
