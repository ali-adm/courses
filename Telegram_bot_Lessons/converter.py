import telebot
from currency_converter import CurrencyConverter
from telebot import types

# 6 - Бот для конвертации валют
# Видеоурок находятся по адресу: https://youtu.be/YrDL6EpYNiA
# В Боте использована библиотека CurrencyConverter: https://pypi.org/project/CurrencyConverter/
# которую необходимо установить: pip install CurrencyConverter. На сайте указано как ее подключать и использовать.

bot = telebot.TeleBot('6883404871:AAHPg4i4CJyJXol5yC-Koj4PY5BjFu7U8HY')  # Создание бота с Telegram HTTP API
currency = CurrencyConverter()  # Создание объекта currency
amount = 0  # Создание глобального объекта amount, указание его начального значения


@bot.message_handler(commands=['conv', 'converter', 'конвертер'])  # Декоратор реакции на команды /conv etc
def converter(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')  # Сообщение от Бота
    bot.register_next_step_handler(message, summa)  # Следующий шаг переход к функции summa


def summa(message):
    global amount  # Объявление глобальной переменной
    try:  # Обработчик исключения
        amount = int(message.text.strip())  # Приведение к формату числа введенного юзером текста
    except ValueError:  # Обработчик ошибки ValueError - неверный формат ввода данных
        bot.send_message(message.chat.id, 'Неверный формат, введите сумму')  # Сообщение о неверном формате
        bot.register_next_step_handler(message, summa)  # Следующий шаг переход к функции summa
        return  # Возврат к try - чтобы не выполнялся дальнейший код

    if amount > 0:  # Условие о том, что введенное число должно быть положительное
        markup = types.InlineKeyboardMarkup(row_width=2)  # Указание максимума кнопок в одном ряду
        btn1 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')  # Создание кнопки 1
        btn2 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn3 = types.InlineKeyboardButton('EUR/GBP', callback_data='eur/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')  # Условие else функции callback
        markup.add(btn1, btn2, btn3, btn4)  # Добавление кнопок в Маркап
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)  # Отправка сообщения с кнопками
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0')  # Сообщение об отрицательном числе
        bot.register_next_step_handler(message, summa)  # Следующий шаг переход к функции summa


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':  # Условие кнопки с другим значением валют
        values = call.data.upper().split('/')  # Переменная с полученными от кнопок значениями
        res = currency.convert(amount, values[0], values[1])  # Вызов конвертации currency со значениями
        bot.send_message(call.message.chat.id, f'Результат: {round (res, 2)}, введите новую сумму')
        bot.register_next_step_handler(call.message, summa)  # Следующий шаг переход к функции summa
    else:
        bot.send_message(call.message.chat.id, 'Введите свою пару значений валют через слэш')
        bot.register_next_step_handler(call.message, my_currency)  #


def my_currency(message):
    try:  # Обработчик исключений
        values = message.text.upper().split('/')  # Получить от юзера данные, разбить по символу / перевести в заглавн.
        res = currency.convert(amount, values[0], values[1])  # Вызов конвертации currency со значениями
        bot.send_message(message.chat.id,f'Результат: {round(res, 2)}, введите новую сумму')
        bot.register_next_step_handler(message, summa)  # Следующий шаг переход к функции summa
    except Exception:  # Любая ошибка, глобальный класс Exeption
        bot.send_message(message.chat.id,'Что-то не так, введите значение заново')
        bot.register_next_step_handler(message, my_currency)  # Следующий шаг переход к функции my_currency


# Program is running continuously
bot.polling(none_stop=True)