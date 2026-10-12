# DICCIONARIO DE DATOS — Proyecto Transporte Masivo
## Dataset: datos_transporte.csv (500 registros)

**Contexto:** Registros simulados de condiciones de operacion en estaciones
de un sistema de transporte masivo, con el objetivo de predecir la alta demanda
de pasajeros mediante un arbol de decision (aprendizaje supervisado).

| Variable | Tipo | Valores | Descripcion |
|---|---|---|---|
| hora_dia | Numerica (entero) | 4 - 22 | Hora del dia en que se tomo el registro |
| dia_semana | Numerica (entero) | 0 - 6 | 0 = lunes ... 6 = domingo |
| es_fin_semana | Numerica (binaria) | 0, 1 | 1 si el dia es sabado o domingo |
| lluvia | Numerica (binaria) | 0, 1 | 1 si hubo lluvia en la jornada |
| tipo_estacion | Categorica | Portal, Intermedia, Cabecera | Ubicacion/rol de la estacion en el sistema |
| frecuencia_buses_min | Numerica (entero) | 3 - 19 | Minutos promedio de espera entre buses |
| alta_demanda | Numerica (binaria) | 0, 1 | **Variable objetivo:** 1 = alta demanda, 0 = baja demanda |

## Notas
- Variable objetivo (etiqueta): alta_demanda → problema de CLASIFICACION binaria.
- Variables predictoras: las 6 restantes (mixtas: numericas y categorica).
- La variable categorica tipo_estacion se convierte a formato numerico
  (one-hot encoding) dentro del codigo antes de entrenar el modelo.
- Los datos son sinteticos, generados bajo reglas realistas de operacion
  (horas pico, lluvia, fin de semana y baja frecuencia aumentan la demanda).

## Referencia teorica
Palma Mendez, J. T. (2008). Inteligencia artificial: metodos, tecnicas y
aplicaciones. Capitulo 17: Aprendizaje de arboles y reglas de decision.
Madrid: McGraw-Hill Espana.
