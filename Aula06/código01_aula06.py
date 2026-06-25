print("=" * 40)
print("TABUADA COMPLETA")
print("=" * 40)

numero = int(input("Digite um número: "))

print("\n--- ADIÇÃO ---")
for i in range(1, 11):
    print(f"{numero} + {i} = {numero + i}")

print("\n--- SUBTRAÇÃO ---")
for i in range(1, 11):
    print(f"{numero} - {i} = {numero - i}")

print("\n--- MULTIPLICAÇÃO ---")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print("\n--- DIVISÃO ---")
for i in range(1, 11):
    print(f"{numero} ÷ {i} = {numero / i:.2f}")
