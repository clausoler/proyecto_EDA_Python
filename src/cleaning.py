def limpiar_columnas_numericas(df, columnas):
    """
    Limpia columnas numéricas que contienen comas decimales y las convierte
    al tipo numérico float.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a limpiar.

    columnas : list
        Lista de columnas que deben convertirse a formato numérico.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas convertidas a tipo numérico.
    """

    df = df.copy()

    for columna in columnas:

        # Reemplazar comas por puntos
        df[columna] = (
            df[columna]
            .astype(str)
            .str.replace(",", ".", regex=False)
        )

        # Convertir a numérico
        df[columna] = pd.to_numeric(
            df[columna],
            errors="coerce"
        )

    return df
 
  
def convertir_binarias(df, columnas):
    """
    Convierte variables binarias numericas
    en categorias de texto.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas binarias.

    columnas : list
        Lista de columnas binarias a convertir.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las variables binarias convertidas.
    """

    df = df.copy()

    mapa = {
        1.0: "Yes",
        0.0: "No"
    }

    for columna in columnas:

        df[columna] = df[columna].map(mapa)

    return df
 

def limpiar_fechas_espanol(df, columna):
    """
    Limpia una columna de fechas que contiene meses en español
    y la convierte al tipo datetime.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene la columna de fechas.

    columna : str
        Nombre de la columna que contiene las fechas.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con la columna convertida a datetime.
    """

    df = df.copy()

    # Convertir a string
    df[columna] = df[columna].astype(str)

    # Reemplazar meses en español por inglés
    for mes_es, mes_en in meses_es_en.items():

        df[columna] = df[columna].str.replace(
            mes_es,
            mes_en,
            regex=False
        )

    # Convertir a datetime
    df[columna] = pd.to_datetime(
        df[columna],
        errors="coerce"
    )

    return df
 
  
def imputar_nulos_mediana(df, columnas):
    """
    Imputa valores nulos en columnas numericas usando la mediana.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a imputar.

    columnas : list
        Lista de columnas numericas en las que se sustituiran los nulos.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con los valores nulos imputados por la mediana.
    """

    df = df.copy()

    for columna in columnas:

        mediana = df[columna].median()

        df[columna] = df[columna].fillna(mediana)

    return df
 
def imputar_nulos_unknown(df, columnas):
    """
    Imputa valores nulos en columnas categoricas usando la etiqueta "unknown".

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a imputar.

    columnas : list
        Lista de columnas categoricas en las que se sustituiran los nulos.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con los valores nulos imputados como "unknown".
    """

    df = df.copy()

    for columna in columnas:

        df[columna] = df[columna].fillna("unknown")

    return df
 
def imputar_nulos_moda(df, columnas):
    """
    Imputa valores nulos usando la moda de cada columna.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las columnas a imputar.

    columnas : list
        Lista de columnas en las que se sustituiran los valores nulos.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con los valores nulos imputados por la moda.
    """

    df = df.copy()

    for columna in columnas:

        moda = df[columna].mode()[0]

        df[columna] = df[columna].fillna(moda)

    return df