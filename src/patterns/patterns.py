"""
Patterns: Módulo de expresiones regulares para validación de patrones
Contiene las definiciones de patrones comunes para análisis léxico
"""

import re
from typing import Dict, List, Tuple


class PatternValidator:
    """Clase que contiene las expresiones regulares y métodos de validación"""
    
    def __init__(self):
        # Definición de patrones mediante expresiones regulares
        self.patterns = {
            # Correo electrónico: usuario@dominio.extension
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            
            # Teléfono colombiano: formatos +57, 57, 3xx xxx xxxx, etc.
            'telefono': r'^(\+57|57)?[\s\-]?[3][0-9]{2}[\s\-]?[0-9]{3}[\s\-]?[0-9]{4}$',
            
            # Fecha: dd/mm/yyyy, dd-mm-yyyy, yyyy/mm/dd
            'fecha': r'^(?:(?:0?[1-9]|[12][0-9]|3[01])[\/\-](?:0?[1-9]|1[012])[\/\-](?:19|20)\d{2}|(?:19|20)\d{2}[\/\-](?:0?[1-9]|1[012])[\/\-](?:0?[1-9]|[12][0-9]|3[01]))$',
            
            # Cédula colombiana: 8-10 dígitos
            'cedula': r'^[1-9][0-9]{7,9}$',
            
            # URL: http://... o https://...
            'url': r'^https?:\/\/(?:[-\w.])+(?:\:[0-9]+)?(?:\/(?:[\w\/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$',
            
            # Código postal colombiano: 6 dígitos
            'codigo_postal': r'^[0-9]{6}$',
            
            # IP Address: xxx.xxx.xxx.xxx
            'ip_address': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            
            # Placa de vehículo colombiano: ABC123 o ABC-123
            'placa_vehiculo': r'^[A-Z]{3}[\-\s]?[0-9]{3}$',
            
            # Contraseña segura: min 8 chars, mayúscula, minúscula, número y carácter especial
            'password_segura': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            
            # Número entero
            'numero_entero': r'^[+-]?[0-9]+$',
            
            # Número decimal
            'numero_decimal': r'^[+-]?[0-9]*\.?[0-9]+$',
        }
        
        # Compilar expresiones regulares para mejor rendimiento
        self.compiled_patterns = {
            name: re.compile(pattern) for name, pattern in self.patterns.items()
        }
    
    def validate_pattern(self, text: str, pattern_name: str) -> bool:
        """
        Valida si un texto cumple con un patrón específico
        
        Args:
            text: Texto a validar
            pattern_name: Nombre del patrón a usar
        
        Returns:
            bool: True si el texto cumple el patrón, False en caso contrario
        """
        if pattern_name not in self.compiled_patterns:
            return False
        
        return bool(self.compiled_patterns[pattern_name].match(text.strip()))
    
    def find_all_patterns(self, text: str, pattern_name: str) -> List[str]:
        """
        Encuentra todas las coincidencias de un patrón en el texto
        
        Args:
            text: Texto donde buscar
            pattern_name: Nombre del patrón a buscar
        
        Returns:
            List[str]: Lista de coincidencias encontradas
        """
        if pattern_name not in self.compiled_patterns:
            return []
        
        return self.compiled_patterns[pattern_name].findall(text)
    
    def analyze_text_patterns(self, text: str) -> Dict[str, List[str]]:
        """
        Analiza un texto y encuentra todos los patrones válidos
        
        Args:
            text: Texto a analizar
        
        Returns:
            Dict[str, List[str]]: Diccionario con patrones encontrados
        """
        results = {}
        
        # Dividir el texto en posibles tokens (palabras, números, símbolos)
        tokens = re.findall(r'\S+', text)
        
        for pattern_name in self.patterns.keys():
            matches = []
            for token in tokens:
                if self.validate_pattern(token, pattern_name):
                    matches.append(token)
            
            if matches:
                results[pattern_name] = matches
        
        return results
    
    def get_pattern_description(self, pattern_name: str) -> str:
        """
        Obtiene la descripción de un patrón específico
        
        Args:
            pattern_name: Nombre del patrón
        
        Returns:
            str: Descripción del patrón
        """
        descriptions = {
            'email': 'Dirección de correo electrónico válida',
            'telefono': 'Número telefónico colombiano',
            'fecha': 'Fecha en formato dd/mm/yyyy, dd-mm-yyyy o yyyy/mm/dd',
            'cedula': 'Cédula de ciudadanía colombiana (8-10 dígitos)',
            'url': 'URL válida con protocolo HTTP o HTTPS',
            'codigo_postal': 'Código postal colombiano (6 dígitos)',
            'ip_address': 'Dirección IP válida (formato IPv4)',
            'placa_vehiculo': 'Placa de vehículo colombiano (ABC123)',
            'password_segura': 'Contraseña segura (8+ chars, mayús, minus, número, especial)',
            'numero_entero': 'Número entero (con o sin signo)',
            'numero_decimal': 'Número decimal (con o sin signo)',
        }
        
        return descriptions.get(pattern_name, 'Patrón no definido')
    
    def get_pattern_examples(self, pattern_name: str) -> List[str]:
        """
        Obtiene ejemplos de un patrón específico
        
        Args:
            pattern_name: Nombre del patrón
        
        Returns:
            List[str]: Lista de ejemplos válidos para el patrón
        """
        examples = {
            'email': ['usuario@ejemplo.com', 'test.email@dominio.co', 'admin@universidad.edu.co'],
            'telefono': ['3001234567', '+57 300 123 4567', '57-315-555-0123'],
            'fecha': ['25/12/2024', '2024/01/15', '01-06-2025'],
            'cedula': ['12345678', '1234567890', '987654321'],
            'url': ['https://www.google.com', 'http://localhost:8080', 'https://github.com/user/repo'],
            'codigo_postal': ['630001', '660001', '170001'],
            'ip_address': ['192.168.1.1', '127.0.0.1', '8.8.8.8'],
            'placa_vehiculo': ['ABC123', 'XYZ-789', 'DEF 456'],
            'password_segura': ['MiPassword123!', 'Segura2024@', 'Clave#Fuerte9'],
            'numero_entero': ['123', '-456', '+789'],
            'numero_decimal': ['123.45', '-67.89', '+3.14159'],
        }
        
        return examples.get(pattern_name, [])
    
    def get_available_patterns(self) -> List[str]:
        """
        Obtiene la lista de patrones disponibles
        
        Returns:
            List[str]: Lista de nombres de patrones disponibles
        """
        return list(self.patterns.keys())