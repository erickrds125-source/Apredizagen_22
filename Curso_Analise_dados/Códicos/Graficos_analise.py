import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv(r'C:\Users\deric\Downloads\Curso_Analise_dados\Data\Dados_brutos\ecommerce_estatistica.csv')
print(df.head())  

# Ajuste no estilo do seaborn
sns.set_theme(style="whitegrid")



# Grafico de histograma
plt.figure(figsize=(10, 5))
sns.histplot(df['N_Avaliações_MinMax'], bins=30, color='#2b5c8f', kde=True, edgecolor='black')   
#plt.hist(df['N_Avaliações_MinMax'], bins=30, color='2b5c8f', alpha=0.8)
plt.title('Distribuição de avaliações (MinMax)', fontsize=14, fontweight='bold')
plt.xlabel('N_Avaliações_MinMax', fontsize=11)
#plt.xticks(ticks=range(0, int(df['N_Avaliações_MinMax'].max()) + 2000, 2000))
plt.ylabel('Frequência', fontsize=11)
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de dispersão e pré visualização de correlação
print('Pré visualização e teste de correlação:\n', df[['N_Avaliações_MinMax', 'Nota_MinMax']].corr())

plt.hexbin(df['N_Avaliações_MinMax'], df['Nota_MinMax'], gridsize=30, cmap='Blues', edgecolors='grey')
plt.colorbar(label='Contagem de pontos')
plt.title('Gráfico de Dispersão Hexbin: Avaliações vs Nota (MinMax)', fontsize=14, fontweight='bold')
plt.xlabel('N_Avaliações_MinMax', fontsize=11)
plt.ylabel('Nota_MinMax', fontsize=11)
plt.tight_layout()
plt.show()



# Mapa de calor
corr = df[['Desconto_MinMax', 'Preço_MinMax']].corr()
plt.subplot( 2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Mapa de Calor: Correlação entre Desconto e Preço (MinMax)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()



# Grafico de barras
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Qtd_Vendidos", y="Preço", estimator="mean", errorbar=None)

plt.title("Preço Médio por Quantidade Vendida")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Preço Médio (R$)")
plt.xticks(rotation=45)
plt.show()



# Grafico de pizza
plt.figure(figsize=(10, 6))
plt.pie(df['Qtd_Vendidos'].value_counts(), labels=df['Qtd_Vendidos'].value_counts().index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribuição de Quantidade Vendida', fontsize=14, fontweight='bold')
plt.axis('equal')  
plt.show()   



# Grafico de densidade
# Plotar a curva de densidade
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x="Nota_MinMax", fill=True, color="teal", alpha=0.5)

plt.title("Distribuição de Densidade - Nota_MinMax")
plt.xlabel("Nota MinMax")
plt.ylabel("Densidade")
plt.show()



# Grafico de regressão
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="Preço",
    y="Desconto_MinMax",
    color="darkred",
    scatter_kws={"alpha": 0.5},  
    line_kws={"color": "black", "linewidth": 2},  
)

plt.title("Regressão Linear: Preço vs. Desconto_MinMax")
plt.xlabel("Preço (R$)")
plt.ylabel("Desconto MinMax")
plt.show()
