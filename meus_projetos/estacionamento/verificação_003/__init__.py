from cmath import cos
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from time import sleep
from meus_projetos.estacionamento.status_de_tela_005 import atualiza
from meus_projetos.estacionamento.pgto_06 import calculo

console = Console()


def vagas(v):
    if v == 0:
        console.print(Panel(f":cross_mark: [bold italic yellow]Infelizmente não a vagas no momento[/]", width=45))
        return  '2'
    else:
        while True:
            console.print(
                Panel("[bold italic green]Deseja estacionar[/]\n"
                      "[bod italic white]\n"
                      "[1] Sim\n"
                      "[2] Não[/]",
                      width=45,
                      title=f"[bold italic yellow]{v} vagas(s) disponivel no momento[/]"
                      )
            )
            r = console.input("[bold italic green]Opção[/]? ")
            if r in {'1', '2'}:
                break
            else:
                atualiza(":-1: Opção inválido. Tente novamente!", 'red')
            sleep(2.5)
        return r


def veiculo(v):
    if v == 10:
        atualiza(":no_entry: Não a veículo no estacionamento!", 'yellow')
        r = False
        sleep(2.5)
    else:
        atualiza(f"Calculando valor do estacionamento...", 'blue')
        sleep(2.5)
        calculo()
        r = True
    return r

