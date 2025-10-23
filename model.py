"""
Model: Handles the data and business logic
"""


class TextModel:
    """Model to store and manage text data"""
    
    def __init__(self):
        self.text = ""
    
    def set_text(self, text):
        """Store the text"""
        self.text = text
    
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
