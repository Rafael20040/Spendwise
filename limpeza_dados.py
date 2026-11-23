
import pandas as pd

# Carregar dados
df = pd.read_csv(
    "dataset/transactions.csv",
    sep=";",
    decimal=","
)

# Converter valores numéricos
colunas = [
    "quantidade",
    "preco_unitario",
    "total",
    "desconto"
]

for coluna in colunas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

# Verificar duplicados
print("Duplicados:", df.duplicated().sum())

# Verificar produtos sem preço unitário
print("\nProdutos sem preço unitário:")
print(
    df[df["preco_unitario"].isna()][
        ["produto", "total"]
    ].to_string(index=False)
)

# Criar coluna com valor efetivamente pago
df["valor_pago"] = df["total"] - df["desconto"]

# Resumo por categoria
resumo = df.groupby(
    "categoria_spendwise"
).agg(
    despesa_bruta=("total", "sum"),
    descontos=("desconto", "sum"),
    despesa_liquida=("valor_pago", "sum"),
    numero_produtos=("produto", "count")
).sort_values(
    "despesa_liquida",
    ascending=False
)

print("\nResumo financeiro:")
print(resumo.round(2))

# Guardar dataset preparado
df.to_csv(
    "dataset/compras_limpo.csv",
    index=False
)

print("\nDataset guardado com sucesso!")
