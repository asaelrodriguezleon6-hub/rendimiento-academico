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

# Limpieza y preprocesamiento
print("\n7. LIMPIEZA Y PREPROCESAMIENTO")

# Eliminar duplicados en caso de que existan
df = df.drop_duplicates()

# Crear promedio general de las tres áreas
df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

# Clasificar el rendimiento académico
def clasificar_rendimiento(promedio):
    if promedio < 60:
        return "Bajo"
    elif promedio < 80:
        return "Medio"
    else:
        return "Alto"

df["performance_level"] = df["average_score"].apply(clasificar_rendimiento)

print("\nPromedio general de los estudiantes:")
print(round(df["average_score"].mean(), 2))

print("\nCantidad de estudiantes por nivel de rendimiento:")
print(df["performance_level"].value_counts())

print("\nEjemplo de las nuevas variables:")
print(df[[
    "math score",
    "reading score",
    "writing score",
    "average_score",
    "performance_level"
]].head())
