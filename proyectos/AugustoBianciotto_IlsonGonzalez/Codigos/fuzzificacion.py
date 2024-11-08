import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time

matplotlib.use('Agg')

# Función de membresía triangular
def membresia_triangular(x, d, e, f):
    if x <= d:
        return 0.0
    elif d < x <= e:
        return ((x - d) / (e - d))
    elif e < x < f:
        return ((f - x) / (f - e))
    else:
        return 0.0

# Calcular límites para los valores mínimo, medio y máximo de una columna
def calcular_limites_membresia(datos, columna_puntaje):
    valor_min = datos[columna_puntaje].min()
    valor_max = datos[columna_puntaje].max()
    valor_medio = (valor_min + valor_max) / 2
    return valor_min, valor_medio, valor_max

# Visualizar funciones de membresía y guardar la imagen
def graficar_funciones_membresia(d_pos, e_pos, f_pos, d_neg, e_neg, f_neg, nombre_archivo):
    x = np.linspace(0, 1, 100)
    
    # Generar valores de membresía
    membresia_bajo = [membresia_triangular(val, 0, d_neg, e_neg) for val in x]
    membresia_medio = [membresia_triangular(val, d_pos, e_pos, f_pos) for val in x]
    membresia_alto = [membresia_triangular(val, e_pos, f_pos, 1) for val in x]

    # Crear gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(x, membresia_bajo, label="Negativo", color='blue')
    plt.plot(x, membresia_medio, label="Neutral", color='green')
    plt.plot(x, membresia_alto, label="Positivo", color='red')
    plt.title("Funciones de Membresía Triangular para Sentimientos")
    plt.xlabel("Puntaje")
    plt.ylabel("Valor de Membresía")
    plt.legend()
    plt.grid(True)
    plt.savefig('Datos/Grafico de la fuzzificacion')
    plt.close()

# Aplicar fuzzificación en datos y calcular tiempo de ejecución
def fuzzificacion(datos):
    if 'puntaje_positivo' not in datos.columns or 'puntaje_negativo' not in datos.columns:
        raise ValueError("Las columnas 'puntaje_positivo' y 'puntaje_negativo' deben existir en el DataFrame.")

    # Definir límites de membresía
    d_pos, e_pos, f_pos = calcular_limites_membresia(datos, 'puntaje_positivo')
    d_neg, e_neg, f_neg = calcular_limites_membresia(datos, 'puntaje_negativo')

    tiempos_fuzzificacion = []

    # Calcular valores de membresía para cada fila
    for indice, fila in datos.iterrows():
        tiempo_inicio = time.time()

        datos.at[indice, 'pos_bajo'] = membresia_triangular(fila['puntaje_positivo'], d_pos, d_pos, e_pos)
        datos.at[indice, 'pos_medio'] = membresia_triangular(fila['puntaje_positivo'], d_pos, e_pos, f_pos)
        datos.at[indice, 'pos_alto'] = membresia_triangular(fila['puntaje_positivo'], e_pos, f_pos, 1)

        datos.at[indice, 'neg_bajo'] = membresia_triangular(fila['puntaje_negativo'], d_neg, d_neg, e_neg)
        datos.at[indice, 'neg_medio'] = membresia_triangular(fila['puntaje_negativo'], d_neg, e_neg, f_neg)
        datos.at[indice, 'neg_alto'] = membresia_triangular(fila['puntaje_negativo'], e_neg, f_neg, 1)

        tiempos_fuzzificacion.append(time.time() - tiempo_inicio)

    # Añadir tiempos al DataFrame
    datos['tiempo_fuzzi'] = tiempos_fuzzificacion

    return datos, d_pos, e_pos, f_pos, d_neg, e_neg, f_neg
