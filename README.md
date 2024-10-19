

<img src="https://github.com/pichu2707/desindexing/blob/master/desindexargsc/static/image/desindexing.jpg" width="300" height="300" alt="Portada desinedexing">

# Desindexing
Script en python para trabajar con la API de Google y poder indexar o desindexar páginas de manera más controlada introducionedo las URLs a mano y la accción que queremos escoger.
Para trabajar con el código es recomendable crear un entorno virtual con el código ```python3 -m venv [nombre_del_entorno]```
Una vez hemos creado el entorno virtual vamos a la carpeta de desindexing y dentro tenemos la de desindexargsc en ella encontraremos una carpeta con una imagen y 2 archivos, el script para indexar
o desindexar y otro que es **requirements.txt** este archivo hay que ejecutarlo con el código ```pip install -r requirements.txt``` de esta manera instalaremos en nuestro entorno virtual las 
librerías necesarias para que pueda funcionar nuestro script.

## Descarga del archivo json
Para la descarga del archivo json podeis seguir los paso que describo en este video [del canal de javilazaro de youtube](https://www.youtube.com/watch?v=OmScw_WQK_A)
Deberas subir el archivo Json a la carpeta del código, el consejo para no tener que cambiar le código es que pongais el mismo nombre al archivo que tenemos en el código *personal.json*

## Posibles problemas
Uno de los problemas que podeis tener es la falta de permisos al no haber subido el archivo a la carpeta, o por no haber dado accesos a GSC al usuario que nos ha creado Google al haber
creado las credenciales.
En alguno de los casos lo sabrás porque al ejecutar el script puedes tener errores *403*.

Si tuvieras más problemas mándame toda la información posible [aquí](mailto:hola@javilazaro.es) e incluye por favor en el asunto que es por este código **Github Desindexing**
