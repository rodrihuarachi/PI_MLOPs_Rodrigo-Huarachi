import pandas as pd
import requests
from bs4 import BeautifulSoup
import ast


def porcentaje_nulos(data):
    
    """
    Informa el porcentaje de nulos.

    Esta función informa el porcentaje de registros
    nulos por columna en un ``DataFrame``.

    Parameters
    ----------
    data : pandas.DataFrame
        El DataFrame que se va a analizar.

    Returns
    -------
    message
        Por columna muestra el porcentaje de registros vacios.
    """
    
    for columna in data.columns:
        porcentaje_nulos = round(data[columna].isna().mean() * 100, 1)
        print(f'La columna {columna} tiene un {porcentaje_nulos}% de valores nulos.')



def registros_anidados(data):
    
    """
    Informa las columnas con registros anidados.

    Esta función informa que columnas tiene
    registros anidados en un ``DataFrame``.

    Parameters
    ----------
    data : pandas.DataFrame
        El DataFrame que se va a analizar.

    Returns
    -------
    list
        Columnas con registros anidados.
    """

    columnas = [] # Lista para almacenar los nombres de las columnas con valores que comienzan con '{' o '['

    # Iteramos a través de las columnas del DataFrame
    for columna in data.columns:
        if any(data[columna].astype(str).str.startswith('[{')) or any(data[columna].astype(str).str.startswith('{')): # Verificamos si al menos un valor de la columna comienza con '[' o '{'
            columnas.append(columna) # Si cumple con la condicion, agregamos el nombre de la columna en la lista

    return columnas


def filas_duplicadas(data):
    
    """
    Informa cantidad de filas duplicadas.

    Esta función informa la cantidad de filas duplicadas
    que hay en un ``DataFrame``.

    Parameters
    ----------
    data : pandas.DataFrame
        El DataFrame que se va a analizar.

    Returns
    -------
    message
        Cantidad de filas duplicadas si las hay.
    """

    cantidad = data.duplicated().sum()

    if cantidad == 0:
        return f'El DataFrame no tiene filas duplicadas'
    else:
        return f'El Dataframe tiene {cantidad} filas duplicadas'
    

def registros_unicos(data,columna):

    """
    Informa cantidad de registros unicos.

    Esta funcion devuelve la cantidad de registros
    unicos que hay en una columna de un ``DataFrame``.

    Parameters
    ----------
    data : pandas.DataFrame
        El DataFrame que se va a analizar.
    columna : str
        La columna del dataframe donde se van a buscar los valores únicos.

    Returns
    -------
    message
        Cantidad de registros unicos si las hay.
    """

    registros = data[columna].nunique()
    
    if registros == 0:
        return f'La columna {columna} no tiene registros unicos'
    else:
        return f'La columna {columna} tiene {registros} registros unicos'
    

def obtener_release_year(url):

    """
    Extraccion del año del lanzamiento del juego.

    Esta función utiliza el ``Web Scrapping`` para 
    extraer el año del lanzamiento del juego en Steam.

    Parameters
    ----------
    url : str
        Url del juego de Steam.

    Returns
    -------
    int
        Año del lanzamiento del juego.    
    """

    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            game_year_element = soup.find('div', {'class': 'date'})
            if game_year_element:
                game_year = game_year_element.text.strip()
                return game_year
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error en la URL {url}: {str(e)}")
        return None
    


def convert_to_list(string):
    """
    Convierte una cadena de texto en una lista de Python.

    Esta función intenta evaluar la cadena de texto como una lista de Python utilizando la función `ast.literal_eval`.
    Si la cadena es válida como una lista, la función la convierte en una lista. Si la cadena es inválida o no puede
    ser evaluada como una lista, la función devuelve una lista vacía.

    Parameters
    ----------
    string : str
        La cadena de texto que se intentará convertir en una lista.

    Returns
    -------
    list
        Una lista de Python creada a partir de la cadena de texto, o una lista vacía si la conversión falla.
    """

    try:
        # Utiliza ast.literal_eval para evaluar la cadena como una lista de Python
        return ast.literal_eval(string)
    except (SyntaxError, ValueError):
        # En caso de error, devuelve una lista vacía o un valor apropiado
        return []

