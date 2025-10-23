"""
Report Generator: Generación de reportes HTML y exportación de datos
"""

import json
import csv
from datetime import datetime
from typing import Dict, List, Any
import os
import base64


class ReportGenerator:
    """Generador de reportes en HTML y exportador de datos"""
    
    def __init__(self, output_dir: str = "data/outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_html_report(self, stats_data: Dict[str, Any], 
                           graph_files: Dict[str, str] = None,
                           filename: str = None) -> str:
        """
        Genera reporte completo en HTML
        
        Args:
            stats_data: Datos estadísticos del análisis
            graph_files: Diccionario con rutas de archivos de gráficos
            filename: Nombre del archivo HTML
        
        Returns:
            str: Ruta del archivo HTML generado
        """
        
        # Template HTML
        html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Análisis Léxico - ProyectoTLF</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .section {{
            background: white;
            margin: 25px 0;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .section h2 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}
        
        .section h3 {{
            color: #764ba2;
            margin: 20px 0 15px 0;
            font-size: 1.3em;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .stat-card {{
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .stat-card h4 {{
            color: #8b4513;
            margin-bottom: 10px;
            font-size: 0.95em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .stat-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #d2691e;
        }}
        
        .graph-container {{
            text-align: center;
            margin: 20px 0;
        }}
        
        .graph-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .pattern-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        
        .pattern-table th,
        .pattern-table td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        
        .pattern-table th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
        }}
        
        .pattern-table tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        .pattern-table tr:hover {{
            background-color: #f5f5f5;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
        
        .highlight {{
            background: linear-gradient(120deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }}
        
        .quality-indicator {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            color: white;
            font-weight: bold;
            margin: 5px;
        }}
        
        .quality-excellent {{ background-color: #28a745; }}
        .quality-good {{ background-color: #17a2b8; }}
        .quality-average {{ background-color: #ffc107; color: #333; }}
        .quality-poor {{ background-color: #dc3545; }}
        
        @media (max-width: 768px) {{
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .container {{
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Reporte de Análisis Léxico</h1>
            <p>Sistema de Validación de Patrones - Universidad del Quindío</p>
            <p><strong>Fecha:</strong> {timestamp}</p>
        </div>
        
        <div class="section">
            <h2>📋 Resumen Ejecutivo</h2>
            <div class="highlight">
                <strong>Análisis completado:</strong> Se procesaron <strong>{total_tokens}</strong> tokens 
                con una precisión del <strong>{accuracy:.1f}%</strong>. 
                Se detectaron <strong>{pattern_variety}</strong> tipos de patrones diferentes 
                en un texto de <strong>{character_count:,}</strong> caracteres.
            </div>
        </div>
        
        <div class="section">
            <h2>📈 Métricas Principales</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h4>Total de Tokens</h4>
                    <div class="value">{total_tokens:,}</div>
                </div>
                <div class="stat-card">
                    <h4>Tokens Válidos</h4>
                    <div class="value">{valid_tokens:,}</div>
                </div>
                <div class="stat-card">
                    <h4>Precisión</h4>
                    <div class="value">{accuracy:.1f}%</div>
                </div>
                <div class="stat-card">
                    <h4>Patrones Detectados</h4>
                    <div class="value">{pattern_variety}</div>
                </div>
                <div class="stat-card">
                    <h4>Complejidad</h4>
                    <div class="value">{complexity_index:.2f}</div>
                </div>
                <div class="stat-card">
                    <h4>Score de Calidad</h4>
                    <div class="value">{quality_score:.1f}</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>🎯 Indicadores de Calidad</h2>
            <p>
                <span class="quality-indicator {quality_class}">{quality_text}</span>
                <span class="quality-indicator {accuracy_class}">Precisión: {accuracy:.1f}%</span>
                <span class="quality-indicator {complexity_class}">Complejidad: {complexity_level}</span>
            </p>
        </div>
        
        {graphs_section}
        
        <div class="section">
            <h2>📝 Análisis Detallado del Texto</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h4>Caracteres</h4>
                    <div class="value">{character_count:,}</div>
                </div>
                <div class="stat-card">
                    <h4>Palabras</h4>
                    <div class="value">{word_count:,}</div>
                </div>
                <div class="stat-card">
                    <h4>Líneas</h4>
                    <div class="value">{line_count:,}</div>
                </div>
                <div class="stat-card">
                    <h4>Longitud Promedio</h4>
                    <div class="value">{avg_word_length:.1f}</div>
                </div>
                <div class="stat-card">
                    <h4>Ratio Mayúsculas</h4>
                    <div class="value">{uppercase_ratio:.1%}</div>
                </div>
                <div class="stat-card">
                    <h4>Diversidad Léxica</h4>
                    <div class="value">{lexical_diversity:.3f}</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>🔍 Patrones Detectados</h2>
            {patterns_table}
        </div>
        
        <div class="section">
            <h2>⚡ Métricas de Rendimiento</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h4>Tokens por Carácter</h4>
                    <div class="value">{tokens_per_character:.3f}</div>
                </div>
                <div class="stat-card">
                    <h4>Cobertura</h4>
                    <div class="value">{coverage_ratio:.1%}</div>
                </div>
                <div class="stat-card">
                    <h4>Eficiencia</h4>
                    <div class="value">{processing_efficiency:.1f}</div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>ProyectoTLF</strong> - Sistema de Análisis Léxico y Validación de Patrones</p>
            <p>Universidad del Quindío - Teoría de Lenguajes Formales - 2025</p>
            <p>Desarrollado por: Diego Carvajal, Nicolás Jurado, Johan Londoño</p>
        </div>
    </div>
</body>
</html>
        """
        
        # Extraer datos de las estadísticas
        text_data = stats_data.get('text_analysis', {})
        token_data = stats_data.get('token_analysis', {})
        pattern_data = stats_data.get('pattern_analysis', {})
        quality_data = stats_data.get('quality_metrics', {})
        complexity_data = stats_data.get('complexity_analysis', {})
        performance_data = stats_data.get('performance_metrics', {})
        
        # Calcular indicadores de calidad
        accuracy = quality_data.get('accuracy', 0)
        quality_score = quality_data.get('quality_score', 0)
        complexity_index = complexity_data.get('complexity_index', 0)
        
        # Determinar clases CSS para indicadores
        quality_class, quality_text = self._get_quality_indicator(quality_score)
        accuracy_class = self._get_accuracy_class(accuracy)
        complexity_class, complexity_level = self._get_complexity_indicator(complexity_index)
        
        # Generar tabla de patrones
        patterns_table = self._generate_patterns_table(pattern_data.get('pattern_metrics', {}))
        
        # Generar sección de gráficos
        graphs_section = self._generate_graphs_section(graph_files) if graph_files else ""
        
        # Formatear el HTML
        html_content = html_template.format(
            timestamp=datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            total_tokens=token_data.get('total_tokens', 0),
            valid_tokens=token_data.get('valid_token_count', 0),
            accuracy=accuracy,
            pattern_variety=pattern_data.get('pattern_variety', 0),
            character_count=text_data.get('character_count', 0),
            complexity_index=complexity_index,
            quality_score=quality_score,
            quality_class=quality_class,
            quality_text=quality_text,
            accuracy_class=accuracy_class,
            complexity_class=complexity_class,
            complexity_level=complexity_level,
            word_count=text_data.get('word_count', 0),
            line_count=text_data.get('line_count', 0),
            avg_word_length=text_data.get('avg_word_length', 0),
            uppercase_ratio=text_data.get('uppercase_ratio', 0),
            lexical_diversity=complexity_data.get('lexical_diversity', 0),
            tokens_per_character=performance_data.get('tokens_per_character', 0),
            coverage_ratio=performance_data.get('coverage_ratio', 0),
            processing_efficiency=performance_data.get('processing_efficiency', 0),
            patterns_table=patterns_table,
            graphs_section=graphs_section
        )
        
        # Guardar archivo
        filename = filename or f"reporte_analisis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
    
    def _get_quality_indicator(self, quality_score: float) -> tuple:
        """Determina el indicador de calidad basado en el score"""
        if quality_score >= 80:
            return "quality-excellent", "Excelente"
        elif quality_score >= 65:
            return "quality-good", "Bueno"
        elif quality_score >= 45:
            return "quality-average", "Regular"
        else:
            return "quality-poor", "Deficiente"
    
    def _get_accuracy_class(self, accuracy: float) -> str:
        """Determina la clase CSS para la precisión"""
        if accuracy >= 80:
            return "quality-excellent"
        elif accuracy >= 65:
            return "quality-good"
        elif accuracy >= 45:
            return "quality-average"
        else:
            return "quality-poor"
    
    def _get_complexity_indicator(self, complexity_index: float) -> tuple:
        """Determina el indicador de complejidad"""
        if complexity_index >= 0.8:
            return "quality-poor", "Muy Alta"
        elif complexity_index >= 0.6:
            return "quality-average", "Alta"
        elif complexity_index >= 0.4:
            return "quality-good", "Media"
        else:
            return "quality-excellent", "Baja"
    
    def _generate_patterns_table(self, pattern_metrics: Dict[str, Dict]) -> str:
        """Genera tabla HTML de patrones detectados"""
        if not pattern_metrics:
            return "<p>No se detectaron patrones válidos.</p>"
        
        table_html = """
        <table class="pattern-table">
            <thead>
                <tr>
                    <th>Patrón</th>
                    <th>Cantidad</th>
                    <th>Porcentaje</th>
                    <th>Longitud Promedio</th>
                    <th>Valores Únicos</th>
                    <th>Diversidad</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for pattern_name, metrics in pattern_metrics.items():
            table_html += f"""
                <tr>
                    <td><strong>{pattern_name.upper()}</strong></td>
                    <td>{metrics.get('count', 0)}</td>
                    <td>{metrics.get('percentage', 0):.1f}%</td>
                    <td>{metrics.get('avg_length', 0):.1f}</td>
                    <td>{metrics.get('unique_values', 0)}</td>
                    <td>{metrics.get('diversity', 0):.3f}</td>
                </tr>
            """
        
        table_html += """
            </tbody>
        </table>
        """
        
        return table_html
    
    def _generate_graphs_section(self, graph_files: Dict[str, str]) -> str:
        """Genera sección HTML con gráficos embebidos"""
        if not graph_files:
            return ""
        
        section_html = """
        <div class="section">
            <h2>📊 Visualizaciones</h2>
        """
        
        graph_titles = {
            'dashboard': 'Dashboard Completo',
            'pattern_pie': 'Distribución de Patrones',
            'token_bar': 'Análisis de Tokens',
            'quality_radar': 'Métricas de Calidad',
            'complexity_hist': 'Análisis de Complejidad',
            'pattern_heatmap': 'Mapa de Calor de Patrones'
        }
        
        for graph_type, filepath in graph_files.items():
            if filepath and os.path.exists(filepath):
                title = graph_titles.get(graph_type, graph_type.replace('_', ' ').title())
                
                # Convertir imagen a base64 para embedder en HTML
                try:
                    with open(filepath, 'rb') as img_file:
                        img_data = base64.b64encode(img_file.read()).decode()
                    
                    section_html += f"""
                    <div class="graph-container">
                        <h3>{title}</h3>
                        <img src="data:image/png;base64,{img_data}" alt="{title}">
                    </div>
                    """
                except Exception as e:
                    section_html += f"""
                    <div class="graph-container">
                        <h3>{title}</h3>
                        <p>Error cargando gráfico: {str(e)}</p>
                    </div>
                    """
        
        section_html += "</div>"
        return section_html
    
    def export_json(self, data: Dict[str, Any], filename: str = None) -> str:
        """Exporta datos a JSON"""
        filename = filename or f"analisis_datos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        return filepath
    
    def export_csv(self, data: Dict[str, Any], filename: str = None) -> str:
        """Exporta datos principales a CSV"""
        filename = filename or f"analisis_resumen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = os.path.join(self.output_dir, filename)
        
        # Extraer datos principales para CSV
        csv_data = []
        
        # Información general
        text_data = data.get('text_analysis', {})
        token_data = data.get('token_analysis', {})
        quality_data = data.get('quality_metrics', {})
        complexity_data = data.get('complexity_analysis', {})
        
        csv_row = {
            'timestamp': data.get('timestamp', ''),
            'caracteres': text_data.get('character_count', 0),
            'palabras': text_data.get('word_count', 0),
            'lineas': text_data.get('line_count', 0),
            'total_tokens': token_data.get('total_tokens', 0),
            'tokens_validos': token_data.get('valid_token_count', 0),
            'precision': quality_data.get('accuracy', 0),
            'score_calidad': quality_data.get('quality_score', 0),
            'indice_complejidad': complexity_data.get('complexity_index', 0),
            'diversidad_lexica': complexity_data.get('lexical_diversity', 0)
        }
        
        # Agregar información de patrones
        pattern_data = data.get('pattern_analysis', {}).get('pattern_metrics', {})
        for pattern_name, metrics in pattern_data.items():
            csv_row[f'patron_{pattern_name}_cantidad'] = metrics.get('count', 0)
            csv_row[f'patron_{pattern_name}_porcentaje'] = metrics.get('percentage', 0)
        
        csv_data.append(csv_row)
        
        # Escribir CSV
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            if csv_data:
                writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
                writer.writeheader()
                writer.writerows(csv_data)
        
        return filepath