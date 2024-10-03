# Importamos FastAPI del paquete fastapi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
# Creamos una instancia de la clase FastAPI para nuestra aplicación
app = FastAPI()

# Asignamos un título a la aplicación
app.title = "Mi aplicación con FastAPI"

# Asignamos una versión a la aplicación
app.version = "0.0.1"\

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

# Definimos una ruta con el método GET para la URL raíz ('/')
@app.get('/', tags=['home'])
# Definimos una función que maneja las solicitudes a la ruta '/'
def message():
    # Devolvemos un mensaje de bienvenida cuando alguien accede a la URL raíz
    return HTMLResponse ('<h1> hello world </h1>')

app.get('/', tags = ['movies'])

def get_movies():
    return movies
