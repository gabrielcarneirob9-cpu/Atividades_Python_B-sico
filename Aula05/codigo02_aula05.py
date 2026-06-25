print("=" * 40)
print("VERIFICADOR DE PREÇOS INTELIGENTE")
print("=" * 40)

produto = input("Digite o nome do produto: ")

quantidade_lojas = int(input("Quantas lojas deseja comparar? "))

menor_preco = float('inf')
melhor_loja = ""

for i in range(1, quantidade_lojas + 1):
    print(f"\nLoja {i}")
    nome_loja = input("Nome da loja: ")
    preco = float(input("Preço do produto: R$ "))

    if preco < menor_preco:
        menor_preco = preco
        melhor_loja = nome_loja

print("\n" + "=" * 40)
print("RESULTADO DA PESQUISA")
print("=" * 40)
print(f"Produto: {produto}")
print(f"Melhor preço: R$ {menor_preco:.2f}")
print(f"Loja recomendada: {melhor_loja}")
print("=" * 40)
