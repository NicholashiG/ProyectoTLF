"""
Main entry point for the Lexical Analysis and Pattern Validation System
Sistema de Análisis Léxico y Validación de Patrones

Punto de entrada principal del sistema reorganizado con estructura modular.
"""

import sys
import os

# Agregar el directorio src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.controller import TextController


def main():
    """Run the application"""
    print("="*70)
    print("SISTEMA DE ANÁLISIS LÉXICO Y VALIDACIÓN DE PATRONES")
    print("Universidad del Quindío - Teoría de Lenguajes Formales")
    print("="*70)
    
    controller = TextController()
    controller.run()


if __name__ == "__main__":
    main()
