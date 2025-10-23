"""
Visualization Module: Generación de gráficos y visualizaciones para análisis de datos
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge
import seaborn as sns
import numpy as np
from typing import Dict, List, Any, Tuple
import os
from datetime import datetime


class GraphGenerator:
    """Generador de gráficos para visualización de estadísticas"""
    
    def __init__(self, output_dir: str = "data/graphs"):
        self.output_dir = output_dir
        self.colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#4ECDC4', 
                      '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
        
        # Configurar estilo
        plt.style.use('default')
        sns.set_palette("husl")
        
        # Crear directorio de salida si no existe
        os.makedirs(output_dir, exist_ok=True)
    
    def create_pattern_distribution_pie(self, pattern_data: Dict[str, int], 
                                       filename: str = None) -> str:
        """
        Crea gráfico de torta para distribución de patrones
        
        Args:
            pattern_data: Diccionario con patrones y sus frecuencias
            filename: Nombre del archivo (opcional)
        
        Returns:
            str: Ruta del archivo guardado
        """
        if not pattern_data:
            return None
        
        # Configurar figura
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Datos para el gráfico
        patterns = list(pattern_data.keys())
        counts = list(pattern_data.values())
        colors = self.colors[:len(patterns)]
        
        # Crear gráfico de torta
        wedges, texts, autotexts = ax.pie(counts, labels=patterns, colors=colors,
                                         autopct='%1.1f%%', startangle=90,
                                         explode=[0.05] * len(patterns))
        
        # Mejorar apariencia
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        # Título y configuración
        ax.set_title('Distribución de Patrones Detectados', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Leyenda
        ax.legend(wedges, [f'{p}: {c}' for p, c in zip(patterns, counts)],
                 title="Patrones", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.tight_layout()
        
        # Guardar archivo
        filename = filename or f"pattern_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_token_analysis_bar(self, token_stats: Dict[str, Any], 
                                 filename: str = None) -> str:
        """
        Crea gráfico de barras para análisis de tokens
        """
        if not token_stats:
            return None
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gráfico 1: Distribución de tipos de tokens
        categories = ['Tokens Válidos', 'Tokens Inválidos', 'Signos de Puntuación']
        values = [
            token_stats.get('valid_token_count', 0),
            token_stats.get('total_tokens', 0) - token_stats.get('valid_token_count', 0),
            0  # Placeholder para puntuación
        ]
        
        bars1 = ax1.bar(categories, values, color=self.colors[:3])
        ax1.set_title('Distribución de Tipos de Tokens', fontweight='bold')
        ax1.set_ylabel('Cantidad')
        
        # Agregar valores en las barras
        for bar, value in zip(bars1, values):
            if value > 0:
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                        str(value), ha='center', va='bottom', fontweight='bold')
        
        # Gráfico 2: Métricas de tokens
        metrics = ['Longitud Promedio', 'Diversidad', 'Ratio de Validez']
        metric_values = [
            token_stats.get('avg_token_length', 0),
            token_stats.get('token_diversity', 0) * 10,  # Escalar para visualización
            token_stats.get('valid_token_ratio', 0) * 10  # Escalar para visualización
        ]
        
        bars2 = ax2.bar(metrics, metric_values, color=self.colors[3:6])
        ax2.set_title('Métricas de Calidad de Tokens', fontweight='bold')
        ax2.set_ylabel('Valor')
        
        # Agregar valores en las barras
        for bar, value in zip(bars2, metric_values):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                    f'{value:.2f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        
        # Guardar archivo
        filename = filename or f"token_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_quality_metrics_radar(self, quality_data: Dict[str, float], 
                                   filename: str = None) -> str:
        """
        Crea gráfico de radar para métricas de calidad
        """
        if not quality_data:
            return None
        
        # Datos para el radar
        categories = list(quality_data.keys())
        values = list(quality_data.values())
        
        # Normalizar valores a escala 0-100
        normalized_values = []
        for key, value in quality_data.items():
            if 'ratio' in key.lower() or 'rate' in key.lower():
                normalized_values.append(value * 100)
            else:
                normalized_values.append(min(value, 100))
        
        # Configurar ángulos para el radar
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        normalized_values += normalized_values[:1]  # Cerrar el círculo
        angles += angles[:1]
        
        # Crear gráfico
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        # Dibujar el radar
        ax.plot(angles, normalized_values, 'o-', linewidth=2, color=self.colors[0])
        ax.fill(angles, normalized_values, alpha=0.25, color=self.colors[0])
        
        # Configurar etiquetas
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_ylim(0, 100)
        
        # Título
        ax.set_title('Métricas de Calidad del Análisis', 
                    fontsize=16, fontweight='bold', pad=30)
        
        # Agregar valores
        for angle, value, category in zip(angles[:-1], normalized_values[:-1], categories):
            ax.text(angle, value + 5, f'{value:.1f}%', 
                   ha='center', va='center', fontweight='bold')
        
        plt.tight_layout()
        
        # Guardar archivo
        filename = filename or f"quality_radar_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_text_complexity_histogram(self, complexity_data: Dict[str, float], 
                                       filename: str = None) -> str:
        """
        Crea histograma para análisis de complejidad
        """
        if not complexity_data:
            return None
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Datos para el histograma
        metrics = list(complexity_data.keys())
        values = list(complexity_data.values())
        
        # Crear gráfico de barras horizontales
        bars = ax.barh(metrics, values, color=self.colors[:len(metrics)])
        
        # Configurar apariencia
        ax.set_title('Análisis de Complejidad del Texto', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Valor de Complejidad')
        
        # Agregar valores en las barras
        for bar, value in zip(bars, values):
            ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                   f'{value:.3f}', ha='left', va='center', fontweight='bold')
        
        plt.tight_layout()
        
        # Guardar archivo
        filename = filename or f"complexity_histogram_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_comparative_timeline(self, history_data: List[Dict], 
                                  filename: str = None) -> str:
        """
        Crea gráfico de línea temporal para análisis comparativo
        """
        if len(history_data) < 2:
            return None
        
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
        
        # Extraer datos temporales
        timestamps = [data['timestamp'][:10] for data in history_data]  # Solo fecha
        accuracies = [data['quality_metrics']['accuracy'] for data in history_data]
        complexities = [data['complexity_analysis'].get('complexity_index', 0) for data in history_data]
        token_counts = [data['token_analysis'].get('total_tokens', 0) for data in history_data]
        
        # Gráfico 1: Precisión a lo largo del tiempo
        ax1.plot(timestamps, accuracies, 'o-', color=self.colors[0], linewidth=2, markersize=6)
        ax1.set_title('Evolución de la Precisión', fontweight='bold')
        ax1.set_ylabel('Precisión (%)')
        ax1.grid(True, alpha=0.3)
        
        # Gráfico 2: Complejidad a lo largo del tiempo
        ax2.plot(timestamps, complexities, 's-', color=self.colors[1], linewidth=2, markersize=6)
        ax2.set_title('Evolución de la Complejidad', fontweight='bold')
        ax2.set_ylabel('Índice de Complejidad')
        ax2.grid(True, alpha=0.3)
        
        # Gráfico 3: Volumen de tokens a lo largo del tiempo
        ax3.bar(timestamps, token_counts, color=self.colors[2], alpha=0.7)
        ax3.set_title('Volumen de Tokens Procesados', fontweight='bold')
        ax3.set_ylabel('Cantidad de Tokens')
        ax3.set_xlabel('Fecha')
        
        # Rotar etiquetas del eje x
        for ax in [ax1, ax2, ax3]:
            ax.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        # Guardar archivo
        filename = filename or f"timeline_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_pattern_heatmap(self, pattern_metrics: Dict[str, Dict], 
                              filename: str = None) -> str:
        """
        Crea mapa de calor para métricas de patrones
        """
        if not pattern_metrics:
            return None
        
        # Preparar datos para el heatmap
        patterns = list(pattern_metrics.keys())
        metrics = ['count', 'percentage', 'avg_length', 'diversity']
        
        # Crear matriz de datos
        data_matrix = []
        for pattern in patterns:
            row = []
            for metric in metrics:
                value = pattern_metrics[pattern].get(metric, 0)
                row.append(value)
            data_matrix.append(row)
        
        # Normalizar datos por columna para mejor visualización
        data_matrix = np.array(data_matrix)
        for j in range(data_matrix.shape[1]):
            col_max = data_matrix[:, j].max()
            if col_max > 0:
                data_matrix[:, j] = data_matrix[:, j] / col_max
        
        # Crear heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        
        im = ax.imshow(data_matrix, cmap='YlOrRd', aspect='auto')
        
        # Configurar ejes
        ax.set_xticks(np.arange(len(metrics)))
        ax.set_yticks(np.arange(len(patterns)))
        ax.set_xticklabels(metrics)
        ax.set_yticklabels(patterns)
        
        # Rotar etiquetas
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        
        # Agregar valores en las celdas
        for i in range(len(patterns)):
            for j in range(len(metrics)):
                original_value = pattern_metrics[patterns[i]].get(metrics[j], 0)
                text = ax.text(j, i, f'{original_value:.1f}',
                             ha="center", va="center", color="black", fontweight='bold')
        
        ax.set_title("Mapa de Calor: Métricas por Patrón", fontsize=16, fontweight='bold')
        
        # Barra de color
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Intensidad Normalizada', rotation=270, labelpad=20)
        
        plt.tight_layout()
        
        # Guardar archivo
        filename = filename or f"pattern_heatmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_comprehensive_dashboard(self, stats_data: Dict[str, Any], 
                                     filename: str = None) -> str:
        """
        Crea un dashboard completo con múltiples visualizaciones
        """
        fig = plt.figure(figsize=(16, 12))
        
        # Configurar subplots
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # 1. Distribución de patrones (pie chart)
        ax1 = fig.add_subplot(gs[0, 0])
        pattern_data = stats_data.get('pattern_analysis', {}).get('pattern_distribution', {})
        if pattern_data:
            ax1.pie(pattern_data.values(), labels=pattern_data.keys(), 
                   autopct='%1.1f%%', colors=self.colors)
            ax1.set_title('Distribución de Patrones', fontweight='bold')
        
        # 2. Métricas de calidad (barras)
        ax2 = fig.add_subplot(gs[0, 1])
        quality_data = stats_data.get('quality_metrics', {})
        if quality_data:
            metrics = list(quality_data.keys())
            values = list(quality_data.values())
            ax2.bar(metrics, values, color=self.colors[1])
            ax2.set_title('Métricas de Calidad', fontweight='bold')
            ax2.tick_params(axis='x', rotation=45)
        
        # 3. Análisis de texto (información textual)
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.axis('off')
        text_data = stats_data.get('text_analysis', {})
        info_text = f"""Análisis de Texto:
        
