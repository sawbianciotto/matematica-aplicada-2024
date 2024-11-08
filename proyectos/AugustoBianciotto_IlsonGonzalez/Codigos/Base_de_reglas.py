import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

# Crear las variables de entrada (puntajes) y salida (sentimiento)
puntaje_positivo = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'puntaje_positivo')
puntaje_negativo = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'puntaje_negativo')
sentimiento = ctrl.Consequent(np.arange(0, 10.1, 1), 'sentimiento')

# Definir las funciones de membresía para los puntajes positivos
puntaje_positivo['bajo'] = fuzz.trimf(puntaje_positivo.universe, [0, 0, 0.5])
puntaje_positivo['medio'] = fuzz.trimf(puntaje_positivo.universe, [0, 0.5, 1])
puntaje_positivo['alto'] = fuzz.trimf(puntaje_positivo.universe, [0.5, 1, 1])

# Definir las funciones de membresía para los puntajes negativos
puntaje_negativo['bajo'] = fuzz.trimf(puntaje_negativo.universe, [0, 0, 0.5])
puntaje_negativo['medio'] = fuzz.trimf(puntaje_negativo.universe, [0, 0.5, 1])
puntaje_negativo['alto'] = fuzz.trimf(puntaje_negativo.universe, [0.5, 1, 1])

# Definir las funciones de membresía para el sentimiento
sentimiento['negativo'] = fuzz.trimf(sentimiento.universe, [0, 0, 5])
sentimiento['neutral'] = fuzz.trimf(sentimiento.universe, [0, 5, 10])
sentimiento['positivo'] = fuzz.trimf(sentimiento.universe, [5, 10, 10])

# Definir las reglas de inferencia
regla1 = ctrl.Rule(puntaje_positivo['bajo'] & puntaje_negativo['bajo'], sentimiento['positivo'])
regla2 = ctrl.Rule(puntaje_positivo['medio'] & puntaje_negativo['bajo'], sentimiento['positivo'])
regla3 = ctrl.Rule(puntaje_positivo['alto'] & puntaje_negativo['bajo'], sentimiento['positivo'])
regla4 = ctrl.Rule(puntaje_positivo['bajo'] & puntaje_negativo['medio'], sentimiento['neutral'])
regla5 = ctrl.Rule(puntaje_positivo['medio'] & puntaje_negativo['medio'], sentimiento['neutral'])
regla6 = ctrl.Rule(puntaje_positivo['alto'] & puntaje_negativo['medio'], sentimiento['negativo'])
regla7 = ctrl.Rule(puntaje_positivo['bajo'] & puntaje_negativo['alto'], sentimiento['negativo'])
regla8 = ctrl.Rule(puntaje_positivo['medio'] & puntaje_negativo['alto'], sentimiento['negativo'])
regla9 = ctrl.Rule(puntaje_positivo['alto'] & puntaje_negativo['alto'], sentimiento['neutral'])

# Crear el sistema de control con las reglas definidas
sistema_sentimiento = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9])
simulacion_sentimiento = ctrl.ControlSystemSimulation(sistema_sentimiento)

# Función para calcular el sentimiento y el tiempo de procesamiento
def calcular_sentimiento(puntaje_pos, puntaje_neg):
    tiempo_inicio = time.time()  # Guardar el tiempo de inicio
    simulacion_sentimiento.input['puntaje_positivo'] = puntaje_pos  # Asignar puntaje positivo
    simulacion_sentimiento.input['puntaje_negativo'] = puntaje_neg  # Asignar puntaje negativo
    simulacion_sentimiento.compute()  # Calcular la salida (sentimiento)
    tiempo_final = time.time()  # Guardar el tiempo final
    tiempo_procesamiento = tiempo_final - tiempo_inicio  # Calcular el tiempo total
    return simulacion_sentimiento.output['sentimiento'], tiempo_procesamiento  # Retornar el resultado y el tiempo
