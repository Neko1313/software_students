import flet as ft
import json

tasks  = {
    0: ft.Container(content=ft.Column([ft.Text('First Element') ])),
    1: ft.Container(content=ft.Column([ft.Text('Second Element')]))
}




def main(page: ft.Page):
    
    def change_tasks(number):
        print(page.controls[0].controls[-1])
        page.controls[0].controls.pop()
        page.controls[0].controls.append(tasks[number])
        page.update()

    
    rail = ft.NavigationRail(destinations=[
        ft.NavigationRailDestination(icon='home', icon_content=ft.Text('1', size=50),data=ft.Container(height=100)),
        ft.NavigationRailDestination(icon_content=ft.Text('2',height=40), indicator_shape=ft.RoundedRectangleBorder),
    ], on_change= lambda e: change_tasks(e.control.selected_index), )
    
    page.add(
            ft.Row(
                [
                    rail,
                    ft.VerticalDivider(width=1),
                    ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                expand=True,
            )
        )

ft.app(target=main)
    
    
    