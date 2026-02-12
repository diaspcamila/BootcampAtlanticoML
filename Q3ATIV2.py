def apenas_uma_lista(lista_a, lista_b):
    return list(set(lista_a) ^ set(lista_b))


if __name__ == "__main__":
    n = int(input("Digite a quantidade de numeros: "))
    a = []
    b = []
    for _ in range(n):
        x = int(input("Digite um numero a: "))
        a.append(x)
        y = int(input("Digite um numero b: "))
        b.append(y)
    print(apenas_uma_lista(a, b))
