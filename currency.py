from config import DATABASE, TABLE
import sqlite3


def get_info(currencies: list) -> dict:
    """Return dict of latest data
    Args:
        currencies (list): Currencies to fetch
    Returns:
        dict: dict of latest data in format {
            'date' : '', 'rates': {'currency': value_float, .....}
        }
    """
    currencies_copy = currencies.copy()
    if 'USD' in currencies_copy:
        currencies_copy.remove('USD')

    result = {'date': '', 'rates': {}}

    with sqlite3.connect(DATABASE) as db:
        db.row_factory = sqlite3.Row
        query = f'SELECT date, {", ".join(currencies_copy)} FROM {TABLE} ORDER BY ID DESC LIMIT 1'
        for item in db.execute(query):
            result['date'] = item['date']
            for cur in currencies_copy:
                result['rates'][cur] = item[cur]

    return result


def calculating(base: str, data: dict, base_num: int = 1) -> dict:
    if base != 'USD':
        base_value = 1 / data['rates'][base]
        del data['rates'][base]
        data['rates']['USD'] = base_value * base_num

    else:
        base_value = 1

    for key in data['rates']:
        if key == 'USD':
            data['rates'][key] = data['rates'][key] * base_num
        else:
            data['rates'][key] = data['rates'][key] * base_value * base_num

    return data


def show_result(base: str, currencies: any, base_num: int = 1) -> str:
    base_noflag = base.split()[0]
    currencies_noflag = list(currencies.keys())
    if base_noflag not in currencies_noflag:
        currencies_noflag.append(base_noflag)

    data = calculating(base_noflag, get_info(currencies_noflag), base_num)

    result = '\n---------------'

    for item in data['rates']:
        result += f'\n{item} {currencies[item]} = {round(data["rates"][item], 3)}'
    result += f'\n---------------\nИнфомация на {data["date"]}'

    return result
