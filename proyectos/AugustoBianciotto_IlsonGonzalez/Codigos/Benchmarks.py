import pandas as pd
import time

def calcular_benchmarks(archivo_entrada_1, archivo_entrada_2, archivo_salida):
    datos1 = pd.read_csv(archivo_entrada_1)  # Cargar el primer dataset
    datos2 = pd.read_csv(archivo_entrada_2)  # Cargar el segundo dataset

    if 'sentence' in datos1.columns:  # Identificar columna de oraciones
        col_oracion = 'sentence'
    elif 'sentences' in datos1.columns:
        col_oracion = 'sentences'
    else:
        print("Error: No se encontró una columna de oraciones en el primer dataset.")
        return

    if 'sentiment' in datos1.columns:  # Identificar columna de etiquetas
        col_etiqueta = 'sentiment'
    elif 'sentimiento' in datos1.columns:
        col_etiqueta = 'sentimiento'
    else:
        print("Error: No se encontró una columna de etiquetas en el primer dataset.")
        return

    datos_combinados = pd.concat([datos1[[col_oracion, col_etiqueta]], datos2], axis=1)  # Combinar los datasets

    resultados = []  # Lista para almacenar los resultados

    for _, fila in datos_combinados.iterrows():  # Iterar por cada fila en los datos combinados
        texto_original = fila[col_oracion]  # Obtener el texto original
        etiqueta_original = fila[col_etiqueta]  # Obtener la etiqueta original
        puntaje_positivo = fila['puntaje_positivo']  # Obtener puntaje positivo
        puntaje_negativo = fila['puntaje_negativo']  # Obtener puntaje negativo
        clase_sentimiento = fila['clase_sentimiento']  # Obtener la clase de sentimiento
        tiempo_ejecucion = fila['tiempo_lexico']  # Obtener el tiempo de ejecución

        resultados.append({  # Almacenar los resultados de cada tweet
            "Oracion original": texto_original,
            "Etiqueta original": etiqueta_original,
            "Puntaje positivo": puntaje_positivo,
            "Puntaje negativo": puntaje_negativo,
            "Resultado de inferencia": clase_sentimiento,
            "Tiempo de ejecucion": tiempo_ejecucion
        })

    resultados_df = pd.DataFrame(resultados)  # Crear un DataFrame con los resultados
    resultados_df.to_csv(archivo_salida, index=False)  # Guardar los resultados en un archivo CSV
    print(f"Resultados detallados guardados en '{archivo_salida}'.")

    datos_combinados['tiempo_total'] = datos_combinados['tiempo_preprocesado'] + datos_combinados['tiempo_lexico'] + datos_combinados['tiempo_fuzzi'] + datos_combinados['Tiempo_Base_reglas'] + datos_combinados['tiempo_defuzzificacion']  # Calcular tiempo total
    tiempo_promedio_total = datos_combinados['tiempo_total'].mean()  # Calcular el tiempo promedio total

    positivos = (datos_combinados['clase_sentimiento'] == 'Positivo').sum()  # Contar los tweets positivos
    negativos = (datos_combinados['clase_sentimiento'] == 'Negativo').sum()  # Contar los tweets negativos
    neutrales = (datos_combinados['clase_sentimiento'] == 'Neutral').sum()  # Contar los tweets neutrales

    print(f"\nTiempo de ejecución promedio total: {tiempo_promedio_total:.4f} segundos")
    print(f"Los tweets positivos son: {positivos}, Los tweets negativos son: {negativos}, Los tweets neutrales son: {neutrales}")
