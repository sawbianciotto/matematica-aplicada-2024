import pandas as pd
import time

def defuzzificacion(data, archivo_salida, valor):
    tiempos_defuzzificacion = []  # Lista para almacenar los tiempos de defuzzificación

    if valor == 0:
        maximo_sentimiento = 10
        umbral_negativo = maximo_sentimiento / 3
        umbral_neutral = 2 * maximo_sentimiento / 3

        def clasificar_sentimiento(puntaje):  # Función para clasificar el sentimiento
            tiempo_inicio = time.time()  # Guardar tiempo de inicio
            if puntaje < umbral_negativo:
                resultado = 'Negativo'
            elif puntaje < umbral_neutral:
                resultado = 'Neutral'
            else:
                resultado = 'Positivo'
            tiempo_final = time.time()  # Guardar tiempo final
            tiempos_defuzzificacion.append(tiempo_final - tiempo_inicio)  # Calcular y guardar el tiempo
            return resultado

        data['clase_sentimiento'] = data['sentimiento_final'].apply(clasificar_sentimiento)  # Aplicar clasificación
        data['tiempo_defuzzificacion'] = tiempos_defuzzificacion  # Añadir los tiempos de procesamiento

    if valor == 1:
        def medir_tiempo_y_devolver_puntaje(puntaje):  # Función para devolver el puntaje sin clasificación
            return puntaje  # Retornar el puntaje de sentimiento

        data['puntaje_sentimiento'] = data['sentimiento_final'].apply(medir_tiempo_y_devolver_puntaje)  # Aplicar puntaje

        # Eliminar columnas innecesarias
        columnas_a_eliminar = ['Tiempo_Base_reglas', 'tiempo_fuzzi', 'tiempo_lexico', 
                               'tiempo_preprocesado', 'pos_bajo', 'pos_medio', 
                               'pos_alto', 'neg_bajo', 'neg_medio', 'neg_alto', 
                               'tiempo_ejecucion', 'sentimiento_final']
        data.drop(columns=columnas_a_eliminar, inplace=True, errors='ignore')  # Eliminar columnas

    data.to_csv(archivo_salida, index=False)  # Guardar los resultados en un archivo CSV
    print(f"Resultados de la defuzzificación guardados en '{archivo_salida}'.")  # Mensaje de confirmación
