import re
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

# Cargar, procesar, analizar sentimiento y guardar el dataset
def analizar_sentimientos(archivo_entrada_csv, archivo_salida_csv):
    datos = pd.read_csv(archivo_entrada_csv)  # Cargar datos originales
    analizador = SentimentIntensityAnalyzer()  # Inicializar analizador de VADER
    
    # Listas para puntajes de sentimiento y tiempos de ejecución
    puntajes_positivos = []
    puntajes_negativos = []
    tiempos_lexico = []

    # Procesar cada texto y calcular sentimiento
    for texto in datos['oraciones']:
        tiempo_inicio = time.time()  # Tiempo de inicio

        # Obtener puntajes de sentimiento
        puntajes_sentimiento = analizador.polarity_scores(texto)
        
        # Calcular puntajes positivo y negativo ajustados
        puntaje_positivo = puntajes_sentimiento['pos'] + max(0, puntajes_sentimiento['compound'])
        puntaje_negativo = puntajes_sentimiento['neg'] + max(0, -puntajes_sentimiento['compound'])
        
        # Normalizar puntajes
        puntaje_total = puntaje_positivo + puntaje_negativo
        if puntaje_total > 0:
            puntajes_positivos.append(puntaje_positivo / puntaje_total)
            puntajes_negativos.append(puntaje_negativo / puntaje_total)
        else:
            puntajes_positivos.append(0.0)
            puntajes_negativos.append(0.0)

        # Guardar tiempo de procesamiento de la oración
        tiempos_lexico.append(time.time() - tiempo_inicio)

    # Añadir puntajes y tiempos al DataFrame
    datos['puntaje_positivo'] = puntajes_positivos
    datos['puntaje_negativo'] = puntajes_negativos
    datos['tiempo_lexico'] = tiempos_lexico

    # Guardar datos procesados en un nuevo archivo CSV
    datos.to_csv(archivo_salida_csv, index=False)
    print(f"Datos con puntajes de sentimiento y tiempo de ejecución guardados en '{archivo_salida_csv}'.")
