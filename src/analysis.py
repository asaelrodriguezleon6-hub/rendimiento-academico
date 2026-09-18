import pandas as pd

# Cargar el dataset
df = pd.read_csv("data/StudentsPerformance.csv")

print("=== ANÁLISIS DEL RENDIMIENTO ACADÉMICO ===")

# Dimensiones del dataset
print("\n1. DIMENSIONES DEL DATASET")
print("Número de registros:", df.shape[0])
print("Número de columnas:", df.shape[1])

# Variables disponibles
print("\n2. VARIABLES")
for columna in df.columns:
    print("-", columna)

# Tipos de datos
print("\n3. TIPOS DE DATOS")
print(df.dtypes)

# Valores faltantes
print("\n4. VALORES FALTANTES")
print(df.isnull().sum())

# Registros duplicados
print("\n5. REGISTROS DUPLICADOS")
print("Número de duplicados:", df.duplicated().sum())

# Estadísticas descriptivas
print("\n6. ESTADÍSTICAS DESCRIPTIVAS")
print(df.describe())
