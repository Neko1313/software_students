import flet as ft
import json

credentials = {
        'name':'',
        'series':'',
        'number':''
        
    }

def main(page: ft.Page):
    
    
    a = 0
    
    def update_data(credentials):
        credentials['series'] = passport_data_input.controls[0].value
        credentials['number'] = passport_data_input.controls[1].value
        credentials['name'] = name_input.controls[1].value + ' ' + name_input.controls[0].value + ' ' + name_input.controls[2].value
        
    def insert_data(e):
        with open("your_json_file", "w") as fp:
            json.dump(credentials, fp)
        
    def close_confirmation(e):
        confirmation.open = False
        page.update()

    def open_confirmation(e):
        
        page.update()
        page.dialog = confirmation
        confirmation.open = True
        page.update()
        credentials['series'] = passport_data_input.controls[0].value
        credentials['number'] = passport_data_input.controls[1].value
        credentials['name'] = name_input.controls[1].value + ' ' + name_input.controls[0].value + ' ' + name_input.controls[2].value
        print(credentials)
    
    upper_text = ft.Text('Пробник',size=24,text_align=ft.alignment.center_left)
    upper_container = ft.Container(content=upper_text,alignment=ft.alignment.center_left,height=122)
    
    page.add(upper_container)
    page.add(ft.Divider(color='#5499BC',leading_indent=0))
    passport_data_input = ft.Row([
        ft.TextField(input_filter=ft.InputFilter(allow=True,regex_string=r"[0-9]",replacement_string=""),max_length=4, counter_text="",helper_text="Серия паспорта",),
        ft.TextField(input_filter=ft.InputFilter(allow=True,regex_string=r"[0-9]",replacement_string=""),max_length=6, counter_text="",helper_text="Номер паспорта")
        
    ],alignment=ft.MainAxisAlignment.CENTER)
    
    name_input = ft.Row([
        ft.TextField(input_filter=ft.InputFilter(allow=True, regex_string=r"[А-ЯЁа-яё\-]+"),helper_text="Фамилия сдающего"),
        ft.TextField(input_filter= ft.InputFilter(allow=True, regex_string=r"[А-ЯЁа-яё\-]+"),helper_text="Имя сдающего"),
        ft.TextField(input_filter= ft.InputFilter(allow=True, regex_string=r"[А-ЯЁа-яё\-]+"),helper_text="Отчество сдающего")
    ],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment= ft.CrossAxisAlignment.CENTER)
    
    center_collumn = ft.Column([
        passport_data_input,
        name_input
    ],alignment=ft.MainAxisAlignment.CENTER,spacing=100)
    
    confirmation = ft.AlertDialog(title=ft.Text('Вы уверены в корректности введённых данных?'), actions=[
            ft.TextButton("Да", on_click=insert_data),
            ft.TextButton("Нет", on_click=close_confirmation),
        ],shape=ft.BeveledRectangleBorder())
    
    
    center_container = ft.Container(content=center_collumn, alignment=ft.alignment.center, width=1920, height=758)
    page.add(center_container)
    submit_button = ft.CupertinoFilledButton('Подтвердить',on_click=open_confirmation)
    page.add(submit_button)

ft.app(main)
