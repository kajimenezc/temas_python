import numpy as np
import matplotlib.pyplot as plt

# Generar cuatro variables para un scatter multivariante
np.random.seed(42)
x = np.random.uniform(0, 10, 200)
y = np.random.uniform(0, 10, 200)
colors = np.random.uniform(0, 100, 200)
sizes = np.random.rand(200) * 200

# Crear gráfico de dispersión multivariante
plt.scatter(x, y, c=colors, s=sizes, cmap='plasma', alpha=0.6)
plt.title('Gráfico de dispersión multivariante')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Valor de color (tercera variable)')
plt.grid(True)
plt.tight_layout()
plt.show()
