# Documentación del proyecto de FastAPI con SQLite y JWT

En este proyecto, se presenta un ejemplo de cómo utilizar FastAPI para desarrollar una aplicación backend que implementa un sistema de autenticación basado en tokens JWT y utiliza SQLite como base de datos local. La biblioteca `PyJWT` es utilizada para manejar la generación y verificación de los tokens JWT.

## Resumen de pasos para el desarrollo del proyecto:

1. Crear un entorno virtual e instalar las dependencias necesarias como FastAPI, Uvicorn, SQLAlchemy, PyJWT y bcrypt.
2. Diseñar el modelo de base de datos utilizando SQLAlchemy, definiendo dos clases principales, `User` y `Task`, incluyendo sus relaciones y restricciones (models.py).
3. Implementar un sistema de autenticación utilizando JWT, junto con funciones de ayuda para administrar contraseñas utilizando la biblioteca bcrypt (auth.py).
4. Desarrollar funciones CRUD para la interacción con la base de datos, permitiendo crear, leer, actualizar y eliminar registros de usuarios y tareas (crud.py).
5. Implementar puntos finales de la API RESTful utilizando FastAPI, exponiendo operaciones que permitan registrarse, iniciar sesión y realizar acciones sobre objetos User y Task (main.py).
6. Agregar un script para ejecutar la aplicación, utilizando uvicorn como servidor ASGI (run.py).

Este proyecto presenta un esquema básico que puede ser mejorado y adaptado según las necesidades específicas de cada caso. Sin embargo, cubre las funcionalidades principales solicitadas y sirve como punto de partida sólido para desarrollar aplicaciones más avanzadas basadas en FastAPI, SQLite y JWT.