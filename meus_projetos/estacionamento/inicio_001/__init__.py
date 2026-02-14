from rich.console import Console
from time import sleep
from meus_projetos.estacionamento.menu_002 import painel
from meus_projetos.estacionamento.status_de_tela_005 import atualiza
from meus_projetos.estacionamento.verificação_003 import vagas, veiculo

console = Console()

def vaga():
    try:
        with open("vaga.txt", "r") as v:
            for c in v:
                vag = int(c)
            return vag
    except FileNotFoundError:
        pass
    else:
        vag = 10
        return vag


def atualizar_vaga(atualizar):
    with open("vaga.txt", "w") as v:
        v.write(f"{atualizar}")



while True:
    resp = painel()
    match resp:
        case '1':
            atualiza("Verificando-se há vagas...")
            sleep(2.5)
            vag = vaga()
            resp = vagas(vag)
            match resp:
                case '1':
                    vag -= 1
                    atualizar_vaga(vag)
                    vaga()
                    atualiza(":white_check_mark:  Veiculo cadastrado com sucesso!")
                case '2':
                    atualiza(":no_entry:  Encerrando cadastro")

            sleep(3.5)
        case '2':
            vag = vaga()
            retorno = veiculo(vag)
            if retorno:
                vag += 1
                atualizar_vaga(vag)
        case '3':
            atualiza(f"Um momento...")
            sleep(3.5)
        case '4':
            atualiza("Saindo")
            sleep(1.5)
            break
        case _:
            atualiza(':-1: Opção inválido. Tente novamente!', 'red')
            sleep(2.5)