Caracteres: {text_data.get('character_count', 0):,}
Palabras: {text_data.get('word_count', 0):,}
Líneas: {text_data.get('line_count', 0):,}
Ratio mayúsculas: {text_data.get('uppercase_ratio', 0):.1%}
Ratio dígitos: {text_data.get('digit_ratio', 0):.1%}"""
        ax3.text(0.1, 0.9, info_text, transform=ax3.transAxes, 
                verticalalignment='top', fontsize=10, fontfamily='monospace')
        
        # 4. Análisis de tokens (histograma)
        ax4 = fig.add_subplot(gs[1, :2])
        token_data = stats_data.get('token_analysis', {})
        if token_data:
            categories = ['Total', 'Válidos', 'Únicos']
            values = [
                token_data.get('total_tokens', 0),
                token_data.get('valid_token_count', 0),
                token_data.get('unique_tokens', 0)
            ]
            bars = ax4.bar(categories, values, color=self.colors[2:5])
            ax4.set_title('Análisis de Tokens', fontweight='bold')
            
            # Agregar valores
            for bar, value in zip(bars, values):
                ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                        str(value), ha='center', va='bottom', fontweight='bold')
        
        # 5. Métricas de rendimiento (radar simplificado)
        ax5 = fig.add_subplot(gs[1, 2])
        perf_data = stats_data.get('performance_metrics', {})
        if perf_data:
            metrics = list(perf_data.keys())
            values = [perf_data[m] * 100 for m in metrics]  # Escalar para visualización
            
            angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False)
            values += values[:1]
            angles = np.concatenate((angles, [angles[0]]))
            
            ax5 = plt.subplot(gs[1, 2], projection='polar')
            ax5.plot(angles, values, 'o-', color=self.colors[5])
            ax5.fill(angles, values, alpha=0.25, color=self.colors[5])
            ax5.set_xticks(angles[:-1])
            ax5.set_xticklabels(metrics)
            ax5.set_title('Rendimiento', fontweight='bold')
        
        # 6. Información de complejidad
        ax6 = fig.add_subplot(gs[2, :])
        complexity_data = stats_data.get('complexity_analysis', {})
        if complexity_data:
            comp_metrics = list(complexity_data.keys())
            comp_values = list(complexity_data.values())
            
            bars = ax6.barh(comp_metrics, comp_values, color=self.colors[6:])
            ax6.set_title('Análisis de Complejidad', fontweight='bold')
            ax6.set_xlabel('Valor')
            
            # Agregar valores
            for bar, value in zip(bars, comp_values):
                ax6.text(bar.get_width() + 0.001, bar.get_y() + bar.get_height()/2,
                        f'{value:.3f}', ha='left', va='center', fontweight='bold')
        
        # Título principal
        fig.suptitle('Dashboard de Análisis Léxico y Validación de Patrones', 
                    fontsize=18, fontweight='bold', y=0.95)
        
        # Guardar archivo
        filename = filename or f"dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def generate_all_graphs(self, stats_data: Dict[str, Any]) -> Dict[str, str]:
        """
        Genera todos los tipos de gráficos disponibles
        
        Returns:
            Dict con las rutas de los archivos generados
        """
        generated_files = {}
        
        try:
            # Distribución de patrones
            pattern_data = stats_data.get('pattern_analysis', {}).get('pattern_distribution', {})
            if pattern_data:
                generated_files['pattern_pie'] = self.create_pattern_distribution_pie(pattern_data)
            
            # Análisis de tokens
            token_data = stats_data.get('token_analysis', {})
            if token_data:
                generated_files['token_bar'] = self.create_token_analysis_bar(token_data)
            
            # Métricas de calidad
            quality_data = stats_data.get('quality_metrics', {})
            if quality_data:
                generated_files['quality_radar'] = self.create_quality_metrics_radar(quality_data)
            
            # Complejidad
            complexity_data = stats_data.get('complexity_analysis', {})
            if complexity_data:
                generated_files['complexity_hist'] = self.create_text_complexity_histogram(complexity_data)
            
            # Heatmap de patrones
            pattern_metrics = stats_data.get('pattern_analysis', {}).get('pattern_metrics', {})
            if pattern_metrics:
                generated_files['pattern_heatmap'] = self.create_pattern_heatmap(pattern_metrics)
            
            # Dashboard completo
            generated_files['dashboard'] = self.create_comprehensive_dashboard(stats_data)
            
        except Exception as e:
            print(f"Error generando gráficos: {e}")
        
        return generated_files