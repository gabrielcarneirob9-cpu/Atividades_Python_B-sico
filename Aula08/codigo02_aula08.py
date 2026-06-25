import random

def rolar_dado():
    return random.randint(1, 6)

print("=" * 30)
print("SIMULADOR DE DADOS")
print("=" * 30)

while True:
    opcao = input("\nDigite 'rolar' para jogar o dado ou 'sair' para encerrar: ").lower()

    if opcao == "sair":
        print("Programa encerrado. Até a próxima!")
        break

    elif opcao == "rolar":
        resultado = rolar_dado()
        print(f"🎲 Você tirou: {resultado}")

    else:
        print("Opção inválida! Digite 'rolar' ou 'sair'.")
