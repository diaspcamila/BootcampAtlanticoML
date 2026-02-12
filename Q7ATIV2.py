import pandas as pd

if __name__ == "__main__":
    df1 = pd.DataFrame({"nome": ["Ana", "Bruno"], "idade": [19, 21]})
    df2 = pd.DataFrame({"nome": ["Camila"], "cidade": ["Recife"]})

    print("Concat por linhas (axis=0):")
    print(pd.concat([df1, df2], axis=0))

    print("\nConcat por colunas (axis=1):")
    print(pd.concat([df1, df2], axis=1))

    df3 = pd.DataFrame({"cidade": ["São Paulo", "Belo Horizonte"], "população": [12176866, 2521564]})
    df4 = pd.DataFrame({"estado": ["SP", "MG"], "sigla": ["São Paulo", "Minas Gerais"]})

    print("\nConcatenação com preenchimento de NaN:")
    resultado = pd.concat([df3, df4], axis=0, ignore_index=True)
    print(resultado)
