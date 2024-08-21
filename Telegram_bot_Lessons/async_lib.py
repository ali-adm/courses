# Видео находится по адресу: https://youtu.be/BvPaua-oC08
# Для работы бота необходимо установить библиотеку aiogram версии не выше 2.5, иначе не работает executor
# pip install -v "aiogram==2.5"
# либо, если в системе уже есть aiogram более поздней версии -
# pip install --force-reinstall -v "aiogram==2.5"

from aiogram import Bot, Dispatcher, executor, types  # Асинхронная библиотека aiogram

bot = Bot('6883404871:AAHPg4i4CJyJXol5yC-Koj4PY5BjFu7U8HY')  # Заводим сущность - Бота, в кач-ве аргумента Bot
dp = Dispatcher(bot)  # Заводим диспетчера - dp, в кач-ве аргумента aiogram Dispatcher


# Параметр Message хранит полную информацию относительно чата и пользователя. Декоратор dp.message_handler,
# только не к боту, как в telebotе, а к диспетчеру, будет отслеживать команды введенные пользователем -
# если указать параметр commands=['start', 'другая_команда"], или фотографии, если указать тип
# content_types=['photo"], видео - content_types=['video"], текст - content_types=['text"],
# или любое сообщение от пользователя - если ничего не указывать - @dp.message_handler().
@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):  # Асинхронный метод. Указан параметр message и его тип.
    # await bot.send_message(message.chat.id, 'Htllo')  # Как в telebot
    # await message.answer('Hello!')  # Создать сообщение
    await message.reply('Hello!')  # Ответ на сообщение
    # file = open('/some.png', 'rb')  # Добавить изображение some.phg в кач-ые переменной file
    # await message.answer_photo(file)  # Отправить изображение file

# Обработчик кнопок InLine (которые под сообщением)
@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()  # Можно указать в скобках row_width= - количество кнопок в ряду
    markup.add(types.InlineKeyboardButton('В Гулю', url='https://google.com'))  # Кнопка "Открыть гугл"
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))  # будет происходить действие hello
    await message.reply('Hello', reply_markup=markup)  # Сообщение Hello, и передача markup


@dp.callback_query_handler()
async def callback(call):  # Действие hello
    await call.message.answer(call.data)  # Вывести данные, которые передаются при нажатии callback_data


# Обработчик кнопок нижних кнопок
@dp.message_handler(commands=['reply'])
async def reply(message: types.message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # Исчезающие кнопки, после одного нажатия
    markup.add(types.KeyboardButton('Site'))  # Кнопка Site
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)  # Сообщение Hello, и передача markup


# Program is running continuously
executor.start_polling(dp)
