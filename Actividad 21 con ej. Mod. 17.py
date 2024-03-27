# Importar un archivo CSV con Pandas

# Se importa la librería pandas
# La documentacion de la libreria se puede ver acá: https://pandas.pydata.org/docs/
import pandas as pd

# Otras librerias necesarias
import numpy as np
import os

# Cambiar el directorio actual con chdir
os.chdir('/users/Usuario/Desktop')

# Se usaa la función read_csv para leer el archivo .csv
# Este archivo es el de las películas de Netflix que hemos venido utilizando y lo ingesta en la variable df
df = pd.read_csv('netflix_titles_2.csv')

# Cambiamos de nombre la columna de DataFrame "duration_num" a "duration"
df['duration_num'] = df['duration']

# Cambiamos el valor de la colunma 'duration_unit'
df['duration_unit'] = ''
