import pandas as pd

# Crear DataFrame de productos
datos_productos = {
    'producto': [
        'Laptop', 'Smartphone', 'Tablet', 'Auriculares',
        'Camisa', 'Pantalón', 'Zapatos', 'Sombrero',
        'Silla', 'Mesa', 'Lámpara', 'Cortinas'
    ],
    'categoria': [
        'Electrónica', 'Electrónica', 'Electrónica', 'Electrónica',
        'Ropa', 'Ropa', 'Ropa', 'Ropa',
        'Hogar', 'Hogar', 'Hogar', 'Hogar'
    ],
    'precio': [
        1200.0, 800.0, 400.0, 150.0,
        25.0, 60.0, 80.0, 15.0,
        100.0, 200.0, 45.0, 30.0
    ],
    'stock': [
        15, 25, 10, 50,
        30, 20, 12, 40,
        8, 5, 18, 22
    ]
}

df_productos = pd.DataFrame(datos_productos)

print("=" * 70)
print("DATAFRAME COMPLETO DE PRODUCTOS")
print("=" * 70)
print(df_productos)
print()

# 1. Filtrar productos de categoría 'Electrónica'
filtro_electronica = df_productos[df_productos['categoria'] == 'Electrónica']
print("=" * 70)
print("1. PRODUCTOS DE CATEGORÍA 'ELECTRÓNICA'")
print("=" * 70)
print(filtro_electronica)
print()

# 2. Productos con precio > 50 y stock < 20
filtro_precio_stock = df_productos[(df_productos['precio'] > 50) & (df_productos['stock'] < 20)]
print("=" * 70)
print("2. PRODUCTOS CON PRECIO > 50 Y STOCK < 20")
print("=" * 70)
print(filtro_precio_stock)
print()

# 3. Productos que contengan 'a' en el nombre
filtro_letra_a = df_productos[df_productos['producto'].str.contains('a', case=False)]
print("=" * 70)
print("3. PRODUCTOS QUE CONTIENEN 'A' EN EL NOMBRE")
print("=" * 70)
print(filtro_letra_a)
print()

# 4. Usar query() para productos de categoría 'Hogar' con precio < 30
filtro_query = df_productos.query("categoria == 'Hogar' and precio < 30")
print("=" * 70)
print("4. PRODUCTOS DE 'HOGAR' CON PRECIO < 30 (USANDO QUERY)")
print("=" * 70)
print(filtro_query)
print()