"""
Ventana Principal del Sistema de Análisis Léxico
Universidad del Quindío - Teoría de Lenguajes Formales

Esta clase implementa la ventana principal de la aplicación con PyQt5
"""

import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QTabWidget, QMenuBar, QToolBar, QStatusBar,
                             QAction, QTextEdit, QLabel, QPushButton, 
                             QSplitter, QGroupBox, QScrollArea, QFrame,
                             QMessageBox, QFileDialog, QProgressBar)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette

# Importar módulos existentes del proyecto
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.core.controller import TextController
from src.core.model import TextModel
from src.analysis.statistics import StatisticsAnalyzer
from src.visualization.graphs import GraphGenerator

class MainWindow(QMainWindow):
    """Ventana principal de la aplicación GUI"""
    
    def __init__(self):
        super().__init__()
        self.controller = TextController()
        self.statistics_analyzer = StatisticsAnalyzer()
        self.graph_generator = GraphGenerator()
        self.current_text = ""
        self.current_analysis = None
        
        self.init_ui()
        self.load_styles()
        
    def init_ui(self):
        """Inicializar la interfaz de usuario"""
        self.setWindowTitle("Sistema de Análisis Léxico - Universidad del Quindío")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(800, 600)
        
        # Crear widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout(central_widget)
        
        # Crear splitter principal
        main_splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(main_splitter)
        
        # Panel izquierdo - Entrada de texto y controles
        left_panel = self.create_left_panel()
        main_splitter.addWidget(left_panel)
        
        # Panel derecho - Resultados y visualizaciones
        right_panel = self.create_right_panel()
        main_splitter.addWidget(right_panel)
        
        # Configurar proporciones del splitter
        main_splitter.setSizes([400, 800])
        
        # Crear menú, toolbar y barra de estado
        self.create_menu_bar()
        self.create_tool_bar()
        self.create_status_bar()
        
        # Conectar señales
        self.connect_signals()
        
    def create_left_panel(self):
        """Crear panel izquierdo con controles de entrada"""
        panel = QFrame()
        panel.setFrameStyle(QFrame.Box)
        layout = QVBoxLayout(panel)
        
        # Grupo de entrada de texto
        input_group = QGroupBox("📝 Entrada de Texto")
        input_layout = QVBoxLayout(input_group)
        
        # Área de texto para entrada
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText(
            "Ingrese el texto a analizar aquí...\n\n"
            "Ejemplo:\n"
            "juan.perez@uqvirtual.edu.co\n"
            "310-555-1234\n"
            "2025-10-22\n"
            "192.168.1.1"
        )
        self.text_input.setMinimumHeight(200)
        input_layout.addWidget(self.text_input)
        
        # Botones de acción
        buttons_layout = QHBoxLayout()
        
        self.analyze_btn = QPushButton("🔍 Analizar Texto")
        self.analyze_btn.setObjectName("analyzeButton")
        buttons_layout.addWidget(self.analyze_btn)
        
        self.clear_btn = QPushButton("🗑️ Limpiar")
        self.clear_btn.setObjectName("clearButton")
        buttons_layout.addWidget(self.clear_btn)
        
        input_layout.addLayout(buttons_layout)
        layout.addWidget(input_group)
        
        # Grupo de opciones de análisis
        options_group = QGroupBox("⚙️ Opciones de Análisis")
        options_layout = QVBoxLayout(options_group)
        
        # Botones de funcionalidades específicas
        self.stats_btn = QPushButton("📊 Generar Estadísticas")
        self.stats_btn.setObjectName("statsButton")
        options_layout.addWidget(self.stats_btn)
        
        self.graphs_btn = QPushButton("📈 Generar Gráficos")
        self.graphs_btn.setObjectName("graphsButton")
        options_layout.addWidget(self.graphs_btn)
        
        self.export_btn = QPushButton("💾 Exportar Reporte")
        self.export_btn.setObjectName("exportButton")
        options_layout.addWidget(self.export_btn)
        
        layout.addWidget(options_group)
        
        # Barra de progreso
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Spacer para empujar elementos hacia arriba
        layout.addStretch()
        
        return panel
        
    def create_right_panel(self):
        """Crear panel derecho con resultados"""
        panel = QFrame()
        panel.setFrameStyle(QFrame.Box)
        
        # Usar tabs para organizar diferentes vistas
        self.tab_widget = QTabWidget()
        
        # Importar widgets especializados
        from .widgets.statistics_widgets import StatisticsPanel, ResultsViewer
        from .widgets.graph_widgets import GraphsPanel
        
        # Tab 1: Resultados del análisis - Usar widget especializado
        self.results_viewer = ResultsViewer()
        self.tab_widget.addTab(self.results_viewer, "📋 Resultados")
        
        # Tab 2: Estadísticas - Usar widget especializado
        self.statistics_panel = StatisticsPanel()
        self.statistics_panel.refresh_requested.connect(self.generate_statistics)
        self.tab_widget.addTab(self.statistics_panel, "📊 Estadísticas")
        
        # Tab 3: Visualizaciones - Usar widget especializado
        self.graphs_panel = GraphsPanel()
        self.tab_widget.addTab(self.graphs_panel, "📈 Gráficos")
        
        # Tab 4: Exportar
        export_tab = self.create_export_tab()
        self.tab_widget.addTab(export_tab, "💾 Exportar")
        
        layout = QVBoxLayout(panel)
        layout.addWidget(self.tab_widget)
        
        return panel
        

        
    def create_export_tab(self):
        """Crear tab de exportación"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Opciones de exportación
        export_group = QGroupBox("💾 Opciones de Exportación")
        export_layout = QVBoxLayout(export_group)
        
        self.export_html_btn = QPushButton("📄 Exportar como HTML")
        self.export_html_btn.setObjectName("exportHtmlButton")
        export_layout.addWidget(self.export_html_btn)
        
        self.export_json_btn = QPushButton("📋 Exportar como JSON")
        self.export_json_btn.setObjectName("exportJsonButton")
        export_layout.addWidget(self.export_json_btn)
        
        self.export_csv_btn = QPushButton("📊 Exportar como CSV")
        self.export_csv_btn.setObjectName("exportCsvButton")
        export_layout.addWidget(self.export_csv_btn)
        
        layout.addWidget(export_group)
        layout.addStretch()
        
        return widget
        
    def create_menu_bar(self):
        """Crear barra de menú"""
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu('📁 Archivo')
        
        open_action = QAction('🔓 Abrir Texto', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction('💾 Guardar Análisis', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_analysis)
        file_menu.addAction(save_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction('❌ Salir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Menú Análisis
        analysis_menu = menubar.addMenu('🔍 Análisis')
        
        analyze_action = QAction('🔍 Analizar Texto', self)
        analyze_action.setShortcut('F5')
        analyze_action.triggered.connect(self.analyze_text)
        analysis_menu.addAction(analyze_action)
        
        stats_action = QAction('📊 Generar Estadísticas', self)
        stats_action.triggered.connect(self.generate_statistics)
        analysis_menu.addAction(stats_action)
        
        graphs_action = QAction('📈 Generar Gráficos', self)
        graphs_action.triggered.connect(self.generate_graphs)
        analysis_menu.addAction(graphs_action)
        
        # Menú Ayuda
        help_menu = menubar.addMenu('❓ Ayuda')
        
        about_action = QAction('ℹ️ Acerca de', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def create_tool_bar(self):
        """Crear barra de herramientas"""
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Acciones principales
        analyze_action = QAction('🔍 Analizar', self)
        analyze_action.triggered.connect(self.analyze_text)
        toolbar.addAction(analyze_action)
        
        toolbar.addSeparator()
        
        stats_action = QAction('📊 Stats', self)
        stats_action.triggered.connect(self.generate_statistics)
        toolbar.addAction(stats_action)
        
        graphs_action = QAction('📈 Gráficos', self)
        graphs_action.triggered.connect(self.generate_graphs)
        toolbar.addAction(graphs_action)
        
        toolbar.addSeparator()
        
        export_action = QAction('💾 Exportar', self)
        export_action.triggered.connect(self.export_html)
        toolbar.addAction(export_action)
        
    def create_status_bar(self):
        """Crear barra de estado"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("✅ Listo para analizar texto")
        
    def connect_signals(self):
        """Conectar señales de la interfaz"""
        self.analyze_btn.clicked.connect(self.analyze_text)
        self.clear_btn.clicked.connect(self.clear_text)
        self.stats_btn.clicked.connect(self.generate_statistics)
        self.graphs_btn.clicked.connect(self.generate_graphs)
        self.export_btn.clicked.connect(self.export_html)
        
        # Botones de exportación
        self.export_html_btn.clicked.connect(self.export_html)
        self.export_json_btn.clicked.connect(self.export_json)
        self.export_csv_btn.clicked.connect(self.export_csv)
        
    def load_styles(self):
        """Cargar estilos CSS"""
        try:
            styles_path = os.path.join(os.path.dirname(__file__), 'styles', 'main.css')
            if os.path.exists(styles_path):
                with open(styles_path, 'r', encoding='utf-8') as f:
                    self.setStyleSheet(f.read())
            else:
                # Estilos básicos si no existe el archivo CSS
                self.setStyleSheet(self.get_default_styles())
        except Exception as e:
            print(f"Error cargando estilos: {e}")
            self.setStyleSheet(self.get_default_styles())
            
    def get_default_styles(self):
        """Obtener estilos por defecto"""
        return """
        QMainWindow {
            background-color: #f5f5f5;
        }
        QGroupBox {
            font-weight: bold;
            border: 2px solid #cccccc;
            border-radius: 8px;
            margin-top: 1ex;
            padding-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #3d8b40;
        }
        """
        
    def analyze_text(self):
        """Analizar el texto ingresado"""
        try:
            self.current_text = self.text_input.toPlainText().strip()
            
            if not self.current_text:
                QMessageBox.warning(self, "Advertencia", "Por favor ingrese texto para analizar")
                return
                
            self.status_bar.showMessage("🔄 Analizando texto...")
            self.progress_bar.setVisible(True)
            self.progress_bar.setRange(0, 0)  # Indeterminado
            
            # Realizar análisis usando el controlador existente
            self.controller.model.set_text(self.current_text)  # Esto dispara el análisis automáticamente
            results = self.controller.model.analyze_text_for_all_patterns()
            
            # Mostrar resultados
            self.display_results(results)
            
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage("✅ Análisis completado")
            
        except Exception as e:
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage("❌ Error en el análisis")
            QMessageBox.critical(self, "Error", f"Error durante el análisis: {str(e)}")
            
    def display_results(self, results):
        """Mostrar resultados del análisis"""
        # Usar el widget especializado para mostrar resultados
        self.results_viewer.display_results(results)
        self.current_analysis = results
        
    def generate_statistics(self):
        """Generar estadísticas del análisis"""
        if not self.current_text:
            QMessageBox.warning(self, "Advertencia", "Primero debe analizar un texto")
            return
            
        try:
            self.status_bar.showMessage("📊 Generando estadísticas...")
            
            # Generar estadísticas usando el analizador existente
            tokens = self.controller.model.tokens if hasattr(self.controller.model, 'tokens') else []
            analysis_stats = self.controller.model.analysis_results if hasattr(self.controller.model, 'analysis_results') else {}
            
            # Generar estadísticas básicas directamente si no hay tokens
            if len(tokens) == 0 and self.current_text:
                stats = self._generate_basic_stats(self.current_text, self.current_analysis)
            else:
                # Generar estadísticas completas con el analizador
                raw_stats = self.statistics_analyzer.analyze_results(tokens, self.current_text, analysis_stats)
                
                # Mapear las estadísticas complejas a formato simple para la GUI
                stats = self._map_complex_stats_to_gui_format(raw_stats)
            
            # Agregar distribución de patrones si hay análisis actual
            if self.current_analysis:
                pattern_dist = {}
                for pattern_name, matches in self.current_analysis.items():
                    pattern_dist[pattern_name] = len(matches) if matches else 0
                stats['pattern_distribution'] = pattern_dist
            
            # Actualizar panel de estadísticas
            self.statistics_panel.update_statistics(stats)
            
            # También generar gráficos de estadísticas
            self.graphs_panel.generate_statistics_graphs(stats)
            
            # Cambiar a la pestaña de estadísticas
            self.tab_widget.setCurrentIndex(1)
            
            self.status_bar.showMessage("✅ Estadísticas generadas")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generando estadísticas: {str(e)}")
            

        
    def generate_graphs(self):
        """Generar gráficos del análisis"""
        if not self.current_analysis:
            QMessageBox.warning(self, "Advertencia", "Primero debe analizar un texto")
            return
            
        try:
            self.status_bar.showMessage("📈 Generando gráficos...")
            
            # Generar gráficos usando el panel especializado
            self.graphs_panel.generate_standard_graphs(self.current_analysis)
            
            # Cambiar a la pestaña de gráficos
            self.tab_widget.setCurrentIndex(2)
            
            self.status_bar.showMessage("✅ Gráficos generados")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generando gráficos: {str(e)}")
            
    def clear_text(self):
        """Limpiar texto y resultados"""
        self.text_input.clear()
        # Limpiar resultados usando el widget especializado
        self.results_viewer.display_results({})
        # Limpiar estadísticas
        self.statistics_panel.update_statistics({})
        # Limpiar gráficos
        self.graphs_panel.clear_graphs()
        # Resetear variables
        self.current_text = ""
        self.current_analysis = None
        self.status_bar.showMessage("🗑️ Texto limpiado")
        
    def open_file(self):
        """Abrir archivo de texto"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo de texto", "", 
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.text_input.setText(content)
                    self.status_bar.showMessage(f"📁 Archivo cargado: {os.path.basename(file_path)}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al abrir archivo: {str(e)}")
                
    def save_analysis(self):
        """Guardar análisis actual"""
        if not self.current_analysis:
            QMessageBox.warning(self, "Advertencia", "No hay análisis para guardar")
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar análisis", "analisis.txt", 
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.results_text.toPlainText())
                    self.status_bar.showMessage(f"💾 Análisis guardado: {os.path.basename(file_path)}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al guardar: {str(e)}")
                
    def export_html(self):
        """Exportar como HTML"""
        if not self.current_analysis:
            QMessageBox.warning(self, "Advertencia", "No hay análisis para exportar")
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Exportar como HTML", "reporte.html", 
            "Archivos HTML (*.html);;Todos los archivos (*)"
        )
        
        if file_path:
            try:
                # Usar el generador de reportes existente
                from src.visualization.reports import ReportGenerator
                report_gen = ReportGenerator()
                
                # Generar datos para el reporte
                # Generar datos para el reporte
                tokens = self.controller.model.tokens if hasattr(self.controller.model, 'tokens') else []
                analysis_stats = self.controller.model.analysis_results if hasattr(self.controller.model, 'analysis_results') else {}
                
                if len(tokens) == 0 and self.current_text:
                    stats = self._generate_basic_stats(self.current_text, self.current_analysis)
                else:
                    stats = self.statistics_analyzer.analyze_results(tokens, self.current_text, analysis_stats)
                
                analysis_data = {
                    'text': self.current_text,
                    'results': self.current_analysis,
                    'statistics': stats
                }
                
                report_gen.generate_html_report(analysis_data, file_path)
                self.status_bar.showMessage(f"📄 HTML exportado: {os.path.basename(file_path)}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error exportando HTML: {str(e)}")
                
    def export_json(self):
        """Exportar como JSON"""
        if not self.current_analysis:
            QMessageBox.warning(self, "Advertencia", "No hay análisis para exportar")
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Exportar como JSON", "datos.json", 
            "Archivos JSON (*.json);;Todos los archivos (*)"
        )
        
        if file_path:
            try:
                import json
                # Generar estadísticas para exportación
                tokens = self.controller.model.tokens if hasattr(self.controller.model, 'tokens') else []
                analysis_stats = self.controller.model.analysis_results if hasattr(self.controller.model, 'analysis_results') else {}
                
                if len(tokens) == 0 and self.current_text:
                    stats = self._generate_basic_stats(self.current_text, self.current_analysis)
                else:
                    stats = self.statistics_analyzer.analyze_results(tokens, self.current_text, analysis_stats)
                
                data = {
                    'texto': self.current_text,
                    'resultados': self.current_analysis,
                    'estadisticas': stats,
                    'fecha_analisis': str(os.path.getmtime(file_path)) if os.path.exists(file_path) else "N/A"
                }
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    
                self.status_bar.showMessage(f"📋 JSON exportado: {os.path.basename(file_path)}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error exportando JSON: {str(e)}")
                
    def export_csv(self):
        """Exportar como CSV"""
        if not self.current_analysis:
            QMessageBox.warning(self, "Advertencia", "No hay análisis para exportar")
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Exportar como CSV", "datos.csv", 
            "Archivos CSV (*.csv);;Todos los archivos (*)"
        )
        
        if file_path:
            try:
                import csv
                
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Patrón', 'Coincidencia', 'Posición'])
                    
                    for pattern_name, matches in self.current_analysis.items():
                        for i, match in enumerate(matches):
                            writer.writerow([pattern_name, match, i+1])
                            
                self.status_bar.showMessage(f"📊 CSV exportado: {os.path.basename(file_path)}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error exportando CSV: {str(e)}")
                
    def _generate_basic_stats(self, text: str, analysis_results: dict = None) -> dict:
        """Generar estadísticas básicas cuando no hay tokens disponibles"""
        import re
        
        # Estadísticas básicas del texto
        text_length = len(text)
        word_count = len(text.split()) if text.strip() else 0
        line_count = len(text.splitlines())
        
        # Contar patrones manualmente si hay resultados de análisis
        pattern_count = 0
        pattern_distribution = {}
        
        if analysis_results:
            for pattern_name, matches in analysis_results.items():
                if matches:
                    count = len(matches)
                    pattern_count += count
                    pattern_distribution[pattern_name] = count
        
        # Calcular métricas básicas
        char_diversity = len(set(text.lower())) / max(len(text), 1) if text else 0
        avg_word_length = sum(len(word) for word in text.split()) / max(word_count, 1) if word_count > 0 else 0
        
        # Complejidad básica (basada en variedad de caracteres y longitud)
        complexity_score = min((char_diversity * avg_word_length * 0.1), 10.0)
        
        # Entropía simple (variedad de caracteres)
        entropy = char_diversity * 3.0  # Aproximación simple
        
        # Diversidad léxica (palabras únicas / total palabras)
        unique_words = len(set(text.lower().split())) if text.strip() else 0
        lexical_diversity = unique_words / max(word_count, 1) if word_count > 0 else 0
        
        # Score de calidad (basado en longitud, patrones encontrados y diversidad)
        quality_score = min((
            (text_length / 1000 * 20) +  # Puntos por longitud
            (pattern_count * 10) +       # Puntos por patrones
            (lexical_diversity * 30) +   # Puntos por diversidad
            (complexity_score * 5)       # Puntos por complejidad
        ), 100.0)
        
        return {
            'text_length': text_length,
            'word_count': word_count,
            'line_count': line_count,
            'pattern_count': pattern_count,
            'pattern_distribution': pattern_distribution,
            'complexity_score': complexity_score,
            'entropy': entropy,
            'lexical_diversity': lexical_diversity,
            'quality_score': quality_score,
            'char_diversity': char_diversity,
            'avg_word_length': avg_word_length,
            'unique_words': unique_words
        }
        
    def _map_complex_stats_to_gui_format(self, raw_stats):
        """Mapear estadísticas complejas al formato simple que espera la GUI"""
        # Extraer datos del formato complejo
        text_analysis = raw_stats.get('text_analysis', {})
        token_analysis = raw_stats.get('token_analysis', {})
        pattern_analysis = raw_stats.get('pattern_analysis', {})
        quality_metrics = raw_stats.get('quality_metrics', {})
        
        # Crear formato simple para la GUI
        gui_stats = {
            # Estadísticas básicas de texto
            'text_length': text_analysis.get('character_count', 0),
            'word_count': text_analysis.get('word_count', 0),
            'line_count': text_analysis.get('line_count', 0),
            
            # Estadísticas de tokens
            'total_tokens': token_analysis.get('total_tokens', 0),
            'valid_tokens': token_analysis.get('valid_token_count', 0),
            'token_diversity': token_analysis.get('token_diversity', 0.0),
            
            # Estadísticas de patrones
            'total_patterns': sum(pattern_analysis.get('pattern_distribution', {}).values()),
            'pattern_distribution': pattern_analysis.get('pattern_distribution', {}),
            'pattern_variety': pattern_analysis.get('pattern_variety', 0),
            
            # Métricas de calidad
            'quality_score': quality_metrics.get('quality_score', 0.0),
            'accuracy': quality_metrics.get('accuracy', 0.0),
            'coverage_ratio': raw_stats.get('performance_metrics', {}).get('coverage_ratio', 0.0),
            
            # Análisis de frecuencias (simplificado)
            'character_frequency': {},
            'avg_word_length': text_analysis.get('avg_word_length', 0.0),
            'complexity_index': raw_stats.get('complexity_analysis', {}).get('complexity_index', 0.0)
        }
        
        return gui_stats
        
    def show_about(self):
        """Mostrar diálogo Acerca de"""
        QMessageBox.about(
            self, 
            "Acerca de - Sistema de Análisis Léxico",
            """
            <h3>Sistema de Análisis Léxico y Validación de Patrones</h3>
            <p><b>Universidad del Quindío</b><br>
            Teoría de Lenguajes Formales<br>
            2025</p>
            
            <p>Esta aplicación permite analizar texto usando expresiones regulares
            para identificar patrones como emails, teléfonos, fechas, IPs y más.</p>
            
            <p><b>Características:</b></p>
            <ul>
            <li>Análisis léxico avanzado</li>
            <li>Estadísticas detalladas</li>
            <li>Visualizaciones gráficas</li>
            <li>Exportación múltiple</li>
            </ul>
            
            <p><b>Versión:</b> 2.0.0 GUI</p>
            """
        )