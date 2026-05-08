import pandas as pd
import numpy as np

# Crear DataFrame con datos de ventas mensuales
datos_ventas = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'ventas': [15000, 18000, 22000, 19000, 25000, 28000,
               32000, 29000, 26000, 24000, 21000, 20000],
    'unidades': [120, 145, 180, 155, 200, 230,
                 260, 240, 210, 195, 170, 160]
}

df_ventas = pd.DataFrame(datos_ventas)

print("=" * 70)
print("DATAFRAME DE VENTAS MENSUALES")
print("=" * 70)
print(df_ventas)
print()

# 1. Resumen estadístico completo usando describe()
print("=" * 70)
print("1. RESUMEN ESTADÍSTICO COMPLETO (describe())")
print("=" * 70)
print(df_ventas.describe())
print()

# 2. Media, mediana y desviación estándar de la columna 'ventas'
print("=" * 70)
print("2. ESTADÍSTICAS DE LA COLUMNA 'VENTAS'")
print("=" * 70)
media_ventas = df_ventas['ventas'].mean()
mediana_ventas = df_ventas['ventas'].median()
desviacion_ventas = df_ventas['ventas'].std()

print(f"Media de ventas:     {media_ventas:.2f}")
print(f"Mediana de ventas:   {mediana_ventas:.2f}")
print(f"Desviación estándar: {desviacion_ventas:.2f}")
print()

# 3. Valor máximo y mínimo de la columna 'unidades'
print("=" * 70)
print("3. VALORES EXTREMOS DE LA COLUMNA 'UNIDADES'")
print("=" * 70)
max_unidades = df_ventas['unidades'].max()
min_unidades = df_ventas['unidades'].min()

print(f"Máximo de unidades: {max_unidades}")
print(f"Mínimo de unidades: {min_unidades}")
print()

# 4. Correlación entre 'ventas' y 'unidades'
print("=" * 70)
print("4. CORRELACIÓN ENTRE 'VENTAS' Y 'UNIDADES'")
print("=" * 70)
correlacion = df_ventas['ventas'].corr(df_ventas['unidades'])
print(f"Coeficiente de correlación: {correlacion:.4f}")

if correlacion > 0.7:
    print("Interpretación: Correlación fuerte positiva")
elif correlacion > 0.3:
    print("Interpretación: Correlación moderada positiva")
elif correlacion > -0.3:
    print("Interpretación: Correlación débil")
elif correlacion > -0.7:
    print("Interpretación: Correlación moderada negativa")
else:
    print("Interpretación: Correlación fuerte negativa")
print()