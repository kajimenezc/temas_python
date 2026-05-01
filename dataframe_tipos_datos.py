import pandas as pd
import numpy as np

# Crear DataFrame con las columnas especificadas
datos = {
    'edad': [25, 30, 35, 28, 32],
    'altura': [1.75, 1.68, 1.82, 1.70, 1.78],
    'nombre': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'activo': [True, False, True, True, False]
}

df = pd.DataFrame(datos)

print("=" * 70)
print("DATAFRAME ORIGINAL")
print("=" * 70)
print(df)
print()

# 1. Verificar y mostrar los tipos de datos iniciales
print("=" * 70)
print("1. TIPOS DE DATOS INICIALES (dtypes)")
print("=" * 70)
print(df.dtypes)
print()

# Calcular memoria antes de las conversiones
print("=" * 70)
print("2. USO DE MEMORIA ANTES DE LAS CONVERSIONES")
print("=" * 70)
memoria_antes = df.memory_usage(deep=True)
print(memoria_antes)
print(f"\nTotal de memoria (antes): {memoria_antes.sum()} bytes")
print()

# 2. Convertir columna 'edad' a float64
df['edad'] = df['edad'].astype('float64')
print("=" * 70)
print("3. CONVERSIÓN: 'edad' -> float64")
print("=" * 70)
print(f"Tipo de 'edad' después de conversión: {df['edad'].dtype}")
print()

# 3. Convertir columna 'altura' a int64
df['altura'] = df['altura'].astype('int64')
print("=" * 70)
print("4. CONVERSIÓN: 'altura' -> int64")
print("=" * 70)
print(f"Tipo de 'altura' después de conversión: {df['altura'].dtype}")
print(f"Nota: Los valores decimales se truncan a enteros: {df['altura'].tolist()}")
print()

# 4. Convertir columna 'nombre' a category
df['nombre'] = df['nombre'].astype('category')
print("=" * 70)
print("5. CONVERSIÓN: 'nombre' -> category")
print("=" * 70)
print(f"Tipo de 'nombre' después de conversión: {df['nombre'].dtype}")
print()

# 5. Mostrar nuevamente los tipos de datos después de las conversiones
print("=" * 70)
print("6. TIPOS DE DATOS DESPUÉS DE LAS CONVERSIONES")
print("=" * 70)
print(df.dtypes)
print()

# Mostrar el DataFrame después de todas las conversiones
print("=" * 70)
print("DATAFRAME DESPUÉS DE LAS CONVERSIONES")
print("=" * 70)
print(df)
print()

# 6. Calcular y mostrar el uso de memoria después de las conversiones
print("=" * 70)
print("7. USO DE MEMORIA DESPUÉS DE LAS CONVERSIONES")
print("=" * 70)
memoria_despues = df.memory_usage(deep=True)
print(memoria_despues)
print(f"\nTotal de memoria (después): {memoria_despues.sum()} bytes")
print()

# Comparación de memoria
print("=" * 70)
print("8. COMPARACIÓN DE USO DE MEMORIA")
print("=" * 70)
print(f"Memoria antes:  {memoria_antes.sum()} bytes")
print(f"Memoria después: {memoria_despues.sum()} bytes")
print(f"Diferencia:     {memoria_despues.sum() - memoria_antes.sum()} bytes")
ahorro_porcentaje = ((memoria_antes.sum() - memoria_despues.sum()) / memoria_antes.sum()) * 100
print(f"Ahorro:         {ahorro_porcentaje:.2f}%")
print()

# Detalles por columna
print("=" * 70)
print("9. DETALLE DE MEMORIA POR COLUMNA")
print("=" * 70)
columnas = df.columns
for col in columnas:
    print(f"{col:15} | Antes: {memoria_antes[col]:6} bytes | Después: {memoria_despues[col]:6} bytes | Cambio: {memoria_despues[col] - memoria_antes[col]:+6} bytes")
