import re
import pandas as pd
import time

# Diccionario de abreviaturas comunes
diccionario_abreviaturas = {
    "idk": "I do not know",
    "imo": "in my opinion",
    "imho": "in my humble opinion",
    "fyi": "for your information",
    "omg": "oh my god",
    "lol": "laughing out loud",
    "btw": "by the way",
    "brb": "be right back",
    "lmao": "laughing my ass off",
    "nvm": "never mind",
    "tbh": "to be honest",
    "smh": "shaking my head",
    "dm": "direct message",
    "afaik": "as far as I know",
    "ikr": "I know right",
    "wtf": "what the fuck",
    "rt": "",  # Eliminar retweet
    "wysiwyg": "what you see is what you get",
    "texn": "technology",
    "lt": "less than",
    "rds": "relational database system",
    "hmu": "hit me up",
    "bff": "best friends forever",
    "ftw": "for the win",
    "irl": "in real life",
    "jk": "just kidding",
    "np": "no problem",
    "rofl": "rolling on the floor laughing",
    "tba": "to be announced",
    "tbd": "to be determined",
    "afk": "away from keyboard",
    "bbl": "be back later",
    "bfn": "bye for now",
    "omw": "on my way",
    "thx": "thanks",
    "ttyl": "talk to you later",
    "gg": "good game",
    "g2g": "got to go",
    "atm": "at the moment",
    "gr8": "great",
    "b4": "before",
    "ur": "your",
    "u": "you",
    "cya": "see you",
    "txt": "text",
    "plz": "please",
    "cu": "see you",
    "bday": "birthday",
}

# Procesar texto: eliminar URLs, menciones, hashtags, expandir abreviaturas y limpiar texto
def preprocesar_texto(texto):
    texto = texto.lower()  # Convertir a minúsculas
    texto = re.sub(r'http\S+|www\.\S+', '', texto)  # Eliminar URLs
    texto = re.sub(r'@\w+', '', texto)  # Eliminar menciones
    texto = re.sub(r'#', '', texto)  # Eliminar símbolos #

    # Reemplazar abreviaturas
    for abreviatura, expansion in diccionario_abreviaturas.items():
        texto = re.sub(r'\b' + re.escape(abreviatura) + r'\b', expansion, texto)

    # Expandir contracciones comunes
    contracciones = {
        "can't": "can not",
        "cannot": "can not",
        "won't": "will not",
        "n't": " not",
        "'re": " are",
        "'s": " is",
        "'d": " would",
        "'ll": " will",
        "'t": " not",
        "'ve": " have",
        "'m": " am",
        "it's": "it is",
        "i'm": "i am",
        "you're": "you are",
        "they're": "they are",
        "we're": "we are",
        "let's": "let us",
        "that's": "that is",
        "who's": "who is",
        "what's": "what is",
        "here's": "here is",
        "there's": "there is",
        "where's": "where is",
        "how's": "how is",
        "cant": "can not",
        "wont": "will not",
        "dont": "do not",
        "doesnt": "does not",
        "didnt": "did not",
        "isnt": "is not",
        "arent": "are not",
        "wasnt": "was not",
        "werent": "were not",
        "havent": "have not",
        "hasnt": "has not",
        "hadnt": "had not",
        "youre": "you are",
        "theyre": "they are",
        "were": "we are",
        "lets": "let us",
        "thats": "that is",
        "whos": "who is",
        "whats": "what is",
        "heres": "here is",
        "theres": "there is",
        "wheres": "where is",
        "hows": "how is",
        "im": "i am",
        " s": "is",
        "ur": "your",
        "u": "you",
    }
    for contraccion, forma_completa in contracciones.items():
        texto = re.sub(r'\b' + re.escape(contraccion) + r'\b', forma_completa, texto)

    texto = re.sub(r'[^\w\s]', '', texto)  # Eliminar signos de puntuación
    texto = re.sub(r'[_]', '', texto)  # Eliminar guiones bajos
    texto = re.sub(r'(.)\1{2,}', r'\1\1', texto)  # Reducir caracteres repetidos
    texto = re.sub(r'\b\w{20,}\b', '', texto)  # Eliminar palabras muy largas
    texto = re.sub(r'\s+', ' ', texto).strip()  # Quitar espacios extra
    return texto

# Cargar, procesar y guardar el dataset
def procesar_y_guardar_dataset(archivo_entrada_csv, archivo_salida_procesado_csv):
    datos = pd.read_csv(archivo_entrada_csv)  # Cargar datos originales
    
    # Procesar texto de cada fila y medir el tiempo de procesamiento
    textos_procesados = []
    tiempos_procesamiento = []
    for texto_original in datos['sentence']:
        tiempo_inicio = time.time() 
        texto_procesado = preprocesar_texto(texto_original)
        textos_procesados.append(texto_procesado)
        tiempos_procesamiento.append(time.time() - tiempo_inicio)

    # Crear DataFrame con textos procesados y tiempos
    datos_procesados = pd.DataFrame({
        'oraciones': textos_procesados,
        'tiempo_preprocesado': tiempos_procesamiento
    })
    
    datos_procesados.to_csv(archivo_salida_procesado_csv, index=False)  # Guardar archivo
    print(f"Datos procesados guardados en '{archivo_salida_procesado_csv}'.")
