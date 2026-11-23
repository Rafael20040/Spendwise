import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("dataset/transactions.csv", sep=";",
    decimal=",")


# 2. Converter colunas numéricas
colunas = ["quantidade", "preco_unitario", "total", "desconto"]
for coluna in colunas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

# 3. Informação geral
print("\n--- DIMENSÕES DO DATASET ---")
print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])

print("\n--- TIPOS DE DADOS ---")
print(df.dtypes)

# 4. Valores em falta
print("\n--- VALORES EM FALTA ---")
print(df.isnull().sum())

# 5. Despesa por categoria
despesa = (
    df.groupby("categoria_spendwise")["total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- DESPESA POR CATEGORIA ---")
print(despesa)

# 6. Produtos mais caros
print("\n--- PRODUTOS MAIS CAROS ---")
print(
    df.nlargest(5, "total")[["produto", "total"]]
)

# 7. Gráfico de despesas
plt.figure(figsize=(10, 6))

sns.barplot(
    x=despesa.values,
    y=despesa.index
)

plt.title("Despesa por categoria")
plt.xlabel("Despesa (€)")
plt.ylabel("Categoria")
plt.tight_layout()

plt.savefig("dataset/despesa_categorias.png")
plt.show()
