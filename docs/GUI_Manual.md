# 🖥️ Manual de Usuario - Interfaz Gráfica

**Sistema de Análisis Léxico y Validación de Patrones - Versión GUI**

## 📋 Introducción

La interfaz gráfica del Sistema de Análisis Léxico proporciona una experiencia moderna e intuitiva para analizar texto utilizando expresiones regulares. Desarrollada con PyQt5, ofrece visualizaciones interactivas, análisis estadístico en tiempo real y exportación de reportes profesionales.

## 🚀 Inicio Rápido

### Ejecutar la Aplicación

```bash
python gui_main.py
```

La aplicación mostrará una pantalla de carga (splash screen) seguida de la ventana principal.

## 🏠 Interfaz Principal

### Panel Izquierdo - Entrada y Controles

#### 📝 Entrada de Texto
- **Área de texto grande** para ingresar el contenido a analizar
- **Texto de ejemplo** incluido para comenzar rápidamente
- **Soporte para texto extenso** con scroll automático

#### ⚙️ Botones de Acción
- **🔍 Analizar Texto**: Ejecuta el análisis léxico completo
- **🗑️ Limpiar**: Limpia el texto y resultados
- **📊 Generar Estadísticas**: Crea análisis estadístico detallado
- **📈 Generar Gráficos**: Produce visualizaciones interactivas
- **💾 Exportar Reporte**: Guarda análisis en múltiples formatos

### Panel Derecho - Resultados y Visualizaciones

La interfaz utiliza **pestañas organizadas** para diferentes tipos de información:

#### 📋 Pestaña: Resultados
- **Visualización organizada** de patrones encontrados
- **Agrupación por tipo** de patrón (email, teléfono, fecha, etc.)
- **Contador automático** de coincidencias
- **Formato profesional** con colores temáticos

#### 📊 Pestaña: Estadísticas
- **Tarjetas de métricas** con valores destacados
- **Estadísticas básicas**: caracteres, palabras, líneas, patrones
- **Análisis avanzado**: complejidad, entropía, diversidad, calidad
- **Barras de progreso** para métricas porcentuales
- **Actualización automática** con botón de refresh

#### 📈 Pestaña: Gráficos
- **Múltiples visualizaciones** en pestañas organizadas
- **Gráfico de torta**: Distribución de patrones encontrados
- **Gráfico de barras**: Cantidad de coincidencias por patrón
- **Gráfico radar**: Métricas de calidad del texto
- **Controles de navegación** de matplotlib integrados
- **Botones de exportación** individual por gráfico

#### 💾 Pestaña: Exportar
- **📄 Exportar como HTML**: Reporte completo con gráficos
- **📋 Exportar como JSON**: Datos estructurados para análisis
- **📊 Exportar como CSV**: Formato de hoja de cálculo

## 🎨 Características Visuales

### Tema Moderno
- **Colores profesionales** con gradientes suaves
- **Iconos emoji** para fácil identificación
- **Efectos hover** en botones y controles
- **Esquema de colores consistente** en toda la aplicación

### Widgets Especializados
- **Tarjetas de estadísticas** con valores destacados
- **Barras de progreso animadas** para métricas
- **Gráficos interactivos** con matplotlib embebido
- **Tooltips informativos** en elementos clave

## 📊 Funcionalidades Avanzadas

### Análisis en Tiempo Real
- **Procesamiento instantáneo** al hacer clic en Analizar
- **Actualización automática** de estadísticas y gráficos
- **Feedback visual** con barra de progreso y mensajes de estado

### Visualizaciones Interactivas
- **Zoom y pan** en gráficos usando controles de matplotlib
- **Múltiples tipos de gráfico** generados automáticamente
- **Colores temáticos** consistentes con la interfaz

### Sistema de Exportación
- **HTML con CSS profesional** para presentaciones
- **JSON estructurado** para integración con otras herramientas
- **CSV para análisis** en Excel o Google Sheets
- **Gráficos embebidos** en base64 para reportes completos

## 🎯 Flujo de Trabajo Recomendado

