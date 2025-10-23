"""
Controller: Coordinates between Model and View for lexical analysis and pattern validation
"""

from .model import TextModel
from .view import TextView


class TextController:
    """Enhanced controller to manage the lexical analysis application flow"""
    
    def __init__(self):
        self.model = TextModel()
        self.view = TextView()
        self.current_text = ""
    
    def run(self):
        """Main application loop with enhanced menu system"""
        self.view.show_message("¡Bienvenido al Sistema de Análisis Léxico y Validación de Patrones!")
        
        # Get text input first
        self._get_text_input()
        
        # Main menu loop
        while True:
            choice = self.view.show_enhanced_menu()
            
            if choice == 0:
                self._exit_application()
                break
            elif choice == 1:
                self._complete_analysis()
            elif choice == 2:
                self._specific_pattern_analysis()
            elif choice == 3:
                self._single_pattern_validation()
            elif choice == 4:
                self._show_available_patterns()
            elif choice == 5:
                self._show_pattern_examples()
            elif choice == 6:
                self._basic_analysis()
            elif choice == 7:
                self._advanced_statistics()
            elif choice == 8:
                self._generate_visualizations()
            elif choice == 9:
                self._export_reports()
            elif choice == 10:
                self._change_text()
            
            self.view.pause()
    
    def _get_text_input(self):
        """Get and store text input from user"""
        text = self.view.get_text_input()
        self.current_text = text
        self.model.set_text(text)
        self.view.show_message(f"\n✅ Texto cargado y analizado: {len(text)} caracteres")
    
    def _complete_analysis(self):
        """Perform complete lexical analysis"""
        if not self.current_text.strip():
            self.view.show_message("❌ No hay texto para analizar. Ingrese texto primero.")
            return
        
        # Get analysis results
        report = self.model.get_lexical_report()
        statistics = self.model.get_analysis_statistics()
        
        # Display complete analysis
        self.view.show_lexical_analysis(report, statistics)
        
        # Show additional information
        valid_tokens = self.model.get_valid_tokens()
        invalid_tokens = self.model.get_invalid_tokens()
        
        if valid_tokens:
            self.view.show_valid_tokens(valid_tokens)
        
        if invalid_tokens:
            self.view.show_invalid_tokens(invalid_tokens)
        
        # Show pattern summary
        summary = self.model.get_pattern_summary()
        if summary:
            self.view.show_pattern_summary(summary, self.model)
        
        # Show statistics
        self.view.show_statistics(statistics)
    
    def _specific_pattern_analysis(self):
        """Analyze text for specific patterns"""
        if not self.current_text.strip():
            self.view.show_message("❌ No hay texto para analizar. Ingrese texto primero.")
            return
        
        available_patterns = self.model.get_available_patterns()
        chosen_pattern = self.view.get_pattern_choice(available_patterns)
        
        # Get tokens for the chosen pattern
        tokens = self.model.get_tokens_by_pattern(chosen_pattern)
        description = self.model.get_pattern_description(chosen_pattern)
        
        # Display results
        self.view.show_pattern_tokens(chosen_pattern, tokens, description)
    
    def _single_pattern_validation(self):
        """Validate a single text against a specific pattern"""
        available_patterns = self.model.get_available_patterns()
        chosen_pattern = self.view.get_pattern_choice(available_patterns)
        
        # Get text to validate
        text_to_validate = self.view.get_validation_input()
        
        # Validate
        is_valid = self.model.validate_single_pattern(text_to_validate, chosen_pattern)
        description = self.model.get_pattern_description(chosen_pattern)
        
        # Show result
        self.view.show_validation_result(text_to_validate, chosen_pattern, is_valid, description)
    
    def _show_available_patterns(self):
        """Display all available patterns"""
        patterns = self.model.get_available_patterns()
        self.view.show_available_patterns(patterns, self.model)
    
    def _show_pattern_examples(self):
        """Show examples for a specific pattern"""
        available_patterns = self.model.get_available_patterns()
        chosen_pattern = self.view.get_pattern_choice(available_patterns)
        
        examples = self.model.get_pattern_examples(chosen_pattern)
        description = self.model.get_pattern_description(chosen_pattern)
        
        self.view.show_pattern_examples(chosen_pattern, examples, description)
    
    def _basic_analysis(self):
        """Perform basic text analysis (original functionality)"""
        if not self.current_text.strip():
            self.view.show_message("❌ No hay texto para analizar. Ingrese texto primero.")
            return
        
        # Get basic processed data from model
        original_text = self.model.get_text()
        length = self.model.get_text_length()
        uppercase = self.model.get_text_uppercase()
        lowercase = self.model.get_text_lowercase()
        
        # Display basic results via view
        self.view.show_text_info(original_text, length, uppercase, lowercase)
    
    def _exit_application(self):
        """Exit the application"""
        self.view.show_goodbye()
    
    def _change_text(self):
        """Allow user to input new text"""
        self._get_text_input()
        self.view.show_message("✅ Nuevo texto cargado y listo para análisis.")
    
    def _advanced_statistics(self):
        """Show advanced statistical analysis"""
        if not self.current_text.strip():
            self.view.show_message("❌ No hay texto para analizar. Ingrese texto primero.")
            return
        
        # Get advanced statistics
        advanced_stats = self.model.get_advanced_statistics()
        stats_report = self.model.get_statistics_report()
        
        # Display advanced statistics
        self.view.show_message("\n📊 ESTADÍSTICAS AVANZADAS")
        self.view.show_message(stats_report)
        
        # Show comparative analysis if available
        comparative = self.model.get_comparative_analysis()
        if 'message' not in comparative:
            self.view.show_message("\n📈 ANÁLISIS COMPARATIVO:")
            trend_analysis = comparative.get('trend_analysis', {})
            for metric, trend in trend_analysis.items():
                self.view.show_message(f"  • {metric}: {trend}")
    
    def _generate_visualizations(self):
        """Generate and show information about graphs"""
        if not self.current_text.strip():
            self.view.show_message("❌ No hay texto para analizar. Ingrese texto primero.")
            return
        
        self.view.show_message("\n📊 GENERANDO VISUALIZACIONES...")
        
        try:
            # Generate graphs
            graph_files = self.model.generate_graphs()
            
            if graph_files:
                self.view.show_message("✅ Gráficos generados exitosamente:")
                for graph_type, filepath in graph_files.items():
                    if filepath:
                        self.view.show_message(f"  • {graph_type}: {filepath}")
                
                self.view.show_message("\n📂 Los gráficos se han guardado en la carpeta 'data/graphs/'")
                self.view.show_message("💡 Puede abrir los archivos PNG para ver las visualizaciones.")
            else:
                self.view.show_message("❌ No se pudieron generar gráficos.")
                
        except Exception as e:
            self.view.show_message(f"❌ Error generando gráficos: {str(e)}")
            self.view.show_message("💡 Asegúrese de tener matplotlib instalado: pip install matplotlib")
    
    def _export_reports(self):
        """Export data and generate reports"""
        if not self.current_text.strip():
            self.view.show_message("❌ No hay texto para analizar. Ingrese texto primero.")
            return
        
        self.view.show_message("\n📤 EXPORTANDO REPORTES Y DATOS...")
        
        try:
            # Export all data files
            exported_files = self.model.export_data_files()
            
            self.view.show_message("✅ Archivos exportados exitosamente:")
            for file_type, filepath in exported_files.items():
                self.view.show_message(f"  • {file_type.upper()}: {filepath}")
            
            self.view.show_message("\n📂 Los archivos se han guardado en la carpeta 'data/outputs/'")
            self.view.show_message("💡 El reporte HTML incluye gráficos embebidos para visualización completa.")
            
            # Show quality metrics
            quality_score = self.model.get_quality_score()
            self.view.show_message(f"\n🎯 Score de Calidad del Análisis: {quality_score:.1f}/100")
            
        except Exception as e:
            self.view.show_message(f"❌ Error exportando reportes: {str(e)}")
            self.view.show_message("💡 Verifique que tenga permisos de escritura en las carpetas de destino.")
