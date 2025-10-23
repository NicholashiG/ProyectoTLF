"""
View: Handles user interaction and display
"""


class TextView:
    """View for console input/output"""
    
    def get_text_input(self):
        """Get text input from the user"""
        return input("Por favor, ingrese un texto: ")
    
    def show_message(self, message):
        """Display a message to the user"""
        print(message)
    
    def show_text_info(self, text, length, uppercase, lowercase):
        """Display information about the text"""
        print("\n" + "="*50)
        print("INFORMACIÓN DEL TEXTO")
        print("="*50)
        print(f"Texto original: {text}")
        print(f"Longitud: {length} caracteres")
        print(f"Mayúsculas: {uppercase}")
        print(f"Minúsculas: {lowercase}")
        print("="*50)
