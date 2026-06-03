# ============================================================
# passageiros.py — Pessoa 2: Sistema de Passageiros
# ============================================================

from viagens import viagens

passageiros = []  # lista principal de passageiros


def cadastrar_passageiro():
    nome = input("Nome do passageiro: ")
    idade = int(input("Idade: "))
    documento = input("Documento (CPF ou RG): ")
    passageiro = {
        "nome": nome,
        "idade": idade,
        "documento": documento
    }
    passageiros.append(passageiro)
    print(f"Passageiro '{nome}' cadastrado com sucesso!")


def adicionar_passageiro_viagem():
    if not passageiros:
        print("Nenhum passageiro cadastrado.")
        return
    if not viagens:
        print("Nenhuma viagem cadastrada.")
        return

    # list comprehension para listar nomes
    nomes = [p["nome"] for p in passageiros]
    print("Passageiros disponíveis:")
    for i, nome in enumerate(nomes, 1):
        print(f"  {i} - {nome}")

    escolha_p = int(input("Escolha o número do passageiro: ")) - 1
    nome_escolhido = passageiros[escolha_p]["nome"]

    print("Viagens disponíveis:")
    codigos = list(viagens.keys())
    for i, cod in enumerate(codigos, 1):
        v = viagens[cod]
        vagas = v['qtd_max_passageiros'] - len(v['passageiros'])
        print(f"  {i} - Código {cod} | {v['planeta']} | {vagas} vagas")

    escolha_v = int(input("Escolha o número da viagem: ")) - 1
    codigo_viagem = codigos[escolha_v]
    viagem = viagens[codigo_viagem]

    if len(viagem["passageiros"]) >= viagem["qtd_max_passageiros"]:
        print("Viagem lotada! Não é possível adicionar mais passageiros.")
        return

    if nome_escolhido in viagem["passageiros"]:
        print("Passageiro já está nesta viagem.")
        return

    viagem["passageiros"].append(nome_escolhido)
    print(f"'{nome_escolhido}' adicionado à viagem para {viagem['planeta']}!")


def listar_passageiros_por_viagem():
    if not viagens:
        print("Nenhuma viagem cadastrada.")
        return
    for codigo, info in viagens.items():
        print(f"\nViagem: {info['planeta']} (Código {codigo})")
        if info["passageiros"]:
            for nome in info["passageiros"]:
                print(f"  - {nome}")
        else:
            print("  (sem passageiros)")


def calcular_custo_total():
    codigo = int(input("Digite o código da viagem: "))
    if codigo not in viagens:
        print("Viagem não encontrada.")
        return
    viagem = viagens[codigo]
    quantidade = len(viagem["passageiros"])
    valor_total = viagem["preco"] * quantidade
    print(f"Viagem para {viagem['planeta']}")
    print(f"Passageiros: {quantidade}")
    print(f"Preço por pessoa: R$ {viagem['preco']:.2f}")
    print(f"Custo total: R$ {valor_total:.2f}")


def listar_viagens_por_preco():
    """Usa lambda para ordenar viagens por preço (bônus)"""
    if not viagens:
        print("Nenhuma viagem cadastrada.")
        return
    ordenadas = sorted(viagens.items(), key=lambda item: item[1]["preco"])
    print("Viagens ordenadas por preço:")
    for cod, v in ordenadas:
        print(f"  Código {cod} | {v['planeta']} | R$ {v['preco']:.2f}")