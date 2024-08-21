import flet as ft
import sqlite3

def main(page: ft.Page):
    # Установка заголовка страницы и темы
    page.title = "Registration"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    # Функция регистрации пользователя
    def register(e):
        # Подключение к базе данных SQLite
        db = sqlite3.connect('tg_app/any.filename')
        cur = db.cursor()

        # Создание таблицы пользователей, если она не существует
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    pass TEXT
                    )''')

        # Вставка данных нового пользователя в таблицу
        cur.execute(f"INSERT INTO users VALUES(NULL, '{user_login.value}', '{user_pass.value}')")

        # Сохранение изменений и закрытие базы данных
        db.commit()
        db.close()

        # Очистка полей ввода и обновление страницы
        user_login.value = ''
        user_pass.value = ''
        btn_reg.text = 'Добавлено'
        page.update()

    # Функция валидации полей ввода
    def validate(e):
        if all([user_login.value, user_pass.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page.update()

    # Создание текстовых полей для логина и пароля, а также кнопки для регистрации
    user_login = ft.TextField(label="Логин", width=200, on_change=validate)
    user_pass = ft.TextField(label="Пароль", password=True, width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text="Добавить", width=200, on_click=register, disabled=True)

    # Добавление элементов интерфейса на страницу
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Регистрация"),
                        user_login,
                        user_pass,
                        btn_reg
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Запуск приложения с функцией main в качестве цели
ft.app(target=main)