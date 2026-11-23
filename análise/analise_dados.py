
import pandas as pd

# Carregar os talões reais
df = pd.read_csv(
    "dataset/transactions.csv",
    sep=";",
    decimal=","
)

# Converter colunas numéricas
colunas = [
    "quantidade",
    "preco_unitario",
    "total",
    "desconto"
]

for coluna in colunas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

print("\n--- PRIMEIRAS COMPRAS ---")
print(df.head(10).to_string(index=False))

print("\n--- PRODUTOS POR CATEGORIA ---")
print(df["categoria_spendwise"].value_counts())

print("\n--- DESPESA POR CATEGORIA ---")
print(
    df.groupby("categoria_spendwise")["total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- DESCONTOS ---")
print(df["desconto"].sum(), "€")

print("\n--- TOTAL DOS PRODUTOS REGISTADOS ---")
print(round(df["total"].sum(), 2), "€")

print("\n--- VALORES POR CONFIRMAR ---")
print(df[df["total"].isna()][["talão", "produto"]])
