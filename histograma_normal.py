import numpy as np
import matplotlib.pyplot as plt

# Generar datos con distribución normal
np.random.seed(42)
datos_normales = np.random.normal(loc=5, scale=2, size=1500)

# Crear histograma
plt.hist(datos_normales, bins=40, color='green', alpha=0.5, edgecolor='red')
plt.title('Histograma de distribución normal (media=5, desviación estándar=2)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
