def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(n ** 0.5)
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True


def numeros_primos(valores):
    return [v for v in valores if eh_primo(v)]


if __name__ == "__main__":
    n = int(input("Digite a quantidade de numeros: "))
    lista = []
    for _ in range(n):
        x = int(input("Digite um numero: "))
        lista.append(x)

    print(numeros_primos(lista))
