"""
Lexical Analyzer: Analizador léxico para el procesamiento de texto
Implementa la tokenización y clasificación según los patrones definidos
"""

import re
from typing import List, Dict, Tuple, Any
from enum import Enum
from ..patterns.patterns import PatternValidator


class TokenType(Enum):
    """Enumeración de tipos de tokens"""
    VALID_PATTERN = "VALID_PATTERN"
    INVALID_TOKEN = "INVALID_TOKEN"
    WHITESPACE = "WHITESPACE"
    PUNCTUATION = "PUNCTUATION"
    UNKNOWN = "UNKNOWN"


class Token:
    """Clase que representa un token encontrado en el análisis"""
    
    def __init__(self, lexeme: str, token_type: TokenType, pattern_name: str = None, 
                 position: int = 0, line: int = 1, column: int = 1):
        self.lexeme = lexeme  # El texto literal del token
        self.token_type = token_type  # Tipo de token
        self.pattern_name = pattern_name  # Nombre del patrón si es válido
        self.position = position  # Posición en el texto
        self.line = line  # Línea donde se encuentra
        self.column = column  # Columna donde se encuentra
    
    def __str__(self):
        if self.pattern_name:
            return f"Token('{self.lexeme}', {self.token_type.value}, {self.pattern_name}, L{self.line}:C{self.column})"
        return f"Token('{self.lexeme}', {self.token_type.value}, L{self.line}:C{self.column})"
    
    def __repr__(self):
        return self.__str__()


