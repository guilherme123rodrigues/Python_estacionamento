from meus_projetos.estacionamento.status_de_tela_005 import atualiza

def ler():
    try:
        lista = []
        with open("veículo.txt", "r", encoding="utf-8") as arquivo:
            for c in arquivo:
                if ';' in c:
                    r = c.strip().split(',')
                    lista.append(r)
    except FileNotFoundError:
        pass
    finally:
        atualiza(":white_check_mark:  Veiculo cadastrado com sucesso!")


def salvar(l):
    with open("veículos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f'{l[0]};{l[1]};{l[2]}\n')
    ler()