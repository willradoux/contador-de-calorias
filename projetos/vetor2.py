def main():

    while True:
        try:
            N = int(input("Digite um número inteiro positivo até 10: "))
            if 1 <= N <= 10:
                break 
            else:
                print("Número fora do limite, tente novamente.")
        except ValueError:
            print("Digite um número inteiro válido.")

    vetor = []

    print(f"Digite {N} números:")
    for i in range(N):
        while True:
            try:
                numero = float(input(f"Número {i+1}: "))
                vetor.append(numero)
                break
            except ValueError:
                print("Digite um número válido.")

    print("Elementos do vetor:")
    for numero in vetor:
        print(numero)

if __name__ == "__main__":
    main()
