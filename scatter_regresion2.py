import numpy as np
import matplotlib.pyplot as plt

# Generar datos x e y relacionados linealmente con ruido
np.random.seed(42)
x = np.random.uniform(0, 50, 100)
ruido = np.random.normal(loc=0, scale=10, size=100)
y = 2.5 * x + ruido

# Ajustar una línea de regresión lineal
pendiente, ordenada = np.polyfit(x, y, 1)
y_regresion = pendiente * x + ordenada

# Crear gráfico de dispersión
plt.scatter(x, y, color='purple', s=50)
plt.plot(x, y_regresion, color='green', label=f'Regresión lineal: y = {pendiente:.2f}x + {ordenada:.2f}')
plt.title('Dispersión de datos con línea de regresión')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
