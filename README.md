# Prediccion de alta demanda en estaciones de transporte masivo

Proyecto de la actividad **Metodos de aprendizaje supervisado**: desarrollo de un
modelo de **arbol de decision** para predecir si una estacion de un sistema de
transporte masivo tendra alta demanda de pasajeros, a partir de condiciones de
operacion (hora del dia, dia de la semana, lluvia, tipo de estacion y frecuencia
de buses).

## Integrantes
- [Nombre del integrante 1]
- [Nombre del integrante 2]

## Fundamentacion teorica
Basado en el capitulo 17 (Aprendizaje de arboles y reglas de decision) de:
Palma Mendez, J. T. (2008). *Inteligencia artificial: metodos, tecnicas y
aplicaciones*. Madrid: McGraw-Hill Espana.

## Estructura del repositorio
```
├── datos_transporte.csv        # Dataset (500 registros)
├── modelo_arbol_decision.py    # Codigo fuente del modelo
├── docs/
│   ├── diccionario_datos.md        # Descripcion de las variables
│   ├── arbol_decision.png          # Visualizacion del arbol entrenado
│   └── importancia_variables.png   # Importancia de cada variable
```

## Descripcion del problema
El sistema de transporte masivo necesita anticipar las estaciones y horarios con
**alta demanda** para optimizar la asignacion de buses y mejorar el servicio.
Se plantea como un problema de **clasificacion binaria supervisada**: dado un
registro de condiciones de operacion, predecir si la demanda sera alta (1) o
baja (0).

## Dataset
`datos_transporte.csv` contiene 500 registros con las siguientes variables:

| Variable | Descripcion |
|---|---|
| hora_dia | Hora del dia del registro (4-22) |
| dia_semana | 0 = lunes ... 6 = domingo |
| es_fin_semana | 1 si es sabado o domingo |
| lluvia | 1 si hubo lluvia en la jornada |
| tipo_estacion | Portal, Intermedia o Cabecera |
| frecuencia_buses_min | Minutos promedio de espera entre buses |
| **alta_demanda** | **Variable objetivo**: 1 = alta, 0 = baja |

Ver el diccionario completo en `docs/diccionario_datos.md`.

## Como ejecutar el proyecto
Requisitos: Python 3.x con las librerias `pandas`, `matplotlib` y `scikit-learn`.

```bash
pip install pandas matplotlib scikit-learn
python modelo_arbol_decision.py
```

El script realiza:
1. Carga y preprocesamiento de datos (one-hot encoding).
2. Division entrenamiento/prueba (80% - 20%).
3. Entrenamiento del arbol de decision (`DecisionTreeClassifier`).
4. Evaluacion: precision, matriz de confusion y reporte de clasificacion.
5. Extraccion de las reglas SI-ENTONCES del arbol.
6. Visualizacion del arbol y de la importancia de variables.
7. Prediccion con un caso nuevo.

## Resultados obtenidos
- **Precision del modelo: 86%**
- Matriz de confusion: [[42, 6], [8, 44]] (sobre 100 registros de prueba)
- Reglas extraidas ejemplo: *SI hora_dia esta entre 16:30 y 19:30 (hora pico de
  la tarde) -> ALTA DEMANDA*.
- Caso nuevo (7 a.m., lunes, con lluvia, buses cada 15 min): prediccion
  **ALTA DEMANDA**.

## Video explicativo
[Agregar aqui el link del video - maximo 10 minutos]
