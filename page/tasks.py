import flet as ft 
import json 
from credentials import Credentials


credentials = Credentials()


#Заменить на свой 
PATHNAME = r'C:\Users\Lab\Desktop\Something\artem_proj\software_students\tasks.json'

def handle_submit(cred, number, answer):
    cred.write_answer(number+1, answer)

def get_task():
    data = show_json(PATHNAME)
    counter = 0
    array = {}
    
    for dict in data:
        el = ft.Column([
            ft.Text(dict['text']),
            ft.CupertinoTextField(),
            ft.Row(
                    [ft.FilledButton('Отправить',on_click= lambda e: (credentials.write_answer(counter+1, 
                                                                              e.control.parent.parent.controls[1].value,),
                                                    ))], alignment=ft.MainAxisAlignment.END
    )
         ], width=1500, horizontal_alignment=ft.CrossAxisAlignment.CENTER, )
        array.update({counter:el})
        counter+=1
    
    
    return(array) 
    
    
def show_json(file):
    with open(file, 'r',  encoding="utf-8") as json_file:
        tasks_raw = json.load(json_file)
    return(tasks_raw)

get_task()