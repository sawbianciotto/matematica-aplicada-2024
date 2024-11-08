from dataset import *
from Lexicon_de_sentimientos import *
from fuzzificacion import *
from Base_de_reglas import *
from defuzzificacion import *
from Benchmarks import *

#----------------------------dataset----------------------------------
archivo_entrada_csv = 'Datos/test_data.csv'
archivo_salida_procesado_csv = 'Datos/testdataset.csv'  # Solo palabras procesadas

# Procesar el dataset y guardarlo en dos nuevos archivos CSV
procesar_y_guardar_dataset(archivo_entrada_csv, archivo_salida_procesado_csv)


#---------------------Lexicon_de_sentimientos-------------------------
archivo_entrada_csv = 'Datos/testdataset.csv'  # Cambia esto al archivo procesado que generaste antes
archivo_salida_csv = 'Datos/testdataset.csv'

# Analizar el sentimiento del dataset y guardarlo en un nuevo archivo CSV
analizar_sentimientos(archivo_entrada_csv, archivo_salida_csv)


#----------------------------------Fuzzificacion----------------------------------
archivo_entrada_csv = 'Datos/testdataset.csv'

try:
    datos = pd.read_csv(archivo_entrada_csv)
except FileNotFoundError:
    print(f"Error: El archivo '{archivo_entrada_csv}' no se encontró.")
    exit(1)

# Fuzzificar los datos y obtener las funciones de membresía
datos_fuzzificados, d_pos, e_pos, f_pos, d_neg, e_neg, f_neg = fuzzificacion(datos)

# Guardar el DataFrame fuzzificado en un archivo CSV
archivo_salida_csv = 'Datos/testdataset.csv'
datos_fuzzificados.to_csv(archivo_salida_csv, index=False)
print(f"El dataset fuzzificado se ha guardado como '{archivo_salida_csv}'.")

# Visualizar las funciones de membresía y guardar el gráfico
archivo_grafico = 'funciones_membresia.png'
graficar_funciones_membresia(d_pos, e_pos, f_pos, d_neg, e_neg, f_neg, archivo_grafico)
print(f"Gráfico de funciones de membresía guardado como '{archivo_grafico}'.")


#-------------------------------------Base de reglas-------------------------------
# Cargar el dataset fuzzificado
archivo_entrada_csv = 'Datos/testdataset.csv'
datos_fuzzificados = pd.read_csv(archivo_entrada_csv)

# Calcular el sentimiento final y el tiempo de ejecución para cada fila del dataset
datos_fuzzificados[['sentimiento_final', 'Tiempo_Base_reglas']] = datos_fuzzificados.apply(
    lambda fila: pd.Series(calcular_sentimiento(fila['puntaje_positivo'], fila['puntaje_negativo'])),
    axis=1
)

# Guardar el DataFrame con los resultados
archivo_salida_csv = 'Datos/testdataset.csv'
datos_fuzzificados.to_csv(archivo_salida_csv, index=False)
print(f"Resultados de sentimiento guardados en '{archivo_salida_csv}'.")


#------------------------------------Defuzzificacion--------------------------------
# Cargar el dataset con los sentimientos finales
archivo_entrada_csv = 'Datos/testdataset.csv'  # Cambia esto al archivo procesado que generaste antes
datos_fuzzificados = pd.read_csv(archivo_entrada_csv)

# Ejecutar la defuzzificación para obtener la clasificación
archivo_salida_csv = 'Datos/testdataset_aux.csv'
defuzzificacion(datos_fuzzificados, archivo_salida_csv, 0)

# Cargar nuevamente el archivo y ejecutar la defuzzificación con otro valor
archivo_entrada_csv = 'Datos/testdataset.csv'  # Cambia esto al archivo procesado que generaste antes
datos_fuzzificados = pd.read_csv(archivo_entrada_csv)

# Ejecutar la defuzzificación y guardar los resultados
archivo_salida_csv = 'Datos/testdataset.csv'
defuzzificacion(datos_fuzzificados, archivo_salida_csv, 1)


#---------------------------------------Benchmarks---------------------------------
archivo_entrada_csv_1 = 'Datos/test_data.csv'  # Archivo CSV con oraciones y etiquetas
archivo_entrada_csv_2 = 'Datos/testdataset_aux.csv'  # Archivo CSV con otros valores y clasificación
archivo_salida_benchmarks_csv = 'Datos/benchmarks_resultados.csv'  # Archivo de salida con resultados detallados

# Calcular los benchmarks y guardar los resultados
calcular_benchmarks(archivo_entrada_csv_1, archivo_entrada_csv_2, archivo_salida_benchmarks_csv)
