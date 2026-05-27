def detectar_outliers_iqr(df, columna):
    """
    Detecta outliers utilizando el metodo IQR.

    Parametros
    ----------
    df : pandas.DataFrame
        DataFrame que contiene la variable.

    columna : str
        Nombre de la columna numerica a analizar.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con los registros considerados outliers.
    """

    q1 = df[columna].quantile(0.25)

    q3 = df[columna].quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr

    limite_superior = q3 + 1.5 * iqr

    outliers = df[
        (df[columna] < limite_inferior)
        |
        (df[columna] > limite_superior)
    ]

    return outliers
     
