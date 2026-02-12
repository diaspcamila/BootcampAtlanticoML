import pandas as pd

def ler_csv_e_exibir_primeiras_linhas(caminho_csv, n):
    df = pd.read_csv(caminho_csv)
    return df.head(n)

if __name__ == "__main__":
    caminho = "dados_exemplo.csv"
    print(ler_csv_e_exibir_primeiras_linhas(caminho, n=3))
