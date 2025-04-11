
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv('dados_vendas_simulado.csv')

# Exibir as 5 primeiras linhas
print("Visualização inicial dos dados:")
print(df.head())

# Converter coluna de data
df['Data'] = pd.to_datetime(df['Data'])

# Vendas totais por categoria
vendas_por_categoria = df.groupby('Categoria')['Total_Venda'].sum().sort_values(ascending=False)
print("\nVendas totais por categoria:")
print(vendas_por_categoria)

# Gráfico de vendas por categoria
plt.figure(figsize=(8, 5))
sns.barplot(x=vendas_por_categoria.values, y=vendas_por_categoria.index, palette="viridis")
plt.title("Total de Vendas por Categoria")
plt.xlabel("Total de Vendas (R$)")
plt.ylabel("Categoria")
plt.tight_layout()
plt.savefig("grafico_vendas_categoria.png")
plt.show()

# Série temporal de vendas
vendas_diarias = df.groupby('Data')['Total_Venda'].sum()

plt.figure(figsize=(10, 5))
vendas_diarias.plot()
plt.title("Total de Vendas por Dia")
plt.xlabel("Data")
plt.ylabel("Total de Vendas (R$)")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_vendas_tempo.png")
plt.show()
