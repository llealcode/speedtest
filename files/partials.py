import flet as ft
from files import functions


class Header(ft.Container):

    def __init__(self):

        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.SPEED, color=ft.Colors.AMBER, size=40),
                    ft.Text(value='Speed Test', size=25, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                ]
            ),
            padding=ft.padding.only(left=20, top=40)
        )


class Body(ft.Container):

    def __init__(self):

        super().__init__(
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        # margin=ft.margin.only(bottom=70),
                        alignment=ft.alignment.center,
                        content=ft.ElevatedButton(
                            content=ft.Text(value='INICIAR', size=30, color=ft.Colors.GREY_900, weight=ft.FontWeight.BOLD),
                            height=200,
                            width=200,
                            bgcolor=ft.Colors.YELLOW_800,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=300)),
                            animate_scale=ft.Animation(duration=800, curve=ft.AnimationCurve.DECELERATE),
                            on_click=lambda e : functions.testar_animar(e, texto_download, texto_upload, texto_ping)
                            
                        )
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=40),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.Icons.FILE_DOWNLOAD_ROUNDED, color=ft.Colors.AMBER, size=30),
                                        texto_download:=ft.Text(value='0.0 Mbps', size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.W_400)
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.Icons.UPLOAD_ROUNDED, color=ft.Colors.AMBER, size=30),
                                        texto_upload:=ft.Text(value='0.0 Mbps', size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.W_400)
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.Icons.NETWORK_PING, color=ft.Colors.AMBER, size=30),
                                        texto_ping:=ft.Text(value='0.0 Ms', size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.W_400)
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )


class Footer(ft.Container):

    def __init__(self):

        super().__init__(
            content=ft.Container(
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.symmetric(vertical=20, horizontal=17),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='© Lucas Leal 2025', 
                            size=15, 
                            weight=ft.FontWeight.W_400, 
                            color=ft.Colors.GREY_200
                        )
                    ]
                )
            )
        )