### 1. Preparar el Texto
```
1. Ejecutar: python gui_main.py
2. Ingresar o cargar texto en el área de entrada
3. Verificar que el texto contenga patrones de interés
```

### 2. Realizar Análisis
```
1. Hacer clic en "🔍 Analizar Texto"
2. Revisar resultados en la pestaña "📋 Resultados"
3. Verificar patrones encontrados y su clasificación
```

### 3. Generar Estadísticas
```
1. Hacer clic en "📊 Generar Estadísticas"
2. Explorar métricas básicas y avanzadas
3. Interpretar scores de calidad y complejidad
```

### 4. Crear Visualizaciones
```
1. Hacer clic en "📈 Generar Gráficos"
2. Navegar entre diferentes tipos de gráficos
3. Usar controles de matplotlib para zoom/pan
```

### 5. Exportar Resultados
```
1. Ir a la pestaña "💾 Exportar"
2. Seleccionar formato deseado (HTML/JSON/CSV)
3. Guardar archivo para presentación o análisis posterior
```

## 🔧 Menús y Atajos de Teclado

### Menú Archivo
- **Ctrl+O**: Abrir archivo de texto
- **Ctrl+S**: Guardar análisis
- **Ctrl+Q**: Salir de la aplicación

### Menú Análisis
- **F5**: Analizar texto
- **Ctrl+T**: Generar estadísticas
- **Ctrl+G**: Generar gráficos

### Barra de Herramientas
- **Botones de acceso rápido** para funciones principales
- **Iconos intuitivos** para fácil identificación
- **Tooltips descriptivos** al pasar el mouse

## 📱 Diseño Responsivo

### Adaptabilidad
- **Ventana redimensionable** con tamaños mínimos
- **Splitters ajustables** entre paneles
- **Scroll automático** en áreas de contenido extenso
- **Tabs organizadas** para mejor uso del espacio

### Compatibilidad
- **Windows, macOS, Linux** soportados
- **Resoluciones desde 800x600** hasta 4K
- **DPI scaling** automático en pantallas de alta resolución

## 🆘 Solución de Problemas

### Problemas Comunes

#### La aplicación no inicia
```bash
# Verificar dependencias
pip install -r requirements.txt

# Verificar PyQt5
python -c "import PyQt5; print('PyQt5 OK')"
```

#### Gráficos no se muestran
```bash
# Verificar matplotlib
python -c "import matplotlib; print('matplotlib OK')"

# Reinstalar si es necesario
pip uninstall matplotlib
pip install matplotlib>=3.7.0
```

#### Errores de CSS
- Los warnings de CSS son normales
- Qt CSS no soporta todas las propiedades CSS3
- No afectan la funcionalidad de la aplicación

### Logs y Depuración
- **Mensajes de estado** en la barra inferior
- **Diálogos de error** para problemas críticos
- **Splash screen** con información de carga

## 🎓 Casos de Uso Académicos

### Para Estudiantes
- **Análisis de textos** para proyectos de programación
- **Visualización de patrones** para comprensión de regex
- **Estadísticas** para análisis de complejidad textual

### Para Profesores
- **Demostración interactiva** de expresiones regulares
- **Análisis comparativo** de diferentes textos
- **Exportación de reportes** para evaluación

### Para Investigación
- **Análisis de corpus** textuales
- **Métricas de calidad** automáticas
- **Exportación de datos** para análisis estadístico

## 🔄 Actualizaciones y Mejoras

### Versión 2.0.0 GUI
- ✅ Interfaz gráfica completa con PyQt5
- ✅ Widgets especializados para estadísticas
- ✅ Gráficos interactivos con matplotlib
- ✅ Sistema de exportación avanzado
- ✅ Tema moderno con CSS profesional

### Próximas Características
- 🔄 Modo oscuro opcional
- 🔄 Más tipos de gráficos
- 🔄 Análisis de múltiples archivos
- 🔄 Integración con bases de datos

---

**Universidad del Quindío - Teoría de Lenguajes Formales - 2025**

*Para soporte técnico o reportar bugs, consulte la documentación del proyecto o contacte al equipo de desarrollo.*