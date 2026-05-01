import pandas as pd

# Crear DataFrame ventas
df_ventas = pd.DataFrame({
    'id_producto': ['A1', 'A2', 'A3', 'A4', 'A2'],
    'fecha': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'unidades_vendidas': [10, 5, 8, 12, 7]
})

# Crear DataFrame productos
df_productos = pd.DataFrame({
    'id_producto': ['A1', 'A2', 'A3', 'A5'],
    'nombre': ['Laptop', 'Monitor', 'Teclado', 'Mouse'],
    'precio': [1200, 300, 100, 50]
})

print("=" * 70)
print("DATAFRAME VENTAS")
print("=" * 70)
print(df_ventas)
print()

print("=" * 70)
print("DATAFRAME PRODUCTOS")
print("=" * 70)
print(df_productos)
print()

# Merge inner
df_inner = pd.merge(df_ventas, df_productos, on='id_producto', how='inner')
print("=" * 70)
print("MERGE INNER")
print("=" * 70)
print(df_inner)
print()

# Merge left
df_left = pd.merge(df_ventas, df_productos, on='id_producto', how='left')
print("=" * 70)
print("MERGE LEFT")
print("=" * 70)
print(df_left)
print()

# Merge outer
df_outer = pd.merge(df_ventas, df_productos, on='id_producto', how='outer')
print("=" * 70)
print("MERGE OUTER")
print("=" * 70)
print(df_outer)
print()

# Calcular valor_total en el merge inner
df_inner['valor_total'] = df_inner['unidades_vendidas'] * df_inner['precio']
print("=" * 70)
print("MERGE INNER CON VALOR TOTAL")
print("=" * 70)
print(df_inner)
print()