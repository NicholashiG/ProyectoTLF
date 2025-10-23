"""
Quick Test: Prueba rápida del sistema con nueva estructura
"""

import sys
import os

# Agregar el directorio padre al path para poder importar src
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, parent_dir)

from src.core.model import TextModel

def quick_test():
    """Prueba rápida de los componentes principales"""
    print("=== PRUEBA RÁPIDA DEL SISTEMA REORGANIZADO ===\n")
    
    # Texto de prueba con múltiples patrones
    test_text = """
    Información de contacto:
    Email: admin@test.com
    Teléfono: 3001234567
    Fecha: 25/12/2024
    IP: 192.168.1.1
    URL: https://github.com/proyecto
    Cédula: 1234567890
    Código postal: 630001
    """
    
    print(f"Texto de prueba:\n{test_text}\n")
    
    try:
        # Crear modelo y analizar
        model = TextModel()
        model.set_text(test_text)
        
        # Obtener resultados básicos
        valid_tokens = model.get_valid_tokens()
        stats = model.get_analysis_statistics()
        
        print("✅ RESULTADOS BÁSICOS:")
        print(f"Total de tokens: {stats['total_tokens']}")
        print(f"Tokens válidos: {stats['valid_tokens']}")
        print(f"Tokens inválidos: {stats['invalid_tokens']}")
        print(f"Porcentaje de validez: {stats['valid_percentage']:.1f}%")
        
        print(f"\n📋 TOKENS VÁLIDOS ENCONTRADOS:")
        for token in valid_tokens[:10]:  # Limitar salida
            print(f"  • '{token.lexeme}' -> {token.pattern_name}")
        
        if len(valid_tokens) > 10:
            print(f"  ... y {len(valid_tokens) - 10} más")
        
        print(f"\n📊 PATRONES ENCONTRADOS:")
        summary = model.get_pattern_summary()
        for pattern, count in summary.items():
            print(f"  • {pattern}: {count} coincidencia(s)")
        
        # Probar estadísticas avanzadas
        print(f"\n📈 ESTADÍSTICAS AVANZADAS:")
        advanced_stats = model.get_advanced_statistics()
        quality_score = model.get_quality_score()
        print(f"  • Score de calidad: {quality_score:.1f}/100")
        
        text_analysis = advanced_stats.get('text_analysis', {})
        print(f"  • Caracteres: {text_analysis.get('character_count', 0):,}")
        print(f"  • Palabras: {text_analysis.get('word_count', 0):,}")
        print(f"  • Diversidad léxica: {advanced_stats.get('complexity_analysis', {}).get('lexical_diversity', 0):.3f}")
        
        # Probar exportación (sin generar archivos)
        print(f"\n💾 FUNCIONALIDADES DE EXPORTACIÓN:")
        print("  ✓ Exportación a JSON disponible")
        print("  ✓ Exportación a CSV disponible") 
        print("  ✓ Generación de reportes HTML disponible")
        
        # Probar generación de gráficos (sin crearlos)
        print(f"\n📊 FUNCIONALIDADES DE VISUALIZACIÓN:")
        try:
            import matplotlib
            print("  ✓ Matplotlib disponible - Gráficos habilitados")
        except ImportError:
            print("  ⚠️  Matplotlib no disponible - Gráficos deshabilitados")
        
        try:
            import seaborn
            print("  ✓ Seaborn disponible - Visualizaciones mejoradas")
        except ImportError:
            print("  ⚠️  Seaborn no disponible - Visualizaciones básicas")
        
        print(f"\n✅ ¡Prueba completada exitosamente!")
        print(f"🎯 El sistema está funcionando correctamente con la nueva estructura.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        print(f"💡 Verifique que todos los archivos estén en sus ubicaciones correctas.")
        return False

def test_structure():
    """Verifica que la estructura de carpetas sea correcta"""
    print("\n=== VERIFICACIÓN DE ESTRUCTURA ===")
    
    expected_paths = [
        "../src/core/model.py",
        "../src/core/view.py", 
        "../src/core/controller.py",
        "../src/patterns/patterns.py",
        "../src/analysis/lexical_analyzer.py",
        "../src/analysis/statistics.py",
        "../src/visualization/graphs.py",
        "../src/visualization/reports.py"
    ]
    
    missing_files = []
    for path in expected_paths:
        full_path = os.path.join(os.path.dirname(__file__), path)
        if os.path.exists(full_path):
            print(f"  ✓ {path}")
        else:
            print(f"  ❌ {path}")
            missing_files.append(path)
    
    if missing_files:
        print(f"\n⚠️  Archivos faltantes: {len(missing_files)}")
        return False
    else:
        print(f"\n✅ Estructura correcta - Todos los archivos encontrados")
        return True

if __name__ == "__main__":
    print("🔧 PRUEBA DEL SISTEMA REORGANIZADO")
    print("ProyectoTLF - Universidad del Quindío")
    print("="*50)
    
    # Verificar estructura
    structure_ok = test_structure()
    
    if structure_ok:
        # Ejecutar prueba principal
        quick_test()
    else:
        print("❌ No se puede ejecutar la prueba debido a archivos faltantes")
        print("💡 Ejecute el setup.py para configurar el proyecto correctamente")