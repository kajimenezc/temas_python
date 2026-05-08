import seaborn as sns
import matplotlib.pyplot as plt

# Estilo general
sns.set_style('darkgrid')

# Cargar el dataset tips
tips = sns.load_dataset('tips')

# Crear histograma de la variable tip con densidad y KDE
sns.histplot(
    data=tips,
    x='tip',
    bins=40,
    stat='density',
    kde=True,
    kde_kws={'color': 'blue'}
)

# Etiquetas y título
plt.title('Distribución de la propina (tip) con KDE')
plt.xlabel('Propina (tip)')
plt.ylabel('Densidad')
plt.tight_layout()
plt.show()
