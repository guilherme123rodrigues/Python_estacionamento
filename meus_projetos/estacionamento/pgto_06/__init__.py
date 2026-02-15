from meus_projetos.estacionamento.status_de_tela_005 import  atualiza
from meus_projetos.estacionamento.preço_07 import tab
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def calculo(dia):
    e = 8
    v_h = 1.5
    console.print(Panel(f"Hora de entrada: \t{e} hrs.\n"
                        f"Hara da saída:\t\t{datetime.now().hour} hrs.\n"
                        "Valor da hora:\t\tR$ 1,50\n"
                        f"Horas estacionado:\t{datetime.now().hour - e} hrs.\n"
                        f"Total:\t\t\tR${(datetime.now().hour - e) * v_h}", width=45, title="Análise"))
    console.print('-'*50)
    sleep(3.5)
    pgto(e, v_h)


def pgto(hr_e, valor):
    hr = datetime.now().hour - hr_e
    console.print(Panel('[1] À vista c/ desconto de 2.5%\n'
                        '[2] Car. de Cré. 2x, 3x ou 4x s/ juros\n'
                        '[3] Pix c/ desconto de 3%',
                        width=45,
                        title="Forma de Pagamento (PGTO)"
                        )
                  )
    p = console.input("Opção: ")
    match p:
        case '1':
            pago = (valor * hr) - (((valor * hr) * 2.50)/100)
        case '2':
            v = int(console.input("Em quantas parcelas vai ser?"))
            pago = valor * hr
            pagar = pago / v
        case '3':
            pago = (valor * hr) - (((valor * hr) * 3) / 100)
        case _:
            console.print("[bold italic red]Opção inválida. Tente novamente![/]")
    atualiza(f":+1: Valor de R$ {pago} confirmado")

    sleep(3.5)
