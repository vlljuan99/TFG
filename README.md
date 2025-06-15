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
