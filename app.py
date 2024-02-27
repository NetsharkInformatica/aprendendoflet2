import flet as ft
#https://www.youtube.com/watch?v=kGNp24U5Oyo
#parei em 2433

def change_main_image(e):
    for elem in options.controls:
        if elem == e.control:
            elem.opacity=1
            main_image.src
            
            

def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK
    products_images=ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
         content=ft.Column(
           alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
             controls=[
                main_image := ft.Image(
                     src='https://abracasa.vteximg.com.br/arquivos/ids/172630/poltrona-costela-algodao-cinza-na-diagonal.jpg?v=637630144106530000',
                     width=800
                 ),
                options:=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://abracasa.vteximg.com.br/arquivos/ids/172630/poltrona-costela-algodao-cinza-na-diagonal.jpg?v=637630144106530000',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                            
                        ),
                        ft.Container(
                            image_src='https://abracasa.vteximg.com.br/arquivos/ids/172630/poltrona-costela-algodao-cinza-na-diagonal.jpg?v=637630144106530000',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                            
                        ),
                        ft.Container(
                            image_src='https://abracasa.vteximg.com.br/arquivos/ids/172630/poltrona-costela-algodao-cinza-na-diagonal.jpg?v=637630144106530000',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                            
                        )
                        
                    ]
                     
                )
                
             ]
         )
    )
    products_details=ft.Container( )

    layout=ft.Container(
        width=800,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=200,color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                products_images,
                products_details
                
            ]
        )
    )


    page.update()

    page.add(layout)


if __name__=="__main__":
    ft.app(target=main)