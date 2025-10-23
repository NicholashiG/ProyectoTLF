"""
Model: Handles the data and business logic for text analysis and pattern validation
"""

from ..analysis.lexical_analyzer import LexicalAnalyzer, Token, TokenType
from ..patterns.patterns import PatternValidator
from ..analysis.statistics import StatisticsAnalyzer
from ..visualization.graphs import GraphGenerator
from ..visualization.reports import ReportGenerator
from typing import List, Dict, Any


class TextModel:
    """Enhanced model to store and manage text data with lexical analysis capabilities"""
    
    def __init__(self):
        self.text = ""
        self.lexical_analyzer = LexicalAnalyzer()
        self.pattern_validator = PatternValidator()
        self.statistics_analyzer = StatisticsAnalyzer()
        self.graph_generator = GraphGenerator()
        self.report_generator = ReportGenerator()
        self.tokens = []
        self.analysis_results = {}
        self.advanced_stats = {}
    
    def set_text(self, text):
        """Store the text and trigger lexical analysis"""
        self.text = text
        # Perform lexical analysis automatically when text is set
        self.tokens = self.lexical_analyzer.analyze(text)
        self.analysis_results = self.lexical_analyzer.get_statistics()
        # Perform advanced statistical analysis
        self.advanced_stats = self.statistics_analyzer.analyze_results(
            self.tokens, text, self.analysis_results
        )
    
    def get_text(self):
        """Retrieve the stored text"""
        return self.text
    
    def get_text_length(self):
        """Get the length of the stored text"""
        return len(self.text)
    
    def get_text_uppercase(self):
        """Get the text in uppercase"""
        return self.text.upper()
    
    def get_text_lowercase(self):
        """Get the text in lowercase"""
        return self.text.lower()
    
    # New methods for lexical analysis and pattern validation
    
    def get_tokens(self) -> List[Token]:
        """Get all tokens from lexical analysis"""
        return self.tokens
    
    def get_valid_tokens(self) -> List[Token]:
        """Get only valid pattern tokens"""
        return self.lexical_analyzer.get_tokens_by_type(TokenType.VALID_PATTERN)
    
    def get_invalid_tokens(self) -> List[Token]:
        """Get only invalid tokens"""
        return self.lexical_analyzer.get_tokens_by_type(TokenType.INVALID_TOKEN)
    
    def get_tokens_by_pattern(self, pattern_name: str) -> List[Token]:
        """Get tokens that match a specific pattern"""
        return self.lexical_analyzer.get_tokens_by_pattern(pattern_name)
    
    def get_analysis_statistics(self) -> Dict[str, Any]:
        """Get statistical information about the analysis"""
        return self.analysis_results
    
    def get_lexical_report(self) -> str:
        """Generate a detailed lexical analysis report"""
        return self.lexical_analyzer.generate_report()
    
    def validate_single_pattern(self, text: str, pattern_name: str) -> bool:
        """Validate if a single text matches a specific pattern"""
        return self.pattern_validator.validate_pattern(text, pattern_name)
    
    def get_available_patterns(self) -> List[str]:
        """Get list of available pattern names"""
        return self.pattern_validator.get_available_patterns()
    
    def get_pattern_description(self, pattern_name: str) -> str:
        """Get description of a specific pattern"""
        return self.pattern_validator.get_pattern_description(pattern_name)
    
    def get_pattern_examples(self, pattern_name: str) -> List[str]:
        """Get examples for a specific pattern"""
        return self.pattern_validator.get_pattern_examples(pattern_name)
    
    def analyze_text_for_all_patterns(self) -> Dict[str, List[str]]:
        """Analyze text and return all patterns found"""
        return self.pattern_validator.analyze_text_patterns(self.text)
    
    def get_pattern_summary(self) -> Dict[str, int]:
        """Get summary of how many tokens were found for each pattern"""
        summary = {}
        valid_tokens = self.get_valid_tokens()
        
        for token in valid_tokens:
            if token.pattern_name in summary:
                summary[token.pattern_name] += 1
            else:
                summary[token.pattern_name] = 1
        
        return summary
    
    def has_valid_patterns(self) -> bool:
        """Check if any valid patterns were found in the text"""
        return len(self.get_valid_tokens()) > 0
    
    def get_error_tokens(self) -> List[Token]:
        """Get tokens that couldn't be classified (invalid or unknown)"""
        invalid_tokens = self.get_invalid_tokens()
        unknown_tokens = self.lexical_analyzer.get_tokens_by_type(TokenType.UNKNOWN)
        return invalid_tokens + unknown_tokens
    
    # New methods for advanced statistics and visualization
    
    def get_advanced_statistics(self) -> Dict[str, Any]:
        """Get advanced statistical analysis"""
        return self.advanced_stats
    
    def get_statistics_report(self) -> str:
        """Get detailed statistics report"""
        return self.statistics_analyzer.get_summary_report()
    
    def export_statistics_to_json(self, filepath: str = None) -> str:
        """Export statistics to JSON file"""
        if not filepath:
            filepath = "data/outputs/statistics.json"
        return self.statistics_analyzer.export_to_json(filepath, self.advanced_stats)
    
    def export_statistics_to_csv(self, filepath: str = None) -> str:
        """Export statistics to CSV file"""
        if not filepath:
            filepath = "data/outputs/statistics.csv"
        return self.statistics_analyzer.export_to_csv(filepath)
    
    def generate_graphs(self) -> Dict[str, str]:
        """Generate all visualization graphs"""
        return self.graph_generator.generate_all_graphs(self.advanced_stats)
    
    def generate_html_report(self, include_graphs: bool = True) -> str:
        """Generate comprehensive HTML report"""
        graph_files = None
        if include_graphs:
            graph_files = self.generate_graphs()
        
        return self.report_generator.generate_html_report(
            self.advanced_stats, graph_files
        )
    
    def export_data_files(self) -> Dict[str, str]:
        """Export all data files (JSON, CSV, HTML)"""
        exported_files = {}
        
        # Export JSON
        json_file = self.report_generator.export_json(self.advanced_stats)
        exported_files['json'] = json_file
        
        # Export CSV
        csv_file = self.report_generator.export_csv(self.advanced_stats)
        exported_files['csv'] = csv_file
        
        # Export HTML report
        html_file = self.generate_html_report(include_graphs=True)
        exported_files['html'] = html_file
        
        return exported_files
    
    def get_comparative_analysis(self) -> Dict[str, Any]:
        """Get comparative analysis if multiple analyses exist"""
        return self.statistics_analyzer.get_comparative_analysis()
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics of the analysis"""
        return self.advanced_stats.get('performance_metrics', {})
    
    def get_complexity_analysis(self) -> Dict[str, Any]:
        """Get text complexity analysis"""
        return self.advanced_stats.get('complexity_analysis', {})
    
    def get_quality_score(self) -> float:
        """Get overall quality score of the analysis"""
        quality_metrics = self.advanced_stats.get('quality_metrics', {})
        return quality_metrics.get('quality_score', 0.0)
