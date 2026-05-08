import seaborn as sns
import matplotlib.pyplot as plt

# Estilo general
sns.set_style('whitegrid')

# Cargar el dataset tips
tips = sns.load_dataset('tips')

# Crear figura y eje
plt.figure(figsize=(10, 6))

# Gráfico de dispersión bivariante con hue por sexo
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='sex',
    palette='coolwarm',
    alpha=0.6,
    edgecolor='w',
    s=70
)

# Línea de regresión en el mismo gráfico
sns.regplot(
    data=tips,
    x='total_bill',
    y='tip',
    scatter=False,
    color='black',
    line_kws={'linewidth': 2, 'label': 'Línea de regresión'}
)

# Etiquetas y título
plt.title('Relación entre total_bill y tip con regresión por sexo')
plt.xlabel('Cuenta total (total_bill)')
plt.ylabel('Propina (tip)')
plt.legend(title='Sexo')
plt.tight_layout()
plt.show()
