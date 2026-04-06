# Análisis Exploratorio de Datos del Programa de Lealtad de Aerolínea

Este proyecto analiza el comportamiento de los clientes dentro del programa de fidelidad de una aerolínea, combinando información de actividad de vuelos y datos demográficos/históricos de membresía.


## Dataset 1: Customer Flight Analysis
Contiene información mensual sobre la actividad de vuelo de cada cliente.

Variables:
- `Loyalty Number`: Identificador único del cliente.
- `Year`, `Month`: Año, mes del vuelo.
- `Flights Booked`: Números totales de vuelos reservados en el mes.
- `Points Accumulated`: Puntos acumulados por el cliente.
- `Points Redeemed`: Puntos usados.
- `Flights with Companions`: Número de vuelos con acompañantes.
- `Total Flights`: Número total de vuelos que el cliente ha realizado.
- `Distance`: La distancia volada total durante el mes.
- `Dollar Cost Points Redeemed`: El valor en dólares de los puntos usados.

## Dataset 2: Customer Loyalty History
Contiene un perfil detallado de los clientes.

Variables:

- `Loyalty Number`: Identificador único del cliente. 
- `Country`,`Province`,`City`,`Postal Code`: Lugar de residencia del cliente.
- `Gender`: Género del cliente.
- `Education`: Nivel educativo alcanzado por el cliente.
- `Salary`: Ingreso anual estimado del cliente.
- `Marital Status`: Estado civil del cliente.
- `Loyalty Card`: Tipo de tarjeta de lealtad que posee el cliente
- `CLV`: Valor total estimado que el cliente aporta a la empresa.
- `Enrollment Type`: Tipo de inscripción del cliente en el programa de lealtad. 
- `Enrollment Year`,`Enrollment Month`: Año, mes de inscripción.
- `Cancellation Year`,`Cancellation Month`: Año, mes en que el cliente canceló su membresía.


# Exploración Inicial de los Datos

En esta fase se realiza una primera inspección de ambos datasets para comprender su estructura, detectar problemas potenciales y orientar las decisiones de limpieza posteriores.

### Dimensiones de los Datos
- **Customer Flight Analysis:** 405.624 filas × 10 columnas  
- **Customer Loyalty History:** 16.737 filas × 16 columnas  

### Vista Previa de los Datos
Se muestran las primeras filas de cada dataset para verificar que la carga se ha realizado correctamente y observar el formato general de las variables.

- `df_flight.head()`
- `df_loyalty.head()`

**Observaciones iniciales:**  
- El dataset de vuelos (`df_flight`) presenta un formato consistente y no se observan valores nulos a simple vista.  

- El dataset de clientes (`df_loyalty`) muestra varias columnas con valores faltantes, especialmente en información relacionada con cancelaciones y salario.

### Tipos de Datos
Se revisan los tipos de datos de cada columna para identificar posibles inconsistencias.

- `df_flights.info()`
- `df_loyalty.info()`

**Hallazgos relevantes:**  
- En `df_flights`, todas las columnas presentan tipos de datos correctos.

- En `df_loyalty`, las columnas `Cancellation Year` y `Cancellation Month` aparecen como float debido a la presencia de nulos, al ser valores enteros, habrá que convertirlos en el proceso de limpieza.

### Valores Nulos
Se analiza la presencia de valores nulos en cada dataset.

- `df_flights.isna().sum()/df_flights.shape[0]*100`
- `df_loyalty.isna().sum()/df_loyalty.shape[0]*100`

**Conclusiones sobre nulos:**  
- Para el `df_flight`, no contiene valores nulos.

- Para el `df_loyalty`, presenta valores nulos en tres columnas:

    - `Salary`con un 25.32%, habrá que analizar y buscar patrones para decidir qué hacer.
    - `Cancellation Year` y `Cancellation Month` con un 87.65%, esto no es alarmante ya que los nulos significan que el cliente sigue estando dado de alta.

### Duplicados
Se comprueba si existen registros duplicados que puedan afectar al análisis.

- `df_flights.duplicated().sum()`
- `df_loyalty.duplicated().sum()`

**Resultado:**  

- Para el `df_flight`, contiene 1864 filas duplicadas, que deberán analizarse y tratarse.
- Para el `df_loyalty`, no contiene valores duplicados.

### Estadísticas Descriptivas Iniciales
Se obtienen estadísticas básicas de las variables numéricas para detectar rangos anómalos, posibles outliers y distribuciones inesperadas.

- `df_flights.describe()`
- `df_loyalty.describe(include=np.number)`

**Interpretación preliminar:**  
- En `df_flights`, variables como `Flights Booked`, `Total Flights, Distance`, `Points Accumulated`, `Points Redeemed` y `Dollar Cost Points Redeemed` presentan desviaciones estándar elevadas, rango de datos amplos entre min y max y la media con la mediana están muy alejadas, por lo que podemos intuir que los datos están dispersos y que los clientes son muy distintos.

- En `df_loyalty`, lo más destacable sería:
    - Columna `Salary`. Existe valor negativo en el minimo, lo cuál no es lógico para un ingreso anual. Puede ser un error en registro o valor atípico. La media y mediana están relativamente cercanas, por lo que la distribución podría acercarse a simétrica. Pendiente del rango, al revisar el salario negativo.

    - CLV: Rango de valores muy altos, dispersión, mediana y media alejadas.
   
   A partir del análisis de las variables categóricas se observan lo siguiente:

- `Country`: Todos los clientes proceden de Canadá, lo que indica que el programa de lealtad está focalizado en este país.
- `Province y City`: Ontario es la provincia con mayor número de clientes y Toronto la ciudad más representada.
- `Gender`: Existe una ligera mayoría de mujeres.
- `Education`: La mayoría de los clientes tienen estudios universitarios.
- `Marital Status`: Predominan los clientes casados.
- `Loyalty Card`: La tarjeta más frecuente es la categoría “Star”.
- `Enrollment Type`: La mayoría de los clientes están inscritos bajo el tipo “Standard”.


### Observaciones generales tras la exploración inicial

- El dataset de vuelos es grande y requiere análisis a los  duplicados.  
- El dataset de clientes presenta tres columnas con valores nulos.  
- Será necesario revisar la coherencia entre ambos datasets antes de la unión.
