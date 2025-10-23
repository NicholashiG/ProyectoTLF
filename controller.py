"""
Controller: Coordinates between Model and View
"""

from model import TextModel
from view import TextView


class TextController:
    """Controller to manage the application flow"""
    
    def __init__(self):
        self.model = TextModel()
        self.view = TextView()
    
    def run(self):
        """Main application logic"""
        # Get text from user via view
        text = self.view.get_text_input()
        
        # Store text in model
        self.model.set_text(text)
        
        # Get processed data from model
        original_text = self.model.get_text()
        length = self.model.get_text_length()
        uppercase = self.model.get_text_uppercase()
        lowercase = self.model.get_text_lowercase()
        
        # Display results via view
        self.view.show_text_info(original_text, length, uppercase, lowercase)
