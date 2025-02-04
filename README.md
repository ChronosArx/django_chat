## Aplicación de Chat en tiempo real.

Las tecnologías utilizadas para poder realizar este chat son:

- Django
- Channels
- Daphne (Servidor asíncrono)
- Django_redis

El chat se hace mediante un consumer de channels en específico uno de websocket asincrónico. Se puede conectar a un chat mediante la siguiente url en postman.

```
ws://localhost:8000/ws/chat/<room_name>/
```

Mediante este url se puede conectar y crear distintos grupos de chat solo indicando un room_name. También mediante código se hizo la adaptación para que al manejar los eventos de envío de mensajes, el usuario que enviara el mensaje no reciba su mensaje de regreso. Para simplificar cuestiones de identificación cada usuario es identificado mediante el identificador único de websocket que channels asigna automáticamente a cada conexión.

Para probar el proyecto de manera local hay que copiar el repositorio mediante el siguiente comando:

```bash
git@github.com:ChronosArx/django_chat.git
```

Para correr el proyecto se recomienda hacerlo mediante docker y las siguientes instrucciones son para hacerlo en modo desarrollo.

El proyecto necesita de algunas variables de entorno para el modo de producción como lo son:

- ENVIRONMENT
- IP_REDIS
- PORT_REDIS
- ALLOWED_HOSTS

Pero para usar las configuraciones de modo desarrollo solo se hará uso de la variable ENVIRONMENT con el valor de **development**. Es necesario crear un archivo .env dentro de la carpeta del proyecto con esta variable entorno, se hará uso de ello más adelante.

Estando dentro de la carpeta del proyecto se creará primeramente la imagen del contenedor de docker.

```bash
docker build -t . chat:1
```

Una vez creada la imagen puedes verificar que aparezca en la lista de imágenes de docker por medio de:

```bash
docker images
```

Con la imagen creada y el archivo .env con su variable de entorno ahora es posible ejecutar el contenedor con el siguiente comando, recuerda estar ubicado en la carpeta del proyecto donde esta el archivo de variables de entorno.

```bash
docker run --name chat -p 8000:8000 --env-file .env -d chat:1
```

Con esto el contenedor estaría ejecutándose en modo desarrollo puede comprobarse que el contenedor se está ejecutando mediante el siguiente comando.

```bash
docker ps
```
