
import flet as ft

class TAppBar(ft.UserControl):

    def __init__(self, *controls: ft.Control):
        super().__init__()
        self.controls = controls

    def build(self):
        '''Custom app bar because I didn't like the one built in to the library.

            You just need the page this is for and a list of controls to populate
            the bar.
        '''

        drag_area = ft.Container(
            ft.Container(
                ft.Row(
                    [*self.controls]
                ),
                margin=ft.margin.only(left=15)
            ),
            bgcolor=ft.colors.BLUE_GREY_700,
            height=40
        )

        control_panel = ft.Container(
            ft.Row(
                [
                    ft.Container(content=ft.ElevatedButton(text='-', on_click=lambda _: self.window_minimize(), on_hover=self.on_hover_min, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), bgcolor=ft.colors.BACKGROUND)),
                    ft.Container(content=ft.ElevatedButton(text='O', on_click=lambda _: self.window_maximize(), on_hover=self.on_hover_max, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), bgcolor=ft.colors.BACKGROUND)),
                    ft.Container(content=ft.ElevatedButton(text='X', on_click=lambda _: self.page.window_close(), on_hover=self.on_hover_close, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), bgcolor=ft.colors.BACKGROUND))
                ],
                spacing=0
            ),
            margin=ft.margin.only(left=5),
            bgcolor=ft.colors.BACKGROUND
        )
        return ft.Row([ft.WindowDragArea(drag_area, expand=True), control_panel], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def window_minimize(self):
        self.page.window_minimized = True
        self.page.update()

    def window_maximize(self):
        if self.page.window_maximized == True:
            self.page.window_maximized = False
        else:
            self.page.window_maximized = True
        self.page.update()

    def on_hover_min(self, e):
        e.control.bgcolor = ft.colors.BLUE_GREY_400 if e.data == 'true' else ft.colors.BACKGROUND
        e.control.update()

    def on_hover_max(self, e):
        e.control.bgcolor = ft.colors.BLUE_400 if e.data == 'true' else ft.colors.BACKGROUND
        e.control.update()

    def on_hover_close(self, e):
        e.control.bgcolor = ft.colors.RED_400 if e.data == 'true' else ft.colors.BACKGROUND
        e.control.update()
