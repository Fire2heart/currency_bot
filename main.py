import telebot
import re
from currency import show_result
from config import TOKEN, rule
from telebot import types

bot = telebot.TeleBot(TOKEN)

currencies_flag_dict = {'USD': 'πΊπΈ', 'EUR': 'πͺπΊ', 'RUB': 'π·πΊ', 'UAH': 'πΊπ¦', 'PLN': 'π΅π±', 'AUD': 'π¦πΊ',
                        'JPY': 'π―π΅', 'CHF': 'π¨π­', 'CAD': 'π¨π¦', 'GBP': 'π¬π§', 'BTC': '', 'ETH': '',
                        'SOL': '', 'BNB': '', 'XRP': '', 'LTC': '', 'CZK': '', 'XLM': ''}

currencies_flag = ['USD πΊπΈ', 'EUR πͺπΊ', 'RUB π·πΊ', 'UAH πΊπ¦', 'PLN π΅π±', 'AUD π¦πΊ', 'JPY π―π΅', 'CHF π¨π­', 'CAD π¨π¦', 'GBP π¬π§']

crypto_list = ['BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'LTC', 'CZK', 'XLM']

sign_list = ['β', 'β']

start_menu_list = ['Crypto π', 'Currency π¦', 'Settings β']

DATA = dict()
DEFAULT_PARAMS = {'USD': 'πΊπΈ', 'EUR': 'πͺπΊ', 'RUB': 'π·πΊ', 'UAH': 'πΊπ¦'}


def build_setting(params):
    global currencies_flag_dict
    markup = types.InlineKeyboardMarkup()
    bb = dict()
    for currency, _ in currencies_flag_dict.items():
        if currency in params.keys():
            bb[currency] = sign_list[1]
        else:
            bb[currency] = sign_list[0]

    buttons = [types.InlineKeyboardButton(
        text=f'{currency} {sign}',
        callback_data=currency) for currency, sign in bb.items()]
    markup.add(*buttons)

    return markup


def build_buttons(flag_dict: dict) -> list:
    buttons_list = []
    for key, value in flag_dict.items():
        temp = f'{key} {value}'
        buttons_list.append(temp)
    return buttons_list


def build_menu(menu_list: list):
    markup = types.ReplyKeyboardMarkup()
    markup.row_width = 2
    buttons = [types.KeyboardButton(b) for b in menu_list]
    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = build_menu(menu_list=start_menu_list)
    bot.send_message(
        message.chat.id, 'π ΠΠ΄Π°ΡΠΎΠ²Π°! ΠΡΠ±ΠΈΡΠ°ΠΉ ΡΠ΅ Π½Π°Π΄Π°π', reply_markup=markup)
    bot.send_message(message.chat.id, 'ΠΠΈΠ±ΠΎ Π½Π°ΠΏΠΈΡΠΈ ΡΠΈΡΠ»ΠΎ ΠΈ Π²Π°Π»ΡΡΡ: "2 btc"')


@bot.message_handler(func=lambda message: message.text == 'Currency π¦')
def show_currency(message):
    menu = currencies_flag.copy()
    menu.append('ΠΠ°Π·Π°Π΄ β©')
    markup = build_menu(menu_list=menu)
    bot.send_message(message.chat.id, 'ΠΡΠ±Π΅ΡΠΈ Π²Π°Π»ΡΡΡ π°', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Crypto π')
def show_crypto(message):
    menu = crypto_list.copy()
    menu.append('ΠΠ°Π·Π°Π΄ β©')
    markup = build_menu(menu_list=menu)
    bot.send_message(message.chat.id, 'ΠΡΠ±Π΅ΡΠΈ Π²Π°Π»ΡΡΡ π°', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.split()[0] in currencies_flag_dict)
def reply(message):
    params = DATA.get(message.chat.id)
    if not params:
        params = DEFAULT_PARAMS
        DATA[message.chat.id] = DEFAULT_PARAMS
    bot.reply_to(message, show_result(message.text, DATA[message.chat.id]))


@bot.message_handler(func=lambda message: message.text == 'ΠΠ°Π·Π°Π΄ β©')
def back(message):
    markup = build_menu(menu_list=start_menu_list)
    bot.send_message(message.chat.id, 'ΠΡΠ±ΠΈΡΠ°ΠΉ ΡΠ΅ Π½Π°Π΄Π°π', reply_markup=markup)


@bot.message_handler(func=lambda message: re.search(rule, message.text))
def direct_convert(message):
    num, currency = message.text.split()
    params = DATA.get(message.chat.id)
    if not params:
        params = DEFAULT_PARAMS
        DATA[message.chat.id] = DEFAULT_PARAMS
    bot.reply_to(message, show_result(currency.upper(), DATA[message.chat.id], int(num)))


@bot.message_handler(func=lambda message: message.text == 'Settings β')
def test(message):
    params = DATA.get(message.chat.id)
    if not params:
        params = DEFAULT_PARAMS
        DATA[message.chat.id] = DEFAULT_PARAMS

    markup_inline = build_setting(params)
    bot.send_message(message.chat.id, 'Settings:', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    currency = call.data
    params = DATA[call.message.chat.id]
    if currency in params.keys():
        del params[currency]
    else:
        params[currency] = currencies_flag_dict[currency]
    markup_inline = build_setting(params)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Settings:',
        reply_markup=markup_inline)


@bot.message_handler(func=lambda message: True)
def wtf(message):
    bot.reply_to(message, 'ΠΠΎΡ Π½Π΅ ΠΏΠΎΠ½ΠΈΠΌΠ°ΡΡ π€·ββ')


bot.infinity_polling()
