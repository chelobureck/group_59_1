# 2. Десктопные приложения 1 ч.  Знакомство PyQt, Flet или Тэкинтер. Понятия Декомпозиция.
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world!")
    greeting_history = []
    history_text = ft.Text("История приветствий")
    six_am = datetime.strptime("6:00", "%H:%M").time()
    day_start = datetime.strptime("12:00", "%H:%M").time()
    day_end = datetime.strptime("18:00", "%H:%M").time()
    night = datetime.strptime("23:59", "%H:%M").time()

    def on_button_click(_):
        name = name_input.value.strip() #type: ignore
        age = age_input.value.strip() #type: ignore
        timestap = datetime.now().strftime("%H:%M")
        time_type_timestap = datetime.strptime(str(timestap), "%H:%M")
        try:
            if name and ( 0 < int(age) < 115):
                greeting_text.color = ft.Colors.WHITE
                if six_am < time_type_timestap.time() < day_start:
                    greeting_text.value = f"{timestap} Доброе утро {name}, ваш возраст {age}"
                elif day_start < time_type_timestap.time() < day_end:
                    greeting_text.value = f"{timestap} Добрый день {name}, ваш возраст {age}"
                elif day_end < time_type_timestap.time() < night:
                    greeting_text.value = f"{timestap} Доброе вечер {name}, ваш возраст {age}"
                else:
                    greeting_text.value = f"{timestap} Доброй ночи {name}, ваш возраст {age}"

                greeting_history.append(f"{timestap} - {name}, возсраст {age}")
                history_text.value = "История приветствий \n" + "\n".join(greeting_history)
            elif name:
                greeting_text.value = "Введите корректный возраст"
                greeting_text.color = ft.Colors.RED
            elif age:
                greeting_text.value = "Введите корректное имя"
                greeting_text.color = ft.Colors.RED
            else:
                greeting_text.value = "Введите корректные данные"
                greeting_text.color = ft.Colors.RED
        except ValueError:
            greeting_text.value = "введите возраст в промежутке 0-115"
            greeting_text.color = ft.Colors.RED
        name_input.value = None
        age_input.value = None
        page.update()

    def on_theme_click(_):
        if page.theme_mode is ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        elif page.theme_mode is ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)
    age_input = ft.TextField(label="Введите возраст", on_submit=on_button_click)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=on_theme_click)
    name_button = ft.ElevatedButton("send", icon=ft.Icons.SEND, on_click=on_button_click)
    # name_button_text = ft.TextButton("send")
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, age_input, name_button, theme_button, history_text) # name_button_text, name_button_icon

try:
    ft.app(target=main) #type: ignore
except ValueError:
    print("ошибка при работе с данными")