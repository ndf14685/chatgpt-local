# ChatGPT-Local

ChatGPT-Local es una aplicación que utiliza el modelo de OpenAI para proporcionar respuestas automatizadas. Este proyecto está diseñado para ejecutarse en un entorno local utilizando Docker, Redis y Elasticsearch para el almacenamiento y la gestión de datos.

## Requisitos Previos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Instalación

Sigue los siguientes pasos para clonar el repositorio y configurar tu entorno:

1. **Clonar el Repositorio**

   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/chatgpt-local.git
   cd chatgpt-local 
   ```

2. **Configurar la Clave de API de OpenAI**

Debes configurar tu clave de API de OpenAI para que la aplicación pueda acceder al modelo de ChatGPT. Sigue estos pasos:

Obtener la clave de API: Si no tienes una, obtén una clave de API en OpenAI.

Agregar la clave de API al archivo .env:

Crea un archivo llamado .env en la raíz del proyecto:
```bash
touch .env
```

Abre el archivo .env y añade la siguiente línea, reemplazando TU_API_KEY por tu clave real:

```bash
OPENAI_API_KEY=TU_API_KEY
```

3. **Construir y Levantar los Contenedores con Docker Compose**

Utiliza Docker Compose para construir y ejecutar los contenedores necesarios para el proyecto:

```bash
docker-compose up --build
```

Este comando hará lo siguiente:

- Construirá el contenedor Docker para la aplicación.
- Levantará los contenedores para Redis y Elasticsearch.
- Iniciará la aplicación Flask en el puerto 5000.


## Uso
Una vez que los contenedores estén en ejecución, puedes interactuar con la API enviando solicitudes HTTP.

## Enviar una Solicitud de Chat
Para enviar una solicitud de chat a la aplicación, utiliza curl o cualquier herramienta para realizar solicitudes HTTP:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"input":"Hola, ¿cómo estás?"}' http://localhost:5000/chat
```

##Recuperar el Historial de Chat
Puedes recuperar el historial de chat almacenado en Elasticsearch con el siguiente comando:

```bash
curl -X GET "http://localhost:5000/historial?user_id=ID_DEL_USUARIO"
```

Reemplaza ID_DEL_USUARIO con el identificador del usuario cuyo historial deseas recuperar.



## Solución de Problemas
Error: No module named '...'
Si obtienes errores relacionados con módulos faltantes, asegúrate de que todas las dependencias estén correctamente listadas en el archivo requirements.txt y que hayas reconstruido el contenedor:

```bash
docker-compose up --build
```

Error de Cuota Excedida
Si recibes un error de "exceeded your current quota" de OpenAI, revisa tu plan y detalles de facturación en la plataforma de OpenAI. Asegúrate de tener suficiente cuota para hacer las solicitudes.

## TODO: 
- Revisar persistencia de data, no esta funcionando
- Realizar un frontend que consuma esta api, ver si sirve
- La respuesta se limita a dos o tres lineas (limitaciones de api me parece)
- 



Contribuciones
Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio, crea una nueva rama para tus cambios y realiza un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

```markdown
### Explicaciones de los Cambios

1. **Configuración de la Clave de API de OpenAI**: Instrucciones detalladas para obtener y configurar la clave de API utilizando un archivo `.env`.
2. **Instrucciones de Instalación**: Pasos claros para clonar el repositorio, configurar el entorno y ejecutar el proyecto.
3. **Uso de la Aplicación**: Instrucciones para enviar solicitudes a la API y recuperar el historial de chat.
4. **Solución de Problemas**: Sección para ayudar a los usuarios a resolver errores comunes.
5. **Contribuciones y Licencia**: Detalles sobre cómo contribuir y el tipo de licencia del proyecto.

Este `README.md` proporciona toda la información necesaria para que un usuario descargue, configure y utilice tu proyecto.
```
