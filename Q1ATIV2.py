def numeros_impares(valores):
    return [v for v in valores if v % 2 != 0]


if __name__ == "__main__":
    n = int(input("Digite a quantidade de numeros: "))
    lista = []
    for _ in range(n):
        x = int(input("Digite um numero: "))
        lista.append(x)

    print(numeros_impares(lista))
