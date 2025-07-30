# OpenMonitor

OpenMonitor es un proyecto de ejemplo que expone una arquitectura con **Django** y **Vue 3** para visualizar datos obtenidos de la API pública de OpenProject.

## Servicios

- **django**: backend basado en Django + Django REST Framework. Expone la API en `/openmonitor-api/`.
- **vue**: frontend construido con Vite y Vue 3. Se sirve en `/openmonitor/`.
- **bbdd_django**: base de datos PostgreSQL para autenticación y configuraciones.
- **nginx**: servidor frontal que redirige el tráfico al frontend y backend.

## Puesta en marcha

```
docker-compose up --build
```

Esto levantará todos los contenedores y la aplicación estará disponible en `http://localhost/openmonitor/`.

## Uso básico

1. Accede a `http://localhost/openmonitor/` e inicia sesión con un usuario de Django.
2. En la interfaz podrás consultar el estado de OpenProject y cargar las métricas de cada proyecto.
3. Para sincronizar datos con la instancia pública de OpenProject, realiza una petición `POST` a `/openmonitor-api/sync/` usando un token de administrador.

Las métricas disponibles muestran el número de _work packages_ abiertos y cerrados por proyecto.
