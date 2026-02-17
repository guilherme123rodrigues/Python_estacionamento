from rich.panel import Panel
from rich.console import Console
from meus_projetos.estacionamento.pgto_006 import calculo

console = Console()

def remover(remove):

    v = False

    with open("veículos.txt", "r", encoding="utf-8") as arquivo:
        veiculos = arquivo.readlines()

    not_remover = []
    yes_remover = ''
    yes_remover2 = ''

    for veiculo in veiculos:
        dado = veiculo.strip().split(';')

        if dado[0] != remove:
            not_remover.append(veiculo)
        elif dado[0] == remove:
            yes_remover = dado[2]
            yes_remover2 = int(yes_remover[:2])

            v = True

        """if not dado[1].startswith(remove):
            l_remover.append(dado)"""

    with open("veículos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(not_remover)

    if v:
        calculo(yes_remover2)
        console.print(Panel(':+1: [bold italic green]Veículo removido do estacionamento[/]'), width=45)
        return v
    else:
        console.print(Panel('[bold italic red]Nenhum veículo registrado com esse CPF[/]'), width=45)
