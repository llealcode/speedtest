import flet as ft
from files import style
from files import partials


def main(page: ft.Page):
    
    style.style_config(page)

    header = partials.Header()
    body = partials.Body()
    footer = partials.Footer()       

    content = ft.ResponsiveRow(
        expand=True,                       
        col=12,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                expand=True,
                col={'xs': 12, 'sm': 7, 'md': 5, 'lg': 4, 'xl': 4, 'xxl': 4},
                padding=ft.padding.all(20),
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[header, body, footer],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
        ]
    )

    page.add(content)


ft.app(main)
