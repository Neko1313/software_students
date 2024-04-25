import flet as ft
import json


def test(page: ft.Page):
    rail = ft.NavigationRail(destinations=[
        ft.NavigationRailDestination(label='1'),
        ft.NavigationRailDestination(label='2')
    ])