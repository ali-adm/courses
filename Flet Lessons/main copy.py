import flet as ft

def main(page: ft.Page):
    page.title = "Weather App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    

ft.app(target=main)
