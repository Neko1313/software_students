import flet as ft
import json
from tasks import get_task

tasks = get_task()
print(tasks)








def task(page: ft.Page):
    
    def change_tasks(number):
        page.views[-1].controls[0].controls.pop()
        page.views[-1].controls[0].controls.append(tasks[number])
        page.update()

    rail = ft.NavigationRail(destinations=[
            ft.NavigationRailDestination(icon='home', icon_content=ft.Text('1', size=50),data=ft.Container(height=100)),
            ft.NavigationRailDestination(icon_content=ft.Text('2',height=40), indicator_shape=ft.RoundedRectangleBorder),
        ], on_change= lambda e: change_tasks(e.control.selected_index), )
    
    task_page = ft.View('/task', [
    ft.Row(
                [
                    rail,
                    ft.VerticalDivider(width=1),
                    ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                expand=True,
            )
])
        
    

    
    
    
    page.views.append(task_page)
    page.go('/task')

ft.app(target=task)
    
    
    