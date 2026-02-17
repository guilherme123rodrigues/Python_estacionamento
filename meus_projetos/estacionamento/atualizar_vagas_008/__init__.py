def vaga():
    try:
        with open("vaga.txt", "r") as v:
            for c in v:
                vag = int(c)
            return vag
    except FileNotFoundError:
        pass
    else:
        vag = 50
        return vag


def atualizar_vaga(atualizar):
    with open("vaga.txt", "w") as v:
        v.write(f"{atualizar}")
