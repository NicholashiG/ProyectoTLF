# ProyectoTLF - Sistema de Análisis Léxico y Validación de Patrones

Sistema completo de análisis léxico y validación de patrones implementado en Python usando el patrón arquitectónico MVC (Modelo-Vista-Controlador). El sistema incluye tanto **interfaz de consola tradicional** como **interfaz gráfica moderna desarrollada con PyQt5**, permitiendo identificar, extraer y validar múltiples tipos de patrones en texto con visualizaciones interactivas y análisis estadístico avanzado.

**Presentado por:**
- Diego Alejandro Carvajal Camargo
- Nicolás Jurado Ramirez  
- Johan Noé Londoño Salazar

**Curso:** Teoría de Lenguajes Formales  
**Universidad del Quindío - 2025**

## 🎯 Objetivos del Proyecto

### Objetivo General
Desarrollar un sistema de búsqueda y validación de patrones en textos mediante expresiones regulares y autómatas, que permita identificar y extraer información estructurada y garantizar la entrada correcta de datos mediante validaciones sintácticas y estructurales.

### Objetivos Específicos
- Implementar expresiones regulares para detectar patrones comunes (emails, teléfonos, fechas, URLs, etc.)
- Desarrollar un analizador léxico que procese textos y genere tokens clasificados
- Crear una interfaz interactiva con validación en tiempo real
- Implementar manejo de errores para símbolos inválidos
- Documentar técnicamente las expresiones regulares y el sistema

## 🏗️ Estructura del Proyecto

El proyecto está organizado en una estructura modular profesional:

```
ProyectoTLF/
├── 📁 src/                          # Código fuente principal
│   ├── 📁 core/                     # Componentes MVC principales
│   │   ├── model.py                 # Modelo con análisis avanzado
│   │   ├── view.py                  # Vista con interfaz mejorada
│   │   └── controller.py            # Controlador con menú expandido
│   ├── 📁 gui/                      # Interfaz gráfica PyQt5
│   │   ├── main_window.py           # Ventana principal GUI
│   │   ├── 📁 widgets/              # Widgets especializados
│   │   │   ├── statistics_widgets.py  # Widgets de estadísticas
│   │   │   └── graph_widgets.py     # Widgets de gráficos matplotlib
│   │   └── 📁 styles/               # Estilos CSS
│   │       └── main.css             # Tema moderno profesional
│   ├── 📁 patterns/                 # Expresiones regulares
│   │   └── patterns.py              # Validador de patrones
│   ├── 📁 analysis/                 # Análisis léxico y estadísticas
│   │   ├── lexical_analyzer.py      # Analizador léxico completo
│   │   └── statistics.py            # Estadísticas avanzadas
│   └── 📁 visualization/            # Gráficos y reportes
│       ├── graphs.py                # Generador de gráficos
│       └── reports.py               # Generador de reportes HTML
├── 📁 tests/                        # Pruebas y demostraciones
│   ├── test_cases.py                # Casos de prueba organizados
│   ├── quick_test.py                # Prueba rápida del sistema
│   └── demo.py                      # Sistema de demostración
├── 📁 data/                         # Datos y archivos de salida
│   ├── 📁 outputs/                  # Reportes y exportaciones
│   └── 📁 graphs/                   # Gráficos generados
├── 📁 docs/                         # Documentación
│   └── documentacion.py             # Documentación técnica
├── 📁 assets/                       # Recursos adicionales
├── main.py                          # Punto de entrada principal
├── setup.py                         # Script de configuración
├── requirements.txt                 # Dependencias del proyecto
└── README.md                        # Este archivo
```

## 🔍 Patrones Soportados

El sistema puede detectar y validar los siguientes patrones:

| Patrón | Descripción | Ejemplos |
|--------|-------------|----------|
| **Email** | Direcciones de correo electrónico | `usuario@ejemplo.com`, `test@dominio.co` |
| **Teléfono** | Números telefónicos colombianos | `3001234567`, `+57 300 123 4567` |
| **Fecha** | Fechas en múltiples formatos | `25/12/2024`, `2024-01-15` |
| **Cédula** | Cédulas de ciudadanía (8-10 dígitos) | `12345678`, `1234567890` |
| **URL** | Direcciones web válidas | `https://www.google.com` |
| **Código Postal** | Códigos postales colombianos | `630001`, `110111` |
| **IP Address** | Direcciones IP IPv4 | `192.168.1.1`, `8.8.8.8` |
| **Placa Vehículo** | Placas de vehículos colombianos | `ABC123`, `XYZ-789` |
| **Contraseña Segura** | Contraseñas con criterios de seguridad | `MiPassword123!` |
| **Números** | Enteros y decimales | `123`, `45.67`, `-89` |

## 💻 Requisitos del Sistema

### Requisitos Básicos
- **Python 3.7 o superior**
- **Librerías estándar:** `re`, `typing`, `enum`, `json`, `csv`, `datetime`
- **Sistema operativo:** Windows, Linux, macOS

### Dependencias Adicionales (para gráficos y visualización)
- **matplotlib >= 3.7.0** - Generación de gráficos
- **seaborn >= 0.12.0** - Visualizaciones estadísticas mejoradas  
- **numpy >= 1.24.0** - Operaciones numéricas
- **PyQt5 >= 5.15.0** - Interfaz gráfica moderna

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Configuración Automática
```bash
python setup.py
```

