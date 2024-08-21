import flet as ft
import sqlite3

def main(page: ft.Page):
    # Установка заголовка страницы и темы
    page.title = "Aliadm App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    # Функция регистрации пользователя
    def register(e):
        # Подключение к базе данных SQLite
        db = sqlite3.connect('tg_app/pyguiapps/db_any.filename')
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
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True
        page.update()

    # Функция авторизации пользователя
    def auth_user(e):
        db = sqlite3.connect('tg_app/pyguiapps/db_any.filename')
        cur = db.cursor()
        cur.execute(f"SELECT * FROM users WHERE login = '{user_login.value}' AND pass = '{user_pass.value}'")
        if cur.fetchone() is not None:
            user_login.value = ''
            user_pass.value = ''
            btn_auth.text = 'Авторизовано'
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text(f'Неверные учетные данные'))
            page.snack_bar.open = True
            page.update()
        db.commit()
        db.close()

    # Создание текстовых полей для логина и пароля, а также кнопок для регистрации и авторизации
    user_login = ft.TextField(label="Логин", width=200, on_change=validate)
    user_pass = ft.TextField(label="Пароль", password=True, width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text="Добавить", width=200, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text="Авторизовать", width=200, on_click=auth_user, disabled=True)

    # Создание панелей для регистрации и авторизации
    panel_register = ft.Row(
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

    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Авторизация"),
                    user_login,
                    user_pass,
                    btn_auth
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Функция для навигации между панелями
    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0: page.add(panel_register)
        elif index == 1: page.add(panel_auth)

    # Создание навигационной панели
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label="Регистрация"),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Авторизация")
        ],
        on_change=navigate
    )

    # Отображение панели регистрации при запуске приложения
    page.add(panel_register)

# Запуск приложения с функцией main в качестве цели
ft.app(target=main)