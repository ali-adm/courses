import telebot
import sqlite3

# 4 - SQLite3
# Подключение БД
# Видеоурок находятся по адресу: https://youtu.be/RpiWnPNTeww
# Create ALIadm Telegram Bot with use his HTTP API
bot = telebot.TeleBot('6883404871:AAHPg4i4CJyJXol5yC-Koj4PY5BjFu7U8HY')


# Принцип взаимодействия бота с БД заключается в следующем: в момент старта бота, или вызова той или иной команды,
# реакция на действия пользователя - создается таблица(ы) (только в том случае, если такой не существует - CREATE TABLE
# IF NOT EXISTS) в БД, и далее происходит взаимодействовие с таблицей(ами) - запись и чтение, стандартный набор функций
# при работе с БД.
@bot.message_handler(commands=['DB', 'db', 'database', ])
def database(message):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет дружок! Сейчас мы тебя совсем не больно зарегистрируем! А ну-ка введи свое имя!')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введи-ка пароль голубчик!')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data="users"))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


# Program is running continuously
bot.polling(none_stop=True)
