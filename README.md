# Asistente-Inscripciones
Este desarrollo integra un Asistente OpenAI con widget messegener de Genesys Cloud

## Descripción

Este proyecto integra un asistente desarrollado en Python con un widget de Genesys Cloud para proporcionar una experiencia de interacción completa a través de un chat embebido en una página web. La aplicación está diseñada para gestionar las interacciones con los usuarios y facilitar el acceso a los servicios ofrecidos para Incripción de Aspirantes.

### Características principales

- **Integración con Genesys Cloud**: Configura y despliega un widget de Genesys en una página web para interactuar con usuarios a través de chat.
- **Asistente Personalizado**: Lógica del asistente en Python para manejar conversaciones, procesar datos y responder de manera dinámica.
- **Autenticación y Gestión de Sesiones**: Autentica y gestiona sesiones de usuarios con la API de Genesys Cloud.

## Requisitos

- Python 3.x
- Librerías necesarias (ver `requirements.txt`):
  - `requests`
  - `pandas`
  - `PureCloudPlatformClientV2`
- Un entorno de despliegue de Genesys Cloud configurado con un `deploymentId`.

## Uso
Configura el archivo assistant.py para definir la lógica de interacción del asistente.
Coloca el archivo widget_genesys.html en el servidor donde se alojará la página web.

- Ejecuta la aplicación en Python `python assistant.py`
- Abre `widget_genesys.html` en un navegador para probar la integración del widget de Genesys con el asistente.

## Estructura del Proyecto
- `assistant.py`: Script principal que maneja la lógica del asistente en Python.
- `widget_genesys.html`: Archivo HTML que incluye el widget de Genesys Cloud para interacción con los usuarios.
- `requirements.txt`: Archivo de dependencias necesarias para el proyecto.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.

- Bryan Ganzen
- 55 75 45 65 81
