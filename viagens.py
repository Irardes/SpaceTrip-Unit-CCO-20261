# ============================================================
# viagens.py — Pessoa 1: Sistema de Viagens Espaciais
# ============================================================

viagens = {}  # dicionário principal de viagens

classes_nave = ("Econômica", "Executiva", "Luxo")
status_opcoes = ("Confirmada", "Em andamento", "Concluída")


def cadastrar_viagens():
    codigo = int(input("Código da viagem: "))
    if codigo in viagens:
        print("Código já existente")
        return
    planeta = input("Planeta de destino: ")
    preco = float(input("Preço da viagem: "))
    duracao = int(input("Duração da viagem (em horas): "))
    qtd_max_passageiros = int(input("Quantidade máxima de passageiros: "))

    print("Status da viagem:\n1 - Confirmada\n2 - Em andamento\n3 - Concluída")
    status = int(input("Escolha o status: "))
    status = status_opcoes[status - 1]

    print("Classe da nave:\n1 - Econômica\n2 - Executiva\n3 - Luxo")
    classe_nave = int(input("Escolha a classe: "))
    classe_nave = classes_nave[classe_nave - 1]

    viagens[codigo] = {
        "planeta": planeta,
        "preco": preco,
        "duracao": duracao,
        "qtd_max_passageiros": qtd_max_passageiros,
        "status": status,
        "classe_nave": classe_nave,
        "passageiros": []
    }
    print("Viagem cadastrada com sucesso!")


def listar_destinos():
    if not viagens:
        print("Nenhuma viagem cadastrada.")
        return
    for codigo, info in viagens.items():
        print(f"Código: {codigo} | Destino: {info['planeta']} | Classe: {info['classe_nave']} | Preço: R$ {info['preco']:.2f}")


def verificar_assentos_disponiveis():
    codigo = int(input("Digite o código da viagem: "))
    if codigo not in viagens:
        print("Viagem não encontrada.")
        return
    info = viagens[codigo]
    assentos_disponiveis = info['qtd_max_passageiros'] - len(info['passageiros'])
    # if ternário conforme requisito
    status_assentos = "Lotado" if assentos_disponiveis == 0 else "Disponível"
    print(f"Assentos disponíveis: {assentos_disponiveis} — Status: {status_assentos}")


def mostrar_destinos_unicos():
    destinos = set()
    for info in viagens.values():
        destinos.add(info['planeta'])
    if not destinos:
        print("Nenhum destino cadastrado.")
        return
    print("Destinos únicos:")
    for destino in destinos:
        print(f"  • {destino}")