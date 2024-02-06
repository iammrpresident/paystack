import logging

class ApiLogger:
    """
    Logger class for Paystack wrapper.
    """

    def __init__(self, log_file_path='api_wrapper.log', log_level=logging.INFO):
        """
        Initialize the logger.
        """
        self.logger = logging.getLogger('api_wrapper')
        self.logger.setLevel(log_level)

        # Create a file handler and set the level to log all messages
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler with a higher log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Create a formatter and attach it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_info(self, message):
        """
        Log an informational message.
        """
        self.logger.info(message)

    def log_error(self, message):
        """
        Log an error message.
        """
        self.logger.error(message)
