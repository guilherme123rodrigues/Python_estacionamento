from rich.console import Console
from time import sleep
from meus_projetos.estacionamento.menu_002 import painel
from meus_projetos.estacionamento.status_de_tela import atualiza

console = Console()

while True:
    resp = painel()
    match resp:
        case '1':
            atualiza("Verificação de vaga concluída :+1:")
            sleep(3.5)
        case '2':
            atualiza(f"Consultando valor para retirada do veículo :+1:")
            sleep(3.5)
        case '3':
            atualiza(f"Outros")
            sleep(3.5)
        case '4':
            atualiza("Saindo")
            sleep(3.5)
            break
        case _:
            atualiza('[bold italic red]Valor inválido :-1:[/]')
            sleep(3.5)