## 🚀 Cómo Ejecutar

### 🖥️ Interfaz Gráfica Moderna (Recomendado)
```bash
python gui_main.py
```
> Nueva interfaz gráfica con PyQt5, visualizaciones interactivas y análisis en tiempo real

### 💻 Aplicación de Consola
```bash
python main.py
```
> Interfaz tradicional de línea de comandos

### 🎬 Demostración Interactiva
```bash
python demo.py
```

### 🧪 Casos de Prueba
```bash
python test_cases.py
```

## 📋 Funcionalidades del Sistema

### 1. **Análisis Léxico Avanzado**
- Tokenización automática con posicionamiento preciso
- Clasificación inteligente por patrones
- Estadísticas detalladas y métricas de calidad
- Análisis de complejidad textual

### 2. **Validación de Patrones Múltiples**
- 11 patrones predefinidos (emails, teléfonos, fechas, etc.)
- Validación individual y masiva
- Ejemplos y documentación integrada
- Métricas de precisión por patrón

### 3. **Visualización y Gráficos**
- 📊 Gráficos de distribución de patrones
- 📈 Análisis de tendencias y comparativas
- 🎯 Dashboard completo con métricas
- 🗺️ Mapas de calor de patrones

### 4. **Sistema de Reportes Avanzado**
- 📄 Reportes HTML con gráficos embebidos
- 📊 Exportación a JSON y CSV
- 📈 Análisis estadístico completo
- 🎯 Métricas de rendimiento y calidad

### 5. **Interfaz Interactiva Mejorada**
- Menú principal con 10+ opciones
- Navegación intuitiva por categorías
- Feedback visual y mensajes informativos
- Gestión de errores robusta

## 🎮 Ejemplo de Uso

### Análisis Completo
```
$ python main.py
Por favor, ingrese un texto para análisis: 
Contacto: admin@empresa.com, Tel: 3001234567, Fecha: 25/12/2024

============================================================
REPORTE DE ANÁLISIS LÉXICO
============================================================
Total de tokens: 6
Tokens válidos: 3 (50.0%)
Tokens inválidos: 3

PATRONES ENCONTRADOS:
• email: 1 (Dirección de correo electrónico válida)
• telefono: 1 (Número telefónico colombiano)  
• fecha: 1 (Fecha en formato dd/mm/yyyy)

TOKENS VÁLIDOS ENCONTRADOS:
• 'admin@empresa.com' -> email (L1:C10)
• '3001234567' -> telefono (L1:C33)
• '25/12/2024' -> fecha (L1:C52)
============================================================
```

### Validación Individual
```
Seleccione una opción: 3
📋 PATRONES DISPONIBLES:
1. email
2. telefono
[...seleccionar patrón...]

Ingrese el texto a validar: admin@test.com

🔍 VALIDACIÓN DE PATRÓN: EMAIL
📝 Descripción: Dirección de correo electrónico válida
📄 Texto analizado: 'admin@test.com'
--------------------------------------------------
✅ VÁLIDO: El texto cumple con el patrón especificado.
```

## 🧪 Casos de Prueba

El sistema incluye casos de prueba exhaustivos:

- **Patrones válidos e inválidos** para cada tipo
- **Texto mixto** con múltiples patrones
- **Casos extremos** (texto vacío, solo puntuación, etc.)
- **Pruebas de rendimiento** con texto largo

## 🔧 Arquitectura Técnica

### Componentes Principales

1. **PatternValidator**: Gestiona expresiones regulares y validación
2. **LexicalAnalyzer**: Realiza tokenización y análisis léxico  
3. **Token**: Representa unidades lexicales con metadata
4. **TextModel**: Modelo de datos expandido con análisis
5. **TextView**: Vista interactiva mejorada
6. **TextController**: Controlador con menú y navegación

### Flujo de Procesamiento

```
Texto de entrada
    ↓
Análisis Léxico (Tokenización)
    ↓
Clasificación por Patrones
    ↓
Generación de Estadísticas
    ↓
Presentación de Resultados
```

## 📚 Marco Teórico

El proyecto implementa conceptos fundamentales de:

- **Lógica Proposicional**: Evaluación binaria de patrones
- **Teoría de Conjuntos**: Operaciones con alfabetos y lenguajes
- **Expresiones Regulares**: Notación algebraica para patrones
- **Autómatas Finitos**: Reconocimiento de lenguajes regulares
- **Análisis Léxico**: Tokenización y clasificación

## 🎯 Resultados Logrados

- ✅ Sistema completo de análisis léxico funcional
- ✅ 11 tipos de patrones implementados y validados
- ✅ Interfaz interactiva con múltiples opciones
- ✅ Manejo robusto de errores y casos extremos
- ✅ Documentación técnica completa
- ✅ Casos de prueba exhaustivos

## 🔮 Posibles Extensiones

- Interfaz gráfica (Tkinter/PyQt)
- Análisis de archivos por lotes
- Nuevos patrones específicos del dominio
- Exportación de resultados (JSON/CSV)
- Integración con bases de datos
- API REST para servicios web

## 👥 Contribuidores

Este proyecto fue desarrollado como parte del curso de Teoría de Lenguajes Formales en la Universidad del Quindío, bajo la supervisión de la profesora Ana María Tamayo Ocampo.
