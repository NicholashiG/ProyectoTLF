"""
View: Handles user interaction and display for lexical analysis and pattern validation
"""

from typing import List, Dict, Any
from ..analysis.lexical_analyzer import Token, TokenType


class TextView:
    """Enhanced view for console input/output with lexical analysis capabilities"""
    
    def get_text_input(self):
        """Get text input from the user"""
        return input("Por favor, ingrese un texto para análisis: ")
    
    def show_message(self, message):
        """Display a message to the user"""
        print(message)
    
    def show_text_info(self, text, length, uppercase, lowercase):
        """Display basic information about the text"""
        print("\n" + "="*60)
        print("INFORMACIÓN BÁSICA DEL TEXTO")
        print("="*60)
        print(f"Texto original: {text}")
        print(f"Longitud: {length} caracteres")
        print(f"Mayúsculas: {uppercase}")
        print(f"Minúsculas: {lowercase}")
        print("="*60)
    
    def show_menu(self):
        """Display the main menu options"""
        print("\n" + "="*60)
        print("SISTEMA DE ANÁLISIS LÉXICO Y VALIDACIÓN DE PATRONES")
        print("="*60)
        print("Seleccione una opción:")
        print("1. Análisis completo del texto")
        print("2. Buscar patrones específicos")
        print("3. Validar un patrón individual")
        print("4. Ver patrones disponibles")
        print("5. Mostrar ejemplos de patrones")
        print("6. Análisis básico (original)")
        print("0. Salir")
        print("="*60)
        
        while True:
            try:
                choice = int(input("Ingrese su opción (0-6): "))
                if 0 <= choice <= 6:
                    return choice
                else:
                    print("Opción inválida. Ingrese un número entre 0 y 6.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    def show_enhanced_menu(self):
        """Display the enhanced main menu with new options"""
        print("\n" + "="*70)
        print("🔬 SISTEMA AVANZADO DE ANÁLISIS LÉXICO Y VALIDACIÓN DE PATRONES")
        print("="*70)
        print("📋 ANÁLISIS Y VALIDACIÓN:")
        print("  1. Análisis completo del texto")
        print("  2. Buscar patrones específicos")
        print("  3. Validar un patrón individual")
        print("  4. Ver patrones disponibles")
        print("  5. Mostrar ejemplos de patrones")
        print("  6. Análisis básico (original)")
        print("\n📊 ESTADÍSTICAS Y VISUALIZACIÓN:")
        print("  7. Estadísticas avanzadas")
        print("  8. Generar gráficos y visualizaciones")
        print("  9. Exportar reportes (HTML/JSON/CSV)")
        print("\n⚙️  CONFIGURACIÓN:")
        print(" 10. Cambiar texto de análisis")
        print("  0. Salir")
        print("="*70)
        
        while True:
            try:
                choice = int(input("Ingrese su opción (0-10): "))
                if 0 <= choice <= 10:
                    return choice
                else:
                    print("Opción inválida. Ingrese un número entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    def show_lexical_analysis(self, report: str, statistics: Dict[str, Any]):
        """Display complete lexical analysis results"""
        print("\n" + report)
        
        if statistics.get('valid_tokens', 0) > 0:
            print(f"\n✅ Se encontraron {statistics['valid_tokens']} tokens válidos de {statistics['total_tokens']} analizados")
        else:
            print(f"\n❌ No se encontraron patrones válidos en el texto analizado")
    
    def show_valid_tokens(self, tokens: List[Token]):
        """Display valid tokens found"""
        if not tokens:
            print("\n❌ No se encontraron tokens válidos.")
            return
        
        print(f"\n✅ TOKENS VÁLIDOS ENCONTRADOS ({len(tokens)}):")
        print("-" * 60)
        
        # Group tokens by pattern
        grouped_tokens = {}
        for token in tokens:
            if token.pattern_name not in grouped_tokens:
                grouped_tokens[token.pattern_name] = []
            grouped_tokens[token.pattern_name].append(token)
        
        for pattern_name, pattern_tokens in grouped_tokens.items():
            print(f"\n📋 {pattern_name.upper()}:")
            for token in pattern_tokens:
                print(f"   • '{token.lexeme}' (Línea {token.line}, Columna {token.column})")
    
    def show_invalid_tokens(self, tokens: List[Token]):
        """Display invalid tokens found"""
        if not tokens:
            print("\n✅ No se encontraron tokens inválidos.")
            return
        
        print(f"\n❌ TOKENS INVÁLIDOS ENCONTRADOS ({len(tokens)}):")
        print("-" * 60)
        
        for token in tokens[:15]:  # Limit to avoid overwhelming output
            print(f"   • '{token.lexeme}' (Línea {token.line}, Columna {token.column})")
        
        if len(tokens) > 15:
            print(f"   ... y {len(tokens) - 15} tokens inválidos más")
    
    def show_pattern_summary(self, summary: Dict[str, int], model):
        """Display summary of patterns found"""
        if not summary:
            print("\n❌ No se encontraron patrones válidos.")
            return
        
        print(f"\n📊 RESUMEN DE PATRONES ENCONTRADOS:")
        print("-" * 60)
        
        for pattern_name, count in summary.items():
            description = model.get_pattern_description(pattern_name)
            print(f"• {pattern_name}: {count} coincidencia(s)")
            print(f"  └─ {description}")
            print()
    
    def get_pattern_choice(self, available_patterns: List[str]) -> str:
        """Get user choice for specific pattern analysis"""
        print("\n📋 PATRONES DISPONIBLES:")
        print("-" * 40)
        
        for i, pattern in enumerate(available_patterns, 1):
            print(f"{i}. {pattern}")
        
        while True:
            try:
                choice = int(input(f"\nSeleccione un patrón (1-{len(available_patterns)}): "))
                if 1 <= choice <= len(available_patterns):
                    return available_patterns[choice - 1]
                else:
                    print(f"Opción inválida. Ingrese un número entre 1 y {len(available_patterns)}.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    def show_pattern_tokens(self, pattern_name: str, tokens: List[Token], description: str):
        """Display tokens for a specific pattern"""
        print(f"\n🔍 ANÁLISIS DEL PATRÓN: {pattern_name.upper()}")
        print(f"📝 Descripción: {description}")
        print("-" * 60)
        
        if not tokens:
            print("❌ No se encontraron tokens para este patrón.")
            return
        
        print(f"✅ Se encontraron {len(tokens)} token(s) válido(s):")
        for token in tokens:
            print(f"   • '{token.lexeme}' (Línea {token.line}, Columna {token.column})")
    
    def get_validation_input(self):
        """Get input for single pattern validation"""
        text = input("\nIngrese el texto a validar: ")
        return text
    
    def show_validation_result(self, text: str, pattern_name: str, is_valid: bool, description: str):
        """Display single pattern validation result"""
        print(f"\n🔍 VALIDACIÓN DE PATRÓN: {pattern_name.upper()}")
        print(f"📝 Descripción: {description}")
        print(f"📄 Texto analizado: '{text}'")
        print("-" * 50)
        
        if is_valid:
            print("✅ VÁLIDO: El texto cumple con el patrón especificado.")
        else:
            print("❌ INVÁLIDO: El texto NO cumple con el patrón especificado.")
    
    def show_available_patterns(self, patterns: List[str], model):
        """Display all available patterns with descriptions"""
        print(f"\n📋 PATRONES DISPONIBLES ({len(patterns)}):")
        print("=" * 60)
        
        for pattern in patterns:
            description = model.get_pattern_description(pattern)
            print(f"\n🔸 {pattern.upper()}")
            print(f"   📝 {description}")
    
    def show_pattern_examples(self, pattern_name: str, examples: List[str], description: str):
        """Display examples for a specific pattern"""
        print(f"\n📋 EJEMPLOS PARA: {pattern_name.upper()}")
        print(f"📝 Descripción: {description}")
        print("-" * 60)
        
        if not examples:
            print("❌ No hay ejemplos disponibles para este patrón.")
            return
        
        print("✅ Ejemplos válidos:")
        for example in examples:
            print(f"   • {example}")
    
    def show_statistics(self, stats: Dict[str, Any]):
        """Display detailed statistics"""
        print(f"\n📊 ESTADÍSTICAS DETALLADAS:")
        print("-" * 40)
        print(f"Total de tokens: {stats.get('total_tokens', 0)}")
        print(f"Tokens válidos: {stats.get('valid_tokens', 0)}")
        print(f"Tokens inválidos: {stats.get('invalid_tokens', 0)}")
        print(f"Signos de puntuación: {stats.get('punctuation_tokens', 0)}")
        print(f"Porcentaje de validez: {stats.get('valid_percentage', 0):.1f}%")
        print(f"Líneas procesadas: {stats.get('lines_processed', 0)}")
    
    def pause(self):
        """Pause for user to read output"""
        input("\nPresione Enter para continuar...")
    
    def show_goodbye(self):
        """Display goodbye message"""
        print("\n" + "="*60)
        print("¡Gracias por usar el Sistema de Análisis Léxico!")
        print("Proyecto de Teoría de Lenguajes Formales")
        print("Universidad del Quindío - 2025")
        print("="*60)
