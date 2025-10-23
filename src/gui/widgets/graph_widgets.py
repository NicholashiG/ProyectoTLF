"""
Widget para integrar matplotlib con PyQt5
Universidad del Quindío - Teoría de Lenguajes Formales
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QComboBox, QGroupBox, QScrollArea,
                             QTabWidget, QFrame, QSizePolicy)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurar estilo de matplotlib
plt.style.use('default')
sns.set_palette("husl")

class MatplotlibCanvas(FigureCanvas):
    """Canvas de matplotlib para PyQt5"""
    
    def __init__(self, figure=None):
        if figure is None:
            self.figure = Figure(figsize=(10, 6), dpi=100)
        else:
            self.figure = figure
            
        super().__init__(self.figure)
        
        # Configuración del canvas
        self.setParent(None)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.updateGeometry()
        
        # Configurar fondo
        self.figure.patch.set_facecolor('white')
        

class GraphWidget(QWidget):
    """Widget individual para mostrar un gráfico"""
    
    export_requested = pyqtSignal(str, object)  # tipo, figura
    
    def __init__(self, title="Gráfico", graph_type="pie"):
        super().__init__()
        self.title = title
        self.graph_type = graph_type
        self.canvas = None
        self.toolbar = None
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz del widget"""
        layout = QVBoxLayout(self)
        
        # Header con título y controles
        header_layout = QHBoxLayout()
        
        title_label = QLabel(self.title)
        title_label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
            color: #212529;
            padding: 8px;
        """)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Botón de exportar
        export_btn = QPushButton("💾 Exportar")
        export_btn.setStyleSheet("""
            QPushButton {
                background: #6f42c1;
                color: white;
                border: none;
                padding: 4px 12px;
                border-radius: 4px;
                font-weight: 600;
                font-size: 10px;
            }
            QPushButton:hover {
                background: #5a32a3;
            }
        """)
        export_btn.clicked.connect(self.export_graph)
        header_layout.addWidget(export_btn)
        
        layout.addLayout(header_layout)
        
        # Crear canvas
        self.canvas = MatplotlibCanvas()
        layout.addWidget(self.canvas)
        
        # Toolbar de navegación (opcional)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("""
            NavigationToolbar2QT {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                padding: 2px;
            }
        """)
        layout.addWidget(self.toolbar)
        
    def create_pie_chart(self, data, labels=None, title="Distribución"):
        """Crear gráfico de torta"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        
        if labels is None:
            labels = [f"Elemento {i+1}" for i in range(len(data))]
            
        colors = sns.color_palette("husl", len(data))
        
        wedges, texts, autotexts = ax.pie(
            data, 
            labels=labels, 
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            explode=[0.05] * len(data)  # Separar ligeramente
        )
        
        # Mejorar apariencia
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
            
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        # Leyenda
        ax.legend(wedges, labels, title="Patrones", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        
    def create_bar_chart(self, data, labels=None, title="Análisis de Barras"):
        """Crear gráfico de barras"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        
        if labels is None:
            labels = [f"Item {i+1}" for i in range(len(data))]
            
        colors = sns.color_palette("viridis", len(data))
        
        bars = ax.bar(labels, data, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Agregar valores encima de las barras
        for bar, value in zip(bars, data):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(data)*0.01,
                   f'{value}', ha='center', va='bottom', fontweight='bold')
                   
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Categorías', fontweight='bold')
        ax.set_ylabel('Cantidad', fontweight='bold')
        
        # Rotar etiquetas si son largas
        if any(len(label) > 8 for label in labels):
            plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
            
        ax.grid(True, alpha=0.3, linestyle='--')
        
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        
    def create_radar_chart(self, data, labels=None, title="Análisis Radar"):
        """Crear gráfico de radar"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111, projection='polar')
        
        if labels is None:
            labels = [f"Métrica {i+1}" for i in range(len(data))]
            
        # Normalizar datos a 0-100 si es necesario
        max_val = max(data)
        if max_val > 100:
            data = [(x / max_val) * 100 for x in data]
            
        # Ángulos para cada métrica
        angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
        data_plot = data[:]
        
        # Cerrar el polígono
        angles += angles[:1]
        data_plot += data_plot[:1]
        
        # Crear el gráfico
        ax.plot(angles, data_plot, 'o-', linewidth=2, label='Métricas', color='#007bff')
        ax.fill(angles, data_plot, alpha=0.25, color='#007bff')
        
        # Configurar etiquetas
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=10)
        
        # Configurar rangos
        ax.set_ylim(0, 100)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8)
        ax.grid(True, alpha=0.3)
        
        ax.set_title(title, fontsize=16, fontweight='bold', pad=30)
        
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        
    def create_histogram(self, data, title="Histograma", bins=20):
        """Crear histograma"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        
        n, bins, patches = ax.hist(data, bins=bins, alpha=0.7, color='skyblue', 
                                  edgecolor='black', linewidth=0.5)
        
        # Colorear barras según altura
        cm = plt.cm.viridis
        for i, p in enumerate(patches):
            p.set_facecolor(cm(n[i] / max(n)))
            
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Valores', fontweight='bold')
        ax.set_ylabel('Frecuencia', fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')
        
        # Estadísticas
        mean_val = np.mean(data)
        std_val = np.std(data)
        ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Media: {mean_val:.2f}')
        ax.legend()
        
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        
    def create_line_plot(self, x_data, y_data, title="Gráfico de Línea", xlabel="X", ylabel="Y"):
        """Crear gráfico de línea"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        
        ax.plot(x_data, y_data, 'o-', linewidth=2, markersize=6, 
                color='#007bff', markerfacecolor='white', markeredgewidth=2)
        
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel(xlabel, fontweight='bold')
        ax.set_ylabel(ylabel, fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')
        
        # Agregar valores en los puntos
        for i, (x, y) in enumerate(zip(x_data, y_data)):
            ax.annotate(f'{y:.1f}', (x, y), textcoords="offset points", 
                       xytext=(0,10), ha='center', fontsize=9)
                       
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        
    def create_heatmap(self, data, title="Mapa de Calor", labels_x=None, labels_y=None):
        """Crear mapa de calor"""
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        
        # Crear heatmap
        im = ax.imshow(data, cmap='YlOrRd', aspect='auto', interpolation='nearest')
        
        # Configurar etiquetas
        if labels_x:
            ax.set_xticks(range(len(labels_x)))
            ax.set_xticklabels(labels_x, rotation=45, ha='right')
            
        if labels_y:
            ax.set_yticks(range(len(labels_y)))
            ax.set_yticklabels(labels_y)
            
        # Agregar valores en las celdas
        for i in range(len(data)):
            for j in range(len(data[0])):
                text = ax.text(j, i, f'{data[i][j]:.1f}',
                             ha="center", va="center", color="black", fontweight='bold')
                             
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        # Colorbar
        cbar = self.canvas.figure.colorbar(im, ax=ax)
        cbar.set_label('Valores', fontweight='bold')
        
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        
    def export_graph(self):
        """Exportar gráfico"""
        if self.canvas and self.canvas.figure:
            self.export_requested.emit(self.graph_type, self.canvas.figure)


class GraphsPanel(QWidget):
    """Panel principal para mostrar múltiples gráficos"""
    
    def __init__(self):
        super().__init__()
        self.graphs = {}
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz del panel"""
        layout = QVBoxLayout(self)
        
        # Header con controles
        header_layout = QHBoxLayout()
        
        title_label = QLabel("📈 Visualizaciones")
        title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: #212529;
            padding: 8px;
        """)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Selector de tipo de gráfico
        self.graph_type_combo = QComboBox()
        self.graph_type_combo.addItems([
            "Gráfico de Torta",
            "Gráfico de Barras", 
            "Gráfico Radar",
            "Histograma",
            "Gráfico de Línea",
            "Mapa de Calor"
        ])
        self.graph_type_combo.setStyleSheet("""
            QComboBox {
                background: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 4px;
                padding: 4px 8px;
                min-width: 150px;
            }
            QComboBox:hover {
                border-color: #007bff;
            }
        """)
        header_layout.addWidget(self.graph_type_combo)
        
        # Botón para generar todos los gráficos
        generate_all_btn = QPushButton("📊 Generar Todos")
        generate_all_btn.setStyleSheet("""
            QPushButton {
                background: #28a745;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #1e7e34;
            }
        """)
        header_layout.addWidget(generate_all_btn)
        
        layout.addLayout(header_layout)
        
        # Área de tabs para los gráficos
        self.graph_tabs = QTabWidget()
        self.graph_tabs.setTabPosition(QTabWidget.North)
        self.graph_tabs.setTabsClosable(False)
        
        # Placeholder inicial
        placeholder_widget = QWidget()
        placeholder_layout = QVBoxLayout(placeholder_widget)
        
        placeholder_label = QLabel("📈 Genere un análisis para ver las visualizaciones")
        placeholder_label.setAlignment(Qt.AlignCenter)
        placeholder_label.setStyleSheet("""
            color: #6c757d;
            font-size: 14px;
            padding: 40px;
            background: #f8f9fa;
            border: 2px dashed #dee2e6;
            border-radius: 8px;
            margin: 20px;
        """)
        placeholder_layout.addWidget(placeholder_label)
        
        self.graph_tabs.addTab(placeholder_widget, "Inicio")
        
        layout.addWidget(self.graph_tabs)
        
    def add_graph(self, graph_type, title, data, **kwargs):
        """Agregar un nuevo gráfico"""
        # Remover placeholder si existe
        if self.graph_tabs.count() == 1 and self.graph_tabs.tabText(0) == "Inicio":
            self.graph_tabs.removeTab(0)
            
        # Crear widget del gráfico
        graph_widget = GraphWidget(title, graph_type)
        
        # Generar el gráfico según el tipo
        if graph_type == "pie":
            labels = kwargs.get('labels', None)
            graph_widget.create_pie_chart(data, labels, title)
        elif graph_type == "bar":
            labels = kwargs.get('labels', None)
            graph_widget.create_bar_chart(data, labels, title)
        elif graph_type == "radar":
            labels = kwargs.get('labels', None)
            graph_widget.create_radar_chart(data, labels, title)
        elif graph_type == "histogram":
            bins = kwargs.get('bins', 20)
            graph_widget.create_histogram(data, title, bins)
        elif graph_type == "line":
            x_data = kwargs.get('x_data', range(len(data)))
            xlabel = kwargs.get('xlabel', 'X')
            ylabel = kwargs.get('ylabel', 'Y')
            graph_widget.create_line_plot(x_data, data, title, xlabel, ylabel)
        elif graph_type == "heatmap":
            labels_x = kwargs.get('labels_x', None)
            labels_y = kwargs.get('labels_y', None)
            graph_widget.create_heatmap(data, title, labels_x, labels_y)
            
        # Agregar tab
        tab_title = title.split()[0] if len(title.split()) > 0 else graph_type.title()
        self.graph_tabs.addTab(graph_widget, tab_title)
        
        # Guardar referencia
        self.graphs[graph_type] = graph_widget
        
        # Cambiar a la nueva pestaña
        self.graph_tabs.setCurrentWidget(graph_widget)
        
    def clear_graphs(self):
        """Limpiar todos los gráficos"""
        self.graph_tabs.clear()
        self.graphs.clear()
        
        # Agregar placeholder
        placeholder_widget = QWidget()
        placeholder_layout = QVBoxLayout(placeholder_widget)
        
        placeholder_label = QLabel("📈 Genere un análisis para ver las visualizaciones")
        placeholder_label.setAlignment(Qt.AlignCenter)
        placeholder_label.setStyleSheet("""
            color: #6c757d;
            font-size: 14px;
            padding: 40px;
            background: #f8f9fa;
            border: 2px dashed #dee2e6;
            border-radius: 8px;
            margin: 20px;
        """)
        placeholder_layout.addWidget(placeholder_label)
        
        self.graph_tabs.addTab(placeholder_widget, "Inicio")
        
    def generate_standard_graphs(self, analysis_data):
        """Generar gráficos estándar basados en los datos de análisis"""
        if not analysis_data:
            return
            
        # Limpiar gráficos existentes
        self.clear_graphs()
        
        # 1. Gráfico de torta - Distribución de patrones
        pattern_counts = {}
        for pattern_name, matches in analysis_data.items():
            if matches and len(matches) > 0:
                pattern_counts[pattern_name] = len(matches)
                
        if pattern_counts:
            self.add_graph(
                "pie", 
                "Distribución de Patrones Encontrados",
                list(pattern_counts.values()),
                labels=list(pattern_counts.keys())
            )
            
        # 2. Gráfico de barras - Cantidad por patrón
        if pattern_counts:
            self.add_graph(
                "bar",
                "Cantidad de Coincidencias por Patrón",
                list(pattern_counts.values()),
                labels=list(pattern_counts.keys())
            )
            
        # 3. Gráfico radar - Métricas de calidad (si hay estadísticas)
        # Esto se puede llamar desde el widget de estadísticas
        
    def generate_statistics_graphs(self, stats_data):
        """Generar gráficos basados en estadísticas"""
        if not stats_data:
            return
            
        # Gráfico radar de métricas
        metrics = []
        labels = []
        
        if 'complexity_score' in stats_data:
            metrics.append(min(stats_data['complexity_score'] * 10, 100))
            labels.append('Complejidad')
            
        if 'entropy' in stats_data:
            metrics.append(min(stats_data['entropy'] * 20, 100))
            labels.append('Entropía')
            
        if 'lexical_diversity' in stats_data:
            metrics.append(stats_data['lexical_diversity'] * 100)
            labels.append('Diversidad')
            
        if 'quality_score' in stats_data:
            metrics.append(stats_data['quality_score'])
            labels.append('Calidad')
            
        if metrics:
            self.add_graph(
                "radar",
                "Métricas de Calidad del Texto",
                metrics,
                labels=labels
            )