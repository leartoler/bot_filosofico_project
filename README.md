Repositorio del proyecto "bot filosófico" ([@_TFbot](https://twitter.com/_TFbot)), coordinado por el [#SeminarioTF](http://stf.filos.unam.mx/).

Visita la [Wiki](https://github.com/transpoetico/bot_filosofico_project/wiki) para seguir la documentación.

Antes de correr el programa, asegúrate de instalar las dependencias necesarias. Podrás encontrar esta info en el archivo "requirements.txt".
Para instalar las dependencias lo único que tienes que hacer es usar un manejador de paquetes para Python.
Se usa **pip** en el ejemplo:

~~~
pip install -r requirements.txt 
~~~

O usando **conda**:

~~~
conda install —file requirements.txt
~~~

También necesitarás los [tokens de acceso de Twiiter](https://developer.twitter.com/) para poderte conectar a la API. Guardarlos en un archivo .py y asegurarte de importarlos en el script de ejecución. 
Ejemplo:
~~~
CONSUMER_KEY = "key"
CONSUMER_SECRET = "key"
ACCESS_TOKEN = "key"
ACCESS_SECRET = "key"
~~~