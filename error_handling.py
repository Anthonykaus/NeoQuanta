import logging

logger = logging.getLogger(__name__)

class ErrorHandler:
    def __init__(self):
        logger.info("Error Handler module initialized.")

    def handle_error(self, error):
        logger.error(f"Error occurred: {error}")
        # Implement error handling logic here
