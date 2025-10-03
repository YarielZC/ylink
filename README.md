# ylink - URL Shortener

![Project Banner](https://via.placeholder.com/1200x300.png?text=ylink%20-%20FastAPI%20URL%20Shortener)

A simple and efficient URL Shortener API built with Python, FastAPI, and MongoDB. Create and manage short links with a clean and fast RESTful interface.

---

## Features

-   **Create Short Links:** Convert any long URL into a unique, short `ylink`.
-   **Fast Redirection:** Instant redirection from short links to their original destination.
-   **User Authentication:** Secure endpoints to manage links on a per-user basis.
-   **Link Management:** Retrieve all links created by an authenticated user.
-   **Scalable:** Built with modern, asynchronous tools to handle high traffic.
-   **Secure:** Implements business logic to prevent abuse, such as limiting the number of links per user.

## Tech Stack

-   **Backend:** [Python](https://www.python.org/) 3.11+
-   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
-   **Database:** [MongoDB](https://www.mongodb.com/) (with [Pymongo](https://pymongo.readthedocs.io/))
-   **Server:** [Uvicorn](https://www.uvicorn.org/)
-   **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
-   **Environment Variables:** [python-dotenv](https://pypi.org/project/python-dotenv/)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.11 or higher
-   A MongoDB database (you can use a free cluster from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))
-   Git

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/YourUsername/ylink.git
    cd ylink
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `.env` file in the root of the project by copying the example file:
    ```sh
    cp .env.example .env
    ```

2.  Open the `.env` file and fill in your environment variables. It's crucial to set your MongoDB connection string.

    ```env
    # .env

    # MongoDB Connection String
    # Make sure to include your database name in the URL
    URL_DB="mongodb+srv://<user>:<password>@<cluster-url>/<db-name>?retryWrites=true&w=majority"

    # JWT Authentication (example)
    SECRET_KEY="your_super_secret_key"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

### Running the Application

Start the development server with Uvicorn:

```sh
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

This API is fully documented using OpenAPI and Swagger UI. Once the server is running, you can access the interactive documentation in your browser to view and test all available endpoints.

-   **Live Documentation:** **[https://ylink-five.vercel.app/docs](https://ylink-five.vercel.app/docs)**
-   **Local Documentation:** `http://127.0.0.1:8000/docs`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
---

# ylink - Acortador de URLs

![Project Banner](https://via.placeholder.com/1200x300.png?text=ylink%20-%20Acortador%20de%20URLs%20con%20FastAPI)

Un Acortador de URLs simple y eficiente construido con Python, FastAPI y MongoDB. Una API simple y eficiente para crear y gestionar enlaces cortos.

---

## Características

-   **Crear Enlaces Cortos:** Convierte cualquier URL larga en un `ylink` corto y único.
-   **Redirección Rápida:** Redirección instantánea desde los enlaces cortos a su destino original.
-   **Autenticación de Usuarios:** Endpoints seguros para gestionar enlaces por usuario.
-   **Gestión de Enlaces:** Obtén todos los enlaces creados por un usuario autenticado.
-   **Escalable:** Construido con herramientas modernas y asíncronas para manejar alto tráfico.
-   **Seguro:** Implementa lógica de negocio para prevenir abusos, como limitar el número de enlaces por usuario.

## Tecnologías Utilizadas

-   **Backend:** [Python](https://www.python.org/) 3.11+
-   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
-   **Base de Datos:** [MongoDB](https://www.mongodb.com/) (con [Pymongo](https://pymongo.readthedocs.io/))
-   **Servidor:** [Uvicorn](https://www.uvicorn.org/)
-   **Validación de Datos:** [Pydantic](https://docs.pydantic.dev/)
-   **Variables de Entorno:** [python-dotenv](https://pypi.org/project/python-dotenv/)

## Cómo Empezar

Sigue estas instrucciones para obtener una copia del proyecto y ejecutarlo en tu máquina local para desarrollo y pruebas.

### Prerrequisitos

-   Python 3.11 o superior
-   Una base de datos MongoDB (puedes usar un clúster gratuito de [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))
-   Git

### Instalación y Configuración

1.  **Clona el repositorio:**
    ```sh
    git clone https://github.com/TuUsuario/ylink.git
    cd ylink
    ```

2.  **Crea y activa un entorno virtual:**
    ```sh
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```sh
    pip install -r requirements.txt
    ```

### Configuración de Variables

1.  Crea un archivo `.env` en la raíz del proyecto copiando el archivo de ejemplo:
    ```sh
    cp .env.example .env
    ```

2.  Abre el archivo `.env` y completa tus variables de entorno. Es crucial configurar tu cadena de conexión de MongoDB.

    ```env
    # .env

    # Cadena de conexión de MongoDB
    # Asegúrate de incluir el nombre de tu base de datos en la URL
    URL_DB="mongodb+srv://<usuario>:<contraseña>@<url-del-cluster>/<nombre-db>?retryWrites=true&w=majority"

    # Autenticación JWT (ejemplo)
    SECRET_KEY="tu_clave_super_secreta"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

### Ejecutar la Aplicación

Inicia el servidor de desarrollo con Uvicorn:

```sh
uvicorn app:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Documentación de la API

Esta API está completamente documentada usando OpenAPI y Swagger UI. Una vez que el servidor esté en funcionamiento, puedes acceder a la documentación interactiva en tu navegador para ver y probar todos los endpoints disponibles.

-   **Documentación en vivo:** **[https://ylink-five.vercel.app/docs](https://ylink-five.vercel.app/docs)**
-   **Documentación local:** `http://127.0.0.1:8000/docs`

## Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para más detalles.