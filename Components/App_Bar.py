
import flet as ft

def TAppBar(page: ft.Page, *controls: ft.Control):
    '''Custom app bar because I didn't like the one built in to the library.

        You just need the page this is for and a list of controls to populate
        the bar.
    '''
    def window_minimize():
        page.window_minimized = True
        page.update()

    def window_maximize():
        if page.window_maximized == True:
            page.window_maximized = False
        else:
            page.window_maximized = True
        page.update()

    def on_hover_min(e):
        e.control.bgcolor = ft.colors.BLUE_GREY_400 if e.data == 'true' else ft.colors.BACKGROUND
        e.control.update()

    def on_hover_max(e):
        e.control.bgcolor = ft.colors.BLUE_400 if e.data == 'true' else ft.colors.BACKGROUND
        e.control.update()

    def on_hover_close(e):
        e.control.bgcolor = ft.colors.RED_400 if e.data == 'true' else ft.colors.BACKGROUND
        e.control.update()

    drag_area = ft.Container(
        ft.Row(
            *controls
        ),
            bgcolor=ft.colors.BLUE_GREY_700
    )

    control_panel = ft.Container(
        ft.Row(
            [
                ft.Container(content=ft.ElevatedButton(text='-', on_click=lambda _: window_minimize(), on_hover=on_hover_min, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), bgcolor=ft.colors.BACKGROUND)),
                ft.Container(content=ft.ElevatedButton(text='O', on_click=lambda _: window_maximize(), on_hover=on_hover_max, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), bgcolor=ft.colors.BACKGROUND)),
                ft.Container(content=ft.ElevatedButton(text='X', on_click=lambda _: page.window_close(), on_hover=on_hover_close, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), bgcolor=ft.colors.BACKGROUND))
            ],
            spacing=0
        ),
        margin=ft.margin.only(left=5),
        bgcolor=ft.colors.BACKGROUND
    )

    return ft.Row([ft.WindowDragArea(drag_area, expand=True), control_panel], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
