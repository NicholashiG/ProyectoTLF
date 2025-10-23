"""
Statistics Module: Análisis estadístico avanzado de los resultados del análisis léxico
"""

import json
import csv
from typing import Dict, List, Any, Tuple
from collections import Counter
import statistics
from datetime import datetime
import os


class StatisticsAnalyzer:
    """Analizador estadístico para resultados de análisis léxico"""
    
    def __init__(self):
        self.analysis_history = []
        self.current_analysis = {}
    
    def analyze_results(self, tokens: List, text: str, analysis_stats: Dict[str, Any]) -> Dict[str, Any]:
        """
        Realiza análisis estadístico completo de los resultados
        
        Args:
            tokens: Lista de tokens del análisis léxico
            text: Texto original analizado
            analysis_stats: Estadísticas básicas del análisis
        
        Returns:
            Dict con estadísticas avanzadas
        """
        stats = {
            'timestamp': datetime.now().isoformat(),
            'text_analysis': self._analyze_text_properties(text),
            'token_analysis': self._analyze_tokens(tokens),
            'pattern_analysis': self._analyze_patterns(tokens),
            'performance_metrics': self._calculate_performance_metrics(tokens, text),
            'quality_metrics': self._calculate_quality_metrics(analysis_stats),
            'distribution_analysis': self._analyze_distributions(tokens),
            'complexity_analysis': self._analyze_complexity(text, tokens)
        }
        
        # Guardar en historial
        self.analysis_history.append(stats)
        self.current_analysis = stats
        
        return stats
    
    def _analyze_text_properties(self, text: str) -> Dict[str, Any]:
        """Analiza propiedades del texto original"""
        words = text.split()
        lines = text.split('\n')
        
        return {
            'character_count': len(text),
            'word_count': len(words),
            'line_count': len(lines),
            'avg_word_length': statistics.mean([len(word) for word in words]) if words else 0,
            'avg_line_length': statistics.mean([len(line) for line in lines]) if lines else 0,
            'whitespace_ratio': text.count(' ') / len(text) if text else 0,
            'punctuation_count': sum(1 for c in text if not c.isalnum() and not c.isspace()),
            'uppercase_ratio': sum(1 for c in text if c.isupper()) / len(text) if text else 0,
            'lowercase_ratio': sum(1 for c in text if c.islower()) / len(text) if text else 0,
            'digit_ratio': sum(1 for c in text if c.isdigit()) / len(text) if text else 0
        }
    
    def _analyze_tokens(self, tokens: List) -> Dict[str, Any]:
        """Analiza propiedades de los tokens"""
        if not tokens:
            return {}
        
        token_lengths = [len(token.lexeme) for token in tokens]
        valid_tokens = [t for t in tokens if hasattr(t, 'pattern_name') and t.pattern_name]
        
        return {
            'total_tokens': len(tokens),
            'avg_token_length': statistics.mean(token_lengths),
            'median_token_length': statistics.median(token_lengths),
            'min_token_length': min(token_lengths),
            'max_token_length': max(token_lengths),
            'token_length_std': statistics.stdev(token_lengths) if len(token_lengths) > 1 else 0,
            'valid_token_count': len(valid_tokens),
            'valid_token_ratio': len(valid_tokens) / len(tokens) if tokens else 0,
            'unique_tokens': len(set(token.lexeme for token in tokens)),
            'token_diversity': len(set(token.lexeme for token in tokens)) / len(tokens) if tokens else 0
        }
    
    def _analyze_patterns(self, tokens: List) -> Dict[str, Any]:
        """Analiza distribución y propiedades de los patrones"""
        valid_tokens = [t for t in tokens if hasattr(t, 'pattern_name') and t.pattern_name]
        
        if not valid_tokens:
            return {'pattern_distribution': {}, 'pattern_metrics': {}}
        
        # Distribución de patrones
        pattern_counts = Counter(token.pattern_name for token in valid_tokens)
        
        # Métricas por patrón
        pattern_metrics = {}
        for pattern_name, count in pattern_counts.items():
            pattern_tokens = [t for t in valid_tokens if t.pattern_name == pattern_name]
            pattern_metrics[pattern_name] = {
                'count': count,
                'percentage': (count / len(valid_tokens)) * 100,
                'avg_length': statistics.mean([len(t.lexeme) for t in pattern_tokens]),
                'unique_values': len(set(t.lexeme for t in pattern_tokens)),
                'diversity': len(set(t.lexeme for t in pattern_tokens)) / count if count > 0 else 0
            }
        
        return {
            'pattern_distribution': dict(pattern_counts),
            'pattern_metrics': pattern_metrics,
            'most_common_pattern': pattern_counts.most_common(1)[0] if pattern_counts else None,
            'pattern_variety': len(pattern_counts),
            'entropy': self._calculate_entropy(list(pattern_counts.values()))
        }
    
    def _calculate_performance_metrics(self, tokens: List, text: str) -> Dict[str, Any]:
        """Calcula métricas de rendimiento del análisis"""
        return {
            'tokens_per_character': len(tokens) / len(text) if text else 0,
            'coverage_ratio': len([t for t in tokens if hasattr(t, 'pattern_name') and t.pattern_name]) / len(tokens) if tokens else 0,
            'processing_efficiency': len(text) / len(tokens) if tokens else 0
        }
    
    def _calculate_quality_metrics(self, analysis_stats: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula métricas de calidad del análisis"""
        total_tokens = analysis_stats.get('total_tokens', 0)
        valid_tokens = analysis_stats.get('valid_tokens', 0)
        invalid_tokens = analysis_stats.get('invalid_tokens', 0)
        
        return {
            'accuracy': (valid_tokens / total_tokens) * 100 if total_tokens > 0 else 0,
            'error_rate': (invalid_tokens / total_tokens) * 100 if total_tokens > 0 else 0,
            'recognition_rate': analysis_stats.get('valid_percentage', 0),
            'quality_score': self._calculate_quality_score(valid_tokens, invalid_tokens, total_tokens)
        }
    
    def _analyze_distributions(self, tokens: List) -> Dict[str, Any]:
        """Analiza distribuciones estadísticas de los tokens"""
        if not tokens:
            return {}
        
        # Distribución por tipo de token
        from ..analysis.lexical_analyzer import TokenType
        type_distribution = Counter()
        
        for token in tokens:
            if hasattr(token, 'token_type'):
                type_distribution[token.token_type.value if hasattr(token.token_type, 'value') else str(token.token_type)] += 1
        
        # Distribución por posición
        positions = []
        for token in tokens:
            if hasattr(token, 'line') and hasattr(token, 'column'):
                positions.append((token.line, token.column))
        
        return {
            'type_distribution': dict(type_distribution),
            'position_analysis': {
                'lines_with_tokens': len(set(pos[0] for pos in positions)) if positions else 0,
                'avg_tokens_per_line': len(tokens) / len(set(pos[0] for pos in positions)) if positions else 0,
                'max_line': max(pos[0] for pos in positions) if positions else 0
            }
        }
    
    def _analyze_complexity(self, text: str, tokens: List) -> Dict[str, Any]:
        """Analiza la complejidad del texto y análisis"""
        if not text or not tokens:
            return {}
        
        # Complejidad léxica
        unique_words = len(set(text.lower().split()))
        total_words = len(text.split())
        
        return {
            'lexical_diversity': unique_words / total_words if total_words > 0 else 0,
            'avg_sentence_length': len(text.split()) / max(1, text.count('.') + text.count('!') + text.count('?')),
            'complexity_index': self._calculate_complexity_index(text),
            'pattern_complexity': len(set(t.pattern_name for t in tokens if hasattr(t, 'pattern_name') and t.pattern_name))
        }
    
    def _calculate_entropy(self, values: List[int]) -> float:
        """Calcula la entropía de Shannon de una distribución"""
        if not values or sum(values) == 0:
            return 0.0
        
        import math
        
        total = sum(values)
        entropy = 0.0
        
        for value in values:
            if value > 0:
                p = value / total
                entropy -= p * math.log2(p) if p > 0 else 0
        
        return entropy
    
    def _calculate_quality_score(self, valid: int, invalid: int, total: int) -> float:
        """Calcula un score de calidad compuesto"""
        if total == 0:
            return 0.0
        
        accuracy = valid / total
        completeness = (valid + invalid) / total  # Qué tanto del texto fue procesado
        
        # Score ponderado
        return (accuracy * 0.7 + completeness * 0.3) * 100
    
    def _calculate_complexity_index(self, text: str) -> float:
        """Calcula un índice de complejidad del texto"""
        if not text:
            return 0.0
        
        words = text.split()
        sentences = max(1, text.count('.') + text.count('!') + text.count('?'))
        
        # Índice basado en longitud promedio de palabras y oraciones
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        avg_sentence_length = len(words) / sentences
        
        return (avg_word_length * 0.4 + avg_sentence_length * 0.6) / 10
    
    def export_to_json(self, filepath: str, stats: Dict[str, Any] = None) -> bool:
        """Exporta estadísticas a JSON"""
        try:
            data = stats or self.current_analysis
            
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error exportando a JSON: {e}")
            return False
    
    def export_to_csv(self, filepath: str) -> bool:
        """Exporta estadísticas históricas a CSV"""
        try:
            if not self.analysis_history:
                return False
            
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Flatten data for CSV
            flattened_data = []
            for analysis in self.analysis_history:
                flat_row = {
                    'timestamp': analysis['timestamp'],
                    'character_count': analysis['text_analysis']['character_count'],
                    'word_count': analysis['text_analysis']['word_count'],
                    'line_count': analysis['text_analysis']['line_count'],
                    'total_tokens': analysis['token_analysis'].get('total_tokens', 0),
                    'valid_tokens': analysis['token_analysis'].get('valid_token_count', 0),
                    'accuracy': analysis['quality_metrics']['accuracy'],
                    'pattern_variety': analysis['pattern_analysis']['pattern_variety'],
                    'complexity_index': analysis['complexity_analysis'].get('complexity_index', 0)
                }
                flattened_data.append(flat_row)
            
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                if flattened_data:
                    writer = csv.DictWriter(f, fieldnames=flattened_data[0].keys())
                    writer.writeheader()
                    writer.writerows(flattened_data)
            
            return True
        except Exception as e:
            print(f"Error exportando a CSV: {e}")
            return False
    
    def get_comparative_analysis(self) -> Dict[str, Any]:
        """Genera análisis comparativo del historial"""
        if len(self.analysis_history) < 2:
            return {'message': 'Se necesitan al menos 2 análisis para comparación'}
        
        recent_analyses = self.analysis_history[-5:]  # Últimos 5 análisis
        
        accuracies = [a['quality_metrics']['accuracy'] for a in recent_analyses]
        complexities = [a['complexity_analysis'].get('complexity_index', 0) for a in recent_analyses]
        token_counts = [a['token_analysis'].get('total_tokens', 0) for a in recent_analyses]
        
        return {
            'trend_analysis': {
                'accuracy_trend': 'improving' if accuracies[-1] > accuracies[0] else 'declining',
                'complexity_trend': 'increasing' if complexities[-1] > complexities[0] else 'decreasing',
                'volume_trend': 'increasing' if token_counts[-1] > token_counts[0] else 'decreasing'
            },
            'averages': {
                'avg_accuracy': statistics.mean(accuracies),
                'avg_complexity': statistics.mean(complexities),
                'avg_tokens': statistics.mean(token_counts)
            },
            'variability': {
                'accuracy_std': statistics.stdev(accuracies) if len(accuracies) > 1 else 0,
                'complexity_std': statistics.stdev(complexities) if len(complexities) > 1 else 0
            }
        }
    
    def get_summary_report(self) -> str:
        """Genera reporte resumen de estadísticas"""
        if not self.current_analysis:
            return "No hay análisis disponible"
        
        stats = self.current_analysis
        
        report = [
            "📊 REPORTE ESTADÍSTICO AVANZADO",
            "=" * 50,
            f"Fecha de análisis: {stats['timestamp'][:19]}",
            "",
            "📝 ANÁLISIS DE TEXTO:",
            f"  • Caracteres: {stats['text_analysis']['character_count']:,}",
            f"  • Palabras: {stats['text_analysis']['word_count']:,}",
            f"  • Líneas: {stats['text_analysis']['line_count']:,}",
            f"  • Longitud promedio de palabra: {stats['text_analysis']['avg_word_length']:.1f}",
            f"  • Ratio de mayúsculas: {stats['text_analysis']['uppercase_ratio']:.1%}",
            "",
            "🔤 ANÁLISIS DE TOKENS:",
            f"  • Total de tokens: {stats['token_analysis'].get('total_tokens', 0):,}",
            f"  • Tokens válidos: {stats['token_analysis'].get('valid_token_count', 0):,}",
            f"  • Ratio de validez: {stats['token_analysis'].get('valid_token_ratio', 0):.1%}",
            f"  • Diversidad de tokens: {stats['token_analysis'].get('token_diversity', 0):.3f}",
            f"  • Longitud media de token: {stats['token_analysis'].get('avg_token_length', 0):.1f}",
            "",
            "🎯 MÉTRICAS DE CALIDAD:",
            f"  • Precisión: {stats['quality_metrics']['accuracy']:.1f}%",
            f"  • Tasa de error: {stats['quality_metrics']['error_rate']:.1f}%",
            f"  • Score de calidad: {stats['quality_metrics']['quality_score']:.1f}%",
            "",
            "📈 ANÁLISIS DE COMPLEJIDAD:",
            f"  • Índice de complejidad: {stats['complexity_analysis'].get('complexity_index', 0):.2f}",
            f"  • Diversidad léxica: {stats['complexity_analysis'].get('lexical_diversity', 0):.3f}",
            f"  • Variedad de patrones: {stats['complexity_analysis'].get('pattern_complexity', 0)}",
            "",
            "🔍 PATRONES DETECTADOS:",
        ]
        
        pattern_metrics = stats['pattern_analysis'].get('pattern_metrics', {})
        for pattern, metrics in pattern_metrics.items():
            report.append(f"  • {pattern}: {metrics['count']} ({metrics['percentage']:.1f}%)")
        
        report.extend([
            "",
            "=" * 50
        ])
        
        return "\n".join(report)