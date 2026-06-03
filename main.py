# ============================================================
# main.py — Menu principal do Sistema de Viagens Espaciais
# ============================================================

from viagens import (
    cadastrar_viagens,
    listar_destinos,
    verificar_assentos_disponiveis,
    mostrar_destinos_unicos
)
from passageiros import (
    cadastrar_passageiro,
    adicionar_passageiro_viagem,
    listar_passageiros_por_viagem,
    calcular_custo_total,
    listar_viagens_por_preco
)


def exibir_menu():
    print("\n" + "=" * 40)
    print("  🚀 SISTEMA DE VIAGENS ESPACIAIS")
    print("=" * 40)
    print("  1 - Cadastrar viagem")
    print("  2 - Listar destinos")
    print("  3 - Verificar assentos disponíveis")
    print("  4 - Mostrar destinos únicos")
    print("  5 - Cadastrar passageiro")
    print("  6 - Adicionar passageiro à viagem")
    print("  7 - Listar passageiros por viagem")
    print("  8 - Calcular custo total da viagem")
    print("  9 - Listar viagens por preço")
    print("  0 - Sair")
    print("=" * 40)


while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_viagens()
    elif opcao == 2:
        listar_destinos()
    elif opcao == 3:
        verificar_assentos_disponiveis()
    elif opcao == 4:
        mostrar_destinos_unicos()
    elif opcao == 5:
        cadastrar_passageiro()
    elif opcao == 6:
        adicionar_passageiro_viagem()
    elif opcao == 7:
        listar_passageiros_por_viagem()
    elif opcao == 8:
        calcular_custo_total()
    elif opcao == 9:
        listar_viagens_por_preco()
    elif opcao == 0:
        print("Encerrando o sistema. Até logo! 🚀")
        break
    else:
        print("Opção inválida. Tente novamente.")