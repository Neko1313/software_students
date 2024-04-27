import flet as ft 
import json 

PATHNAME = r'C:\Users\Lab\Desktop\Something\artem_proj\tasks.json'

def get_task():
    data = show_json(PATHNAME)
    counter = 0
    array = {}
    
    for dict in data:
        el = ft.Column([
            ft.Text(dict['text']),
            ft.CupertinoTextField(),
            ft.FilledButton('Отправить ответ')
         ])
        array.update({counter:el})
        counter+=1
    
    
    return(array) 
    
    
def show_json(file):
    with open(file, 'r',  encoding="utf-8") as json_file:
        tasks_raw = json.load(json_file)
    return(tasks_raw)
    
    
show_json(r'C:\Users\Lab\Desktop\Something\artem_proj\tasks.json')

get_task()