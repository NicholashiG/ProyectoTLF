#!/usr/bin/env python3
"""
Lanzador GUI para el Sistema de Análisis Léxico
Universidad del Quindío - Teoría de Lenguajes Formales

Este archivo permite ejecutar la interfaz gráfica de la aplicación
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox, QSplashScreen
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QFont, QColor

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_splash_screen():
    """Crear pantalla de carga"""
    # Crear un pixmap para el splash screen
    pixmap = QPixmap(400, 300)
    pixmap.fill(QColor(248, 249, 250))
    
    # Dibujar contenido del splash
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    
    # Título
    font_title = QFont("Arial", 18, QFont.Bold)
    painter.setFont(font_title)
    painter.setPen(QColor(33, 37, 41))
    painter.drawText(pixmap.rect(), Qt.AlignCenter | Qt.AlignTop, 
                    "Sistema de Análisis Léxico")
    
    # Subtítulo
    font_subtitle = QFont("Arial", 12)
    painter.setFont(font_subtitle)
    painter.setPen(QColor(108, 117, 125))
    painter.drawText(pixmap.rect().adjusted(0, 50, 0, 0), Qt.AlignCenter | Qt.AlignTop,
                    "Universidad del Quindío\nTeoría de Lenguajes Formales")
    
    # Emoji/Icono
    font_emoji = QFont("Arial", 48)
    painter.setFont(font_emoji)
    painter.setPen(QColor(0, 123, 255))
    painter.drawText(pixmap.rect().adjusted(0, -50, 0, 0), Qt.AlignCenter,
                    "🔍")
    
    # Versión
    font_version = QFont("Arial", 10)
    painter.setFont(font_version)
    painter.setPen(QColor(134, 142, 150))
    painter.drawText(pixmap.rect().adjusted(0, 0, 0, -20), Qt.AlignCenter | Qt.AlignBottom,
                    "Versión 2.0.0 GUI - Cargando...")
    
    painter.end()
    
    return QSplashScreen(pixmap)

def check_dependencies():
    """Verificar dependencias necesarias"""
    missing_deps = []
    
    try:
        import matplotlib
    except ImportError:
        missing_deps.append("matplotlib")
        
    try:
        import seaborn
    except ImportError:
        missing_deps.append("seaborn")
        
    try:
        import numpy
    except ImportError:
        missing_deps.append("numpy")
        
    return missing_deps

def show_error_dialog(title, message):
    """Mostrar diálogo de error"""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

def main():
    """Función principal"""
    # Crear aplicación Qt
    app = QApplication(sys.argv)
    app.setApplicationName("Sistema de Análisis Léxico")
    app.setApplicationVersion("2.0.0 GUI")
    app.setOrganizationName("Universidad del Quindío")
    app.setOrganizationDomain("uniquindio.edu.co")
    
    # Configurar estilo de la aplicación
    app.setStyle('Fusion')  # Estilo moderno
    
    # Verificar dependencias
    missing_deps = check_dependencies()
    if missing_deps:
        error_msg = (
            "Faltan dependencias necesarias para ejecutar la aplicación:\n\n"
            f"• {', '.join(missing_deps)}\n\n"
            "Por favor, instale las dependencias ejecutando:\n"
            "pip install -r requirements.txt"
        )
        show_error_dialog("Dependencias Faltantes", error_msg)
        return 1
    
    # Crear y mostrar splash screen
    splash = create_splash_screen()
    splash.show()
    app.processEvents()
    
    try:
        # Importar la ventana principal
        from src.gui.main_window import MainWindow
        
        # Actualizar splash
        splash.showMessage("Inicializando interfaz...", Qt.AlignBottom | Qt.AlignCenter, QColor(108, 117, 125))
        app.processEvents()
        
        # Crear ventana principal
        main_window = MainWindow()
        
        # Función para cerrar splash y mostrar ventana
        def show_main_window():
            splash.finish(main_window)
            main_window.show()
            main_window.status_bar.showMessage("✅ Aplicación iniciada correctamente")
        
        # Timer para mostrar splash por al menos 2 segundos
        QTimer.singleShot(2000, show_main_window)
        
        # Ejecutar aplicación
        return app.exec_()
        
    except ImportError as e:
        splash.close()
        error_msg = (
            f"Error importando módulos de la aplicación:\n\n"
            f"{str(e)}\n\n"
            "Verifique que todos los archivos estén en su lugar y que "
            "la estructura del proyecto sea correcta."
        )
        show_error_dialog("Error de Importación", error_msg)
        return 1
        
    except Exception as e:
        splash.close()
        error_msg = (
            f"Error inesperado al iniciar la aplicación:\n\n"
            f"{str(e)}\n\n"
            "Consulte la documentación o contacte al desarrollador."
        )
        show_error_dialog("Error de Aplicación", error_msg)
        return 1

if __name__ == "__main__":
    sys.exit(main())