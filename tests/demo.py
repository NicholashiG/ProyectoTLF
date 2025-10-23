"""
Demo: Programa de demostración del sistema de análisis léxico
Muestra ejemplos de funcionamiento con diferentes tipos de texto
"""

from controller import TextController
from test_cases import get_test_cases, get_mixed_text_examples, get_edge_cases
import time


class DemoController:
    """Controlador de demostración para mostrar funcionalidades"""
    
    def __init__(self):
        self.controller = TextController()
    
    def run_demo(self):
        """Ejecuta la demostración completa"""
        print("="*70)
        print("DEMOSTRACIÓN DEL SISTEMA DE ANÁLISIS LÉXICO")
        print("Proyecto de Teoría de Lenguajes Formales")
        print("Universidad del Quindío - 2025")
        print("="*70)
        
        # Menú de demostración
        while True:
            print("\n🎯 OPCIONES DE DEMOSTRACIÓN:")
            print("1. Demostración automática con ejemplos")
            print("2. Probar patrones específicos")
            print("3. Análisis de texto mixto")
            print("4. Casos extremos")
            print("5. Usar aplicación principal")
            print("0. Salir")
            
            choice = input("\nSeleccione una opción (0-5): ")
            
            if choice == "0":
                print("\n¡Gracias por ver la demostración!")
                break
            elif choice == "1":
                self._automatic_demo()
            elif choice == "2":
                self._pattern_specific_demo()
            elif choice == "3":
                self._mixed_text_demo()
            elif choice == "4":
                self._edge_cases_demo()
            elif choice == "5":
                self.controller.run()
            else:
                print("❌ Opción inválida. Intente de nuevo.")
            
            if choice != "5":
                input("\nPresione Enter para continuar...")
    
    def _automatic_demo(self):
        """Demostración automática con ejemplos predefinidos"""
        print("\n🤖 DEMOSTRACIÓN AUTOMÁTICA")
        print("-" * 50)
        
        # Obtener casos de prueba
        test_cases = get_test_cases()
        
        # Demostrar cada tipo de patrón
        for pattern_type, patterns in test_cases.items():
            print(f"\n📋 Demostrando: {pattern_type.upper()}")
            print("-" * 30)
            
            # Tomar algunos ejemplos válidos e inválidos
            valid_examples = patterns["validos"][:3]
            invalid_examples = patterns["invalidos"][:2]
            
            # Crear texto de prueba
            test_text = " ".join(valid_examples + invalid_examples)
            print(f"📄 Texto de prueba: {test_text}")
            
            # Procesar con el modelo
            self.controller.model.set_text(test_text)
            
            # Obtener resultados
            valid_tokens = self.controller.model.get_valid_tokens()
            invalid_tokens = self.controller.model.get_invalid_tokens()
            
            # Mostrar resultados
            print(f"✅ Tokens válidos encontrados: {len(valid_tokens)}")
            for token in valid_tokens:
                if token.pattern_name == pattern_type:
                    print(f"   • '{token.lexeme}' -> {token.pattern_name}")
            
            if invalid_tokens:
                print(f"❌ Tokens inválidos: {len(invalid_tokens)}")
                for token in invalid_tokens[:3]:  # Limitar salida
                    print(f"   • '{token.lexeme}'")
            
            time.sleep(1)  # Pausa para lectura
    
    def _pattern_specific_demo(self):
        """Demostración de patrones específicos"""
        print("\n🎯 DEMOSTRACIÓN DE PATRONES ESPECÍFICOS")
        print("-" * 50)
        
        # Obtener patrones disponibles
        patterns = self.controller.model.get_available_patterns()
        
        print("Patrones disponibles:")
        for i, pattern in enumerate(patterns, 1):
            description = self.controller.model.get_pattern_description(pattern)
            print(f"{i:2}. {pattern}: {description}")
        
        try:
            choice = int(input(f"\nSeleccione un patrón (1-{len(patterns)}): "))
            if 1 <= choice <= len(patterns):
                selected_pattern = patterns[choice - 1]
                
                # Mostrar ejemplos del patrón
                examples = self.controller.model.get_pattern_examples(selected_pattern)
                description = self.controller.model.get_pattern_description(selected_pattern)
                
                print(f"\n📋 Patrón: {selected_pattern.upper()}")
                print(f"📝 Descripción: {description}")
                print(f"✅ Ejemplos válidos:")
                for example in examples:
                    print(f"   • {example}")
                
                # Probar validación individual
                print(f"\n🧪 Prueba de validación:")
                for example in examples[:3]:
                    is_valid = self.controller.model.validate_single_pattern(example, selected_pattern)
                    status = "✅ VÁLIDO" if is_valid else "❌ INVÁLIDO"
                    print(f"   '{example}' -> {status}")
                
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Entrada inválida.")
    
    def _mixed_text_demo(self):
        """Demostración con texto mixto"""
        print("\n📄 DEMOSTRACIÓN CON TEXTO MIXTO")
        print("-" * 50)
        
        examples = get_mixed_text_examples()
        
        for i, example in enumerate(examples[:3], 1):  # Limitar a 3 ejemplos
            print(f"\n📋 Ejemplo {i}:")
            print("-" * 20)
            print(example.strip())
            
            # Analizar el texto
            self.controller.model.set_text(example)
            
            # Obtener estadísticas
            stats = self.controller.model.get_analysis_statistics()
            summary = self.controller.model.get_pattern_summary()
            
            print(f"\n📊 Resultados del análisis:")
            print(f"   • Total tokens: {stats.get('total_tokens', 0)}")
            print(f"   • Tokens válidos: {stats.get('valid_tokens', 0)}")
            print(f"   • Tokens inválidos: {stats.get('invalid_tokens', 0)}")
            print(f"   • Porcentaje validez: {stats.get('valid_percentage', 0):.1f}%")
            
            if summary:
                print(f"\n🎯 Patrones encontrados:")
                for pattern, count in summary.items():
                    print(f"   • {pattern}: {count} coincidencia(s)")
            
            if i < 3:  # No pausar en el último
                time.sleep(2)
    
    def _edge_cases_demo(self):
        """Demostración con casos extremos"""
        print("\n⚠️  DEMOSTRACIÓN DE CASOS EXTREMOS")
        print("-" * 50)
        
        edge_cases = get_edge_cases()
        
        cases_info = [
            ("Texto vacío", ""),
            ("Solo espacios", "   \n\n\t  "),
            ("Solo puntuación", "!@#$%^&*()[]{}.,;:"),
            ("Un solo carácter", "a"),
            ("Patrón con ruido", "!!!admin@test.com??? 3001234567###"),
        ]
        
        for case_name, case_text in cases_info:
            print(f"\n🧪 Caso: {case_name}")
            print(f"📄 Texto: '{case_text[:50]}{'...' if len(case_text) > 50 else ''}'")
            
            # Analizar
            self.controller.model.set_text(case_text)
            stats = self.controller.model.get_analysis_statistics()
            
            print(f"📊 Resultado:")
            print(f"   • Total tokens: {stats.get('total_tokens', 0)}")
            print(f"   • Tokens válidos: {stats.get('valid_tokens', 0)}")
            
            # Mostrar tokens válidos si los hay
            valid_tokens = self.controller.model.get_valid_tokens()
            if valid_tokens:
                print("   • Patrones encontrados:")
                for token in valid_tokens:
                    print(f"     - '{token.lexeme}' -> {token.pattern_name}")
            
            time.sleep(1)


def main():
    """Función principal de la demostración"""
    demo = DemoController()
    demo.run_demo()


if __name__ == "__main__":
    main()