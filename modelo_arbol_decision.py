"""
Modelo de aprendizaje supervisado: Arbol de decision
Proyecto: Transporte masivo - Prediccion de alta demanda en estaciones
Basado en el capitulo 17 de Palma Mendez (2008): arboles y reglas de decision
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Cargar datos
df = pd.read_csv('datos_transporte.csv')

# 2. Preprocesamiento: convertir variable categorica a numerica (one-hot)
df = pd.get_dummies(df, columns=['tipo_estacion'], drop_first=True)

# 3. Separar variables independientes (X) y dependiente (y)
X = df.drop('alta_demanda', axis=1)
y = df['alta_demanda']

# 4. Division entrenamiento (80%) / prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 5. Entrenamiento del arbol de decision
modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
modelo.fit(X_train, y_train)

# 6. Evaluacion
y_pred = modelo.predict(X_test)
print("Precision del modelo:", round(accuracy_score(y_test, y_pred), 3))
print("\nMatriz de confusion:\n", confusion_matrix(y_test, y_pred))
print("\nReporte de clasificacion:\n", classification_report(y_test, y_pred))

# 7. Reglas de decision extraidas del arbol (reglas SI-ENTONCES)
print("\nREGLAS DE DECISION DEL MODELO:")
print(export_text(modelo, feature_names=list(X.columns)))

# 8. Visualizacion del arbol
plt.figure(figsize=(16, 8))
plot_tree(modelo, feature_names=list(X.columns), class_names=['Baja', 'Alta'],
          filled=True, rounded=True, fontsize=9)
plt.title('Arbol de decision - Prediccion de demanda en estaciones')
plt.tight_layout()
plt.savefig('arbol_decision.png', dpi=150)
plt.show()

# 9. Importancia de las variables
importancias = pd.Series(modelo.feature_importances_, index=X.columns).sort_values()
importancias.plot(kind='barh', title='Importancia de variables')
plt.tight_layout()
plt.savefig('importancia_variables.png', dpi=150)
plt.show()

# 10. Prueba con un caso nuevo (prediccion)
caso_nuevo = pd.DataFrame({'hora_dia': [7], 'dia_semana': [1], 'es_fin_semana': [0],
                           'lluvia': [1], 'frecuencia_buses_min': [15],
                           'tipo_estacion_Intermedia': [0], 'tipo_estacion_Portal': [1]})
prediccion = modelo.predict(caso_nuevo)[0]
print("\nCaso nuevo (hora pico, lluvia, pocos buses):",
      "ALTA DEMANDA" if prediccion == 1 else "BAJA DEMANDA")
