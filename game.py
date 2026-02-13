import flet as ft

def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "Corinthians"
    page.bgcolor = "#191970"
    
    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {imagem_correta}",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "🦅"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "🙁"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não é o {imagem_correta}. Tente de novo."
        
        container_palmeiras.on_click = None
        container_corinthians.on_click = None
        container_saopaulo.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = f"Clique no {imagem_correta}"

        container_palmeiras.image.opacity = 1.0
        container_palmeiras.on_click = jogar
        container_palmeiras.content.size = 0
        container_palmeiras.content.value = "Palmeiras"

        container_corinthians.image.opacity = 1.0
        container_corinthians.on_click = jogar
        container_corinthians.content.size = 0
        container_corinthians.content.value = "Corinthians"

        container_saopaulo.image.opacity = 1.0
        container_saopaulo.on_click = jogar
        container_saopaulo.content.size = 0
        container_saopaulo.content.value = "São Paulo"
        
        page.update()

    # Container Palmeiras
    container_palmeiras = ft.Container(
        content=ft.Text(
            "Palmeiras",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/palmeiras.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container Corinthians
    container_corinthians = ft.Container(
        content=ft.Text(
            "Corinthians",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/cor.png",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )
    # Container São Paulo
    container_saopaulo = ft.Container(
        content=ft.Text(
            "São Paulo",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/sao.png",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Selecione a imagem certa",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_palmeiras,
                        container_corinthians,
                        container_saopaulo
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

ft.run(main)