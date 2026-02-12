import pandas as pd


if __name__ == "__main__":
    dados = {
        "nome": ["Ana", "Bruno", None, "Diego"],
        "idade": [19, None, 23, 18],
        "cidade": ["Recife", "Fortaleza", "Salvador", None],
    }
    df = pd.DataFrame(dados)

    resumo = {
        "qtd_na": df.isna().sum(),
        "dropna_linhas": df.dropna(),
        "fillna_zero": df.fillna(0),
        "fillna_media": df.fillna(df.mean(numeric_only=True)),
        "fillna_nao_informado": df.fillna("nao informado"),
    }
    print("Quantidade de NaN por coluna:\n", resumo["qtd_na"], "\n")
    print("Dropna (remove linhas com NaN):\n", resumo["dropna_linhas"], "\n")
    print("Fillna com zero:\n", resumo["fillna_zero"], "\n")
    print("Fillna com media (colunas numericas):\n", resumo["fillna_media"], "\n")
    print("Fillna com 'nao informado':\n", resumo["fillna_nao_informado"], "\n")
