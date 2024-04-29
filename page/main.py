import flet as ft
import json
from tasks import get_task

credentials = {
        'name':'',
        'series':'',
        'number':''
        
    }

tasks = get_task()

def main(page: ft.Page):
    
    
    # Функции, связанные со страницей ввода данных    
    def insert_data(e):
        with open("your_json_file", "w") as fp:
            json.dump(credentials, fp)
        confirmation.open = False
        page.update()
        route_change('/tasks')
        page.go('/tasks')
        
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
    
    
    
    
    #Связанные со страницей ввода компоненты
    upper_text = ft.Text('Пробник',size=24,text_align=ft.alignment.center_left)
    upper_container = ft.Container(content=upper_text,alignment=ft.alignment.center_left,height=122)
    
    passport_data_input = ft.Row([
        
        ft.TextField(
            input_filter=ft.InputFilter(
                allow=True,regex_string=r"[0-9]",
                replacement_string=""
                ),
            max_length=4, 
            counter_text="",
            helper_text="Серия паспорта",),
        
        ft.TextField(
            input_filter=ft.InputFilter(
                allow=True,regex_string=r"[0-9]",
                replacement_string=""
                ),
            max_length=6, 
            counter_text="",
            helper_text="Номер паспорта")
        
    ],alignment=ft.MainAxisAlignment.CENTER)
    
    name_input = ft.Row([
        ft.TextField(
            input_filter=ft.InputFilter(
                allow=True, 
                regex_string=r"[А-ЯЁа-яё\-]+"),
            helper_text="Фамилия сдающего"),
        
        ft.TextField(
            input_filter= ft.InputFilter(
                allow=True, 
                regex_string=r"[А-ЯЁа-яё\-]+"),
            helper_text="Имя сдающего"),
        
        ft.TextField(
            input_filter= ft.InputFilter(
                allow=True, 
                regex_string=r"[А-ЯЁа-яё\-]+"),
            helper_text="Отчество сдающего")
        
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
    
    submit_button = ft.CupertinoFilledButton('Подтвердить',on_click=open_confirmation)
    
    
    
    
    #Функции, связанные со страницей заданий
    def change_tasks(number):
        page.views[-1].controls[0].controls.pop()
        page.views[-1].controls[0].controls.append(tasks[number])
        page.update()




    #Компоненты, связанные со страницей заданий
    rail = ft.NavigationRail(destinations=[
            ft.NavigationRailDestination(icon='home', icon_content=ft.Text('1', size=50),data=ft.Container(height=100)),
            ft.NavigationRailDestination(icon_content=ft.Text('2',height=40), indicator_shape=ft.RoundedRectangleBorder),
        ], on_change= lambda e: change_tasks(e.control.selected_index), )
    
    
    
    
    #Компоновка View страницы заданий
    task_page = ft.View('/tasks', [
    ft.Row(
                [
                    rail,
                    ft.VerticalDivider(width=1),
                    ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                expand=True,
            )
        ])
    
    
    #Роутинг
    def route_change(route):
        page.views.clear()
        page.views.append(ft.View('/', [
            upper_container, ft.Divider(color='#5499BC',leading_indent=0), confirmation, center_container, submit_button
        ]))
        if page.route == '/tasks':
            page.views.append(
                task_page
            )
        page.update()
        
    page.on_route_change = route_change
    page.go(page.route)
    
    
ft.app(main)
