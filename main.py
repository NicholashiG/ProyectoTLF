"""
Main entry point for the MVC text application
"""

from controller import TextController


def main():
    """Run the application"""
    controller = TextController()
    controller.run()


if __name__ == "__main__":
    main()
