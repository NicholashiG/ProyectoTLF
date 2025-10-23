#!/usr/bin/env python3
"""
Demo de la Interfaz Gráfica - Sistema de Análisis Léxico
Universidad del Quindío - Teoría de Lenguajes Formales

Este script demuestra las capacidades de la nueva interfaz gráfica
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_demo_text():
    """Crear texto de demostración con múltiples patrones"""
    return """
🎯 TEXTO DE DEMOSTRACIÓN - SISTEMA DE ANÁLISIS LÉXICO

📧 Contactos de Email:
- juan.perez@uniquindio.edu.co
- maria.rodriguez@uqvirtual.edu.co
- admin@proyectotlf.com
- soporte.tecnico@universidad.gov.co

📞 Números de Teléfono:
- 310-555-1234
- (6) 7359800
- +57 6 7359800
- 3145678901

📅 Fechas Importantes:
- 2025-10-22
- 15/03/2025
- 2025/12/25
- 01-01-2026

🌐 Direcciones Web:
- https://www.uniquindio.edu.co
- http://proyectotlf.com
- https://github.com/universidad/proyectotlf
- www.ejemplos.edu.co

🏠 Direcciones IP:
- 192.168.1.1
- 10.0.0.1
- 172.16.0.1
- 192.168.100.254

🆔 Identificadores:
- ID12345
- REF_2025_001
- DOC-TLF-2025
- USER_123456

📮 Códigos Postales:
- 630001
- 110111
- 050001
- 760001

💳 Números de Tarjeta:
- 4532-1234-5678-9012
- 5412-3456-7890-1234

🔢 Números de Cuenta:
- ACC-123456789
- CTA_987654321

✅ Este texto contiene múltiples patrones para demostrar 
las capacidades avanzadas del sistema de análisis léxico.

📊 El sistema podrá:
- Identificar todos los patrones válidos
- Generar estadísticas detalladas
- Crear visualizaciones interactivas
- Exportar reportes profesionales

🎓 Universidad del Quindío - Teoría de Lenguajes Formales - 2025
"""

def demo_gui():
    """Ejecutar demostración de la GUI"""
    try:
        # Importar la ventana principal
        from src.gui.main_window import MainWindow
        
        # Crear aplicación
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
            
        # Configurar aplicación
        app.setApplicationName("Demo GUI - Sistema de Análisis Léxico")
        app.setApplicationVersion("2.0.0 Demo")
        
        # Crear ventana principal
        main_window = MainWindow()
        
        # Cargar texto de demostración
        demo_text = create_demo_text()
        main_window.text_input.setText(demo_text)
        
        # Mostrar ventana
        main_window.show()
        
        # Función para análisis automático después de 3 segundos
        def auto_analyze():
            """Realizar análisis automático para la demo"""
            try:
                # Ejecutar análisis
                main_window.analyze_text()
                
                # Mensaje informativo
                QMessageBox.information(
                    main_window,
                    "🎯 Demo Automática",
                    """
                    <h3>¡Análisis Completado!</h3>
                    
                    <p>El sistema ha analizado automáticamente el texto de demostración.</p>
                    
                    <p><b>Próximos pasos sugeridos:</b></p>
                    <ul>
                    <li>📋 Revise los resultados en la pestaña "Resultados"</li>
                    <li>📊 Genere estadísticas haciendo clic en "Generar Estadísticas"</li>
                    <li>📈 Cree gráficos haciendo clic en "Generar Gráficos"</li>
                    <li>💾 Exporte reportes desde la pestaña "Exportar"</li>
                    </ul>
                    
                    <p><i>¡Explore todas las funcionalidades de la interfaz!</i></p>
                    """
                )
                
                # Auto-generar estadísticas después de 2 segundos más
                QTimer.singleShot(2000, lambda: main_window.generate_statistics())
                
                # Auto-generar gráficos después de 4 segundos más
                QTimer.singleShot(4000, lambda: main_window.generate_graphs())
                
            except Exception as e:
                QMessageBox.warning(
                    main_window,
                    "Error en Demo",
                    f"Error durante la demostración automática:\n{str(e)}"
                )
        
        # Programar análisis automático
        QTimer.singleShot(3000, auto_analyze)
        
        # Mostrar mensaje de bienvenida
        QTimer.singleShot(1000, lambda: QMessageBox.information(
            main_window,
            "🎉 Bienvenido a la Demo GUI",
            """
            <h3>Sistema de Análisis Léxico - Versión GUI</h3>
            
            <p>Esta demostración muestra las capacidades avanzadas 
            de la nueva interfaz gráfica desarrollada con PyQt5.</p>
            
            <p><b>Características destacadas:</b></p>
            <ul>
            <li>🖥️ Interfaz moderna y profesional</li>
            <li>📊 Estadísticas en tiempo real</li>
            <li>📈 Gráficos interactivos</li>
            <li>💾 Exportación múltiple</li>
            <li>🎨 Tema moderno con CSS</li>
            </ul>
            
            <p><i>El análisis comenzará automáticamente en 3 segundos...</i></p>
            """
        ))
        
        # Configurar mensaje de estado
        main_window.status_bar.showMessage("🎬 Demostración iniciada - Análisis automático en 3 segundos...")
        
        return app.exec_()
        
    except ImportError as e:
        print(f"❌ Error importando módulos GUI: {e}")
        print("💡 Asegúrese de que PyQt5 esté instalado: pip install PyQt5")
        return 1
        
    except Exception as e:
        print(f"❌ Error en la demostración: {e}")
        return 1

def main():
    """Función principal"""
    print("🎬 Iniciando demostración de la GUI...")
    print("📋 Cargando texto con múltiples patrones...")
    print("🚀 Abriendo interfaz gráfica...")
    print()
    
    return demo_gui()

if __name__ == "__main__":
    sys.exit(main())