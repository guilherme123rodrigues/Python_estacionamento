from time import sleep
from rich.console import Console
from rich.table import Table
from meus_projetos.estacionamento.status_de_tela_005 import atualiza

console = Console()

semana = 'R$1.50'
fins_de_semana = 'R$3.50'
feriados = 'R$5.50'

def tab(d=''):
    if d == '1':
        return 1.50
    elif d == '2':
        return 3.50
    elif d == '3':
        return 5.50

    tab = Table(title='Preços R$', title_style='green')

    tab.add_column(header='Dia da semana', header_style='bold italic white', justify='left', style='bold italic white')
    tab.add_column(header='Valor da hora', header_style='bold italic white', justify='center', style='bold italic white')

    tab.add_row('Seg. à Sex.', semana)
    tab.add_row('Sábados e Domingos', fins_de_semana)
    tab.add_row('Feriados', feriados)

    console.print(tab)
