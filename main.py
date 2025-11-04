# 2. Десктопные приложения 1 ч.  Знакомство PyQt, Flet или Тэкинтер. Понятия Декомпозиция.
import flet as ft

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    greeting_text = ft.Text("Hello world!")

    name_input = ft.TextField(label="Введите имя")

    name_button = ft.ElevatedButton("send", icon=ft.Icons.SEND)
    name_button_text = ft.TextButton("send")
    name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, name_button, name_button_text, name_button_icon)



ft.app(target=main) #type: ignore
