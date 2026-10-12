# Predicción de alta demanda en estaciones de transporte masivo

Proyecto de la actividad **Métodos de aprendizaje supervisado** (Inteligencia Artificial, Corporación Universitaria Iberoamericana). Desarrolla un modelo de **árbol de decisión** que predice si una estación de un sistema de transporte masivo (tipo TransMilenio) tendrá alta demanda de pasajeros, a partir de las condiciones de operación: hora del día, día de la semana, lluvia, tipo de estación y frecuencia de buses.

## Integrantes
- Johan David Cifuentes Linares
- Brayan David Gil Barbosa

**Docente:** Sandra Bautista

## Video explicativo
Video (máx. 10 min) con la explicación del proyecto, el código y los resultados: **PEGAR_LINK_DEL_VIDEO_AQUI**

## Fundamentación teórica
Basado en el capítulo 17 (Aprendizaje de árboles y reglas de decisión) de:
Palma Méndez, J. T. (2008). *Inteligencia artificial: métodos, técnicas y aplicaciones*. Madrid: McGraw-Hill España.

## Estructura del repositorio
```
├── README.md
├── datos_transporte.csv            # Dataset (500 registros)
├── modelo_arbol_decision.py        # Código fuente del modelo
└── docs/
    ├── diccionario_datos.md        # Descripción de las variables
    ├── pruebas.md                  # Documento de pruebas (matriz de confusión y métricas)
    ├── arbol_decision.png          # Visualización del árbol entrenado
    └── importancia_variables.png   # Importancia de cada variable
```

## Descripción del problema
El sistema de transporte masivo necesita anticipar las estaciones y horarios con **alta demanda** para optimizar la asignación de buses y mejorar el servicio. Se plantea como un problema de **clasificación binaria supervisada**: dado un registro de condiciones de operación, predecir si la demanda será alta (1) o baja (0).

## Dataset
`datos_transporte.csv` contiene 500 registros **sintéticos**, generados con reglas realistas de operación, con las siguientes variables:

| Variable | Descripción |
|---|---|
| hora_dia | Hora del día del registro (4-22) |
| dia_semana | 0 = lunes ... 6 = domingo |
| es_fin_semana | 1 si es sábado o domingo |
| lluvia | 1 si hubo lluvia en la jornada |
| tipo_estacion | Portal, Intermedia o Cabecera |
| frecuencia_buses_min | Minutos promedio de espera entre buses |
| **alta_demanda** | **Variable objetivo**: 1 = alta, 0 = baja |

Ver el diccionario completo en [`docs/diccionario_datos.md`](docs/diccionario_datos.md).

## Cómo ejecutar el proyecto
Requisitos: Python 3.x con las librerías `pandas`, `matplotlib` y `scikit-learn`.

```bash
python -m pip install pandas matplotlib scikit-learn
python modelo_arbol_decision.py
```

En Windows también puede usarse `py -m pip install ...` y `py modelo_arbol_decision.py`. El script abre dos ventanas con gráficas (el árbol y la importancia de variables): hay que cerrarlas para que el programa termine.

El script realiza:
1. Carga y preprocesamiento de datos (one-hot encoding de `tipo_estacion`).
2. División entrenamiento/prueba (80 % - 20 %, estratificada, `random_state=42`).
3. Entrenamiento del árbol de decisión (`DecisionTreeClassifier`, `max_depth=4`).
4. Evaluación: precisión, matriz de confusión y reporte de clasificación.
5. Extracción de las reglas SI-ENTONCES del árbol.
6. Visualización del árbol y de la importancia de variables.
7. Predicción con un caso nuevo.

## Resultados obtenidos
Evaluación sobre 100 registros de prueba (48 de baja demanda y 52 de alta demanda):

- **Precisión global (accuracy): 86 %**
- **Matriz de confusión:**

| | Predicho: Baja | Predicho: Alta |
|---|---|---|
| **Real: Baja** | 42 | 6 |
| **Real: Alta** | 8 | 44 |

- Clase alta demanda: precisión 0,88, sensibilidad (recall) 0,85, F1 0,86.
- Clase baja demanda: precisión 0,84, sensibilidad (recall) 0,88, F1 0,86.
- Regla extraída de ejemplo: *SI hora_dia está entre las 17 y las 19 (hora pico de la tarde) -> ALTA DEMANDA*.
- Caso nuevo (7 a. m., martes, con lluvia, buses cada 15 min, estación Portal): predicción **ALTA DEMANDA**.

El análisis completo está en [`docs/pruebas.md`](docs/pruebas.md).

## Distribución del trabajo
- **Datos y código:** dataset, diccionario de datos y modelo en Python.
- **Pruebas y documentación:** documento de pruebas, imágenes del árbol, mapa conceptual y presentación del problema y las conclusiones.

El historial de commits y de Pull Requests de este repositorio muestra el aporte de cada integrante.