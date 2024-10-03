Configuración de un servidor con FastAPI

Creación de un entorno virtual (venv): Se creó un entorno virtual utilizando venv. Un entorno virtual es un ambiente aislado que permite instalar y gestionar paquetes de Python específicos para un proyecto, sin afectar al sistema global.

python -m venv nombre_del_entorno

Activación del entorno virtual: Se activó el entorno virtual para asegurar que las dependencias se instalen y se ejecuten dentro de este entorno aislado.

Instalación de Uvicorn: Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) que se utiliza para ejecutar aplicaciones FastAPI de manera asincrónica. Se instaló Uvicorn dentro del entorno virtual.

pip install uvicorn

Desarrollo de una aplicación FastAPI simple: Se creó un archivo Python con un código mínimo de FastAPI. El código define una instancia de la clase FastAPI y una ruta (/) que responde con un mensaje "Hello world!" cuando se realiza una solicitud GET.

```**Ejecución de la aplicación con Uvicorn:** Se utilizó el servidor Uvicorn para ejecutar la aplicación FastAPI. La aplicación se configuró para escuchar en todas las interfaces (`0.0.0.0`) y en un puerto específico.


`uvicorn nombre_del_archivo:app --reload --host 0.0.0.0 --port 8000`


* `nombre_del_archivo` es el nombre del archivo Python que contiene la aplicación FastAPI.
* `--reload` habilita la recarga automática de la aplicación cuando se realizan cambios en el código.
* `--host 0.0.0.0` permite que la aplicación sea accesible desde cualquier dirección IP en la red.
* `--port 8000` especifica el puerto en el que la aplicación escuchará las solicitudes.