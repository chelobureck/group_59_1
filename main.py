# 2. Десктопные приложения 1 ч.  Знакомство PyQt, Flet или Тэкинтер. Понятия Декомпозиция.
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    greeting_text = ft.Text("Hello world!")
    greeting_history = []
    history_text = ft.Text("История приветствий")

    def on_button_click(_):
        name = name_input.value.strip() #type: ignore
        timestap = datetime.now().strftime("%H:%M")
        if name:
            greeting_text.value = f"{timestap} Hello {name}"
            name_input.value = None

            greeting_history.append(f"{timestap} - {name}")
            history_text.value = "История приветствий \n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)

    name_button = ft.ElevatedButton("send", icon=ft.Icons.SEND, on_click=on_button_click)
    # name_button_text = ft.TextButton("send")
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, name_button) # name_button_text, name_button_icon


ft.app(target=main) #type: ignore