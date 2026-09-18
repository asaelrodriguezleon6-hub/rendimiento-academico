# Análisis del rendimiento académico

Proyecto de análisis y preprocesamiento de datos realizado con Python utilizando el dataset **Students Performance in Exams** de Kaggle.

## Objetivo

Analizar el rendimiento académico de los estudiantes a partir de sus calificaciones en matemáticas, lectura y escritura, además de explorar algunas variables que pueden estar relacionadas con sus resultados.

## Dataset

Se utilizó el dataset **Students Performance in Exams**, el cual contiene 1000 registros y 8 variables.

Las principales variables utilizadas son:

- Género.
- Grupo étnico.
- Nivel educativo de los padres.
- Tipo de almuerzo.
- Curso de preparación para el examen.
- Calificación de matemáticas.
- Calificación de lectura.
- Calificación de escritura.

El archivo utilizado se encuentra en:

`data/StudentsPerformance.csv`

## Estructura del proyecto

```text
rendimiento-academico/
├── data/
│   └── StudentsPerformance.csv
├── outputs/
│   ├── curso_preparacion.png
│   ├── distribucion_rendimiento.png
│   └── promedio_areas.png
├── src/
│   └── analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```
## Entorno virtual

Para crear el entorno virtual en Linux:

```bash
python3 -m venv .venv
```

Para activarlo:

```bash
source .venv/bin/activate
```

Para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la carpeta principal del proyecto ejecutar:

```bash
python3 src/analysis.py
```

El programa realiza la exploración, limpieza, preprocesamiento y análisis de los datos. También genera las gráficas dentro de la carpeta `outputs/`.

## Preprocesamiento

Se verificaron los valores faltantes y los registros duplicados. El dataset no presentó valores faltantes ni registros duplicados.

Se creó la variable `average_score`, que representa el promedio de las calificaciones de matemáticas, lectura y escritura.

También se creó la variable `performance_level` con los siguientes criterios:

- **Bajo:** promedio menor a 60.
- **Medio:** promedio desde 60 y menor a 80.
- **Alto:** promedio igual o mayor a 80.

## Resultados

El promedio general de los estudiantes fue de **67.77**.

El área con mayor promedio fue lectura con **69.17**, seguida de escritura con **68.05** y matemáticas con **66.09**.

Los estudiantes que completaron el curso de preparación obtuvieron un promedio de **72.67**, mientras que quienes no lo completaron obtuvieron **65.04**.

La distribución de los niveles de rendimiento fue:

- **Medio:** 51.7 %
- **Bajo:** 28.5 %
- **Alto:** 19.8 %

También se observó que, dentro de este dataset, los grupos con mayores niveles de educación de los padres presentan promedios académicos más altos.
## Conclusiones

El análisis permitió conocer el comportamiento general del rendimiento académico de los estudiantes en matemáticas, lectura y escritura.

Lectura presentó el promedio más alto de las tres áreas analizadas. También se observó que los estudiantes que completaron el curso de preparación tuvieron un promedio mayor que quienes no lo completaron.

La mayoría de los estudiantes se clasificó en un nivel de rendimiento Medio. Además, en este dataset se observa una asociación entre el nivel educativo de los padres y el promedio académico.

Los resultados obtenidos describen las relaciones presentes en los datos analizados, pero no permiten afirmar que estas variables sean directamente la causa del rendimiento académico.

