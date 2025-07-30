# Backend de OpenMonitor

Este directorio contiene el servicio de backend construido con **Django** y **Django REST Framework**.
Permite sincronizar datos de OpenProject y exponer métricas a través de una API.

## Requisitos

- Python 3.11
- Base de datos PostgreSQL (variables `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_HOST`)

## Instalación

```bash
pip install -r requirements.txt
```

## Migraciones y superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Ejecución en desarrollo

```bash
python manage.py runserver 0.0.0.0:8000
```

La API queda disponible en `http://localhost:8000/openmonitor-api/`.

## Sincronizar con OpenProject

El endpoint `POST /openmonitor-api/sync/` requiere autenticación por token y permisos de administrador. Sincroniza proyectos, usuarios, estados y _work packages_ desde la API pública de OpenProject.

```bash
curl -X POST \
  -H "Authorization: Token <tu_token>" \
  http://localhost:8000/openmonitor-api/sync/
```

## Obtener métricas

`GET /openmonitor-api/projects/` devuelve cada proyecto con el número de paquetes de trabajo abiertos y cerrados.

## Gestión de usuarios inactivos

Los administradores pueden consultar las cuentas no activadas mediante:

```bash
curl -H "Authorization: Token <admin_token>" http://localhost:8000/openmonitor-api/inactive-users/
```

Para activar una cuenta específica:

```bash
curl -X POST -H "Authorization: Token <admin_token>" \
  http://localhost:8000/openmonitor-api/activate-user/<id>/
```

## Pruebas

```bash
python manage.py test --settings=openmonitor.settings_test
```
