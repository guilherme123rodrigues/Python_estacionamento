from rich.console import Console
from time import sleep
from meus_projetos.estacionamento.menu_002 import painel
from meus_projetos.estacionamento.status_de_tela_005 import atualiza
from meus_projetos.estacionamento.verificação_003 import vagas, veiculo
from meus_projetos.estacionamento.preço_07 import tab
from meus_projetos.estacionamento.atualizar_vagas_08 import vaga, atualizar_vaga
from meus_projetos.estacionamento.salve_veiculo_004 import salvar

console = Console()

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
                    console.print('-'*50)
                    cpf = console.input('CPF do titúlar: ')
                    placa = console.input('Placa do veículo: ')
                    cor = console.input('Cor do veículo: ')
                    console.print('-' * 50)
                    placa1 = placa[:5]
                    placa2 = '-' + placa[5:]
                    placa3 = placa1 + placa2

                    salvar([cpf, placa3, cor])
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
            console.print('-'*50)
            tab()
            console.print('-'*50)
            sleep(4)
        case '4':
            atualiza("Saindo")
            sleep(1.5)
            break
        case _:
            atualiza(':-1: Opção inválido. Tente novamente!', 'red')
            sleep(1)
