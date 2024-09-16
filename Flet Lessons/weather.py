import flet as ft
import requests

def main(page: ft.Page):
    # Установка заголовка страницы и темы
    page.title = "Weather App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Создание текстового поля для ввода города и текстового поля для отображения погоды
    user_data = ft.TextField(label="Введите город", width=400)
    weather_data = ft.Text("")

    # Обработчик события для получения информации о погоде
    def get_info(e):
        if len(user_data.value) <= 2:
            return
        API = '5b7e510687689b527393081e3fc3188f'
        URL = (f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric&lang=ru')
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value = "Погода " + str(temp)
        page.update()

    # Обработчик события для смены темы
    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == 'dark' else 'dark'
        page.update()

    # Добавление элементов интерфейса на страницу
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text("Программа погоды")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Получить", on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )

# Запуск приложения с функцией main в качестве цели
ft.app(target=main)