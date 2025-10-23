"""
Widget especializado para mostrar estadísticas
Universidad del Quindío - Teoría de Lenguajes Formales
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QFrame, QScrollArea, QGridLayout, QProgressBar,
                             QPushButton, QGroupBox)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtSignal
from PyQt5.QtGui import QFont, QPalette

class StatisticCard(QFrame):
    """Tarjeta individual para mostrar una estadística"""
    
    def __init__(self, title, value, description="", color="#007bff"):
        super().__init__()
        self.setFrameStyle(QFrame.Box)
        self.setStyleSheet(f"""
            StatisticCard {{
                border: 2px solid #dee2e6;
                border-radius: 10px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #ffffff, stop: 1 #f8f9fa
                );
                padding: 12px;
                margin: 4px;
            }}
            StatisticCard:hover {{
                border-color: {color};
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
        """)
        
        layout = QVBoxLayout(self)
        
        # Título
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(f"""
            font-size: 12px;
            font-weight: 600;
            color: #6c757d;
            margin-bottom: 4px;
        """)
        layout.addWidget(title_label)
        
        # Valor principal
        value_label = QLabel(str(value))
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet(f"""
            font-size: 24px;
            font-weight: 700;
            color: {color};
            margin: 8px 0;
        """)
        layout.addWidget(value_label)
        
        # Descripción (opcional)
        if description:
            desc_label = QLabel(description)
            desc_label.setAlignment(Qt.AlignCenter)
            desc_label.setStyleSheet("""
                font-size: 10px;
                color: #868e96;
                margin-top: 4px;
            """)
            desc_label.setWordWrap(True)
            layout.addWidget(desc_label)


class ProgressStatCard(QFrame):
    """Tarjeta con barra de progreso para estadísticas porcentuales"""
    
    def __init__(self, title, value, max_value=100, color="#28a745"):
        super().__init__()
        self.setFrameStyle(QFrame.Box)
        self.setStyleSheet(f"""
            ProgressStatCard {{
                border: 2px solid #dee2e6;
                border-radius: 10px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #ffffff, stop: 1 #f8f9fa
                );
                padding: 12px;
                margin: 4px;
            }}
            ProgressStatCard:hover {{
                border-color: {color};
            }}
        """)
        
        layout = QVBoxLayout(self)
        
        # Título y valor
        header_layout = QHBoxLayout()
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 12px;
            font-weight: 600;
            color: #495057;
        """)
        header_layout.addWidget(title_label)
        
        value_label = QLabel(f"{value}/{max_value}")
        value_label.setAlignment(Qt.AlignRight)
        value_label.setStyleSheet(f"""
            font-size: 12px;
            font-weight: 700;
            color: {color};
        """)
        header_layout.addWidget(value_label)
        
        layout.addLayout(header_layout)
        
        # Barra de progreso
        progress_bar = QProgressBar()
        progress_bar.setMaximum(max_value)
        progress_bar.setValue(value)
        progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #dee2e6;
                border-radius: 6px;
                background: #f8f9fa;
                text-align: center;
                height: 8px;
            }}
            QProgressBar::chunk {{
                background: {color};
                border-radius: 4px;
            }}
        """)
        layout.addWidget(progress_bar)


class StatisticsPanel(QWidget):
    """Panel principal para mostrar todas las estadísticas"""
    
    refresh_requested = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz del panel"""
        layout = QVBoxLayout(self)
        
        # Header con título y botón de refresh
        header_layout = QHBoxLayout()
        
        title_label = QLabel("📊 Estadísticas del Análisis")
        title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: #212529;
            padding: 8px;
        """)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        refresh_btn = QPushButton("🔄 Actualizar")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background: #17a2b8;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #138496;
            }
        """)
        refresh_btn.clicked.connect(self.refresh_requested.emit)
        header_layout.addWidget(refresh_btn)
        
        layout.addLayout(header_layout)
        
        # Área scrollable para las estadísticas
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # Widget contenedor para las tarjetas
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        
        # Placeholder inicial
        self.placeholder_label = QLabel("📈 Ejecute un análisis para ver las estadísticas")
        self.placeholder_label.setAlignment(Qt.AlignCenter)
        self.placeholder_label.setStyleSheet("""
            color: #6c757d;
            font-size: 14px;
            padding: 40px;
            background: #f8f9fa;
            border: 2px dashed #dee2e6;
            border-radius: 8px;
            margin: 20px;
        """)
        self.content_layout.addWidget(self.placeholder_label)
        
        scroll_area.setWidget(self.content_widget)
        layout.addWidget(scroll_area)
        
    def update_statistics(self, stats_data):
        """Actualizar las estadísticas mostradas"""
        
        # Limpiar contenido anterior
        for i in reversed(range(self.content_layout.count())): 
            child = self.content_layout.itemAt(i).widget()
            if child:
                child.setParent(None)
        
        if not stats_data:
            self.content_layout.addWidget(self.placeholder_label)
            return
            
        # Estadísticas básicas
        basic_group = QGroupBox("📝 Estadísticas Básicas")
        basic_layout = QGridLayout(basic_group)
        
        basic_stats = [
            ("Caracteres", stats_data.get('text_length', 0), "Total de caracteres", "#007bff"),
            ("Palabras", stats_data.get('word_count', 0), "Número de palabras", "#28a745"),
            ("Líneas", stats_data.get('line_count', 0), "Líneas de texto", "#17a2b8"),
            ("Patrones", stats_data.get('total_patterns', 0), "Patrones encontrados", "#fd7e14")
        ]
        
        for i, (title, value, desc, color) in enumerate(basic_stats):
            card = StatisticCard(title, value, desc, color)
            basic_layout.addWidget(card, i // 2, i % 2)
            
        self.content_layout.addWidget(basic_group)
        
        # Estadísticas avanzadas
        advanced_group = QGroupBox("🔍 Análisis Avanzado")
        advanced_layout = QGridLayout(advanced_group)
        
        # Métricas de calidad (mapeadas desde diferentes campos)
        complexity = stats_data.get('complexity_index', stats_data.get('complexity_score', 0))
        entropy = stats_data.get('entropy', 0)
        diversity = stats_data.get('token_diversity', stats_data.get('lexical_diversity', 0))
        quality = stats_data.get('quality_score', 0)
        
        advanced_stats = [
            ("Complejidad", f"{complexity:.2f}", "Complejidad textual", "#6f42c1"),
            ("Entropía", f"{entropy:.3f}", "Entropía informacional", "#e83e8c"),
            ("Diversidad", f"{diversity:.3f}", "Diversidad léxica", "#20c997"),
            ("Calidad", f"{quality:.1f}/100", "Score de calidad", "#ffc107")
        ]
        
        for i, (title, value, desc, color) in enumerate(advanced_stats):
            card = StatisticCard(title, value, desc, color)
            advanced_layout.addWidget(card, i // 2, i % 2)
            
        self.content_layout.addWidget(advanced_group)
        
        # Barras de progreso para métricas porcentuales
        progress_group = QGroupBox("📊 Métricas de Rendimiento")
        progress_layout = QVBoxLayout(progress_group)
        
        # Calidad como progreso
        quality_progress = ProgressStatCard("Calidad del Texto", int(quality), 100, "#28a745")
        progress_layout.addWidget(quality_progress)
        
        # Diversidad como progreso (normalizada a 100)
        diversity_progress = ProgressStatCard("Diversidad Léxica", int(diversity * 100), 100, "#17a2b8")
        progress_layout.addWidget(diversity_progress)
        
        # Complejidad como progreso (normalizada)
        complexity_progress = ProgressStatCard("Complejidad", int(min(complexity * 10, 100)), 100, "#fd7e14")
        progress_layout.addWidget(complexity_progress)
        
        self.content_layout.addWidget(progress_group)
        
        # Distribución de patrones si hay datos
        if 'pattern_distribution' in stats_data:
            pattern_group = QGroupBox("🎯 Distribución de Patrones")
            pattern_layout = QVBoxLayout(pattern_group)
            
            for pattern_name, count in stats_data['pattern_distribution'].items():
                if count > 0:
                    pattern_card = StatisticCard(
                        pattern_name.title(),
                        count,
                        f"{count} coincidencias encontradas",
                        "#6c757d"
                    )
                    pattern_layout.addWidget(pattern_card)
                    
            self.content_layout.addWidget(pattern_group)
            
        # Espaciador al final
        self.content_layout.addStretch()


class ResultsViewer(QWidget):
    """Visor de resultados mejorado"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz del visor"""
        layout = QVBoxLayout(self)
        
        # Header
        header_layout = QHBoxLayout()
        
        title_label = QLabel("📋 Resultados del Análisis")
        title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: #212529;
            padding: 8px;
        """)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Contador de resultados
        self.results_counter = QLabel("0 resultados")
        self.results_counter.setStyleSheet("""
            color: #6c757d;
            font-weight: 500;
            padding: 8px;
        """)
        header_layout.addWidget(self.results_counter)
        
        layout.addLayout(header_layout)
        
        # Área de resultados
        self.results_area = QScrollArea()
        self.results_area.setWidgetResizable(True)
        
        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout(self.results_widget)
        
        # Placeholder
        self.placeholder = QLabel("🔍 Los resultados aparecerán aquí después del análisis")
        self.placeholder.setAlignment(Qt.AlignCenter)
        self.placeholder.setStyleSheet("""
            color: #6c757d;
            font-size: 14px;
            padding: 40px;
            background: #f8f9fa;
            border: 2px dashed #dee2e6;
            border-radius: 8px;
            margin: 20px;
        """)
        self.results_layout.addWidget(self.placeholder)
        
        self.results_area.setWidget(self.results_widget)
        layout.addWidget(self.results_area)
        
    def display_results(self, results_data):
        """Mostrar resultados del análisis"""
        # Limpiar contenido anterior
        for i in reversed(range(self.results_layout.count())): 
            child = self.results_layout.itemAt(i).widget()
            if child:
                child.setParent(None)
                
        if not results_data:
            self.results_layout.addWidget(self.placeholder)
            self.results_counter.setText("0 resultados")
            return
            
        total_matches = 0
        
        for pattern_name, matches in results_data.items():
            if matches:
                # Crear grupo para cada patrón
                pattern_group = QGroupBox(f"🎯 {pattern_name.title()}")
                pattern_layout = QVBoxLayout(pattern_group)
                
                for i, match in enumerate(matches, 1):
                    match_label = QLabel(f"{i}. {match}")
                    match_label.setStyleSheet("""
                        background: #e7f3ff;
                        border: 1px solid #b8daff;
                        border-radius: 4px;
                        padding: 8px;
                        margin: 2px;
                        font-family: 'Consolas', monospace;
                        color: #004085;
                    """)
                    pattern_layout.addWidget(match_label)
                    total_matches += 1
                    
                self.results_layout.addWidget(pattern_group)
                
        # Actualizar contador
        self.results_counter.setText(f"{total_matches} resultados encontrados")
        
        # Espaciador
        self.results_layout.addStretch()