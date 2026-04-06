#Funciones para la limpieza de datos:

def min_datos (df):
    ''' Función para poner en minúsculas y quitar espacios por guiones bajos en columnas df
    Devuelve el df.columns'''
    
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ","_")

    return df.columns

def dato_a_int(valor):
    ''' Función que pasa valores float a int, si es  False, None o texto devuelve el mismo valor'''

    try:
        # Convertimos a float y luego a int para quitar el .0
        return int(float(valor))
    except (ValueError, TypeError):
        return valor
    
def nulos_false_int(df):
    '''Función que le recibe una columna y rellena los nulos por "False" y aplica la función dato_a_int
    Devuelve el df modificado'''
    df = df.fillna("False")
    df= df.apply(dato_a_int)
    
    return df

#Funciones para el análisis de los datos

def detectar_outliers_iqr(df, columna):
    '''Función que calcula los quartiles para calcular el IQR y sacar los límites y el número de outliers
    Devuelve el limite superior, limite inferior y la cantidad de outliers'''
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    limite_superior = q3 + 1.5 * iqr
    limite_inferior = q1 - 1.5 * iqr
    
    #hago la máscara y digo que me saque un df con los outliers, luego le hago un len y devuelvo la cantidad de ellos.
    outliers = df[(df[columna] > limite_superior) | (df[columna] < limite_inferior)] 
    return limite_superior, limite_inferior, len(outliers)
    