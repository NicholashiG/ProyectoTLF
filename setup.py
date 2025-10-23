"""
Setup Script: Script de configuración e instalación del proyecto
"""

import os
import sys
import subprocess
from pathlib import Path


def install_requirements():
    """Instala las dependencias necesarias"""
    print("📦 Instalando dependencias...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error instalando dependencias: {e}")
        return False


def create_directories():
    """Crea los directorios necesarios para el proyecto"""
    print("📁 Creando directorios...")
    
    directories = [
        'data/outputs',
        'data/graphs', 
        'logs',
        'temp'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   ✓ {directory}")
    
    print("✅ Directorios creados")


def check_python_version():
    """Verifica la versión de Python"""
    print("🐍 Verificando versión de Python...")
    
    if sys.version_info < (3, 7):
        print("❌ Se requiere Python 3.7 o superior")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} - Compatible")
    return True


def test_imports():
    """Prueba las importaciones principales"""
    print("🧪 Probando importaciones...")
    
    required_modules = [
        'matplotlib',
        'seaborn', 
        'numpy'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"   ✓ {module}")
        except ImportError:
            print(f"   ❌ {module}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"❌ Falló la importación de: {', '.join(failed_imports)}")
        return False
    
    print("✅ Todas las importaciones exitosas")
    return True


def run_quick_test():
    """Ejecuta una prueba rápida del sistema"""
    print("🚀 Ejecutando prueba rápida...")
    
    try:
        # Import local modules
        sys.path.insert(0, 'src')
        from src.core.model import TextModel
        
        # Create model and test
        model = TextModel()
        model.set_text("Prueba: admin@test.com, Tel: 3001234567")
        
        stats = model.get_analysis_statistics()
        if stats.get('total_tokens', 0) > 0:
            print("✅ Prueba rápida exitosa")
            return True
        else:
            print("❌ La prueba rápida falló")
            return False
            
    except Exception as e:
        print(f"❌ Error en prueba rápida: {e}")
        return False


def show_usage_info():
    """Muestra información de uso"""
    print("\n" + "="*60)
    print("🎯 CONFIGURACIÓN COMPLETADA")
    print("="*60)
    print("Para usar el sistema:")
    print("  • Aplicación principal: python main.py")
    print("  • Demostración: python tests/demo.py")
    print("  • Pruebas: python tests/quick_test.py")
    print("")
    print("Estructura del proyecto:")
    print("  • src/core/: Componentes principales (MVC)")
    print("  • src/patterns/: Expresiones regulares")
    print("  • src/analysis/: Analizador léxico y estadísticas")
    print("  • src/visualization/: Gráficos y reportes")
    print("  • tests/: Casos de prueba y demostraciones")
    print("  • data/: Archivos de salida y gráficos")
    print("  • docs/: Documentación")
    print("")
    print("📊 Los gráficos se guardan en: data/graphs/")
    print("📄 Los reportes se guardan en: data/outputs/")
    print("="*60)


def main():
    """Función principal de setup"""
    print("🔧 CONFIGURACIÓN DEL PROYECTO TLF")
    print("Universidad del Quindío - Teoría de Lenguajes Formales")
    print("="*60)
    
    # Verificar Python
    if not check_python_version():
        return False
    
    # Crear directorios
    create_directories()
    
    # Instalar dependencias
    if not install_requirements():
        print("\n⚠️  Las dependencias no se instalaron correctamente.")
        print("Puede intentar instalar manualmente con:")
        print("pip install matplotlib seaborn numpy")
        
        # Continuar sin dependencias opcionales
        print("\n🔄 Continuando sin dependencias de visualización...")
    
    # Probar importaciones
    if not test_imports():
        print("\n⚠️  Algunas dependencias no están disponibles.")
        print("Las funcionalidades de gráficos estarán limitadas.")
    
    # Prueba rápida
    if not run_quick_test():
        print("\n⚠️  La prueba rápida falló, pero puede continuar.")
    
    # Mostrar información de uso
    show_usage_info()
    
    print("\n🎉 ¡Configuración completada!")
    return True


if __name__ == "__main__":
    main()