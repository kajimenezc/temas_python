import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos ficticios
datos = {
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': [10, 15, 7, 12]
}

df = pd.DataFrame(datos)

# Estilo general
sns.set_theme(style='whitegrid')

# Crear gráfico de barras
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x='Categoría',
    y='Valor',
    hue='Categoría',
    palette='pastel'
)

# Personalizar título
plt.title('Gráfico de barras personalizado', fontsize=16, color='blue', fontweight='bold')

# Personalizar etiquetas
plt.xlabel('Categorías', fontsize=12, color='darkgray')
plt.ylabel('Valores', fontsize=12, color='darkgray')

# Eliminar bordes izquierdo y derecho
sns.despine(left=True, right=True)

plt.tight_layout()
plt.show()
