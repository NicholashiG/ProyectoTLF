# ProyectoTLF

Aplicación de consola en Python que solicita un texto al usuario y muestra información sobre él, implementada usando el patrón arquitectónico MVC (Modelo-Vista-Controlador).

## Estructura del Proyecto

El proyecto sigue el patrón MVC:

- **model.py**: Modelo - Gestiona los datos y la lógica de negocio del texto
- **view.py**: Vista - Maneja la interacción con el usuario (entrada/salida por consola)
- **controller.py**: Controlador - Coordina el modelo y la vista
- **main.py**: Punto de entrada principal de la aplicación

## Requisitos

- Python 3.6 o superior

## Cómo ejecutar

```bash
python main.py
```

## Funcionamiento

1. La aplicación solicita al usuario que ingrese un texto
2. Muestra información sobre el texto ingresado:
   - Texto original
   - Longitud en caracteres
   - Texto en mayúsculas
   - Texto en minúsculas

## Ejemplo de uso

```
$ python main.py
Por favor, ingrese un texto: Hola Mundo
==================================================
INFORMACIÓN DEL TEXTO
==================================================
Texto original: Hola Mundo
Longitud: 10 caracteres
Mayúsculas: HOLA MUNDO
Minúsculas: hola mundo
==================================================
```