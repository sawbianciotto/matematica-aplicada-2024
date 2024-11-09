### Proyecto final de Matemática Aplicada.
##### Algoritmo de análisis de sentimiento difuso a partir de tweets en base al artículo.
  
[Vashishtha, S., & Susan, S. (2019). Fuzzy rule based unsupervised sentiment analysis from social media posts. Expert Systems with Applications, 138, 112834.](http://www.researchgate.net/profile/Srishti-Vashishtha-2/publication/334622166_Fuzzy_Rule_based_Unsupervised_Sentiment_Analysis_from_Social_Media_Posts/links/5ece42174585152945149e5b/Fuzzy-Rule-based-Unsupervised-Sentiment-Analysis-from-Social-Media-Posts.pdf "Vashishtha, S., & Susan, S. (2019). Fuzzy rule based unsupervised sentiment analysis from social media posts. Expert Systems with Applications, 138, 112834.")
#### Integrantes
- Oscar Augusto Bianciotto Lobasso.
- Ilson Matías González Estigarribia.

#### Entorno virtual (no es obligatorio)
- Creación del entorno virtual.
    ```bash
    python -m venv .ve
    ```

- Activación del entorno virtual.
    > Windows
    
    Cambiar la política de ejecución en Windows en PowerShell como administrador (solo si es necesario)
    ```bash
    Set-ExecutionPolicy RemoteSigned
    ```
    Luego ejecutar:
    ```bash
    .ve\Scripts\activate
    ```
    Cambiar la política de ejecución de scripts puede tener implicaciones de seguridad, por lo que se recomienda cambiarla de nuevo a `Restricted` si ya no necesitas ejecutar scripts. Para hacerlo, ejecuta:
    ```bash
    Set-ExecutionPolicy Restricted
    ```
    > MacOs y Linux
    ```bash
    source .ve/bin/activate
    ```
- Desactivación del entorno virtual.
    ```bash
    deactivate
    ```

#### Instalación
Instalar las dependencias necesarias usando requirements.txt
```bash
pip install -r requirements.txt
```
#### Ejecución
Luego de la instalación de las dependencias, ejecutamos el archivo `main.py`
```bash
python Codigos/main.py
```

#### Resultados
Los resultados del análisis se encuentran en la carpeta Datos/, donde se guardan los archivos generados por el algoritmo.