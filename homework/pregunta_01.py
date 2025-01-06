import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """

    # Leer el archivo y limpiar las líneas vacías
    with open("files/input/clusters_report.txt", "r") as f:
        lineas = [linea.strip() for linea in f.readlines() if linea.strip()]

    # Combinar la primera y segunda línea del archivo
    lineas[0] = lineas[0] + " " + lineas[1]
    lineas.pop(1)

    # Definir los nombres de las columnas y convertirlas a minúsculas con guiones bajos
    columnas = ["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"]
    columnas = [columna.lower().replace(" ", "_") for columna in columnas]

    # Preparar los datos para el DataFrame
    datos = []
    for linea in lineas[2:]:
        partes = linea.split()

        # Si la primera parte de la línea es un número, procesar la fila
        if partes[0].isdigit():
            cluster = int(partes[0])
            cantidad_palabras_clave = int(partes[1])
            porcentaje_palabras_clave = float(partes[2].replace(",", "."))
            principales_palabras_clave = " ".join(partes[4:]).rstrip('.')
            
            datos.append({
                "cluster": cluster,
                "cantidad_de_palabras_clave": cantidad_palabras_clave,
                "porcentaje_de_palabras_clave": porcentaje_palabras_clave,
                "principales_palabras_clave": principales_palabras_clave
            })
        else:
            # Si la línea no tiene un número, agregamos palabras clave adicionales a la fila anterior
            datos[-1]["principales_palabras_clave"] += " " + " ".join(partes).rstrip('.')

    # Crear el DataFrame con los datos y las columnas definidas
    df = pd.DataFrame(datos, columns=columnas)

    return df