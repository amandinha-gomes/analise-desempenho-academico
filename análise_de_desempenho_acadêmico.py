
# Analise Descritiva do Desempenho Acadêmico

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("desempenho_estudantes.txt")
df = pd.read_csv("desempenho_estudantes.txt", sep="\t")
df = pd.read_csv("desempenho_estudantes.txt", sep=";")
df.head()

df = pd.read_csv("desempenho_estudantes.txt")
print(df.head(25))

# Estatísticas descritivas
print(df.describe())

# Dados ausentes
print("\nValores ausentes:\n", df.isnull().sum())

# Distribuição das notas finais
plt.figure(figsize=(8,5))
sns.histplot(df['nota_final'], bins=10, kde=True, color="blue")
plt.title("Distribuição das Notas Finais")
plt.xlabel("Nota Final")
plt.ylabel("Frequência")
plt.savefig("grafico_notas.png")
plt.show()

# Converter a coluna 'evasao' para valores numéricos
df['evasao_numeric'] = df['evasao'].apply(lambda x: 1 if x == 'Sim' else 0)

# Mapa de correlação
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Mapa de Correlação")
plt.savefig("mapa_correlacao.png")
plt.show()

# Boxplot: Nota final x Evasão
plt.figure(figsize=(8,6))
sns.boxplot(x="evasao", y="nota_final", data=df)
plt.title("Notas Finais por Evasão")
plt.savefig("boxplot_evasao.png")
plt.show()

# Comparação entre cursos
plt.figure(figsize=(8,6))
sns.boxplot(x="curso", y="nota_final", data=df)
plt.title("Notas Finais por Curso")
plt.savefig("boxplot_curso.png")
plt.show()