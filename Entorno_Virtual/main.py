# Importamos FastAPI del paquete fastapi
from fastapi import FastAPI

# Creamos una instancia de la clase FastAPI para nuestra aplicación
app = FastAPI()

# Asignamos un título a la aplicación
app.title = "Mi aplicación con FastAPI"

# Asignamos una versión a la aplicación
app.version = "0.0.1"

# Definimos una ruta con el método GET para la URL raíz ('/')
@app.get('/', tags=['home'])
# Definimos una función que maneja las solicitudes a la ruta '/'
def message():
    # Devolvemos un mensaje de bienvenida cuando alguien accede a la URL raíz
    return "Hello world!"
