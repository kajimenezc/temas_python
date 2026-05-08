import pandas as pd
import numpy as np

# Configurar semilla para reproducibilidad
np.random.seed(42)

# Crear datos de ventas
datos_ventas = {
    'categoría': np.random.choice(['Electrónica', 'Ropa', 'Hogar'], size=30),
    'región': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], size=30),
    'ventas': np.random.randint(100, 1001, size=30),
    'unidades': np.random.randint(1, 21, size=30)
}

df_ventas = pd.DataFrame(datos_ventas)

print("=" * 70)
print("DATAFRAME ORIGINAL CON DATOS DE VENTAS")
print("=" * 70)
print(df_ventas)
print()
print(f"Total de registros: {len(df_ventas)}")
print()

# Mostrar estadísticas básicas
print("=" * 70)
print("INFORMACIÓN DEL DATAFRAME")
print("=" * 70)
print(df_ventas.info())
print()

print("=" * 70)
print("RESUMEN ESTADÍSTICO")
print("=" * 70)
print(df_ventas.describe())
print()

# Crear tabla pivotante sin márgenes
print("=" * 70)
print("TABLA PIVOTANTE: VENTAS POR CATEGORÍA Y REGIÓN (Sin márgenes)")
print("=" * 70)
pivot_sin_margenes = pd.pivot_table(df_ventas, 
                                    values='ventas', 
                                    index='categoría', 
                                    columns='región', 
                                    aggfunc='sum')
print(pivot_sin_margenes)
print()

# Crear tabla pivotante con márgenes
print("=" * 70)
print("TABLA PIVOTANTE: VENTAS POR CATEGORÍA Y REGIÓN (Con márgenes)")
print("=" * 70)
pivot_con_margenes = pd.pivot_table(df_ventas, 
                                    values='ventas', 
                                    index='categoría', 
                                    columns='región', 
                                    aggfunc='sum',
                                    margins=True,
                                    margins_name='Total')
print(pivot_con_margenes)
print()

# Reemplazar NaN con ceros
print("=" * 70)
print("TABLA PIVOTANTE: VENTAS (Con márgenes y NaN reemplazados por 0)")
print("=" * 70)
pivot_limpio = pd.pivot_table(df_ventas, 
                              values='ventas', 
                              index='categoría', 
                              columns='región', 
                              aggfunc='sum',
                              margins=True,
                              margins_name='Total')
pivot_limpio = pivot_limpio.fillna(0)
print(pivot_limpio)
print()

# Crear tabla pivotante para unidades
print("=" * 70)
print("TABLA PIVOTANTE: UNIDADES POR CATEGORÍA Y REGIÓN")
print("=" * 70)
pivot_unidades = pd.pivot_table(df_ventas, 
                                values='unidades', 
                                index='categoría', 
                                columns='región', 
                                aggfunc='sum',
                                margins=True,
                                margins_name='Total')
pivot_unidades = pivot_unidades.fillna(0)
print(pivot_unidades)
print()

# Análisis adicional: promedio de ventas por categoría y región
print("=" * 70)
print("TABLA PIVOTANTE: PROMEDIO DE VENTAS POR CATEGORÍA Y REGIÓN")
print("=" * 70)
pivot_promedio = pd.pivot_table(df_ventas, 
                                values='ventas', 
                                index='categoría', 
                                columns='región', 
                                aggfunc='mean',
                                margins=True,
                                margins_name='Promedio Total')
pivot_promedio = pivot_promedio.fillna(0)
print(pivot_promedio.round(2))
print()

# Resumen por categoría
print("=" * 70)
print("RESUMEN: VENTAS TOTALES POR CATEGORÍA")
print("=" * 70)
ventas_por_categoria = df_ventas.groupby('categoría')['ventas'].agg(['sum', 'mean', 'count'])
ventas_por_categoria.columns = ['Total Ventas', 'Promedio Ventas', 'Cantidad Transacciones']
print(ventas_por_categoria)
print()

# Resumen por región
print("=" * 70)
print("RESUMEN: VENTAS TOTALES POR REGIÓN")
print("=" * 70)
ventas_por_region = df_ventas.groupby('región')['ventas'].agg(['sum', 'mean', 'count'])
ventas_por_region.columns = ['Total Ventas', 'Promedio Ventas', 'Cantidad Transacciones']
print(ventas_por_region)
print()