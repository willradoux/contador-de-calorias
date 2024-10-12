N = int(input("Digite um número inteiro até 10:"))
vetor = []

print(f"digite {N} números")

for i in range(N):
    numero = float(input(f"número {i+1}: "))
    vetor.append(numero)

print("elemento do vetor")
for numero in vetor:
    print(numero)