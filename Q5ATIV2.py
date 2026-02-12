def ordenar_por_nome(l):
    return sorted(l, key=lambda p: p[0], reverse=False)


if __name__ == "__main__":
    lista = []
    n = int(input("Digite a quantidade de pessoas: "))
    for _ in range(n):
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        lista.append((nome, idade))
    print(ordenar_por_nome(lista))
