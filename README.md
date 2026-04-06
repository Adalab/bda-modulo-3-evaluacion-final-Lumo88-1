# ✈️ Análisis Exploratorio del Programa de Lealtad de Aerolínea

## 📋 Descripción del Proyecto
Este proyecto consiste en un **Análisis Exploratorio de Datos (EDA)** y una fase de **Visualización de Datos** aplicados al programa de lealtad de una aerolínea. El objetivo es identificar patrones de comportamiento en los pasajeros, entender la estacionalidad de los vuelos y analizar la relación entre el nivel socioeconómico de los clientes y su valor de vida (CLV).

## 🛠️ Tecnologías Utilizadas
* **Python 3.10+**
* **Pandas**: Limpieza, manipulación y segmentación de datos.
* **Seaborn & Matplotlib**: Generación de visualizaciones estadísticas avanzadas.
* **NumPy**: Manejo de valores nulos y operaciones vectorizadas.
* **Jupyter Notebook**: Documentación y ejecución del flujo de trabajo.

## 🗂️ Estructura del Dataset
El análisis integra datos de dos fuentes principales:
1. **Actividad de Vuelos**: Reservas por mes/año, distancia recorrida y puntos acumulados.
2. **Perfiles de Clientes**: Ubicación geográfica, salario, nivel educativo, estado civil y tipo de tarjeta de fidelidad.

---

## 🔍 Fases del Análisis

### 1. Limpieza y Preparación (Data Cleaning)
* Unión de dataframes y manejo de datos faltantes en variables críticas como `salary`.
* Creación de segmentos de valor mediante técnicas de filtrado avanzado 
* Identificación y tratamiento de *outliers* utilizando el rango intercuartílico (IQR).

### 2. Visualización de Datos (Key Insights)
Se han abordado las siguientes preguntas de negocio:
* **Estacionalidad**: Identificación de picos de demanda en verano (Julio) y finales de año.
* **Correlación Distancia-Puntos**: Análisis de las distintas pendientes de acumulación según el nivel de fidelidad.
* **Distribución Geográfica**: Ontario como hub principal de clientes.
* **Análisis Socioeconómico**: Impacto del nivel educativo (especialmente Doctores y Másters) en el nivel salarial y el CLV.

---

## 📈 Conclusiones Principales
* **Crecimiento**: Se observa un incremento consistente en el volumen de reservas entre 2017 y 2018.
* **Segmentación**: El 45.5% de los clientes pertenecen al nivel "Star", indicando una base de fidelización masiva.
* **Perfil VIP**: Los clientes con Doctorado presentan salarios significativamente superiores (~180k), representando un nicho de alto valor para servicios premium.
* **Demografía**: Existe un equilibrio de género casi perfecto en todos los estados civiles, predominando el segmento de personas casadas.

---