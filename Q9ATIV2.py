import pandas as pd

if __name__ == "__main__":
    dados = {
        "nome": ["Ana", "Bruno", "Camila", "Diego"],
        "idade": [19, 21, 23, 18],
        "cidade": ["Recife", "Fortaleza", "Salvador", "Recife"],
    }
    df = pd.DataFrame(dados)

    cond = (df["idade"] >= 20)
    resultado = df.loc[cond, "nome"]
    print(resultado)
