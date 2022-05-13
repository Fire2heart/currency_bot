import telebot
import re
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)

currencies_flag_dict = {'USD': '🇺🇸', 'EUR': '🇪🇺', 'RUB': '🇷🇺', 'UAH': '🇺🇦', 'PLN': '🇵🇱', 'AUD': '🇦🇺',
                        'CNY': '🇨🇳', 'JPY': '🇯🇵', 'CHF': '🇨🇭', 'CAD': '🇨🇦', 'GBP': '🇬🇧'}

crypto_list = ['BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'LTC', 'CZK', 'XLM']
start_menu_list = ['Crypto 💎', 'Currency 🏦']

rule = '\d\s[A-Z, a-z]{3}'


def build_buttons(flag_dict: dict) -> list:
    buttons_list = []
    for key, value in flag_dict.items():
        temp = f'{key} {value}'
        list.append(temp)
    return buttons_list


def build_menu(menu_list: list):
    markup = types.ReplyKeyboardMarkup()
    buttons = [types.KeyboardButton(b) for b in menu_list]
    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = build_menu(menu_list=start_menu_list)
    bot.send_message(
        message.chat.id, '🖖 Здарова! Выбирай че нада👇', reply_markup=markup)
    bot.send_message(message.chat.id, 'Либо напиши число и валюту: "2 btc"')


@bot.message_handler(func=lambda message: message.text == 'Currency 🏦')
def show_currency(message):
    menu = build_buttons(currencies_flag_dict)
    menu.append('Назад ↩')
    markup = build_menu(menu_list=menu)
    bot.send_message(message.chat.id, 'Выбери валюту 💰', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in crypto_list)
def reply_currency(message):
    # bot.reply_to(message, show_currency(message.text, currencies_flag_dict))


@bot.message_handler(func=lambda message: message.text == 'Crypto 💎')
def show_crypto(message):
    menu = crypto_list.copy()
    menu.append('Назад ↩')
    markup = build_menu(menu_list=menu)
    bot.send_message(message.chat.id, 'Выбери валюту 💰', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in crypto_list)
def reply_crypto(message):
    # bot.reply_to(message, show_currency(message.text, currencies_flag_dict))


@bot.message_handler(func=lambda message: message.text == 'Назад ↩')
def back(message):
    markup = build_menu(menu_list=start_menu_list)
    bot.send_message(message.chat.id, 'Выбирай че нада👇', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def wtf(message):
    bot.reply_to(message, 'Моя не понимать 🤷‍♂')


bot.infinity_polling()

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text in start_menu_list and message.text == 'Currency 🏦':
#         menu_w = currencies_list.copy()
#         menu_w.append('Назад ↩')
#         markup = menu(menu_list=menu_w)
#         bot.send_message(message.chat.id, 'Выбери валюту 💰',
#                          reply_markup=markup)

#     elif message.text in start_menu_list and message.text == 'Crypto 💎':
#         menu_w = crypto_list.copy()
#         menu_w.append('Назад ↩')
#         markup = menu(menu_list=menu_w)
#         bot.send_message(message.chat.id, 'Выбери валюту 💰',
#                          reply_markup=markup)

#     elif message.text == 'Назад ↩':
#         markup = menu(menu_list=start_menu_list)
#         bot.send_message(message.chat.id, 'Выбирай че нада👇',
#                          reply_markup=markup)

#     elif message.text in crypto_list:
#         bot.reply_to(message, show_currency(message.text, currencies_list))

#     elif message.text in currencies_list:
#         bot.reply_to(message, show_currency(message.text, currencies_list))

#     elif bool(re.search(rule, message.text)):
#         base = ''.join(message.text.split()[1:])
#         bot.reply_to(message, show_currency(
#             base.upper(), currencies_list, int(''.join(message.text.split()[:1]))))

#     else:
#         bot.reply_to(message, 'Моя не понимать 🤷‍♂')


# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     markup = show_buttons(currencies)
#     if call.message:
#         if call.data == 'USD 🇺🇸':
#             bot.edit_message_text(chat_id = call.message.chat.id,
#                                   message_id= call.message.id,  text= 'Money!', reply_markup=markup)
#         elif call.data == 'question2':
#             bot.send_message(call.message.chat.id, 'Ну и вали!!', reply_markup=markup)
