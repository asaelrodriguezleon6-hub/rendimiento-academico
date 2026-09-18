import pandas as pd
import matplotlib.pyplot as plt
import os
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

# Crear carpeta de resultados si no existe
os.makedirs("outputs", exist_ok=True)

print("\n8. ANÁLISIS DE LOS DATOS")

# ANÁLISIS 1: promedio por área
promedios_areas = df[
    ["math score", "reading score", "writing score"]
].mean()

print("\nAnálisis 1 - Promedio por área:")
print(promedios_areas.round(2))
print("Área con mayor promedio:", promedios_areas.idxmax())

# Visualización 1
promedios_areas.plot(
    kind="bar",
    title="Promedio de calificaciones por área"
)
plt.ylabel("Calificación promedio")
plt.xlabel("Área")
plt.tight_layout()
plt.savefig("outputs/promedio_areas.png")
plt.close()


# ANÁLISIS 2: curso de preparación
promedio_preparacion = df.groupby(
    "test preparation course"
)["average_score"].mean()

print("\nAnálisis 2 - Promedio según curso de preparación:")
print(promedio_preparacion.round(2))

# Visualización 2
promedio_preparacion.plot(
    kind="bar",
    title="Rendimiento según curso de preparación"
)
plt.ylabel("Promedio general")
plt.xlabel("Curso de preparación")
plt.tight_layout()
plt.savefig("outputs/curso_preparacion.png")
plt.close()


# ANÁLISIS 3: educación de los padres
promedio_padres = df.groupby(
    "parental level of education"
)["average_score"].mean().sort_values(ascending=False)

print("\nAnálisis 3 - Promedio según educación de los padres:")
print(promedio_padres.round(2))


# ANÁLISIS 4: distribución del rendimiento
distribucion = df["performance_level"].value_counts()
porcentajes = df["performance_level"].value_counts(normalize=True) * 100

print("\nAnálisis 4 - Distribución del rendimiento:")
print(distribucion)

print("\nPorcentaje por nivel:")
print(porcentajes.round(2))

# Visualización 3
distribucion.plot(
    kind="bar",
    title="Distribución de niveles de rendimiento"
)
plt.ylabel("Número de estudiantes")
plt.xlabel("Nivel de rendimiento")
plt.tight_layout()
plt.savefig("outputs/distribucion_rendimiento.png")
plt.close()

print("\nVisualizaciones guardadas en la carpeta outputs/")
