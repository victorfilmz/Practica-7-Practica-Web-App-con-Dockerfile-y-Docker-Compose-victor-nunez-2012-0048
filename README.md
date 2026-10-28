# Práctica 7: Práctica Web App con Dockerfile y Docker Compose - Víctor Núñez (2012-0048)

## Descripción
Esta práctica consiste en crear y desplegar una aplicación web en Python (Flask) conectada a una base de datos MySQL, orquestando ambos servicios mediante Docker Compose y construyendo la imagen web a través de un Dockerfile.

## Objetivo
- Crear un entorno multi-contenedor con Docker Compose.
- Construir una aplicación web Flask que verifique conexión a MySQL.
- Gestionar variables de entorno y persistencia de datos mediante volúmenes.

## Requisitos
- Docker Desktop instalado y en ejecución.

## Ejecución del proyecto

1. Clonar el repositorio.
2. Abrir la terminal en la carpeta del proyecto.
3. Levantar los contenedores:

```bash
docker compose up -d --build
```

4. Verificar que ambos contenedores (`web` y `db`) estén en ejecución:

```bash
docker compose ps
```

5. Acceder a la aplicación web desde el navegador:

```
http://localhost:5000
```

6. Para detener los contenedores:

```bash
docker compose down
```

## Resultado esperado
Al entrar a `http://localhost:5000` se muestra el mensaje de bienvenida confirmando la conexión exitosa a MySQL:
- **¡Hola Mundo!**
- **Práctica 7: Web App con Dockerfile y Docker Compose**
- **¡Conexión a MySQL exitosa! 🚀**
- **Víctor Núñez - Matrícula: 2012-0048**

## Autor
Víctor Núñez - Matrícula: 2012-0048
