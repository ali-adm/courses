import telebot
import webbrowser
from telebot import types

# Видеоуроки находятся по адресу: https://youtu.be/RpiWnPNTeww
# Create ALIadm Telegram Bot with use his HTTP API
bot = telebot.TeleBot('6883404871:AAHPg4i4CJyJXol5yC-Koj4PY5BjFu7U8HY')


# Основние кнопки (внизу, у строки ввода).
# Декоратор message_handler обрабатывает команды с помощью параметра commands. После получения /start -
# bot.send_message возвращает "Привет", и отрисовываются кнопки с текстом - reply_markup=markup.
# Для отрисовывания кнопок создватся объект markup, и к нему применяется метод types.ReplyKeyboardMarkup,
# далее создаются кнопки btn1,2,3 - методом types.KeyboardButton с параметрам - текстом, который будет
# отображаться на кнопках. Дизайн расположения кнопок задавется markup.row, где в кач-ве аргументов
# указываеются кнопки. В даном случае будет одана кнопка btn1 сверху, в первом ряду, а под ней второй ряд,
# c двумая кнопками btn2 и btn3.
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    # file = open('./photo.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
# Закомментированые части кода - могут отсылать пользователю фото, аудио, и видео файлы, путем указания
# файла file = open('./photo.jpg', 'rb') - в данном слуаеше указан файл photo.jpg из той же директории, где
# находится этот python файл. Файл photo.jpg будет открыт для юзера в режиме чтения (rb). Таким же образом можно
# передавать файлы *.mp3,*mp4.


# Назнечение кнопкам действий:
# В предыдущей функции start было назначено действие on-click следующего шага,
# после действия юзера - bot.register_next_step_handler(message, on_click). Далее идет описание что делать,
# есил сработал on_click. Если on_click с параметром "Перейти на сайт", то Бот, в качестве теста пишет
# сообщение "Website is open", прикрутить можно любой функционал. Аналогично происходит для on_click "Удалить
# фото". После срабатывания действия, никакие дальнейшие действия работаь больше не будут, потому что
# не указаны - т.е. бот остановится.
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')


# Handles text
# The "message_handler" decorator handles commands using the "commands" parameter
# Commands 'link', 'site', 'youtube', 'website' that open the specified URL
@bot.message_handler(commands=['link', 'site', "youtube", 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/@alexgray1523')


# Add the commands "start", "main", and "hello" and the action of are commands is to send a message to the user
@bot.message_handler(commands=['main', 'hello'])
# Add function. From message extract first and last name of user.
def main(message):
    bot.send_message(message.chat.id, f'Салам! {message.from_user.first_name} {message.from_user.last_name}')


# This is a copy of the previous function that handles the help command instead of "start", "main", and "hello"
@bot.message_handler(commands=['help', ])
# Add function. May use with HTML tags (parse_mode='html') for Bold, Regular Underline (подчектнутый шрифт) fonts etc
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


# This decorator handles simple test 'привет', and 'reply_to' return user ID by request
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Салам! {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


# Кнопки внизу сообщения.
# Декоратор message_handler обрабатывает файлы с помощью content_types. После получения, в данном случае
# изображения bot.reply_to возвращает сообщение с текстом "Шикарное фото!", и отрисовываются кнопки с
# текстом - reply_markup=markup. Для отрисовывания кнопок создватся объект markup, и к нему применяется
# метод types.InlineKeyboardMarkup, далее создаются кнопки btn1,2,3 - методом types.InlineKeyboardButton с
# параметрам - текстом, который будет отображаться на кнопках, и дейстиями производимыми кнопками, путем
# указания параметра callback_data, который будет описан ниже. Дизайн расположения кнопок задавется markup.row,
# где в кач-ве аргументов указываеются кнопки. В даном случае будет одана кнопка btn1 сверху, в первом ряду,
# а под ней второй ряд, c двумая кнопками btn2 и btn3.
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти в Гулю', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Шикарное фото!', reply_markup=markup)


# Описание callback_data: с помощью декоратора callback_query_handler и анонимной функции лямбда - которая возвращает
# True при пустом параметре) создается функция callback_message, которой в качестве аргумента присваивается callback.
# Далее создаются методы для редактирования текста и удаления присланного рисунка.
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


# Program is running continuously
bot.polling(none_stop=True)