class LexicalAnalyzer:
    """Analizador léxico principal"""
    
    def __init__(self):
        self.pattern_validator = PatternValidator()
        self.tokens = []
        self.current_position = 0
        self.current_line = 1
        self.current_column = 1
        self.text = ""
        
        # Patrones para caracteres especiales
        self.whitespace_pattern = re.compile(r'\s+')
        self.punctuation_pattern = re.compile(r'[.,;:!?()[\]{}"\'`~@#$%^&*+=|\\<>/\-_]')
        self.word_pattern = re.compile(r'\S+')
    
    def analyze(self, text: str) -> List[Token]:
        """
        Analiza el texto completo y retorna la lista de tokens
        
        Args:
            text: Texto a analizar
        
        Returns:
            List[Token]: Lista de tokens encontrados
        """
        self.text = text
        self.tokens = []
        self.current_position = 0
        self.current_line = 1
        self.current_column = 1
        
        while self.current_position < len(text):
            self._skip_whitespace()
            
            if self.current_position >= len(text):
                break
            
            # Intentar extraer el siguiente token
            token = self._extract_next_token()
            if token:
                self.tokens.append(token)
        
        return self.tokens
    
    def _skip_whitespace(self):
        """Salta espacios en blanco y actualiza posición"""
        while (self.current_position < len(self.text) and 
               self.text[self.current_position].isspace()):
            
            if self.text[self.current_position] == '\n':
                self.current_line += 1
                self.current_column = 1
            else:
                self.current_column += 1
                
            self.current_position += 1
    
    def _extract_next_token(self) -> Token:
        """
        Extrae el siguiente token del texto
        
        Returns:
            Token: El token extraído o None si no se puede extraer
        """
        if self.current_position >= len(self.text):
            return None
        
        # Buscar el final del token actual (hasta el siguiente espacio o final)
        start_pos = self.current_position
        start_line = self.current_line
        start_column = self.current_column
        
        # Extraer hasta el siguiente espacio, pero preservar algunos caracteres especiales
        # que son importantes para patrones como emails e IPs
        end_pos = start_pos
        while (end_pos < len(self.text) and 
               not self.text[end_pos].isspace()):
            # Si encontramos puntuación que no es parte de patrones comunes, parar
            char = self.text[end_pos]
            if char in ',;!?()[]{}"\'':
                break
            end_pos += 1
        
        # Si no hemos avanzado, es un carácter de puntuación simple
        if end_pos == start_pos:
            char = self.text[start_pos]
            if char in ',;!?()[]{}"\'':
                lexeme = char
                self.current_position += 1
                self.current_column += 1
                return Token(lexeme, TokenType.PUNCTUATION, None, 
                           start_pos, start_line, start_column)
            else:
                # Carácter desconocido
                lexeme = char
                self.current_position += 1
                self.current_column += 1
                return Token(lexeme, TokenType.UNKNOWN, None, 
                           start_pos, start_line, start_column)
        
        # Extraer el lexeme
        lexeme = self.text[start_pos:end_pos]
        
        # Actualizar posición
        self.current_position = end_pos
        self.current_column += len(lexeme)
        
        # Clasificar el token
        pattern_name = self._classify_token(lexeme)
        
        if pattern_name:
            return Token(lexeme, TokenType.VALID_PATTERN, pattern_name,
                        start_pos, start_line, start_column)
        else:
            return Token(lexeme, TokenType.INVALID_TOKEN, None,
                        start_pos, start_line, start_column)
    
    def _is_part_of_pattern(self, start_pos: int, current_pos: int) -> bool:
        """
        Determina si el carácter actual podría ser parte de un patrón válido
        """
        if current_pos >= len(self.text):
            return False
        
        char = self.text[current_pos]
        # Permitir puntos, arrobas, guiones, dos puntos como parte de patrones
        if char in '.@-:/#':
            return True
        
        return False
    
    def _classify_token(self, lexeme: str) -> str:
        """
        Clasifica un lexeme según los patrones disponibles
        
        Args:
            lexeme: El texto del token
        
        Returns:
            str: Nombre del patrón si coincide, None si no coincide con ninguno
        """
        for pattern_name in self.pattern_validator.get_available_patterns():
            if self.pattern_validator.validate_pattern(lexeme, pattern_name):
                return pattern_name
        
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas del análisis realizado
        
        Returns:
            Dict[str, Any]: Diccionario con estadísticas
        """
        if not self.tokens:
            return {}
        
        valid_tokens = [t for t in self.tokens if t.token_type == TokenType.VALID_PATTERN]
        invalid_tokens = [t for t in self.tokens if t.token_type == TokenType.INVALID_TOKEN]
        punctuation_tokens = [t for t in self.tokens if t.token_type == TokenType.PUNCTUATION]
        
        # Contar por tipos de patrones
        pattern_counts = {}
        for token in valid_tokens:
            if token.pattern_name in pattern_counts:
                pattern_counts[token.pattern_name] += 1
            else:
                pattern_counts[token.pattern_name] = 1
        
        return {
            'total_tokens': len(self.tokens),
            'valid_tokens': len(valid_tokens),
            'invalid_tokens': len(invalid_tokens),
            'punctuation_tokens': len(punctuation_tokens),
            'pattern_counts': pattern_counts,
            'valid_percentage': (len(valid_tokens) / len(self.tokens)) * 100 if self.tokens else 0,
            'lines_processed': self.current_line,
        }
    
    def get_tokens_by_type(self, token_type: TokenType) -> List[Token]:
        """
        Obtiene tokens filtrados por tipo
        
        Args:
            token_type: Tipo de token a filtrar
        
        Returns:
            List[Token]: Lista de tokens del tipo especificado
        """
        return [token for token in self.tokens if token.token_type == token_type]
    
    def get_tokens_by_pattern(self, pattern_name: str) -> List[Token]:
        """
        Obtiene tokens de un patrón específico
        
        Args:
            pattern_name: Nombre del patrón
        
        Returns:
            List[Token]: Lista de tokens que coinciden con el patrón
        """
        return [token for token in self.tokens 
                if token.token_type == TokenType.VALID_PATTERN and 
                token.pattern_name == pattern_name]
    
    def generate_report(self) -> str:
        """
        Genera un reporte detallado del análisis
        
        Returns:
            str: Reporte en formato texto
        """
        if not self.tokens:
            return "No se han analizado tokens."
        
        stats = self.get_statistics()
        report_lines = [
            "="*60,
            "REPORTE DE ANÁLISIS LÉXICO",
            "="*60,
            f"Texto analizado: {len(self.text)} caracteres",
            f"Líneas procesadas: {stats['lines_processed']}",
            f"Total de tokens: {stats['total_tokens']}",
            "",
            "DISTRIBUCIÓN DE TOKENS:",
            f"  • Tokens válidos: {stats['valid_tokens']} ({stats['valid_percentage']:.1f}%)",
            f"  • Tokens inválidos: {stats['invalid_tokens']}",
            f"  • Signos de puntuación: {stats['punctuation_tokens']}",
            "",
        ]
        
        if stats['pattern_counts']:
            report_lines.append("PATRONES ENCONTRADOS:")
            for pattern, count in stats['pattern_counts'].items():
                description = self.pattern_validator.get_pattern_description(pattern)
                report_lines.append(f"  • {pattern}: {count} ({description})")
            report_lines.append("")
        
        # Mostrar tokens válidos
        valid_tokens = self.get_tokens_by_type(TokenType.VALID_PATTERN)
        if valid_tokens:
            report_lines.append("TOKENS VÁLIDOS ENCONTRADOS:")
            for token in valid_tokens:
                report_lines.append(f"  • '{token.lexeme}' -> {token.pattern_name} (L{token.line}:C{token.column})")
            report_lines.append("")
        
        # Mostrar tokens inválidos
        invalid_tokens = self.get_tokens_by_type(TokenType.INVALID_TOKEN)
        if invalid_tokens:
            report_lines.append("TOKENS INVÁLIDOS ENCONTRADOS:")
            for token in invalid_tokens[:10]:  # Limitar a 10 para no saturar
                report_lines.append(f"  • '{token.lexeme}' (L{token.line}:C{token.column})")
            if len(invalid_tokens) > 10:
                report_lines.append(f"  ... y {len(invalid_tokens) - 10} más")
            report_lines.append("")
        
        report_lines.append("="*60)
        
        return "\n".join(report_lines)