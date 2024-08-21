import telebot
import requests
import json

# 5 - Бот для получения погоды, который не ломается при не корректном указании локации, города.
# Видеоурок находятся по адресу: https://youtu.be/v8Nqa78v2tE
# Необходимо установить requests - pip install requests
# Для получения погоды использован API с сайта https://openweathermap.org/, где необходимо зарегистрироваться. Там-же
# на сайте есть описание способов использования API.


# Создание бота (bot) Telegram используя его HTTP API, который можно получить у botfather'a и создание переменной API
# где указывается API, полученный от openweathermap.org.
bot = telebot.TeleBot('6883404871:AAHPg4i4CJyJXol5yC-Koj4PY5BjFu7U8HY')
API = '5b7e510687689b527393081e3fc3188f'

# Создание декоратора, который будет реагировать на команду /weather (или /погода) и запрашивать название города.
@bot.message_handler(commands=['weather', 'погода'])
def weather(message):
    bot.send_message(message.chat.id, 'Привет синоптик! Напиши город, где ты хочешь узнать погоду!')


# Декоратор, получает имя города. Далее полученный текст - название города преобразуется в прописной, без пробелов
# до и после слова, далее подставляется вместе с API в URL запроса openweathermap.org. Если от openweathermap.org
# приходит ответ (проверка статуса запроса - успешная обработка URL 200) - он приходит в JSON формате, который
# обрабатывается, и выводится пользователю в виде понятного ответа. Во втором блоке, с помощью тернарного условия,
# выбирается в зависимости от значения температуры одно из двух изображений, и посылается пользователю. Если статус
# запроса отличен от 200 - пользователю посылается сообщение о том, что такого города не существует.
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"Таки сейчас погода: {temp}")

        image = 'weather-sun.jpg' if temp > 5.0 else 'weather-cloud.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Нет такого города, географ!')


# Program is running continuously
bot.polling(none_stop=True)
