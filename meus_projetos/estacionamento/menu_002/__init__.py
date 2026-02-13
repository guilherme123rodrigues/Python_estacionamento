from rich.console import Console
from rich.panel import Panel

console = Console()

def painel():
    console.print(Panel.fit("[bold italic]\n[green]Menu de opções abaixo :point_down:[/]\n"
                            "\n[1] Estacionar"
                            "\n[2] Tirar o veículo"
                            "\n[3] Outros"
                            "\n[4] Sair[/]",
                            width=43, title='[bold italic white]Bem - vindo ao estacionamento Rodrigues[/]'),
                            style='yellow')
    return console.input("[bold italic green]Opções: [/]")
