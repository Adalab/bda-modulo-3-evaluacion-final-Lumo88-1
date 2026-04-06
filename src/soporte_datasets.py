#Funciones para la limpieza de datos:

def min_datos (df):
    ''' Función para poner en minúsculas y quitar espacios por guiones bajos en columnas df'''
    
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
    df = df.fillna("False")
    df= df.apply(dato_a_int)
    
    return df

#Funciones para el análisis de los datos

def detectar_outliers_iqr(df, columna):
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    limite_superior = q3 + 1.5 * iqr
    limite_inferior = q1 - 1.5 * iqr
    
    outliers = df[(df[columna] > limite_superior) | (df[columna] < limite_inferior)]
    return limite_superior, len(outliers)
    