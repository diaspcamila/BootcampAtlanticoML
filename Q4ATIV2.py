def segundo_maior(valores):
    if valores is None:
        raise ValueError("A lista nao pode ser None.")

    maior = None
    segundo = None

    for v in valores:
        if maior is None or v > maior:
            segundo = maior
            maior = v
        elif v != maior and (segundo is None or v > segundo):
            segundo = v

    if segundo is None:
        raise ValueError("A lista precisa ter pelo menos dois valores distintos.")

    return segundo


if __name__ == "__main__":
    n = int(input("Digite a quantidade de numeros: "))
    lista = []
    for _ in range(n):
        x = int(input("Digite um numero: "))
        lista.append(x)
    print(segundo_maior(lista))
