from rich.console import Console
from time import sleep
from meus_projetos.estacionamento.menu_002 import painel
from meus_projetos.estacionamento.status_de_tela_005 import atualiza
from meus_projetos.estacionamento.verificação_003 import vagas
from meus_projetos.estacionamento.preço_007 import tab
from meus_projetos.estacionamento.atualizar_vagas_008 import vaga, atualizar_vaga
from meus_projetos.estacionamento.salve_veiculo_004 import salvar
from meus_projetos.estacionamento.pgto_006 import calculo
from meus_projetos.estacionamento.remover_veículo_009 import remover


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
                    hr = console.input('Horário da entrada: ')
                    console.print('-' * 50)
                    placa1 = placa[:4]
                    placa2 = '-' + placa[-4:]
                    placa3 = placa1 + placa2

                    salvar([cpf, placa3, hr])
                case '2':
                    atualiza(":no_entry:  Encerrando cadastro")

            sleep(3.5)
        case '2':
            vag = vaga()
            veiculo_remover = console.input('Insirá o número do CPF para identificar o veículo: ')
            r = remover(veiculo_remover)
            if r:
                vag += 1
                atualizar_vaga(vag)
            sleep(2.5)
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
